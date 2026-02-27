import streamlit as st

# 1. КОНФИГУРАЦИЯ И ПРЕМИУМ-СТИЛЬ
st.set_page_config(page_title="AI Architecture PRO 2026", page_icon="💎", layout="centered")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap');
    
    .stApp { background-color: #000000; color: #ffffff; font-family: 'Inter', sans-serif; }
    
    /* Тройной градиент для заголовка */
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

    /* Стилизация ввода */
    div[data-baseweb="input"], div[data-baseweb="textarea"] {
        border: 1px solid #1a1a1a !important;
        border-radius: 16px !important;
        background-color: #050505 !important;
    }
    
    /* Кнопки навигации с неоновым свечением */
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
    .stButton > button:hover {
        box-shadow: 0 8px 30px rgba(0, 242, 234, 0.5);
        transform: translateY(-2px);
    }

    /* Кнопка СКАЧАТЬ (Черный текст на Белом фоне) */
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
        box-shadow: 0 0 20px rgba(0, 242, 234, 0.3) !important;
    }

    /* Окно с Промтом */
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

    /* Блок инструкции */
    .instruction-card {
        background: linear-gradient(135deg, #0a0a0a 0%, #111 100%);
        border: 1px solid #222;
        border-radius: 15px;
        padding: 25px;
        margin-top: 30px;
    }

    footer {visibility: hidden;}
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# 2. ЛОГИКА И СОХРАНЕНИЕ
if 'step' not in st.session_state: st.session_state.step = 1
if 'data' not in st.session_state:
    st.session_state.data = {
        "name": "", "price": "1000", "header": "", "sub": "", "desc": "", 
        "features": "", "cta": "ПОДТВЕРДИТЬ И ЗАКАЗАТЬ", "img_link": "", 
        "theme_name": "Deep Black", "theme_color": "#000000", "accent_color": "#00f2ea", 
        "admin_pass": "MasterKey2026!", "pays": ["ЮMoney (Quickpay)"]
    }

def next_step(): st.session_state.step += 1
def prev_step(): st.session_state.step -= 1

# --- ШАПКА ---
st.markdown('<div class="main-title">AI ARCHITECT PRO</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Enterprise Level Generation System</div>', unsafe_allow_html=True)

# --- ШАГ 1: БИЗНЕС И МАРКЕТИНГ ---
if st.session_state.step == 1:
    st.markdown("### 💎 01. Информация о продукте")
    st.session_state.data["name"] = st.text_input("Название проекта/бренда", value=st.session_state.data["name"])
    st.session_state.data["header"] = st.text_input("Главный оффер (Заголовок H1)", value=st.session_state.data["header"], placeholder="Например: Премиальная плитка из Италии с доставкой")
    st.session_state.data["sub"] = st.text_input("Подзаголовок (УТП)", value=st.session_state.data["sub"])
    st.session_state.data["desc"] = st.text_area("Детальное описание продукта", value=st.session_state.data["desc"], height=100)
    st.session_state.data["img_link"] = st.text_input("Ссылка на изображение или референс дизайна", value=st.session_state.data["img_link"], placeholder="https://example.com/product.jpg")
    st.session_state.data["features"] = st.text_area("Преимущества (по одному в строке)", value=st.session_state.data["features"])
    st.session_state.data["price"] = st.text_input("Цена товара (в рублях)", value=st.session_state.data["price"])
    
    st.write("")
    if st.button("ПЕРЕЙТИ К ТЕХНИЧЕСКИМ НАСТРОЙКАМ →"):
        if st.session_state.data["name"] and st.session_state.data["header"]:
            next_step()
            st.rerun()
        else: st.error("Заполните название и заголовок!")

# --- ШАГ 2: ВИЗУАЛ И БЕЗОПАСНОСТЬ ---
elif st.session_state.step == 2:
    st.markdown("### 🎨 02. Визуальная стратегия и Доступ")
    col1, col2 = st.columns(2)
    with col1:
        st.session_state.data["theme_color"] = st.color_picker("Основной фон", value=st.session_state.data["theme_color"])
    with col2:
        st.session_state.data["accent_color"] = st.color_picker("Акцент (кнопки)", value=st.session_state.data["accent_color"])
    
    st.session_state.data["admin_pass"] = st.text_input("Пароль от панели управления", value=st.session_state.data["admin_pass"])
    
    st.write("")
    c1, c2 = st.columns(2)
    with c1: 
        if st.button("← НАЗАД"): prev_step(); st.rerun()
    with c2: 
        if st.button("К ВЫБОРУ ОПЛАТЫ →"): next_step(); st.rerun()

# --- ШАГ 3: ИНТЕГРАЦИИ ---
elif st.session_state.step == 3:
    st.markdown("### 💳 03. Финансовые системы")
    st.session_state.data["pays"] = st.multiselect("Выберите методы оплаты для интеграции", 
                                                ["ЮMoney (API/Quickpay)", "NowPayments (Крипто)", "Stripe", "PayPal"], 
                                                default=["ЮMoney (API/Quickpay)"])
    
    st.write("")
    c1, c2 = st.columns(2)
    with c1: 
        if st.button("← НАЗАД"): prev_step(); st.rerun()
    with c2: 
        if st.button("⚡ СФОРМИРОВАТЬ ЭКСПЕРТНЫЙ ПРОМТ"): next_step(); st.rerun()

# --- ШАГ 4: ФИНАЛЬНЫЙ РЕЗУЛЬТАТ ---
elif st.session_state.step == 4:
    st.markdown("### 🚀 ВАША СИСТЕМНАЯ ИНСТРУКЦИЯ ГОТОВА")
    
    d = st.session_state.data
    
    # МОЩНЕЙШИЙ ПРОФЕССИОНАЛЬНЫЙ ПРОМТ
    expert_prompt = f"""Ты — Senior Full-Stack Architect и CTO с 15-летним опытом разработки e-commerce систем. Твоя задача — создать безупречный, безопасный и высококонверсионный онлайн-магазин.

### РОЛЬ И ПОВЕДЕНИЕ
- Ты работаешь в режиме пошагового создания файлов.
- На каждый запрос "создай [имя файла]" выдавай ТОЛЬКО чистый код без вступительных фраз и пояснений.
- Используй современные стандарты безопасности (защита от SQL-инъекций, XSS, проверка CSRF).

### КОНТЕКСТ ПРОЕКТА
- **Название:** {d['name']}
- **Продукт:** {d['desc']}
- **Цена:** {d['price']} RUB

### МАРКЕТИНГОВАЯ СТРУКТУРА
- **H1:** {d['header']}
- **Sub:** {d['sub']}
- **Изображение:** {d['img_link'] if d['img_link'] else 'standard_placeholder.jpg'}
- **Преимущества:**
{chr(10).join([f'  * {line}' for line in d['features'].splitlines()])}

### ТЕХНИЧЕСКИЙ СТЕК
- **Backend:** Native PHP 8.1+ (без тяжелых фреймворков).
- **Database:** SQLite3 (автоматическая инициализация таблиц при первом запуске).
- **Frontend:** HTML5, Modern JS, Tailwind CSS (через CDN).
- **Архитектура:** Mobile-first, чистая типографика, премиальные отступы.

### ФАЙЛОВАЯ СТРУКТУРА
1. **index.php** — продающий лендинг с высокой конверсией.
2. **config.php** — глобальные настройки, ключи оплаты и пароль админа ({d['admin_pass']}).
3. **admin.php** — защищенная панель (статистика заказов, управление ценой и файлами).
4. **thank_you.php** — страница после оплаты с защищенной ссылкой на скачивание.
5. **callback.php** — обработчик платежных уведомлений ({", ".join(d['pays'])}).

### ТРЕБОВАНИЯ К ДИЗАЙНУ
- **Фон:** {d['theme_color']}
- **Акцент:** {d['accent_color']}
- **Стиль:** Премиальный минимализм, использование subtle shadows и плавных переходов.

### ПЕРВАЯ МИССИЯ
Проанализируй вводные данные. Предложи оптимальную структуру базы данных и архитектуру взаимодействия файлов. Жди моей команды для генерации кода config.php."""

    st.markdown('<div class="result-box">', unsafe_allow_html=True)
    st.code(expert_prompt, language="text")
    st.markdown('</div>', unsafe_allow_html=True)

    # ПОДРОБНАЯ ИНСТРУКЦИЯ
    st.markdown(f"""
    <div class="instruction-card">
        <h4 style="color:#00f2ea; margin-top:0;">📋 ИНСТРУКЦИЯ ПО ЗАПУСКУ:</h4>
        <ol style="font-size:0.95rem; line-height:1.6;">
            <li>Нажмите на иконку копирования в правом верхнем углу блока с текстом выше.</li>
            <li>Откройте <b>ChatGPT</b> (рекомендуется GPT-4o) или <b>Claude 3.5 Sonnet</b>.</li>
            <li>Отправьте этот текст первым сообщением. Это "обучит" нейросеть вашему проекту.</li>
            <li>Когда ИИ ответит, напишите ему: <b>"Создай файл config.php"</b>.</li>
            <li>Затем по очереди запрашивайте остальные файлы: index.php, admin.php и т.д.</li>
            <li>Полученный код сохраняйте в файлы с соответствующими названиями и загружайте на хостинг.</li>
        </ol>
    </div>
    """, unsafe_allow_html=True)

    st.write("")
    # ЯРКАЯ КНОПКА СКАЧИВАНИЯ
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
