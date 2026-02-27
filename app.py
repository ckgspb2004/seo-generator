import streamlit as st

# 1. КОНФИГУРАЦИЯ И ПРИНУДИТЕЛЬНАЯ ОЧИСТКА ИНТЕРФЕЙСА
st.set_page_config(page_title="AI Architecture PRO 2026", page_icon="💎", layout="centered")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap');
    
    /* 1. ПОЛНОЕ УДАЛЕНИЕ СЛУЖЕБНЫХ ЭЛЕМЕНТОВ STREAMLIT */
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    .stDeployButton {display:none;}
    [data-testid="stStatusWidget"] {display:none;}
    /* Убираем кнопку хостинга в правом нижнем углу */
    .viewerBadge_container__1QSob {display: none !important;}
    .viewerBadge_link__1S137 {display: none !important;}
    
    /* 2. ГЛАВНЫЙ СТИЛЬ */
    .stApp { background-color: #000000; color: #ffffff; font-family: 'Inter', sans-serif; }
    
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
        font-size: 0.9rem;
        margin-bottom: 40px;
        text-transform: uppercase;
        letter-spacing: 3px;
    }

    div[data-baseweb="input"], div[data-baseweb="textarea"] {
        border: 1px solid #1a1a1a !important;
        border-radius: 16px !important;
        background-color: #050505 !important;
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
        box-shadow: 0 4px 15px rgba(0, 242, 234, 0.2);
    }
    
    /* Кнопка СКАЧАТЬ (Яркая и заметная) */
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
        box-shadow: 0 0 25px rgba(0, 242, 234, 0.4) !important;
    }

    .result-box {
        background: #080808;
        border: 1px solid #222;
        border-radius: 20px;
        padding: 30px;
        font-family: 'Consolas', monospace;
        color: #e0e0e0;
        line-height: 1.5;
        border-left: 5px solid #00f2ea;
    }

    .instruction-card {
        background: linear-gradient(135deg, #0a0a0a 0%, #111 100%);
        border: 1px solid #222;
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
        "features": "", "cta": "ПОДТВЕРДИТЬ И ЗАКАЗАТЬ", "img_link": "", 
        "theme_color": "#000000", "accent_color": "#00f2ea", 
        "admin_pass": "MasterKey2026!", "pays": ["ЮMoney (Quickpay)"]
    }

def next_step(): st.session_state.step += 1
def prev_step(): st.session_state.step -= 1

# --- ШАПКА ---
st.markdown('<div class="main-title">AI ARCHITECT PRO</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Enterprise Level Generation System</div>', unsafe_allow_html=True)

# --- ШАГ 1: БИЗНЕС ---
if st.session_state.step == 1:
    st.markdown("### 💎 01. Информация о продукте")
    st.session_state.data["name"] = st.text_input("Название проекта/бренда", value=st.session_state.data["name"])
    st.session_state.data["header"] = st.text_input("Главный оффер (Заголовок H1)", value=st.session_state.data["header"])
    st.session_state.data["sub"] = st.text_input("Подзаголовок (УТП)", value=st.session_state.data["sub"])
    st.session_state.data["desc"] = st.text_area("Детальное описание продукта", value=st.session_state.data["desc"], height=100)
    st.session_state.data["img_link"] = st.text_input("Ссылка на картинку или референс дизайна", value=st.session_state.data["img_link"])
    st.session_state.data["features"] = st.text_area("Преимущества (каждое с новой строки)", value=st.session_state.data["features"])
    st.session_state.data["price"] = st.text_input("Цена товара (в рублях)", value=st.session_state.data["price"])
    
    st.write("")
    if st.button("ПЕРЕЙТИ К ТЕХНИЧЕСКИМ НАСТРОЙКАМ →"):
        if st.session_state.data["name"] and st.session_state.data["header"]:
            next_step()
            st.rerun()
        else: st.error("Заполните обязательные поля!")

# --- ШАГ 2: ВИЗУАЛ ---
elif st.session_state.step == 2:
    st.markdown("### 🎨 02. Визуальная стратегия")
    col1, col2 = st.columns(2)
    with col1:
        st.session_state.data["theme_color"] = st.color_picker("Цвет фона", value=st.session_state.data["theme_color"])
    with col2:
        st.session_state.data["accent_color"] = st.color_picker("Цвет кнопок", value=st.session_state.data["accent_color"])
    
    st.session_state.data["admin_pass"] = st.text_input("Пароль администратора", value=st.session_state.data["admin_pass"])
    
    st.write("")
    c1, c2 = st.columns(2)
    with c1: 
        if st.button("← НАЗАД"): prev_step(); st.rerun()
    with c2: 
        if st.button("К ВЫБОРУ ОПЛАТЫ →"): next_step(); st.rerun()

# --- ШАГ 3: ОПЛАТА ---
elif st.session_state.step == 3:
    st.markdown("### 💳 03. Платёжные шлюзы")
    st.session_state.data["pays"] = st.multiselect("Выберите методы оплаты", 
                                                ["ЮMoney (API/Quickpay)", "NowPayments (Крипто)", "Stripe", "PayPal"], 
                                                default=["ЮMoney (API/Quickpay)"])
    st.write("")
    c1, c2 = st.columns(2)
    with c1: 
        if st.button("← НАЗАД"): prev_step(); st.rerun()
    with c2: 
        if st.button("⚡ СФОРМИРОВАТЬ ЭКСПЕРТНЫЙ ПРОМТ"): next_step(); st.rerun()

# --- ШАГ 4: ФИНАЛ ---
elif st.session_state.step == 4:
    st.markdown("### 🚀 ВАША СИСТЕМНАЯ ИНСТРУКЦИЯ ГОТОВА")
    
    d = st.session_state.data
    
    expert_prompt = f"""Ты — Senior Full-Stack Architect и CTO с 15-летним опытом.

ЗАДАЧА
Создать высококонверсионный магазин "{d['name']}". 
На мой запрос "создай [имя файла]" выдавай ТОЛЬКО чистый код без пояснений.

ДАННЫЕ ПРОЕКТА
- Название: {d['name']} | Цена: {d['price']} RUB
- H1: {d['header']} | Sub: {d['sub']}
- Референс: {d['img_link'] if d['img_link'] else 'standard_placeholder.jpg'}
- Преимущества: {d['features'].replace('\\n', ', ')}

ТЕХНИЧЕСКИЙ СТЕК
PHP 8.1+, SQLite3, Tailwind CSS (CDN), Mobile-first.

СТРУКТУРА ФАЙЛОВ
index.php, config.php, admin.php (pass: {d['admin_pass']}), thank_you.php, callback.php.

ПЛАТЕЖИ
Интегрировать: {", ".join(d['pays'])}. Обязательна проверка контрольных подписей хэша.

ДИЗАЙН
Фон: {d['theme_color']} | Акцент: {d['accent_color']} | Стиль: Премиальный минимализм.

ПЕРВАЯ МИССИЯ
Проанализируй вводные данные. Предложи структуру БД и архитектуру. Жди моей команды для кода config.php."""

    st.markdown('<div class="result-box">', unsafe_allow_html=True)
    st.code(expert_prompt, language="text")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown(f"""
    <div class="instruction-card">
        <h4 style="color:#00f2ea; margin:0 0 10px 0;">📋 ИНСТРУКЦИЯ ПО ЗАПУСКУ:</h4>
        <p style="font-size:0.9rem; margin:0;">1. Скопируйте текст выше.<br>2. Отправьте его в ChatGPT-4 или Claude 3.5.<br>3. Пишите ИИ: <b>"Создай файл config.php"</b>, а затем остальные.</p>
    </div>
    """, unsafe_allow_html=True)

    st.write("")
    st.download_button(
        label="📥 СКАЧАТЬ ПОЛНОЕ ТЗ (ПРОМТ) НА КОМПЬЮТЕР",
        data=expert_prompt,
        file_name=f"Expert_TZ_{d['name']}.txt",
        mime="text/plain"
    )
    
    if st.button("🔄 СОЗДАТЬ НОВЫЙ ПРОЕКТ"):
        st.session_state.step = 1
        st.rerun()

st.markdown("<br><center style='color: #444;'>💎 PREMIUM AI ARCHITECT SYSTEM | v.4.2 | 2026</center>", unsafe_allow_html=True)
