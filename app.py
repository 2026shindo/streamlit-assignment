import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 웹 앱 브라우저 탭 설정
st.set_page_config(page_title="Streamlit 과제 대시보드", page_icon="📊", layout="wide")

st.title("🎬 Streamlit 프로그래밍 과제")
st.subheader("학번과 이름을 입력한 후 과제를 수행하세요.")

# 사용자 입력 구역
student_info = st.text_input("학번 및 이름 (예: 30101 홍길동)")

if student_info:
    st.write(f"**제출자:** {student_info}")
    st.markdown("---")

    # 💡 이 아래에 학생들이 직접 코드를 작성하도록 안내합니다.
    st.info("이 곳에 과제 요구사항(데이터 분석 및 시각화 등)을 구현하세요.")
