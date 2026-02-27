import streamlit as st

# 1. КОНФИГУРАЦИЯ И УЛЬТРА-ДИЗАЙН
st.set_page_config(page_title="AI Architecture PRO 2026", page_icon="💎", layout="centered")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap');
    
    .stApp { background-color: #000000; color: #ffffff; font-family: 'Inter', sans-serif; }
    
    /* Градиентный заголовок */
    .main-title {
        text-align: center;
        background: linear-gradient(to right, #00f2ea, #00ff41, #7000ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 3.5rem;
        font-weight: 900;
        letter-spacing: -2px;
        margin-bottom: 5px;
    }
    
    .subtitle {
        text-align: center;
        color: #555;
        font-size: 1rem;
        margin-bottom: 40px;
        text-transform: uppercase;
        letter-spacing: 2px;
    }

    /* Стилизация полей ввода */
    div[data-baseweb="input"], div[data-baseweb="textarea"] {
        border: 1px solid #1a1a1a !important;
        border-radius: 16px !important;
        background-color: #050505 !important;
        transition: 0.3s;
    }
    div[data-baseweb="input"]:focus-within {
        border-color: #00f2ea !important;
        box-shadow: 0 0 20px rgba(0, 242, 234, 0.1);
    }

    /* Кнопки навигации */
    .stButton > button {
        background: linear-gradient(90deg, #00f2ea, #0072ff) !important;
        color: white !important;
        border: none !important;
        border-radius: 14px !important;
        height: 60px;
        width: 100%;
        font-weight: 900 !important;
        font-size: 1.1rem !important;
        text-transform: uppercase;
        letter-spacing: 1px;
        transition: 0.4s;
    }
    .stButton > button:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 30px rgba(0, 242, 234, 0.6);
    }

    /* Кнопка СКАЧАТЬ (Исправленная видимость текста) */
    .stDownloadButton > button {
        background: #ffffff !important;
        color: #000000 !important;
        border: 2px solid #00f2ea !important;
        border-radius: 14px !important;
        height: 70px !important;
        width: 100% !important;
        font-weight: 900 !important;
        font-size: 1.2rem !important;
        text-transform: uppercase !important;
        margin-top: 20px !important;
    }
    .stDownloadButton > button:hover {
        background: #00f2ea !important;
        color: #000000 !important;
    }

    /* Контейнер результата */
    .result-container {
        background: #080808;
        border: 1px solid #1a1a1a;
        border-radius: 20px;
        padding: 30px;
        margin-top: 20px;
        line-height: 1.6;
    }

    footer {visibility: hidden;}
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# 2. ЛОГИКА
if 'step' not in st.session_state: st.session_state.step = 1
if 'data' not in st.session_state:
    st.session_state.data = {
        "name": "", "price": "1000", "header": "", "sub": "", "desc": "", 
        "features": "", "cta": "ПОЛУЧИТЬ ДОСТУП", "img_link": "", 
        "theme": "#000000", "accent": "#00f2ea", "admin_pass": "SecurePass99#",
        "pays": ["ЮMoney (API)"]
    }

def next_step(): st.session_state.step += 1
def prev_step(): st.session_state.step -= 1

# --- ШАПКА ---
st.markdown('<div class="main-title">AI PRO GEN</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Система генерации экспертных инструкций</div>', unsafe_allow_html=True)

# --- ШАГ 1: МАРКЕТИНГ ---
if st.session_state.step == 1:
    st.markdown("### 💎 01. Концепция и Контент")
    st.session_state.data["name"] = st.text_input("Название бренда/проекта", value=st.session_state.data["name"])
    st.session_state.data["header"] = st.text_input("Убойный заголовок (H1)", placeholder="Например: Твой бизнес на автопилоте")
    st.session_state.data["sub"] = st.text_input("Подзаголовок", placeholder="Сделаем всё за 24 часа...")
    st.session_state.data["desc"] = st.text_area("Полное описание продукта", height=100)
    st.session_state.data["img_link"] = st.text_input("Ссылка на картинку товара или референс", placeholder="https://site.ru/image.jpg")
    st.session_state.data["features"] = st.text_area("Список преимуществ (каждое с новой строки)")
    st.session_state.data["price"] = st.text_input("Стоимость (в рублях)", value=st.session_state.data["price"])
    
    if st.button("ПЕРЕЙТИ К ДИЗАЙНУ →"):
        if st.session_state.data["name"] and st.session_state.data["header"]:
            next_step()
            st.rerun()
        else: st.error("Заполните название и заголовок!")

# --- ШАГ 2: ВИЗУАЛ ---
elif st.session_state.step == 2:
    st.markdown("### 🎨 02. Визуальный код")
    col1, col2 = st.columns(2)
    with col1:
        st.session_state.data["theme"] = st.color_picker("Цвет фона", value=st.session_state.data["theme"])
    with col2:
        st.session_state.data["accent"] = st.color_picker("Цвет кнопок", value=st.session_state.data["accent"])
    
    st.session_state.data["admin_pass"] = st.text_input("Мастер-пароль админа", value=st.session_state.data["admin_pass"])
    
    st.write("")
    c1, c2 = st.columns(2)
    with c1: 
        if st.button("← НАЗАД"): prev_step(); st.rerun()
    with c2: 
        if st.button("К ПЛАТЕЖАМ →"): next_step(); st.rerun()

# --- ШАГ 3: ИНТЕГРАЦИИ ---
elif st.session_state.step == 3:
    st.markdown("### 💳 03. Платёжные шлюзы")
    st.session_state.data["pays"] = st.multiselect("Выберите методы оплаты", 
                                                ["ЮMoney (API)", "NowPayments (Крипто)", "Stripe", "PayPal"], 
                                                default=["ЮMoney (API)"])
    
    st.write("")
    c1, c2 = st.columns(2)
    with c1: 
        if st.button("← НАЗАД"): prev_step(); st.rerun()
    with c2: 
        if st.button("⚡ СОЗДАТЬ ФИНАЛЬНЫЙ ПРОМТ"): next_step(); st.rerun()

# --- ШАГ 4: РЕЗУЛЬТАТ ---
elif st.session_state.step == 4:
    st.markdown("### 🚀 ВАШ ЭКСПЕРТНЫЙ ПРОМТ ГОТОВ")
    
    d = st.session_state.data
    
    expert_prompt = f"""Ты — Senior Full-Stack разработчик и Архитектор систем.

ЗАДАЧА
Спроектировать магазин "{d['name']}". 
На мой запрос "создай [имя файла]" выдавай ТОЛЬКО чистый код без пояснений.

ДАННЫЕ ПРОЕКТА
- Бренд: {d['name']}
- Цена товара: {d['price']} RUB

МАРКЕТИНГ
Заголовок: {d['header']}
Подзаголовок: {d['sub']}
Описание: {d['desc']}
Изображение: {d['img_link'] if d['img_link'] else 'standard_placeholder.jpg'}
Преимущества:
{chr(10).join([f'- {line}' for line in d['features'].splitlines()])}

ТЕХНИЧЕСКИЙ СТЕК
- PHP 8.1+, SQLite3, Tailwind CSS, Mobile-first.

ФАЙЛЫ
index.php, thank_you.php, admin.php (пароль: {d['admin_pass']}), config.php, callback.php.

ДИЗАЙН
Фон: {d['theme']} | Акцент: {d['accent']} | Стиль: Премиальный минимализм.
"""

    st.markdown('<div class="result-container">', unsafe_allow_html=True)
    st.code(expert_prompt, language="text")
    st.markdown('</div>', unsafe_allow_html=True)

    st.info("""
    👉 **ИНСТРУКЦИЯ:**
    1. Скопируйте текст выше.
    2. Вставьте в ChatGPT-4 или Claude 3.5.
    3. Пишите нейросети: **"Создай config.php"**, а затем остальные файлы.
    """)

    # КНОПКА СКАЧИВАНИЯ С ВИДИМЫМ ТЕКСТОМ
    st.download_button(
        label="📥 СКАЧАТЬ ГОТОВОЕ ТЗ (ПРОМТ)",
        data=expert_prompt,
        file_name=f"PRO_TZ_{d['name']}.txt",
        mime="text/plain"
    )
    
    if st.button("🔄 СОЗДАТЬ НОВЫЙ ПРОЕКТ"):
        st.session_state.step = 1
        st.rerun()

st.markdown("<br><center style='color: #444;'>💎 PREMIUM AI SYSTEM 2026</center>", unsafe_allow_html=True)
