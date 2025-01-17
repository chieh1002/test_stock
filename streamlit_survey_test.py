import streamlit as st
import pandas as pd

df = pd.read_excel('MATNR_streamlit_test.xlsx')
df = df.fillna('空白')
df = df.astype(str)

st.title("盤點")
st.write("請篩選出相對應的位置並填寫數量與新儲格欄位:")

st.sidebar.header("篩選器")
factory_filter = st.sidebar.selectbox(
    "選擇工廠",
    df["工廠"].unique()
)

place_filter = st.sidebar.multiselect(
    "選擇儲存地點",
    options=df[df["工廠"]==factory_filter]["儲存地點"].unique(),
    default=df[df["工廠"]==factory_filter]["儲存地點"].unique()
)
stock_filter = st.sidebar.multiselect(
    "選擇儲格",
    options=df[(df["工廠"]==factory_filter)&(df["儲存地點"].isin(place_filter))]["儲格"].unique(),
    default=df[(df["工廠"]==factory_filter)&(df["儲存地點"].isin(place_filter))]["儲格"].unique()
)

filtered_df = df[
    (df["工廠"]==factory_filter) &
    (df["儲存地點"].isin(place_filter)) &
    (df["儲格"].isin(stock_filter))
]

filtered_df['數量'] = ''
filtered_df['新儲位'] = ''
edited_df = st.data_editor(filtered_df[['儲存地點','儲格','物料','物料說明','物料規格','基礎計量單位','數量','新儲位']].sort_values(by=['儲存地點']), use_container_width=True,hide_index=True)

st.download_button(
    label="下載已更新表格",
    data=edited_df.to_csv(index=False).encode('utf-8'),
    file_name="updated_results.csv",
    mime="text/csv"
)
