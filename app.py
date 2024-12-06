import streamlit as st
import openai
import datetime

# OpenAI APIキーの設定
openai.api_key = "YOUR_OPENAI_API_KEY"

# ページ設定
st.set_page_config(
    page_title="経営相談ツール",
    page_icon="💡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSSでおしゃれなデザイン
st.markdown(
    """
    <style>
    body {
        background-color: #f0f8f7;
        font-family: 'Arial', sans-serif;
    }
    .block-container {
        padding: 2rem;
        border-radius: 10px;
        background: #eafaf9;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    h1, h2, h3, h4 {
        color: #2c5d52;
    }
    .stButton>button {
        background-color: #4caf50;
        color: white;
        border: none;
        border-radius: 5px;
        padding: 10px 20px;
    }
    .stButton>button:hover {
        background-color: #45a049;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ヘッダーセクション
st.title(" 経営相談・事業計画ツール")
st.markdown("このアプリでは、経営状況を整理し、AIを活用して事業計画の作成をサポートします。")

# OpenAI 壁打ちセクション
st.header(" 経営相談 AI 壁打ち")
user_input = st.text_area("相談したい内容を入力してください", placeholder="例: 新規市場参入を検討しています。アドバイスをください。")

if st.button("AIに相談する"):
    if user_input.strip():
        with st.spinner("AIが回答を考えています..."):
            response = openai.ChatCompletion.create(
                model="gpt-4",  # または "gpt-3.5-turbo"
                messages=[
                    {"role": "system", "content": "あなたは経営の専門家です。経営相談にアドバイスを提供してください。"},
                    {"role": "user", "content": user_input},
                ],
                temperature=0.7,
                max_tokens=150,
            )
        st.markdown("### AIからのアドバイス")
        st.write(response["choices"][0]["message"]["content"].strip())
    else:
        st.warning("相談内容を入力してください。")

# サイドバー
with st.sidebar:
    st.header("🔍 メニュー")
    st.markdown("[Page1: 事業アイデアと目標設定](page1)")
    st.markdown("[Page2: 市場分析と競合研究](page2)")
    st.markdown("[Page3: 財務計画とシミュレーション](page3)")
    st.markdown("---")
    st.subheader("📅 スケジュール")
    st.date_input("重要な日程", datetime.date.today())

st.markdown("---")
st.write("© 2024 経営相談ツール")
