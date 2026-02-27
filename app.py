import streamlit as st

# 1. КОНФИГУРАЦИЯ
st.set_page_config(page_title="AI TZ Expert v3.0", page_icon="💎", layout="centered")

# 2. КРУТОЙ ДИЗАЙН (Улучшенный черный + Центрирование)
st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #ffffff; }
    .main-title {
        text-align: center;
        background: linear-gradient(90deg, #00f2ea, #00ff41);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 3.5rem; font-weight: 900; margin-bottom: 5px;
    }
    .subtitle { text-align: center; color: #666; margin-bottom: 40px; font-size: 1.2rem; }
    
    div[data-baseweb="input"], div[data-baseweb="textarea"], div[data-baseweb="select"] {
        border: 1px solid #222 !important;
        border-radius: 15px !important;
        background-color: #050505 !important;
    }
    
    .step-node { text-align: center; padding: 15px; border-bottom: 2px solid #111; flex-grow: 1; color: #333; font-size: 0.9rem; }
    .step-node-active { color: #00f2ea; border-bottom: 2px solid #00f2ea; }
    
    .stButton > button {
        background: linear-gradient(135deg, #00f2ea 0%, #0072ff 100%) !important;
        color: white !important; border: none !important; width: 100%; border-radius: 12px !important;
        height: 55px; font-weight: bold !important; font-size: 1.1rem;
    }
    
    /* Оформление окна с результатом */
    .result-box {
        background-color: #0a0a0a;
        padding: 30px;
        border-radius: 20px;
        border: 1px dashed #00f2ea;
        font-family: 'Courier New', monospace;
        color: #d1d1d1;
        line-height: 1.6;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. ЛОГИКА
if 'step' not in st.session_state: st.session_state.step = 1
if 'data' not in st.session_state:
    st.session_state.data = {
        "name": "", "desc": "", "aud": "", "theme": "Deep Black", 
        "style": "Минимализм", "pays": [], "security": False
    }

# --- ШАПКА ---
st.markdown('<div class="main-title">AI ARCHITECT</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Генерация сверхточных системных инструкций</div>', unsafe_allow_html=True)

# ИНДИКАТОР
cols = st.columns(4)
names = ["Продукт", "Визуал", "Стек", "Финал"]
for i, n in enumerate(names):
    active = "step-node-active" if st.session_state.step == i+1 else ""
    cols[i].markdown(f'<div class="step-node {active}">{n}</div>', unsafe_allow_html=True)

st.write("")

# ШАГ 1
if st.session_state.step == 1:
    st.markdown("### 01. Контекст продукта")
    st.session_state.data["name"] = st.text_input("Название бизнеса", value=st.session_state.data["name"])
    st.session_state.data["desc"] = st.text_area("Суть предложения и УТП", value=st.session_state.data["desc"], height=120)
    st.session_state.data["aud"] = st.text_input("Портрет клиента", value=st.session_state.data["aud"])
    if st.button("ПРОДОЛЖИТЬ →"):
        if st.session_state.data["name"] and st.session_state.data["desc"]:
            st.session_state.step = 2
            st.rerun()

# ШАГ 2
elif st.session_state.step == 2:
    st.markdown("### 02. Визуальная стратегия")
    st.session_state.data["theme"] = st.select_slider("Атмосфера", options=["Black Luxe", "Tech Blue", "Organic Green", "Cyber Red"], value=st.session_state.data["theme"])
    st.session_state.data["style"] = st.radio("Стиль интерфейса", ["Clean UI (Минимализм)", "Glassmorphism (Футуризм)", "Classic Business", "High Contrast"], horizontal=True)
    col1, col2 = st.columns(2)
    if col1.button("← НАЗАД"): st.session_state.step = 1; st.rerun()
    if col2.button("ДАЛЕЕ →"): st.session_state.step = 3; st.rerun()

# ШАГ 3
elif st.session_state.step == 3:
    st.markdown("### 03. Технические требования")
    st.session_state.data["pays"] = st.multiselect("Финансовые интеграции", ["Crypto (BTC/USDT)", "Visa/Mastercard", "Stripe", "Apple/Google Pay"], default=st.session_state.data["pays"])
    st.session_state.data["security"] = st.toggle("Повышенный протокол безопасности данных", value=st.session_state.data["security"])
    col1, col2 = st.columns(2)
    if col1.button("← НАЗАД"): st.session_state.step = 2; st.rerun()
    if col2.button("СФОРМИРОВАТЬ ЭКСПЕРТНОЕ ТЗ"): st.session_state.step = 4; st.rerun()

# ШАГ 4 - РЕЗУЛЬТАТ С МОЩНЫМ ПРОМТОМ
elif st.session_state.step == 4:
    st.markdown("### 🔥 Ваш профессиональный System Prompt")
    
    # ВОТ ЗДЕСЬ МЫ СОЗДАЕМ МОЩНЫЙ ПРОМТ
    expert_prompt = f"""### SYSTEM ROLE
Ты — Senior Solution Architect и ведущий Full-stack разработчик с 15-летним опытом в e-commerce и Fintech. Твоя специализация — создание высококонверсионных, безопасных и масштабируемых цифровых экосистем.

### PROJECT CONTEXT
- **Бренд:** {st.session_state.data['name']}
- **Бизнес-задача:** {st.session_state.data['desc']}
- **Целевая аудитория:** {st.session_state.data['aud']}

### ARCHITECTURAL REQUIREMENTS
1. **Визуальный стек:** Реализовать стиль "{st.session_state.data['style']}" с использованием цветовой палитры "{st.session_state.data['theme']}". Фокус на UX: интуитивная навигация, скорость отклика < 200мс.
2. **Финансовый уровень:** Интеграция {", ".join(st.session_state.data['pays']) if st.session_state.data['pays'] else "стандартных шлюзов"}. Архитектура транзакций должна быть атомарной и устойчивой к сбоям.
3. **Безопасность:** {"Внедрить стандарт OWASP, сквозное шифрование данных и защиту от SQL-инъекций/XSS." if st.session_state.data['security'] else "Базовый уровень безопасности веб-приложения."}

### OPERATIONAL GUIDELINES
- Пиши только чистый, самодокументированный код (DRY, SOLID).
- Каждое решение должно быть обосновано с точки зрения SEO и конверсии (CRO).
- Не используй лишних слов и вступлений. Сразу переходи к реализации.
- На любые вопросы отвечай как технический директор (CTO): кратко, по делу, с акцентом на результат.

### FIRST MISSION
Проанализируй вводные данные и предложи структуру проекта, которая обеспечит максимальную производительность для сегмента "{st.session_state.data['aud']}". Жди моей команды для написания первого файла."""

    st.markdown(f'<div class="result-box"><pre style="white-space: pre-wrap;">{expert_prompt}</pre></div>', unsafe_allow_html=True)
    
    st.write("")
    st.download_button("📥 СКАЧАТЬ ИНСТРУКЦИЮ (.TXT)", expert_prompt)
    if st.button("🔄 НОВАЯ ГЕНЕРАЦИЯ"):
        st.session_state.step = 1
        st.rerun()

st.write("---")
st.caption("⚡ Enterprise AI Architect | Premium Generation Tool")
