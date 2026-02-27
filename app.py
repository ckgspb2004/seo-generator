import streamlit as st

# 1. КОНФИГУРАЦИЯ
st.set_page_config(page_title="Генератор ТЗ Про", page_icon="💠", layout="centered")

# 2. УЛЬТРА-ДИЗАЙН (ЧЕРНЫЙ ПРЕМИУМ)
st.markdown("""
    <style>
    /* Главный фон */
    .stApp { background-color: #000000; color: #ffffff; }
    
    /* Кастомный логотип Г */
    .logo-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        padding: 20px 0;
    }
    .logo-icon {
        background: linear-gradient(135deg, #00f2ea 0%, #0072ff 100%);
        width: 60px; height: 60px;
        border-radius: 15px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 35px;
        font-weight: 900;
        color: white;
        box-shadow: 0 0 20px rgba(0, 242, 234, 0.4);
        margin-bottom: 15px;
    }
    .main-title {
        font-family: 'Inter', sans-serif;
        font-size: 2.8rem;
        font-weight: 800;
        letter-spacing: -1px;
        background: linear-gradient(90deg, #ffffff, #888888);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 0;
    }

    /* Рамки и поля ввода */
    div[data-baseweb="input"], div[data-baseweb="textarea"], div[data-baseweb="select"] {
        border: 1px solid #222 !important;
        border-radius: 12px !important;
        background-color: #080808 !important;
    }
    div[data-baseweb="input"]:focus-within {
        border-color: #00f2ea !important;
    }
    
    /* Красивые заголовки шагов */
    .step-bar {
        display: flex;
        justify-content: space-between;
        margin: 30px 0;
        border-bottom: 1px solid #111;
        padding-bottom: 10px;
    }
    .step-item { color: #444; font-size: 0.8rem; font-weight: bold; text-transform: uppercase; }
    .step-item-active { color: #00f2ea; text-shadow: 0 0 10px #00f2ea; }

    /* Кнопки */
    .stButton > button {
        background: #ffffff !important;
        color: #000000 !important;
        border: none !important;
        border-radius: 10px !important;
        height: 55px;
        font-weight: 800 !important;
        font-size: 1rem !important;
        transition: all 0.3s ease;
    }
    .stButton > button:hover {
        background: #00f2ea !important;
        transform: scale(1.02);
    }
    
    /* Окно результата */
    .result-area {
        background: #0a0a0a;
        border: 1px solid #1a1a1a;
        border-radius: 15px;
        padding: 25px;
        font-family: 'Monaco', monospace;
        color: #efefef;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. ЛОГИКА СОХРАНЕНИЯ ДАННЫХ
if 'step' not in st.session_state: st.session_state.step = 1
# Чистим данные при первом запуске или ошибке
if 'data' not in st.session_state or 'theme' not in st.session_state.data:
    st.session_state.data = {
        "name": "", "desc": "", "aud": "", 
        "theme": "Черный Бриллиант", "style": "Минимализм", 
        "pays": [], "security": False
    }

# --- ВЕРХНЯЯ ЧАСТЬ (ЛОГО И НАЗВАНИЕ) ---
st.markdown("""
    <div class="logo-container">
        <div class="logo-icon">Г</div>
        <div class="main-title">ГЕНЕРАТОР ТЗ</div>
        <div style="color: #666; font-size: 0.9rem; margin-top: 5px;">Профессиональное проектирование систем</div>
    </div>
    """, unsafe_allow_html=True)

# ИНДИКАТОР ШАГОВ
st.markdown(f"""
    <div class="step-bar">
        <div class="step-item {'step-item-active' if st.session_state.step == 1 else ''}">01. Продукт</div>
        <div class="step-item {'step-item-active' if st.session_state.step == 2 else ''}">02. Визуал</div>
        <div class="step-item {'step-item-active' if st.session_state.step == 3 else ''}">03. Техстек</div>
        <div class="step-item {'step-item-active' if st.session_state.step == 4 else ''}">04. Финал</div>
    </div>
    """, unsafe_allow_html=True)

# --- ШАГИ ---
if st.session_state.step == 1:
    st.markdown("### 🛠 Информация о продукте")
    st.session_state.data["name"] = st.text_input("Название вашего проекта *", value=st.session_state.data.get("name", ""))
    st.session_state.data["desc"] = st.text_area("Суть продукта и задачи *", value=st.session_state.data.get("desc", ""), height=150)
    st.session_state.data["aud"] = st.text_input("Целевая аудитория", value=st.session_state.data.get("aud", ""))
    
    if st.button("СЛЕДУЮЩИЙ ШАГ →"):
        if st.session_state.data["name"] and st.session_state.data["desc"]:
            st.session_state.step = 2
            st.rerun()
        else: st.error("Пожалуйста, заполните обязательные поля!")

elif st.session_state.step == 2:
    st.markdown("### 🎨 Визуальная стратегия")
    themes = ["Черный Бриллиант", "Техно Синий", "Неоновый Зеленый", "Королевский Золотой"]
    # Проверка, чтобы не было ошибки выбора
    current_theme = st.session_state.data["theme"]
    if current_theme not in themes: current_theme = themes[0]
    
    st.session_state.data["theme"] = st.select_slider("Выберите атмосферу", options=themes, value=current_theme)
    st.session_state.data["style"] = st.radio("Стиль интерфейса", ["Минимализм", "Футуризм", "Деловой", "Яркий"], horizontal=True)
    
    col1, col2 = st.columns(2)
    if col1.button("← НАЗАД"): st.session_state.step = 1; st.rerun()
    if col2.button("ДАЛЕЕ →"): st.session_state.step = 3; st.rerun()

elif st.session_state.step == 3:
    st.markdown("### ⚙️ Технические параметры")
    st.session_state.data["pays"] = st.multiselect("Методы оплаты", ["Криптовалюты", "Банковские карты", "Электронные чеки"], default=st.session_state.data["pays"])
    st.session_state.data["security"] = st.toggle("Максимальный уровень защиты данных", value=st.session_state.data["security"])
    
    col1, col2 = st.columns(2)
    if col1.button("← НАЗАД"): st.session_state.step = 2; st.rerun()
    if col2.button("СФОРМИРОВАТЬ ЭКСПЕРТНОЕ ТЗ"): st.session_state.step = 4; st.rerun()

elif st.session_state.step == 4:
    st.markdown("### ✨ Ваше профессиональное ТЗ готово")
    
    # СИЛЬНЫЙ ЭКСПЕРТНЫЙ ПРОМТ
    expert_prompt = f"""СИСТЕМНАЯ ИНСТРУКЦИЯ (SYSTEM PROMPT)
Ты — Ведущий Архитектор программного обеспечения и эксперт по продуктовому маркетингу. Твоя цель — реализовать проект на высшем уровне.

КОНТЕКСТ ПРОЕКТА:
- Бренд: {st.session_state.data['name']}
- Задача: {st.session_state.data['desc']}
- Аудитория: {st.session_state.data['aud']}

ДИЗАЙН И ИНТЕРФЕЙС:
- Основная визуальная тема: {st.session_state.data['theme']}
- Концепция UI: {st.session_state.data['style']} (фокус на удобство пользователя и конверсию).

ТЕХНИЧЕСКИЕ ТРЕБОВАНИЯ:
- Оплата: {", ".join(st.session_state.data['pays']) if st.session_state.data['pays'] else "Стандартная"}
- Безопасность: {"Продвинутое шифрование и защита от атак уровня Enterprise" if st.session_state.data['security'] else "Базовый уровень"}

ТВОЯ РОЛЬ:
1. Выдавай только оптимизированный, чистый и готовый к работе код.
2. При проектировании учитывай психологию продаж для сегмента "{st.session_state.data['aud']}".
3. Отвечай кратко, профессионально, без лишних вступлений.

ПЕРВОЕ ЗАДАНИЕ:
Предложи полную дорожную карту (Roadmap) разработки этого проекта. С чего начнем?"""

    st.markdown(f'<div class="result-area"><pre style="white-space: pre-wrap; font-size: 14px;">{expert_prompt}</pre></div>', unsafe_allow_html=True)
    
    st.write("")
    st.download_button("📥 СКАЧАТЬ ПРОМТ (.TXT)", expert_prompt)
    if st.button("🔄 НАЧАТЬ НОВЫЙ ПРОЕКТ"):
        st.session_state.step = 1
        st.rerun()

st.markdown("<br><center style='color: #333; font-size: 0.8rem;'>© 2024 Premium AI System</center>", unsafe_allow_html=True)
