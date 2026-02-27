import streamlit as st
import pandas as pd

# 1. Настройка стиля (Делаем "дорогой" темный вид)
st.set_page_config(page_title="Генератор ТЗ", page_icon="⚡", layout="centered")

st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    div.stButton > button {
        width: 100%;
        background-color: #00d1b2;
        color: white;
        border-radius: 10px;
        height: 3em;
        font-weight: bold;
    }
    .stProgress > div > div > div > div { background-color: #00d1b2; }
    </style>
    """, unsafe_allow_html=True)

# 2. Логика переключения шагов
if 'step' not in st.session_state:
    st.session_state.step = 1

def next_step(): st.session_state.step += 1
def prev_step(): st.session_state.step -= 1

# --- ЗАГОЛОВОК И ПРОГРЕСС ---
st.title("⚡ Генератор ТЗ")
st.write("Создайте идеальное задание для вашего проекта")

# Рисуем шаги
cols = st.columns(4)
steps_names = ["Продукт", "Дизайн", "Оплата", "Результат"]
for i, name in enumerate(steps_names):
    if st.session_state.step == i + 1:
        cols[i].markdown(f"**🟢 {name}**")
    else:
        cols[i].markdown(f"⚪ {name}")

st.divider()

# --- ШАГ 1: ИНФОРМАЦИЯ О ПРОДУКТЕ ---
if st.session_state.step == 1:
    st.subheader("01 Информация о продукте")
    shop_name = st.text_input("Название магазина *", placeholder="Например: Digital Pro Store")
    lang = st.selectbox("Язык сайта", ["Русский", "English"])
    description = st.text_area("Что продаёшь — подробное описание *", placeholder="Опиши продукт подробно...")
    audience = st.text_area("Целевая аудитория *", placeholder="Кто твой покупатель?")
    
    if st.button("Далее: Внешний вид →"):
        if shop_name and description:
            st.session_state.shop_name = shop_name
            st.session_state.description = description
            next_step()
        else:
            st.error("Заполни обязательные поля!")

# --- ШАГ 2: ВНЕШНИЙ ВИД ---
elif st.session_state.step == 2:
    st.subheader("02 Внешний вид магазина")
    theme = st.radio("Цветовая тема", ["Тёмная", "Светлая", "Синяя", "Золотая"], horizontal=True)
    style = st.select_slider("Стиль оформления", options=["Минимализм", "Яркий", "Деловой"])
    
    col_nav = st.columns(2)
    if col_nav[0].button("← Назад"): prev_step()
    if col_nav[1].button("Далее: Оплата →"):
        st.session_state.theme = theme
        st.session_state.style = style
        next_step()

# --- ШАГ 3: ОПЛАТА ---
elif st.session_state.step == 3:
    st.subheader("03 Платёжные системы")
    pay_sys = st.multiselect("Выберите способы оплаты", ["ЮMoney", "Криптовалюта", "Карты РФ", "PayPal"])
    
    col_nav = st.columns(2)
    if col_nav[0].button("← Назад"): prev_step()
    if col_nav[1].button("⚡ Сгенерировать ТЗ"):
        st.session_state.pay_sys = pay_sys
        next_step()

# --- ШАГ 4: РЕЗУЛЬТАТ ---
elif st.session_state.step == 4:
    st.success("✅ Ваше ТЗ готово!")
    
    result_text = f"""
    ## ЗАДАЧА
    Создать магазин: {st.session_state.shop_name}
    Язык: {st.session_state.get('lang', 'Русский')}
    
    ## КОНТЕНТ
    Описание: {st.session_state.description}
    Аудитория: {audience if 'audience' in locals() else 'Общая'}
    
    ## ДИЗАЙН
    Тема: {st.session_state.theme}
    Стиль: {st.session_state.style}
    
    ## ОПЛАТА
    Системы: {", ".join(st.session_state.pay_sys)}
    """
    
    st.code(result_text, language="markdown")
    st.download_button("Скачать ТЗ", result_text)
    
    if st.button("🔄 Начать заново"):
        st.session_state.step = 1
        st.rerun()

st.caption("© 2024 Мой Генератор ТЗ")
