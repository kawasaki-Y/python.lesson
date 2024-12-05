import streamlit as st
import pandas as pd

st.write("hello daisy")

st.write("hello :green[daisy]")

st.title("hello daisy")

st.title("hello daisy  \U0001F458　")

st.write(
  pd.DataFrame(
    {
      "first column": [1,2,3,4],
      "second column": [10,20,30,40],
    }
  )
)

st.link_button("Click here","https://www.mindmeister.com/app/folders")

st.header("Love sick daisy", divider = "rainbow")

code = """print("daisy")"""
st.code(code, language="python")

agree = st.checkbox("I agree")
if agree:
    st.write("Okay")

# st.multiselect(
#     "好きな色は何ですか？",
#     ["白","黒","ピンク"]
# )

options = st.multiselect(
    "好きな色は何ですか？",
    ["白","黒","ピンク"]
)

st.write("あなたが選んだ色は:",options)

options = st.radio(
    "好きな色は何ですか？",
    ["白","黒","ピンク"]
)

st.write("あなたが選んだ色は:",options)

# 修正できるフレームワーク
df = pd.DataFrame(
    {
        "colors": ["白", "黒", "ピンク"],
        "rating": [4, 5, 3],
    }
)

# Streamlitのデータエディタ
edited_df = st.data_editor(df)

# "rating"が最大の行を取得し、その"colors"列の値を取得
max_rating_color = edited_df.loc[edited_df["rating"].idxmax(), "colors"]

# 結果を表示
st.write(max_rating_color)

# 修正できるフレームワーク
df = pd.DataFrame(
    {
        "colors": ["白", "黒", "ピンク"],
        "rating": [4, 5, 3],
        "mark": [True, False, True]  # 初期値をTrue/Falseで設定
    }
)

# Streamlitのデータエディタを使って編集可能に
edited_df = st.data_editor(
    df,
    use_container_width=True  # データエディタを幅いっぱいに表示
)

# "rating"が最大の行を取得し、その"colors"列の値を取得
max_rating_color = edited_df.loc[edited_df["rating"].idxmax(), "colors"]

edited_df = edited_df[edited_df["mark"] == True]

# 結果を表示
st.write("Ratingが最大の色:", max_rating_color)

# # チェックボックス状態を確認
# selected_colors = edited_df.loc[edited_df["mark"], "colors"]
# st.write("チェックされた色:", selected_colors.tolist())

# ダウンロードボタン
csv = edited_df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="CSVをダウンロード",
    data=csv,
    file_name="sample_df.csv",
    mime="text/csv"
)

# プログレスバー表示
df = pd.DataFrame(
    {
        "sales": [20, 55, 100, 80],
        "progress_sales": [20, 55, 100, 80],
    }
)

st.data_editor(
    df,
      column_config={
            "progress_sales":st.column_config.ProgressColumn(
              min_value=0,
              max_value=100,
            ),
    },
)

# 修正したデータフレーム
df = pd.DataFrame(
    {
        "date": pd.date_range(start="2023-01-01", periods=6, freq="D"),
        "sales": [0, 4, 26, 2, 50, 0]
    }
)

# Streamlitのデータエディタでデータ表示
st.data_editor(df)

# 時系列データのグラフ表示
st.line_chart(df.set_index("date"))

# スライダー
age = st.slider("あなたは何歳ですか？",0,130,40)
st.write("私は", age, "差異です")

# 日付選択
import datetime
date = st.date_input("あなたが生まれました",datetime.date(2000, 1, 1))
st.write("私は", date, "に生まれました")

# ユーザーの自由記述
text = st.text_input("入力してください", "毛呂和哉")
st.write(text)

# カラムを分ける
col1, col2 = st.columns(2)
with col1:
    st.title("Column1")
    st.write("これはカラムの1です")
with col2:
    st.title("Column2")
    st.write("これはカラムの2です")

# タブを分ける
tab1, tab2 = st.tabs(["tab1", "tab2"])
with tab1:
    st.title("Tab1")
    st.write("これはタブの1です")
with tab2:
    st.title("Tab2")
    st.write("これはタブの2です")

# アコーディオン
with st.expander("もっと詳しく見る"):
    st.write("XXX")

# ポップアップ表示
with st.popover("もっと詳しく見る"):
    st.write("XXX")

# サイドバー表示
with st.sidebar:
    st.title("XXX")
    st.write("XXX")

# notification
agree = st.checkbox("同意しますか？")
if agree:
  st.toast("Thank you", icon="👍")

# エフェクト
birthday = st.checkbox("今日はあなたの誕生日ですか？")
if birthday:
  st.toast("誕生日おめでとう！", icon="👍")
  st.balloons()

# 複数ページ実装
st.page_link("app.py",label="Home", icon="👩")
st.page_link("pages/page1.py",label="page1", icon="👩")
st.page_link("pages/page2.py",label="page2", icon="👩")
st.page_link("https://docs.streamlit.io/develop/api-reference",label="streamlitのAPIドキュメント", icon="👩")
