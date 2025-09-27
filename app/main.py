import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from logic import generate_sample_csv

st.title("📊 CSV分析ツール")

st.header("CSV アップロード")
# CSVアップロード
uploaded_file = st.file_uploader("CSVファイルをアップロードしてください", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.subheader("📄 データプレビュー")
    st.dataframe(df.head())

    # 外れ値除去 (95パーセンタイル以上を除外する例)
    if "value" in df.columns:
        filtered_df = df[df["value"] < df["value"].quantile(0.95)]

        st.subheader("📈 基本統計量")
        st.write("平均値:", filtered_df["value"].mean())
        st.write("最大値:", filtered_df["value"].max())
        st.write("最小値:", filtered_df["value"].min())

        # グラフ描画
        fig, ax = plt.subplots()
        ax.plot(filtered_df["value"])
        ax.set_title("Valueの推移")
        st.pyplot(fig)
    else:
        st.warning("⚠️ 'value' カラムが存在しません。CSVの列名を確認してください。")

st.divider()

# サンプルのCSV作成ボタン
st.header("サンプルCSV作成")
rows = st.slider("行数を選択", 10, 200, 50)

if st.button("CSVを生成"):
    df = generate_sample_csv(rows)
    st.dataframe(df)

    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button("📥 CSVをダウンロード", csv, "sample.csv", "text/csv")
