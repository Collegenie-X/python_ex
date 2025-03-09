import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

def plot_histogram(df, selected_column):
    """선택된 열에 대한 히스토그램을 시각화하는 함수"""
    st.write("### 선택된 열에 대한 차트 시각화")
    fig, ax = plt.subplots()
    sns.histplot(df[selected_column], kde=True, ax=ax)
    ax.set_title(f"{selected_column}의 히스토그램")
    st.pyplot(fig)

def plot_bar_chart(df, bar_column):
    """다른 열에 대한 막대 차트를 시각화하는 함수"""
    st.write("### 다른 열에 대한 막대 차트")
    bar_fig, bar_ax = plt.subplots()
    sns.countplot(x=bar_column, data=df, ax=bar_ax)
    bar_ax.set_title(f"{bar_column}에 대한 막대 차트")
    st.pyplot(bar_fig)
