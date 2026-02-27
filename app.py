import streamlit as st
import requests
import json
from bs4 import BeautifulSoup
import trafilatura
from collections import Counter
import re
import pandas as pd

# Твой ключ API Serper
SERPER_API_KEY = "c0d0cfb9aa136fa3f4818f973da0617602910ef6"

def get_data(query):
    url = "https://google.serper.dev/search"
    payload = json.dumps({"q": query, "gl": "ru", "hl": "ru"})
    headers = {'X-API-KEY': SERPER_API_KEY, 'Content-Type': 'application/json'}
    try:
        response = requests.request("POST", url, headers=headers, data=payload)
        return response.json().get('organic', [])[:7]
    except:
        return []

def analyze_page(url):
    try:
        downloaded = trafilatura.fetch_url(url)
        if not downloaded: return None
        text = trafilatura.extract(downloaded)
        soup = BeautifulSoup(downloaded, 'html.parser')
        headers = [h.get_text().strip() for h in soup.find_all(['h2', 'h3']) if len(h.get_text()) > 10]
        return {"title": soup.title.string if soup.title else "Без заголовка", "text": text, "headers": headers, "words": len(text.split()) if text else 0}
    except: return None

# Настройка внешнего вида сайта
st.set_page_config(page_title="SEO TZ Generator", layout="wide")
st.title("🚀 Генератор ТЗ для копирайтера")
st.write("Анализ ТОП-7 конкурентов и подготовка требований.")

query = st.text_input("Введите поисковый запрос (тему статьи):")

if st.button("Сгенерировать ТЗ"):
    if not query:
        st.warning("Сначала введите запрос!")
    else:
        with st.spinner('Анализирую выдачу Google...'):
            results = get_data(query)
            data_list, all_texts, all_headers = [], [], []

            for res in results:
                page = analyze_page(res['link'])
                if page:
                    page['url'] = res['link']
                    data_list.append(page)
                    all_texts.append(page['text'])
                    all_headers.extend(page['headers'])

            if data_list:
                df = pd.DataFrame(data_list)[['title', 'words', 'url']]
                st.subheader("📊 Анализ ТОП-7 конкурентов")
                st.dataframe(df, use_container_width=True)
                
                avg_words = int(df['words'].mean())
                st.success(f"💡 Рекомендуемый объем: ~{avg_words} слов (примерно {avg_words*7} знаков)")

                col1, col2 = st.columns(2)
                with col1:
                    st.subheader("🔑 Ключевые слова (LSI)")
                    full_text = " ".join(all_texts).lower()
                    words = re.findall(r'\b[а-яё]{5,15}\b', full_text)
                    st.write(", ".join([k[0] for k in Counter(words).most_common(25)]))

                with col2:
                    st.subheader("📑 Заголовки конкурентов")
                    for h in list(set(all_headers))[:15]:
                        st.write(f"- {h}")
            else:
                st.error("Не удалось получить данные. Попробуйте другой запрос.")
