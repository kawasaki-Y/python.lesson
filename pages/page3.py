import streamlit as st
import openai
import pandas as pd

# OpenAI APIキーの設定
openai.api_key = "YOUR_OPENAI_API_KEY"

st.set_page_config(page_title="Page3: 財務計画", page_icon="📉", layout="wide")

st.title("📉 財務計画とシミュレーション")

revenue = st.number_input("年間売上予測 (万円)", min_value=0, step=10)
cost = st.number_input("年間コスト予測 (万円)", min_value=0, step=10)
profit = revenue - cost
st.metric("予測利益", f"{profit} 万円")

if st.button("AIで財務計画をシミュレート"):
    with st.spinner("AIが財務計画を分析中..."):
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=f"以下の財務データを基にアドバイスを提供してください:\n\n売上: {revenue}万円\nコスト: {cost}万円\n\n",
            max_tokens=150,
            temperature=0.7
        )
    st.write("### AIのシミュレーション結果")
    st.write(response.choices[0].text.strip())
