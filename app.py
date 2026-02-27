import streamlit as st

# 1. КОНФИГУРАЦИЯ И ЯДЕРНЫЙ CSS ДЛЯ ОЧИСТКИ
st.set_page_config(page_title="AI Architecture PRO 2026", page_icon="💎", layout="centered")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap');
    
    /* 1. УЛЬТРА-ОЧИСТКА (МЕТОД ТЕРМИНАТОРА) */
    /* Скрываем всё через официальные ID тестов Streamlit */
    [data-testid="stViewerBadge"], 
    [data-testid="stHeader"], 
    [data-testid="stDecoration"], 
    [data-testid="stStatusWidget"],
    footer, .stDeployButton {
        display: none !important;
        max-height: 0px !important;
        visibility: hidden !important;
        opacity: 0 !important;
    }

    /* Создаем физическую черную "заплатку" в правом нижнем углу экрана */
    /* Это перекроет кнопку, даже если она принудительно вылезет */
    .stApp::after {
        content: "";
        position: fixed;
        bottom: 0;
        right: 0;
        width: 200px;
        height: 50px;
        background: #000000 !important;
        z-index: 999999;
    }

    /* 2. ГЛАВНЫЙ ПРЕМИУМ-СТИЛЬ */
    .stApp { 
        background-color: #000000 !important; 
        color: #ffffff !important; 
        font-family: 'Inter', sans-serif; 
    }
    
    /* Фикс для видимости всех текстов */
    .stMarkdown, p, label, .stSelectbox, .stTextInput, .stTextArea {
        color: white !important;
    }

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
        color: #444 !important;
        font-size: 0.9rem;
        margin-bottom: 40px;
        text-transform: uppercase;
        letter-spacing: 3px;
    }

    /* Стили полей ввода */
    div[data-baseweb="input"], div[data-baseweb="textarea"] {
        border: 1px solid #222 !important;
        border-radius: 16px !important;
        background-color: #050505 !important;
    }

    /* Кнопки навигации (Неон) */
    .stButton > button {
        background: linear-gradient(90deg, #00f2ea, #0072ff) !important;
        color: white !important;
        border: none !important;
        border-radius: 14px !important;
        height: 60px;
        width: 100%;
        font-weight: 900 !important;
        text-transform: uppercase;
    }

    /* Кнопка СКАЧАТЬ (Белая с неоновой рамкой) */
    .stDownloadButton > button {
        background: #ffffff !important;
        color: #000000 !important;
        border: 2px solid #00f2ea !important;
        border-radius: 14px !important;
        height: 75px !important;
        width: 100% !important;
        font-weight: 900 !important;
        font-size: 1.3rem !important;
        text-transform: uppercase !important;
        box-shadow: 0 0 30px rgba(0, 242, 234, 0.4) !important;
    }

    .result-box {
        background: #080808;
        border: 1px solid #222;
        border-radius: 20px;
        padding: 30px;
        font-family: 'Consolas', monospace;
        color: #eee;
        line-height: 1.6;
        border-left: 5px solid #00f2ea;
    }

    .instruction-card {
        background: #0a0a0a;
        border: 1px solid #1ed760;
        border-radius: 15px;
        padding: 25px;
        margin-top: 30px;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. ЛОГИКА
if 'step' not in st.session_state: st.session_state.step = 1
if 'data' not in st.session_state:
    st.session_state.data = {
        "name": "", "price": "1000", "header": "", "sub": "", "desc": "", 
        "features": "", "img_link": "", "theme_color": "#000000", 
        "accent_color": "#00f2ea", "admin_pass": "SecureKey2026!", "pays": ["ЮMoney"]
    }

# --- КОНТЕНТ ---
st.markdown('<div class="main-title">AI ARCHITECT PRO</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Premium Enterprise Generation System</div>', unsafe_allow_html=True)

# ШАГ 1
if st.session_state.step == 1:
    st.markdown("### 💎 01. Продукт и Контекст")
    st.session_state.data["name"] = st.text_input("Название проекта/бренда", value=st.session_state.data["name"])
    st.session_state.data["header"] = st.text_input("Главный оффер (Заголовок H1)", value=st.session_state.data["header"])
    st.session_state.data["sub"] = st.text_input("Подзаголовок (УТП)", value=st.session_state.data["sub"])
    st.session_state.data["desc"] = st.text_area("Детальное описание продукта", value=st.session_state.data["desc"], height=100)
    st.session_state.data["img_link"] = st.text_input("Ссылка на референс изображения", value=st.session_state.data["img_link"])
    st.session_state.data["features"] = st.text_area("Преимущества (списком)", value=st.session_state.data["features"])
    st.session_state.data["price"] = st.text_input("Цена в рублях", value=st.session_state.data["price"])
    
    if st.button("ПЕРЕЙТИ К ТЕХНИЧЕСКИМ НАСТРОЙКАМ →"):
        if st.session_state.data["name"] and st.session_state.data["header"]:
            st.session_state.step = 2
            st.rerun()

# ШАГ 2
elif st.session_state.step == 2:
    st.markdown("### 🎨 02. Визуальная стратегия")
    col1, col2 = st.columns(2)
    with col1:
        st.session_state.data["theme_color"] = st.color_picker("Фон", value=st.session_state.data["theme_color"])
    with col2:
        st.session_state.data["accent_color"] = st.color_picker("Акцент", value=st.session_state.data["accent_color"])
    
    st.session_state.data["admin_pass"] = st.text_input("Пароль админа", value=st.session_state.data["admin_pass"])
    
    c1, c2 = st.columns(2)
    if c1.button("← НАЗАД"): st.session_state.step = 1; st.rerun()
    if c2.button("К ОПЛАТЕ →"): st.session_state.step = 3; st.rerun()

# ШАГ 3
elif st.session_state.step == 3:
    st.markdown("### 💳 03. Платёжные шлюзы")
    st.session_state.data["pays"] = st.multiselect("Выберите системы", 
                                                ["ЮMoney (Quickpay)", "NowPayments (Крипто)", "Stripe", "PayPal"], 
                                                default=["ЮMoney (Quickpay)"])
    c1, c2 = st.columns(2)
    if c1.button("← НАЗАД"): st.session_state.step = 2; st.rerun()
    if c2.button("⚡ ГЕНЕРИРОВАТЬ ЭКСПЕРТНОЕ ТЗ"): st.session_state.step = 4; st.rerun()

# ШАГ 4
elif st.session_state.step == 4:
    st.markdown("### 🚀 ВАША СИСТЕМНАЯ ИНСТРУКЦИЯ ГОТОВА")
    
    d = st.session_state.data
    
    expert_prompt = f"""Ты — Senior Full-Stack Architect и CTO с 15-летним опытом.

ЗАДАЧА: Спроектировать высококонверсионный магазин "{d['name']}". 
ПРАВИЛО: На запрос "создай [имя файла]" выдавай ТОЛЬКО чистый код без пояснений.

БИЗНЕС-ДАННЫЕ:
- Продукт: {d['name']} | Цена: {d['price']} RUB
- Оффер: {d['header']} | {d['sub']}
- Референс: {d['img_link']}
- Плюсы: {d['features'].replace('\\n', ', ')}

СТЕК: PHP 8.1, SQLite3, Tailwind CSS (CDN).
ФАЙЛЫ: index.php, config.php, admin.php (pass: {d['admin_pass']}), thank_you.php, callback.php.
ОПЛАТА: {", ".join(d['pays'])}. Проверка SHA-1/HMAC обязательна.
ВИЗУАЛ: Фон {d['theme_color']}, Акцент {d['accent_color']}, стиль Минимализм.

ПЕРВАЯ МИССИЯ: Проанализируй данные и предложи структуру БД. Жди команды для config.php."""

    st.markdown('<div class="result-box">', unsafe_allow_html=True)
    st.code(expert_prompt, language="text")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown(f"""
    <div class="instruction-card">
        <h4 style="color:#1ed760; margin:0 0 10px 0;">📋 ИНСТРУКЦИЯ ДЛЯ КЛИЕНТА:</h4>
        <p style="font-size:0.9rem; margin:0; color:#ddd;">
            1. Скопируйте текст из черного блока выше.<br>
            2. Отправьте его первым сообщением в <b>ChatGPT-4</b> или <b>Claude 3.5</b>.<br>
            3. После подтверждения пишите ИИ: <b>"Создай файл config.php"</b>, а затем остальные файлы по списку.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.write("")
    st.download_button(
        label="📥 СКАЧАТЬ ЭКСПЕРТНЫЙ ПРОМТ (ТЗ)",
        data=expert_prompt,
        file_name=f"Expert_TZ_{d['name']}.txt",
        mime="text/plain"
    )
    
    if st.button("🔄 НОВЫЙ ПРОЕКТ"):
        st.session_state.step = 1
        st.rerun()

st.markdown("<br><center style='color: #444;'>💎 PREMIUM AI ARCHITECT SYSTEM | v.4.5 | 2026</center>", unsafe_allow_html=True)
