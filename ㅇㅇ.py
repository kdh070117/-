import streamlit as st
import pandas as pd
import plotly.express as px

# 앱 제목
st.title("📊 데이터 시각화 웹앱 (Google Drive + Plotly)")

# 데이터 로드 함수 (캐싱 포함)
DATA_URL = "https://drive.google.com/uc?export=download&id=1wPk1URO_NXKOmvXOsFAY8RlNCrR3IFnw"

@st.cache_data
def fetch_data():
    return pd.read_csv(DATA_URL)

# 데이터 불러오기
df = fetch_data()

# 데이터 미리보기
st.subheader("📄 데이터 미리보기")
st.dataframe(df.head())

# 유저가 시각화할 컬럼 선택
st.subheader("📈 Plotly 그래프")
columns = df.columns.tolist()

if len(columns) >= 2:
    x_axis = st.selectbox("X축 컬럼", columns, index=0)
    y_axis = st.selectbox("Y축 컬럼", columns, index=1)

    # Plotly 그래프 생성
    fig = px.scatter(df, x=x_axis, y=y_axis, title=f"{x_axis} vs {y_axis}")
    st.plotly_chart(fig, use_container_width=True)
else:
    st.error("데이터에 최소 2개의 컬럼이 필요합니다.")
