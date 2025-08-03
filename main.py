import streamlit as st
import gspread
from google.oauth2.service_account import Credentials
import pandas as pd

# 구글 API 권한 범위 (scope)
SCOPES = ['https://spreadsheets.google.com/feeds',
          'https://www.googleapis.com/auth/drive']

# st.secrets에서 서비스 계정 정보 불러오기
service_account_info = st.secrets["google_service_account"]

# Credentials 객체 생성
credentials = Credentials.from_service_account_info(service_account_info, scopes=SCOPES)

# gspread 클라이언트 생성
client = gspread.authorize(credentials)

# 구글 시트 문서 열기 (문서명 입력)
spreadsheet = client.open("FA 리스트")

# 시트 리스트 가져오기
worksheets = spreadsheet.worksheets()

# 특정 조건으로 시트 선택 (예: 이름이 "_fa"로 끝나는 시트)
target_ws = None
for ws in worksheets:
    if ws.title.endswith("_fa"):
        target_ws = ws
        break

if target_ws:
    data = target_ws.get_all_records()
    df = pd.DataFrame(data)
    st.success(f"불러온 시트명: {target_ws.title}")
    st.dataframe(df)
else:
    st.error("조건에 맞는 시트를 찾지 못했습니다.")