import streamlit as st

# 1. КОНФИГУРАЦИЯ И СТИЛЬ (Premium Black)
st.set_page_config(page_title="PRO Generator v4.0", page_icon="🏗️", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #ffffff; }
    .logo-container { text-align: center; padding: 20px 0; }
    .logo-icon {
        background: linear-gradient(135deg, #00f2ea 0%, #0072ff 100%);
        width: 70px; height: 70px; border-radius: 20px;
        display: inline-flex; align-items: center; justify-content: center;
        font-size: 40px; font-weight: 900; color: white;
        box-shadow: 0 0 30px rgba(0, 242, 234, 0.3); margin-bottom: 10px;
    }
    .main-title { font-size: 2.5rem; font-weight: 850; background: linear-gradient(90deg, #fff, #555); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
    
    /* Стилизация карточек ввода */
    div[data-baseweb="input"], div[data-baseweb="textarea"] {
        border: 1px solid #222 !important; border-radius: 12px !important; background-color: #050505 !important;
    }
    
    .stButton > button {
        background: #ffffff !important; color: #000 !important; border-radius: 12px !important;
        height: 55px; font-weight: 800 !important; border: none !important; width: 100%;
    }
    .stButton > button:hover { background: #00f2ea !important; box-shadow: 0 0 20px #00f2ea66; }
    
    .prompt-box {
        background: #0a0a0a; border: 1px solid #1ed760; border-radius: 15px;
        padding: 20px; font-family: 'Consolas', monospace; font-size: 13px; color: #ddd; line-height: 1.5;
    }
    </style>
    """, unsafe_allow_html=True)

# Инициализация стейта
if 'step' not in st.session_state: st.session_state.step = 1
if 'data' not in st.session_state:
    st.session_state.data = {
        "name": "", "price": "1000", "header": "", "sub": "", "desc": "", 
        "features": "", "cta": "Купить сейчас", "img": "", 
        "theme": "#1a1200", "accent": "#f59e0b", "admin_pass": "Admin777#",
        "pays": ["ЮMoney (Quickpay)"]
    }

# ЛОГО
st.markdown('<div class="logo-container"><div class="logo-icon">Г</div><div class="main-title">PRO ГЕНЕРАТОР ТЗ</div></div>', unsafe_allow_html=True)

# ШАГ 1: МАРКЕТИНГ
if st.session_state.step == 1:
    st.subheader("📦 01. Информация и Маркетинг")
    st.session_state.data["name"] = st.text_input("Название проекта (Бренд)", value=st.session_state.data["name"])
    st.session_state.data["price"] = st.text_input("Цена товара (цифрами, в рублях)", value=st.session_state.data["price"])
    st.session_state.data["header"] = st.text_input("Главный заголовок (H1)", placeholder="Например: Керамическая плитка в СПб")
    st.session_state.data["sub"] = st.text_input("Подзаголовок", placeholder="Широкий ассортимент в наличии...")
    st.session_state.data["desc"] = st.text_area("Описание продукта (для блока 'О нас')", height=100)
    st.session_state.data["features"] = st.text_area("Преимущества (каждое с новой строки)", placeholder="- Свой склад\n- Быстрая доставка")
    st.session_state.data["img"] = st.text_input("Ссылка на картинку товара", placeholder="https://site.ru/image.jpg")
    
    if st.button("ДАЛЕЕ: ТЕХНИЧЕСКИЙ СТИЛЬ →"):
        if st.session_state.data["name"] and st.session_state.data["header"]:
            st.session_state.step = 2
            st.rerun()
        else: st.error("Заполни Название и Заголовок!")

# ШАГ 2: ВИЗУАЛ
elif st.session_state.step == 2:
    st.subheader("🎨 02. Внешний вид и Доступ")
    col1, col2 = st.columns(2)
    with col1:
        st.session_state.data["theme"] = st.color_picker("Цвет фона сайта", value="#1a1200")
    with col2:
        st.session_state.data["accent"] = st.color_picker("Акцентный цвет (кнопки)", value="#f59e0b")
    
    st.session_state.data["admin_pass"] = st.text_input("Пароль администратора (будет вшит в конфиг)", value=st.session_state.data["admin_pass"])
    
    c1, c2 = st.columns(2)
    if c1.button("← НАЗАД"): st.session_state.step = 1; st.rerun()
    if c2.button("ДАЛЕЕ: ПЛАТЕЖИ →"): st.session_state.step = 3; st.rerun()

# ШАГ 3: ПЛАТЕЖИ
elif st.session_state.step == 3:
    st.subheader("💳 03. Платежные системы")
    st.session_state.data["pays"] = st.multiselect("Выберите системы для интеграции", 
                                                ["ЮMoney (Quickpay)", "NowPayments (Крипто)"], 
                                                default=st.session_state.data["pays"])
    
    st.info("Программа автоматически пропишет логику проверки SHA-1 и HMAC подписей для этих систем.")
    
    c1, c2 = st.columns(2)
    if c1.button("← НАЗАД"): st.session_state.step = 2; st.rerun()
    if c2.button("🚀 СГЕНЕРИРОВАТЬ ПРОФЕССИОНАЛЬНОЕ ТЗ"): st.session_state.step = 4; st.rerun()

# ШАГ 4: ФИНАЛЬНЫЙ ПРОМТ (Аналог Орфеева)
elif st.session_state.step == 4:
    st.subheader("🔥 Ваше экспертное ТЗ")
    
    d = st.session_state.data
    
    # ФОРМИРУЕМ МОЩНЫЙ ТЕКСТ
    full_prompt = f"""Ты — senior full-stack разработчик с глубоким опытом в e-commerce.

## ЗАДАЧА
Создать профессиональный магазин одного цифрового товара. Работай итерациями: я называю файл, ты выдаешь ТОЛЬКО чистый код этого файла без пояснений.

## ПРОЕКТ
Название: {d['name']}
Язык: Русский
Цена: {d['price']} RUB

## МАРКЕТИНГОВЫЙ КОНТЕНТ
Заголовок: {d['header']}
Подзаголовок: {d['sub']}
Описание: {d['desc']}
Преимущества:
{chr(10).join([f'- {line}' for line in d['features'].splitlines()])}
CTA кнопка: {d['cta']}
Изображение: {d['img'] if d['img'] else 'standard_placeholder.jpg'}

## ФАЙЛОВАЯ СТРУКТУРА
- index.php (Лендинг)
- thank_you.php (Страница успеха/скачивания)
- admin.php (Панель управления)
- config.php (Конфигурация и пароли)
- callback_yoomoney.php (Обработчик платежей)
- callback_nowpayments.php (Обработчик крипто)
- /goods/ (Папка для файлов продажи)
- /uploads/ (Папка для картинок)

## ТЕХНИЧЕСКИЙ СТЕК
- PHP 8.1+ (Native)
- SQLite3 (База данных заказов)
- Tailwind CSS (CDN)
- Адаптивность: Mobile-first

## ЦВЕТОВАЯ СХЕМА
Фон: {d['theme']}
Акцент: {d['accent']}
Стиль: Профессиональный, строгий, премиальные отступы и тени.

## ЛОГИКА ОПЛАТЫ
{"1. ЮMoney: Проверка SHA-1 подписи (notification_type&operation_id&amount&currency&datetime&sender&codepro&{secret}&label). Статус заказа обновляется при совпадении хэша." if "ЮMoney (Quickpay)" in d['pays'] else ""}
{"2. NowPayments: Проверка HMAC-SHA512 подписи заголовка x-nowpayments-sig. Обработка статуса 'finished'." if "NowPayments (Крипто)" in d['pays'] else ""}

## АДМИН-ПАНЕЛЬ
- Доступ по паролю: {d['admin_pass']}
- Функции: Изменение цены, настройка кошельков/API ключей, загрузка файла товара, просмотр списка заказов (SQLite).

## ОГРАНИЧЕНИЯ
- Код должен работать на shared-хостинге (Beget/Reg.ru).
- Никакого Composer, только чистый PHP.
- SQLite база создается автоматически при первом посещении."""

    st.markdown(f'<div class="prompt-box"><pre style="white-space: pre-wrap;">{full_prompt}</pre></div>', unsafe_allow_html=True)
    
    st.write("")
    st.download_button("📥 СКАЧАТЬ ТЗ В .TXT", full_prompt)
    if st.button("🔄 НОВЫЙ ПРОЕКТ"):
        st.session_state.step = 1
        st.rerun()

st.markdown("<br><center style='color: #444;'>© 2024 AI Engineering System</center>", unsafe_allow_html=True)
