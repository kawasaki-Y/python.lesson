import streamlit as st
# import openai

# # OpenAI APIキーの設定
# openai.api_key = "YOUR_OPENAI_API_KEY"

# ページ設定
st.set_page_config(page_title="Page1: 事業アイデア", page_icon="💡", layout="wide")

# カスタムCSSの適用
st.markdown(
    """
    <style>
    /* 背景色を薄緑に設定 */
    .stApp {
        background-color: #ffffff;
        padding: 20px;
    }
    /* 入力と出力セクションのスタイル */
    .custom-container {
        background-color: #ffffff;
        border-radius: 10px;
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
        padding: 20px;
        margin: 10px 0;
    }
    /* ボタンのカスタマイズ */
    .stButton button {
        background-color: #4caf50;
        color: white;
        font-size: 16px;
        padding: 10px 20px;
        border-radius: 8px;
        border: none;
        cursor: pointer;
    }
    .stButton button:hover {
        background-color: #45a049;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# タイトル
st.title("🌟 事業アイデアと目標設定")

# 入力セクション
st.markdown('<div class="custom-container">', unsafe_allow_html=True)
st.subheader("📋 事業の概要を入力")
idea = st.text_area("事業の概要を入力してください", placeholder="例: 新しいサブスクリプションサービスの立ち上げ。")
st.subheader("🎯 目標を記述")
goal = st.text_area("目標を記述してください（例: 年間売上、顧客獲得目標など）。")
st.markdown('</div>', unsafe_allow_html=True)

# ボタンとフィードバックセクション
if st.button("AIでフィードバックを受け取る"):
    if idea or goal:
        with st.spinner("AIがフィードバックを作成中..."):
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=f"以下の事業アイデアと目標について具体的なアドバイスを提供してください:\n\n事業アイデア: {idea}\n目標: {goal}\n\n",
                max_tokens=150,
                temperature=0.7
            )
        st.markdown('<div class="custom-container">', unsafe_allow_html=True)
        st.subheader("🤖 AIからのフィードバック")
        st.write(response.choices[0].text.strip())
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.warning("事業アイデアと目標を入力してください。")
