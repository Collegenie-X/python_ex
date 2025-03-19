###
### pip install streamlit
### streamlit run ex.py
### localhost:8501
###

import streamlit as st

# 제목 추가
st.title("Streamlit 기본 UI 예제")

# 텍스트 추가
st.write("Streamlit을 사용한 첫 번째 웹 애플리케이션입니다.")

# 버튼 추가
if st.button("클릭하세요"):
    st.write("버튼이 클릭되었습니다!")


st.write("\n\n--------------------------------------------------------\n\n")

#### 텍스트 입력
name = st.text_input("이름을 입력하세요:")
if name:
    st.write(f"안녕하세요, {name}님!")

#### 숫자 입력
age = st.number_input("나이를 입력하세요:", min_value=0, max_value=100, step=5)
st.write(f"당신의 나이는 {age}세 입니다.")

#### 슬라이더
slider_value = st.slider("슬라이더", 0, 100)
st.write(f"슬라이더 값: {slider_value}")

#### 선택 박스
option = st.selectbox("좋아하는 색을 선택하세요:", ["빨강", "초록", "파랑"])
st.write(f"선택한 색은 [{option}]입니다.")

st.write("\n\n--------------------------------------------------------\n\n")

import pandas as pd
import numpy as np

### 데이터 생성 10개 데이터 생성
data = pd.DataFrame(np.random.randn(10, 2), columns=["A", "B"])

### 라인 차트
st.title("Line Chart")
st.line_chart(data)

#### 바 차트
# st.title("Bar Chart")
# st.bar_chart(data)


# st.write("\n\n--------------------------------------------------------\n\n")


####### 파일 업로드
# uploaded_file = st.file_uploader("CSV 파일 업로드", type=["csv"])

# if uploaded_file is not None:
#     # CSV 파일을 pandas DataFrame으로 읽기
#     df = pd.read_csv(uploaded_file)
#     st.write("업로드된 데이터:", df)


# ###### 파일 다운로드
# @st.cache
# def convert_df(df):
#     return df.to_csv(index=False)


# csv = convert_df(df)
# st.download_button(
#     label="CSV 파일 다운로드",
#     data=csv,
#     file_name="downloaded_data.csv",
#     mime="text/csv",
# )
