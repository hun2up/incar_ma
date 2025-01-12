import streamlit as st
import mysql.connector
import pandas as pd

# 제목 출력
st.header("채권관리 대시보드")

# MySQL 데이터베이스에 연결
def create_connection():
    return mysql.connector.connect(
        host='https://92b5-218-39-88-242.ngrok-free.app',
        port=8080,  # ngrok이 제공한 포트 번호
        user='hun2up',
        password='INcar851!',
        database='incar_ma'
    )

# MySQL에서 데이터를 불러와 pandas DataFrame으로 반환
def fetch_data():
    connection = create_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM fa")
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return pd.DataFrame(result)

# Streamlit UI
st.title('MySQL 데이터베이스 데이터')

try:
    df = fetch_data()
    st.write(df)  # 데이터프레임 출력
except Exception as e:
    st.error(f"데이터를 불러오는 중 오류가 발생했습니다: {e}")

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
