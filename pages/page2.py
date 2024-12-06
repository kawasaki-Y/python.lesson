import streamlit as st
import openai

# OpenAI APIキーの設定
openai.api_key = "YOUR_OPENAI_API_KEY"

st.set_page_config(page_title="Page2: 市場分析", page_icon="📊", layout="wide")

st.title("📊 市場分析と競合研究")

market = st.text_area("ターゲット市場について説明してください（例: 市場規模や成長性）。")
competitors = st.text_area("主要な競合の情報を入力してください。")

if st.button("AIで分析を行う"):
    if market or competitors:
        with st.spinner("AIが分析結果を作成中..."):
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=f"以下の市場分析と競合情報に基づき、具体的なアドバイスを提供してください:\n\n市場分析: {market}\n競合情報: {competitors}\n\n",
                max_tokens=150,
                temperature=0.7
            )
        st.write("### AIの分析結果")
        st.write(response.choices[0].text.strip())
    else:
        st.warning("市場分析または競合情報を入力してください。")