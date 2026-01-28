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

@st.cache_data
def load_data_cached():
    return pd.read_csv("./data_analysis/imdb_top_1000.csv")

df = load_data_cached()
st.info("데이터가 캐싱되었습니다! 이후 로드는 즉시 완료됩니다.")

df_clean = df.copy()
df_clean['Runtime_min'] = df_clean['Runtime'].str.extract(r'(\d+)').astype(float)

st.dataframe(df_clean.head(10))

df_clean['Gross_numeric'] = df_clean['Gross'].replace({',': ''}, regex=True).astype(float)

st.dataframe(df_clean.head(10))

df_clean['Released_Year'] = pd.to_numeric(df_clean['Released_Year'], errors='coerce')
df_clean['Decade'] = (df_clean['Released_Year'] // 10 * 10).astype('Int64').astype(str) + 's'

st.subheader("결과")
comparison = df_clean[['Series_Title', 'Released_Year', 'Decade']].head(10)
st.dataframe(comparison)

st.subheader("연대별 분포")
decade_counts = df_clean['Decade'].value_counts().sort_index()
st.bar_chart(decade_counts)

