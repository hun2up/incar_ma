import streamlit as st
import pandas as pd

# Create a connection object.
conn = st.connection("gsheets", type="gspread")

# 이 코드는 이미 DataFrame을 반환합니다
df = conn.read(
    worksheet="fa",   # 시트 이름
    ttl="10m",        # 캐시 유지 시간
    usecols=[0, 1],   # 첫 두 열
    nrows=3           # 3행만 읽기
)

# df는 DataFrame이므로 바로 사용 가능
st.dataframe(df)