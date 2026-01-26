import streamlit as st
import pandas as pd

st.text("Hello")

df = pd.read_csv("./data_analysis/imdb_top_1000.csv")
st.success(f"데이터 로딩 성공! 총 {len(df)}개 행")

st.dataframe(df)

col1, col2 = st.columns(2)

with col1:
    st.subheader("컬럼 이름")
    st.write(df.columns.tolist())

with col2:
    st.subheader("데이터 타입")
    st.dataframe(
        df.dtypes.
        astype(str).
        reset_index().
        rename(
            columns={'index': '컬럼', 0: '타입'}
        )
    )

st.subheader("통계")
st.dataframe(df.describe())