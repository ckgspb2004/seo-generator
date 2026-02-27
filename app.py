import streamlit as st

# 1. КОНФИГУРАЦИЯ
st.set_page_config(page_title="AI TZ Premium", page_icon="🔮", layout="centered")

# 2. ДИЗАЙН (Улучшенный черный + Центрирование)
st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #ffffff; }
    .main-title {
        text-align: center;
        background: linear-gradient(90deg, #00f2ea, #00ff41);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 3rem; font-weight: 800; margin-bottom: 0px;
    }
    .subtitle { text-align: center; color: #888; margin-bottom: 40px; }
    
    /* Стилизация рамок */
    div[data-baseweb="input"], div[data-baseweb="textarea"], div[data-baseweb="select"] {
        border: 1px solid #1e1e1e !important;
        border-radius: 12px !important;
        background-color: #0a0a0a !important;
    }
    
    .step-node { text-align: center; padding: 10px; border-bottom: 2px solid #1e1e1e; flex-grow: 1; color: #444; font-weight: bold; }
    .step-node-active { color: #00f2ea; border-bottom: 2px solid #00f2ea; text-shadow: 0 0 10px rgba(0, 242, 234, 0.5); }
    
    .stButton > button {
        background: linear-gradient(135deg, #00f2ea 0%, #0072ff 100%) !important;
        color: white !important; border: none !important; width: 100%; border-radius: 8px !important;
        height: 50px; font-weight: bold !important; text-transform: uppercase;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. ИНИЦИАЛИЗАЦИЯ ДАННЫХ (Чтобы не было ошибок NameError)
if 'step' not in st.session_state: st.session_state.step = 1
if 'data' not in st.session_state:
    st.session_state.data = {
        "name": "", "desc": "", "aud": "", "theme": "Deep Black", 
        "style": "Минимализм", "pays": [], "security": False
    }

def next_step(): st.session_state.step += 1
def prev_step(): st.session_state.step -= 1

# --- ЗАГОЛОВОК ---
st.markdown('<div class="main-title">AI ГЕНЕРАТОР ТЗ</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Создание системных инструкций для разработки</div>', unsafe_allow_html=True)

# --- ИНДИКАТОР ШАГОВ ---
step_cols = st.columns(4)
names = ["Продукт", "Стиль", "Оплата", "Финал"]
for i, name in enumerate(names):
    is_active = "step-node-active" if st.session_state.step == i + 1 else ""
    step_cols[i].markdown(f'<div class="step-node {is_active}">{i+1}. {name}</div>', unsafe_allow_html=True)

st.write("") 

# --- ШАГ 1: ПРОДУКТ ---
if st.session_state.step == 1:
    st.markdown("### 🛠 Информация о проекте")
    st.session_state.data["name"] = st.text_input("Название магазина", value=st.session_state.data["name"], placeholder="Например: Digital Pro Store")
    st.session_state.data["desc"] = st.text_area("Что продаёшь (подробно)", value=st.session_state.data["desc"], placeholder="Опиши продукт, какие проблемы он решает...", height=150)
    st.session_state.data["aud"] = st.text_input("Целевая аудитория", value=st.session_state.data["aud"], placeholder="Например: владельцы малого бизнеса")
    
    if st.button("Далее: Внешний вид →"):
        if st.session_state.data["name"] and st.session_state.data["desc"]:
            next_step()
            st.rerun()
        else: st.error("Заполни название и описание!")

# --- ШАГ 2: ВИЗУАЛ ---
elif st.session_state.step == 2:
    st.markdown("### 🎨 Дизайн и Атмосфера")
    st.session_state.data["theme"] = st.select_slider("Цветовая палитра", options=["Deep Black", "Cyber Blue", "Neon Green", "Royal Gold"], value=st.session_state.data["theme"])
    st.session_state.data["style"] = st.radio("Стиль оформления", ["Минимализм", "Футуризм", "Классика", "Яркий"], horizontal=True, index=["Минимализм", "Футуризм", "Классика", "Яркий"].index(st.session_state.data["style"]))
    
    c1, c2 = st.columns(2)
    with c1: 
        if st.button("← Назад"): prev_step(); st.rerun()
    with c2: 
        if st.button("Далее: Оплата →"): next_step(); st.rerun()

# --- ШАГ 3: ОПЛАТА ---
elif st.session_state.step == 3:
    st.markdown("### ⚙️ Платежные системы")
    st.session_state.data["pays"] = st.multiselect("Выберите методы оплаты", ["ЮMoney", "Криптовалюта", "Карты РФ", "PayPal"], default=st.session_state.data["pays"])
    st.session_state.data["security"] = st.checkbox("Повышенная безопасность (SSL/Шифрование)", value=st.session_state.data["security"])
    
    c1, c2 = st.columns(2)
    with c1: 
        if st.button("← Назад"): prev_step(); st.rerun()
    with c2: 
        if st.button("🔮 Сгенерировать промт"): next_step(); st.rerun()

# --- ШАГ 4: РЕЗУЛЬТАТ (Тот самый "Промт как у Орфеева") ---
elif st.session_state.step == 4:
    st.markdown("### ✨ Ваше системное ТЗ готово!")
    
    # ВОТ ЗДЕСЬ ЗАШИТ ШАБЛОН (ПРОМТ)
    system_prompt = f"""Ты — senior full-stack разработчик с огромным опытом в e-commerce.

## ЗАДАЧА
Создать профессиональный онлайн-магазин цифровых товаров. 
Название проекта: {st.session_state.data['name']}

## ОПИСАНИЕ ПРОДУКТА
{st.session_state.data['desc']}
Целевая аудитория: {st.session_state.data['aud']}

## ТЕХНИЧЕСКИЙ ДИЗАЙН
- Цветовая схема: {st.session_state.data['theme']}
- Визуальный стиль: {st.session_state.data['style']}

## ФУНКЦИОНАЛ
- Интеграция платежей: {", ".join(st.session_state.data['pays']) if st.session_state.data['pays'] else "Стандартная"}
- Безопасность: {"Высокий приоритет (Шифрование)" if st.session_state.data['security'] else "Базовая"}

Твоя роль — выдавать только чистый код файлов по запросу, без лишних объяснений. Начнем с создания структуры базы данных. Жди моей команды."""

    st.markdown('<div style="background-color: #0a0a0a; padding: 20px; border-radius: 12px; border: 1px solid #00f2ea;">', unsafe_allow_html=True)
    st.markdown(f"```\n{system_prompt}\n```")
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.write("")
    st.download_button("📥 Скачать файл промта", system_prompt)
    if st.button("🔄 Начать заново"):
        st.session_state.step = 1
        st.rerun()

st.write("---")
st.caption("⚡ AI Premium System | Powered by Your Logic")
