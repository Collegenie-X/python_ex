import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from matplotlib import rcParams


##### sudo apt-get install fonts-nanum
##### from matplotlib import rcParams

##### # 한글 폰트 설정
##### rcParams['font.family'] = 'NanumGothic'  # 예시: 나눔고딕 폰트 설정
##### rcParams['axes.unicode_minus'] = False  # 마이너스 부호 깨짐 방지


# 한글 폰트 설정
rcParams["font.family"] = "NanumGothic"  # 예시: 나눔고딕 폰트 설정
rcParams["axes.unicode_minus"] = False  # 마이너스 부호 깨짐 방지

st.title("1. 선 그래프 (Line Chart)")

# 데이터 생성
x = np.arange(0, 10, 0.1)
y = np.sin(x)

# 선 그래프 그리기
st.line_chart(y)


# 멀티 데이터 생성
data = {
    "Year": [2020, 2021, 2022, 2023],
    "Sales": [100, 150, 120, 170],
    "Profit": [30, 40, 35, 45],
}

# 데이터를 Pandas DataFrame으로 변환
df = pd.DataFrame(data)

# Streamlit 기본 차트 사용
st.line_chart(df.set_index("Year"))


# 데이터 생성
x = np.arange(0, 10, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)

# 옵션 선택 (차트 유형 선택)
chart_type = st.selectbox(
    "차트 유형을 선택하세요", ["선 그래프", "막대 그래프", "영역 그래프"]
)

# 차트 그리기
fig, ax = plt.subplots(figsize=(10, 6))

if chart_type == "선 그래프":
    ax.plot(x, y1, label="sin(x)", color="b")
    ax.plot(x, y2, label="cos(x)", color="r")
    ax.set_title("Line Charts (Sine & Cosine)")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.legend()

elif chart_type == "막대 그래프":
    ax.bar(x, y1, label="sin(x)", alpha=0.6)
    ax.bar(x, y2, label="cos(x)", alpha=0.6)
    ax.set_title("Box Charts (Sine & Cosine)")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.legend()

elif chart_type == "영역 그래프":
    ax.fill_between(x, y1, color="b", alpha=0.3, label="sin(x)")
    ax.fill_between(x, y2, color="r", alpha=0.3, label="cos(x)")
    ax.set_title("Area Charts (Sine & Cosine)")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.legend()

# 그래프 출력
st.pyplot(fig)


st.title("2.막대 그래프")
# 딕셔너리 데이터 생성
data = {"A": 10, "B": 20, "C": 30, "D": 40}

# 막대 그래프 그리기
st.bar_chart(data)


# 데이터 생성
x = np.arange(0, 10, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)


st.title("3. 영역 그래프")

# 데이터 생성
x = np.arange(0, 10, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)

# 영역 그래프 그리기
st.area_chart({"sin(x)": y1, "cos(x)": y2})

st.title("4. 히스토그램")
# 데이터 생성
data = np.random.randn(1000)

# 히스토그램 그리기
st.bar_chart(np.histogram(data, bins=20)[0])


st.title("5. 산점도(Scatter Plot)")

# 데이터 생성
x = np.random.rand(100)
y = np.random.rand(100)

# 산점도 그리기
st.scatter_chart({"x": x, "y": y})
