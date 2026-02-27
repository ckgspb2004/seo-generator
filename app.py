import streamlit as st

# 1. КОНФИГУРАЦИЯ И УЛЬТРА-ДИЗАЙН
st.set_page_config(page_title="AI Architecture PRO", page_icon="💎", layout="centered")

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

    /* Подсвеченные кнопки */
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
        cursor: pointer;
        transition: 0.4s;
        box-shadow: 0 4px 15px rgba(0, 242, 234, 0.3);
    }
    .stButton > button:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 30px rgba(0, 242, 234, 0.6);
        filter: brightness(1.1);
    }

    /* Кнопка скачивания (особенная) */
    .download-btn {
        display: inline-block;
        padding: 20px 40px;
        background: #ffffff;
        color: #000000 !important;
        border-radius: 50px;
        font-weight: 900;
        text-decoration: none;
        text-align: center;
        margin-top: 20px;
        border: 2px solid #00f2ea;
        box-shadow: 0 0 20px rgba(255, 255, 255, 0.2);
    }

    /* Контейнер результата */
    .result-container {
        background: #080808;
        border: 1px solid #111;
        border-radius: 20px;
        padding: 30px;
        margin-top: 20px;
        line-height: 1.6;
    }

    /* Прячем стандартные элементы */
    footer {visibility: hidden;}
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# 2. ЛОГИКА ШАГОВ
if 'step' not in st.session_state: st.session_state.step = 1
if 'data' not in st.session_state:
    st.session_state.data = {
        "name": "", "price": "1000", "header": "", "sub": "", "desc": "", 
        "features": "", "cta": "ПОЛУЧИТЬ ДОСТУП", "img": "", 
        "theme": "#000000", "accent": "#00f2ea", "admin_pass": "SecurePass99#",
        "pays": ["ЮMoney"]
    }

def next_step(): st.session_state.step += 1
def prev_step(): st.session_state.step -= 1

# --- ШАПКА ---
st.markdown('<div class="main-title">AI PRO GEN</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">System Architecture & Marketing Generator</div>', unsafe_allow_html=True)

# --- ШАГ 1: МАРКЕТИНГ ---
if st.session_state.step == 1:
    st.markdown("### 💎 01. Концепция и Продажи")
    st.session_state.data["name"] = st.text_input("Название бренда/проекта", value=st.session_state.data["name"])
    st.session_state.data["header"] = st.text_input("Убойный заголовок (H1)", placeholder="Например: Твой бизнес на автопилоте")
    st.session_state.data["sub"] = st.text_input("Подзаголовок (выгода)", placeholder="Сделаем всё за 24 часа с гарантией...")
    st.session_state.data["desc"] = st.text_area("Полное описание продукта", height=100)
    st.session_state.data["features"] = st.text_area("Список преимуществ (каждое с новой строки)")
    st.session_state.data["price"] = st.text_input("Стоимость (в рублях)", value=st.session_state.data["price"])
    
    if st.button("ПЕРЕЙТИ К ДИЗАЙНУ →"):
        if st.session_state.data["name"] and st.session_state.data["header"]:
            next_step()
            st.rerun()
        else: st.error("Заполните название и заголовок!")

# --- ШАГ 2: ТЕХНИЧЕСКИЙ ВИЗУАЛ ---
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
    
    # ФОРМИРУЕМ МОЩНЫЙ ПРОМТ
    expert_prompt = f"""Ты — Senior Full-Stack разработчик и Архитектор систем. Твоя специализация — высоконагруженные e-commerce проекты.

ЗАДАЧА
Спроектировать и написать код для онлайн-магазина "{d['name']}". 
Работай в режиме пошаговой выдачи файлов. На мой запрос "создай [имя файла]" выдавай ТОЛЬКО чистый, оптимизированный код без лишних пояснений.

ДАННЫЕ ПРОЕКТА
- Бренд: {d['name']}
- Цена товара: {d['price']} RUB

МАРКЕТИНГОВАЯ СТРУКТУРА
Заголовок: {d['header']}
Подзаголовок: {d['sub']}
Описание: {d['desc']}
Преимущества:
{chr(10).join([f'- {line}' for line in d['features'].splitlines()])}
CTA кнопка: {d['cta']}

ТЕХНИЧЕСКИЙ СТЕК
- Язык: PHP 8.1+ (Native)
- База данных: SQLite3 (автоматическое создание таблиц)
- Стили: Tailwind CSS via CDN
- Верстка: Адаптивная, Mobile-first

АРХИТЕКТУРА ФАЙЛОВ
1. index.php — Лендинг с высокой конверсией
2. thank_you.php — Страница выдачи товара
3. admin.php — Панель управления (доступ: {d['admin_pass']})
4. config.php — Конфиг (БД, ключи, настройки)
5. callback.php — Обработчик платежей ({", ".join(d['pays'])})

ЛОГИКА ОПЛАТЫ И БЕЗОПАСНОСТИ
- Реализовать строгую проверку контрольной подписи (SHA-1/HMAC) для входящих уведомлений.
- Использовать подготовленные выражения SQL для защиты от инъекций.
- Все ключи и пароли хранить исключительно в config.php.

ДИЗАЙН
Фон: {d['theme']}
Акцент: {d['accent']}
Стиль: Премиальный минимализм, четкая типографика, плавные тени.

ОГРАНИЧЕНИЯ
- Никаких внешних зависимостей (composer не использовать).
- Код должен работать "из коробки" на любом shared-хостинге (Beget/Reg.ru).
"""

    st.markdown('<div class="result-container">', unsafe_allow_html=True)
    st.code(expert_prompt, language="text")
    st.markdown('</div>', unsafe_allow_html=True)

    # ИНСТРУКЦИЯ
    st.info("""
    👉 **ЧТО ДЕЛАТЬ ДАЛЬШЕ?**
    1. Скопируйте текст выше (иконка в углу рамки).
    2. Зайдите в **ChatGPT (версия GPT-4)** или **Claude 3.5 Sonnet**.
    3. Вставьте этот текст первым сообщением.
    4. Когда нейросеть подтвердит готовность, пишите ей: **"Создай config.php"**, а затем по очереди остальные файлы.
    """)

    # КНОПКА СКАЧИВАНИЯ
    st.download_button(
        label="📥 СКАЧАТЬ ТЗ ФАЙЛОМ",
        data=expert_prompt,
        file_name=f"TZ_{d['name']}.txt",
        mime="text/plain",
        help="Нажмите, чтобы сохранить ТЗ на компьютер"
    )
    
    if st.button("🔄 НОВЫЙ ПРОЕКТ"):
        st.session_state.step = 1
        st.rerun()

st.markdown("<br><center style='color: #222;'>💎 PREMIUM AI SYSTEM 2024</center>", unsafe_allow_html=True)
