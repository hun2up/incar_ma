import streamlit as st
import pandas as pd
import streamlit as st
import psycopg2

# 제목 출력
st.header("채권관리 대시보드")

# Initialize connection.
conn = st.connection("postgresql", type="sql")

# Perform query.
df = conn.query('SELECT * FROM fa;', ttl="10m")

# Print results.
for row in df.itertuples():
    st.write(f"{row.name} has a :{row.pet}:")


# 제목 출력
st.header("데이터 관리")

# 파일 업로드 위젯
uploaded_file = st.file_uploader("필요한 지표자료를 csv 파일 형태로 업로드해 주세요.", type=["csv"])

# 파일이 업로드된 경우 처리
if uploaded_file is not None:
    # CSV 파일을 판다스로 읽기
    df = pd.read_csv(uploaded_file)
    
    # 데이터 프레임 표시
    st.write("업로드된 CSV 데이터:")
    st.dataframe(df)
