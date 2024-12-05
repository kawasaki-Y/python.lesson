import streamlit as st
import pandas as pd
import numpy as np
from pptx import Presentation
from io import BytesIO
import matplotlib.pyplot as plt
from fpdf import FPDF

# ページ設定
st.set_page_config(page_title="高度財務計画支援", layout="wide")

# セッションステート初期化
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []
if "responses" not in st.session_state:
    st.session_state["responses"] = {}

# カスタムCSS
st.markdown("""
    <style>
    .reportview-container {
        background-color: #f7f9fc;
    }
    .sidebar .sidebar-content {
        background-color: #ffffff;
    }
    h1, h2, h3 {
        color: #003566;
    }
    .stButton button {
        background-color: #0066cc;
        color: white;
        font-size: 18px;
        border-radius: 5px;
        padding: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# タイトル
st.title("📊 高度財務計画支援アプリ")
st.markdown("事業計画作成から財務予測、プレゼン資料作成をサポートします。")

# 動的な質問分岐
st.header("💬 チャットで事業計画をサポート")
questions = [
    {"id": "target_audience", "text": "ターゲット顧客層はどのような人々ですか？", "next": "differentiation"},
    {"id": "differentiation", "text": "競合との差別化ポイントは何ですか？", "next": "strengths"},
    {"id": "strengths", "text": "事業の強みと弱みを教えてください。", "next": "sales_goal"},
    {"id": "sales_goal", "text": "初年度の売上目標はどれくらいですか？", "next": "initial_cost"},
    {"id": "initial_cost", "text": "事業に必要な初期資金はいくらですか？", "next": None},
]

if len(st.session_state["chat_history"]) < len(questions):
    current_question = questions[len(st.session_state["chat_history"])]
    user_response = st.text_input(current_question["text"], key=current_question["id"])
    if st.button("送信"):
        st.session_state["chat_history"].append({"question": current_question, "response": user_response})
        st.session_state["responses"][current_question["id"]] = user_response

# チャット履歴の表示
st.subheader("チャット履歴")
for chat in st.session_state["chat_history"]:
    st.write(f"**質問:** {chat['question']['text']}")
    st.write(f"**回答:** {chat['response']}")

# 財務計画の生成
st.header("📈 財務計画 (PL, BS, CF)")
if st.button("財務計画を生成"):
    try:
        # 入力データの取得
        sales_goal = float(st.session_state["responses"].get("sales_goal", "0").replace("万", ""))
        initial_cost = float(st.session_state["responses"].get("initial_cost", "0").replace("万", ""))
        cogs = sales_goal * 0.6  # 仮の原価率60%
        operating_expenses = sales_goal * 0.2  # 仮の販売費および一般管理費
        profit = sales_goal - cogs - operating_expenses

        # PL
        pl = pd.DataFrame({
            "項目": ["売上", "売上原価", "営業利益", "最終利益"],
            "金額": [sales_goal, -cogs, -operating_expenses, profit],
        })

        # BS
        assets = initial_cost + profit
        bs = pd.DataFrame({
            "項目": ["資産", "負債", "純資産"],
            "金額": [assets, initial_cost * 0.5, assets - initial_cost * 0.5],
        })

        # CF
        cf = pd.DataFrame({
            "項目": ["営業キャッシュフロー", "投資キャッシュフロー", "財務キャッシュフロー"],
            "金額": [profit, -initial_cost, initial_cost * 0.5],
        })

        # 結果表示
        st.subheader("損益計算書 (PL)")
        st.write(pl)

        st.subheader("貸借対照表 (BS)")
        st.write(bs)

        st.subheader("キャッシュフロー計算書 (CF)")
        st.write(cf)

        # グラフ表示
        st.subheader("📊 財務計画グラフ")
        fig, ax = plt.subplots()
        ax.bar(pl["項目"], pl["金額"], color=["green", "red", "blue", "purple"])
        ax.set_title("損益計算書 (PL)")
        st.pyplot(fig)

    except Exception as e:
        st.error(f"財務計画の生成中にエラーが発生しました: {e}")

# プレゼン資料出力
st.header("📤 プレゼン資料作成")
if st.button("スライドを生成"):
    try:
        ppt = Presentation()
        slide = ppt.slides.add_slide(ppt.slide_layouts[5])
        slide.shapes.title.text = "事業計画概要"

        # 内容の作成
        content = "\n".join([f"{k}: {v}" for k, v in st.session_state["responses"].items()])
        textbox = slide.shapes.add_textbox(0, 100, 500, 400)
        textbox.text = content

        # PLスライド
        slide2 = ppt.slides.add_slide(ppt.slide_layouts[5])
        slide2.shapes.title.text = "財務計画"
        pl_text = "\n".join([f"{row['項目']}: {row['金額']}万円" for _, row in pl.iterrows()])
        slide2.shapes.add_textbox(0, 100, 500, 400).text = f"PL:\n{pl_text}"

        # 保存してダウンロード
        output = BytesIO()
        ppt.save(output)
        output.seek(0)
        st.download_button(
            label="スライドをダウンロード",
            data=output,
            file_name="business_plan.pptx",
            mime="application/vnd.openxmlformats-officedocument.presentationml.presentation"
        )
    except Exception as e:
        st.error(f"スライド作成中にエラーが発生しました: {e}")

# PDF出力
st.header("📄 PDFレポート作成")
if st.button("PDFを生成"):
    try:
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt="事業計画概要", ln=True, align='C')
        for k, v in st.session_state["responses"].items():
            pdf.cell(200, 10, txt=f"{k}: {v}", ln=True)
        pdf.output("business_plan.pdf")
        with open("business_plan.pdf", "rb") as pdf_file:
            st.download_button(
                label="PDFをダウンロード",
                data=pdf_file,
                file_name="business_plan.pdf",
                mime="application/pdf"
            )
    except Exception as e:
        st.error(f"PDF生成中にエラーが発生しました: {e}")
