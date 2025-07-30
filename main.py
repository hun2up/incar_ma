import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

# 구글 인증
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds_dict = dict(st.secrets["google_service_account"])
creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
client = gspread.authorize(creds)

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