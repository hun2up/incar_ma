import streamlit as st
from google.oauth2.service_account import Credentials
import gspread
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

# 구글 시트 문서 열기
spreadsheet = client.open("FA 리스트")  # 문서 자체의 이름 (예: 'fa 데이터 모음')

# 모든 시트 목록 가져오기
worksheets = spreadsheet.worksheets()

# 'fa'로 끝나는 시트 찾기
target_ws = None
for ws in worksheets:
    if ws.title.endswith("_fa"):  # 또는 .endswith("fa") 도 가능
        target_ws = ws
        break

if target_ws:
    # 데이터 가져오기
    data = target_ws.get_all_records()
    df = pd.DataFrame(data)
    st.success(f"불러온 시트: {target_ws.title}")
    st.dataframe(df)
else:
    st.error("FA 리스트 파일을 찾을 수 없습니다.")