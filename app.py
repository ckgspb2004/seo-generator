import streamlit as st
import streamlit.components.v1 as components

# 1. КОНФИГУРАЦИЯ
st.set_page_config(page_title="AI Architecture PRO 2026", page_icon="💎", layout="centered")

# 2. ИНЪЕКЦИЯ СКРИПТА-УБИЙЦЫ (JavaScript)
# Этот скрипт будет искать и удалять элементы Streamlit каждые 100мс
components.html(
    """
    <script>
    const removeStreamlitBranding = () => {
        // Убираем корону (Deploy button)
        const deployBtn = window.parent.document.querySelector(".stDeployButton");
        if (deployBtn) deployBtn.remove();

        // Убираем футер (Hosted with Streamlit)
        const footer = window.parent.document.querySelector("footer");
        if (footer) footer.remove();

        // Убираем Badge (красную кнопку в углу)
        const badges = window.parent.document.querySelectorAll('[data-testid="stViewerBadge"]');
        badges.forEach(badge => badge.remove());
        
        const toolbar = window.parent.document.querySelector('div[class*="stToolbar"]');
        if (toolbar) toolbar.remove();
    };
    
    // Запускаем цикл проверки
    setInterval(removeStreamlitBranding, 100);
    </script>
    """,
    height=0,
)

# 3. CSS ДЛЯ ВЕРСТКИ
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap');
    
    /* Скрываем всё через CSS (дублирующий слой) */
    #MainMenu {visibility: hidden !important;}
    header {visibility: hidden !important;}
    footer {visibility: hidden !important;}
    .stDeployButton {display:none !important;}
    [data-testid="stViewerBadge"] {display: none !important;}

    /* ГЛАВНЫЙ СТИЛЬ */
    .stApp { 
        background-color: #000000 !important; 
        color: #ffffff !important; 
        font-family: 'Inter', sans-serif; 
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

    /* Поля ввода */
    div[data-baseweb="input"], div[data-baseweb="textarea"] {
        border: 1px solid #222 !important;
        border-radius: 16px !important;
        background-color: #050505 !important;
    }

    /* Кнопки */
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

# 4. ЛОГИКА
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

if st.session_state.step == 1:
    st.markdown("### 💎 01. Информация о продукте")
    st.session_state.data["name"] = st.text_input("Название проекта/бренда", value=st.session_state.data["name"])
    st.session_state.data["header"] = st.text_input("Главный оффер (Заголовок H1)", value=st.session_state.data["header"])
    st.session_state.data["sub"] = st.text_input("Подзаголовок (УТП)", value=st.session_state.data["sub"])
    st.session_state.data["desc"] = st.text_area("Детальное описание продукта", value=st.session_state.data["desc"], height=100)
    st.session_state.data["img_link"] = st.text_input("Ссылка на изображение товара", value=st.session_state.data["img_link"])
    st.session_state.data["features"] = st.text_area("Преимущества (списком)", value=st.session_state.data["features"])
    st.session_state.data["price"] = st.text_input("Цена товара (RUB)", value=st.session_state.data["price"])
    
    if st.button("ДАЛЕЕ →"):
        if st.session_state.data["name"] and st.session_state.data["header"]:
            st.session_state.step = 2
            st.rerun()

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
    if c2.button("ДАЛЕЕ →"): st.session_state.step = 3; st.rerun()

elif st.session_state.step == 3:
    st.markdown("### 💳 03. Платёжные шлюзы")
    st.session_state.data["pays"] = st.multiselect("Выберите системы", 
                                                ["ЮMoney (Quickpay)", "NowPayments (Крипто)", "Stripe", "PayPal"], 
                                                default=["ЮMoney (Quickpay)"])
    c1, c2 = st.columns(2)
    if c1.button("← НАЗАД"): st.session_state.step = 2; st.rerun()
    if c2.button("⚡ СГЕНЕРИРОВАТЬ ЭКСПЕРТНОЕ ТЗ"): st.session_state.step = 4; st.rerun()

elif st.session_state.step == 4:
    st.markdown("### 🚀 ВАШ ЭКСПЕРТНЫЙ ПРОМТ ГОТОВ")
    d = st.session_state.data
    expert_prompt = f"""Ты — Senior Full-Stack Architect и CTO с 15-летним опытом разработки.
ЗАДАЧА: Спроектировать высококонверсионный магазин "{d['name']}". 
ИНСТРУКЦИЯ: На запрос "создай [имя файла]" выдавай ТОЛЬКО чистый код без пояснений.
БИЗНЕС-ДАННЫЕ: {d['name']} | Цена: {d['price']} RUB.
ОФФЕР: {d['header']} | {d['sub']}.
ТЕХНИЧЕСКИЙ СТЕК: PHP 8.1, SQLite3, Tailwind CSS.
ОПЛАТА: {", ".join(d['pays'])}. Проверка подписи обязательна."""

    st.markdown('<div class="result-box">', unsafe_allow_html=True)
    st.code(expert_prompt, language="text")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown(f"""
    <div class="instruction-card">
        <h4 style="color:#1ed760; margin:0 0 10px 0;">📋 ИНСТРУКЦИЯ ДЛЯ КЛИЕНТА:</h4>
        <p style="font-size:0.9rem; margin:0; color:#ddd;">
            1. Скопируйте текст из черного блока выше.<br>
            2. Отправьте его первым сообщением в <b>ChatGPT-4</b> или <b>Claude 3.5</b>.<br>
            3. После подтверждения пишите ИИ: <b>"Создай файл config.php"</b>.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.write("")
    st.download_button(label="📥 СКАЧАТЬ ЭКСПЕРТНЫЙ ПРОМТ (ТЗ)", data=expert_prompt, file_name=f"Expert_TZ_{d['name']}.txt", mime="text/plain")
    
    if st.button("🔄 НОВЫЙ ПРОЕКТ"):
        st.session_state.step = 1
        st.rerun()

st.markdown("<br><center style='color: #444;'>💎 PREMIUM AI ARCHITECT SYSTEM | v.4.5 | 2026</center>", unsafe_allow_html=True)
