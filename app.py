import streamlit as st
from collections import Counter
import re

# 1. КОНФИГУРАЦИЯ СТРАНИЦЫ
st.set_page_config(page_title="AI TZ Premium", page_icon="🔮", layout="centered")

# 2. КРУТОЙ ДИЗАЙН (CSS)
st.markdown("""
    <style>
    /* Глубокий черный фон для всего приложения */
    .stApp {
        background-color: #000000;
        color: #ffffff;
    }
    
    /* Стилизация центрального заголовка */
    .main-title {
        text-align: center;
        font-family: 'Exo 2', sans-serif;
        background: linear-gradient(90deg, #00f2ea, #00ff41);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 3rem;
        font-weight: 800;
        margin-bottom: 10px;
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 15px;
    }
    
    .subtitle {
        text-align: center;
        color: #888;
        font-size: 1.1rem;
        margin-bottom: 40px;
    }

    /* Оформление рамок для полей ввода */
    div[data-baseweb="input"], div[data-baseweb="textarea"] {
        border: 1px solid #1e1e1e !important;
        border-radius: 12px !important;
        background-color: #0a0a0a !important;
        transition: all 0.3s ease;
    }
    
    div[data-baseweb="input"]:focus-within, div[data-baseweb="textarea"]:focus-within {
        border: 1px solid #00f2ea !important;
        box-shadow: 0 0 15px rgba(0, 242, 234, 0.2);
    }

    /* Красивые карточки шагов */
    .step-container {
        display: flex;
        justify-content: space-around;
        margin-bottom: 30px;
    }
    
    .step-node {
        text-align: center;
        padding: 10px;
        border-bottom: 2px solid #1e1e1e;
        flex-grow: 1;
        color: #444;
        font-weight: bold;
    }
    
    .step-node-active {
        color: #00f2ea;
        border-bottom: 2px solid #00f2ea;
        text-shadow: 0 0 10px rgba(0, 242, 234, 0.5);
    }

    /* Кнопки в стиле киберпанк */
    .stButton > button {
        background: linear-gradient(135deg, #00f2ea 0%, #0072ff 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 12px 24px !important;
        font-weight: bold !important;
        text-transform: uppercase;
        letter-spacing: 1px;
        transition: transform 0.2s, box-shadow 0.2s !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 20px rgba(0, 242, 234, 0.4) !important;
    }
    
    /* Убираем стандартные рамки Streamlit */
    header {visibility: hidden;}
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    </style>
    """, unsafe_allow_html=True)

# 3. ЛОГИКА ШАГОВ
if 'step' not in st.session_state:
    st.session_state.step = 1

def next_step(): st.session_state.step += 1
def prev_step(): st.session_state.step -= 1

# --- ШАПКА ---
st.markdown('<div class="main-title">🔮 AI ГЕНЕРАТОР ТЗ</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Интеллектуальная система проектирования цифровых продуктов</div>', unsafe_allow_html=True)

# --- ИНДИКАТОР ШАГОВ ---
step_cols = st.columns(4)
names = ["Продукт", "Стиль", "Оплата", "Финал"]
for i, name in enumerate(names):
    is_active = "step-node-active" if st.session_state.step == i + 1 else ""
    step_cols[i].markdown(f'<div class="step-node {is_active}">{i+1}. {name}</div>', unsafe_allow_html=True)

st.write("") # Отступ

# --- ШАГ 1: ПРОДУКТ ---
if st.session_state.step == 1:
    st.markdown("### 🛠 Основная информация")
    with st.container():
        shop_name = st.text_input("Название вашего проекта", placeholder="Например: CyberStore X")
        description = st.text_area("Детальное описание продукта", placeholder="Опишите, что именно вы предлагаете...", height=150)
        audience = st.text_input("Целевая аудитория", placeholder="Кто ваши клиенты?")
        
    if st.button("Далее: Визуальный стиль →"):
        if shop_name and description:
            st.session_state.shop_name = shop_name
            st.session_state.description = description
            st.session_state.audience = audience
            next_step()
            st.rerun()
        else:
            st.error("Пожалуйста, заполните название и описание.")

# --- ШАГ 2: ВИЗУАЛ ---
elif st.session_state.step == 2:
    st.markdown("### 🎨 Эстетика и Интерфейс")
    theme = st.select_slider("Цветовая палитра", options=["Deep Black", "Cyber Blue", "Neon Green", "Royal Gold"])
    ui_style = st.radio("Стиль UI", ["Минимализм", "Футуризм", "Классика", "Яркий акцент"], horizontal=True)
    
    col_nav = st.columns([1,1])
    with col_nav[0]: 
        if st.button("← Назад"): 
            prev_step()
            st.rerun()
    with col_nav[1]: 
        if st.button("Далее: Технологии →"):
            st.session_state.theme = theme
            st.session_state.ui_style = ui_style
            next_step()
            st.rerun()

# --- ШАГ 3: ТЕХНОЛОГИИ (ОПЛАТА) ---
elif st.session_state.step == 3:
    st.markdown("### ⚙️ Интеграции и Оплата")
    pays = st.multiselect("Платежные шлюзы", ["Crypto Pay", "Stripe", "ЮMoney", "Банковские карты"])
    security = st.checkbox("Нужна повышенная защита данных (SSL/Encryption)")
    
    col_nav = st.columns([1,1])
    with col_nav[0]: 
        if st.button("← Назад"): 
            prev_step()
            st.rerun()
    with col_nav[1]: 
        if st.button("🔮 Сгенерировать финальное ТЗ"):
            st.session_state.pays = pays
            next_step()
            st.rerun()

# --- ШАГ 4: РЕЗУЛЬТАТ ---
elif st.session_state.step == 4:
    st.markdown("### ✨ Ваше идеальное ТЗ сформировано")
    
    final_output = f"""## 🧠 ТЕХНИЧЕСКОЕ ЗАДАНИЕ: {st.session_state.shop_name.upper()}

### 📌 ПРОДУКТ
- **Описание:** {st.session_state.description}
- **Аудитория:** {st.session_state.audience}

### 🎨 ДИЗАЙН-КОНЦЕПЦИЯ
- **Цветовое решение:** {st.session_state.theme}
- **Стиль интерфейса:** {st.session_state.ui_style}

### 💳 ТЕХНИЧЕСКИЙ СТЕК
- **Методы оплаты:** {", ".join(st.session_state.pays) if st.session_state.pays else "Не указано"}
- **Безопасность:** {"Включена (High Priority)" if security else "Стандартная"}

---
*Сгенерировано в AI Premium TZ Tool*
    """
    
    st.markdown('<div style="background-color: #0a0a0a; padding: 20px; border-radius: 15px; border: 1px solid #00f2ea;">', unsafe_allow_html=True)
    st.markdown(final_output)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.download_button("📥 Скачать ТЗ в формате .txt", final_output)
    
    if st.button("🔄 Создать новое ТЗ"):
        st.session_state.step = 1
        st.rerun()

st.write("---")
st.caption("⚡ Premium AI System | 2024")
