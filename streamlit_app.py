import streamlit as st

# 스타일용 CSS (컬러 등)
st.markdown("""
    <style>
    .title {
        color: #4B8BBE;
        font-size: 36px;
        font-weight: bold;
        text-align: center;
    }
    .section-header {
        color: #306998;
        font-size: 24px;
        margin-top: 20px;
        border-bottom: 2px solid #306998;
    }
    .info-text {
        font-size: 18px;
        margin-bottom: 6px;
    }
    </style>
""", unsafe_allow_html=True)

# 타이틀
st.markdown('<div class="title">📊 산업데이터시각화 수업 소개</div>', unsafe_allow_html=True)

# 기본정보
st.markdown('<div class="section-header">📚 기본 정보</div>', unsafe_allow_html=True)
info_items = [
    '교과목명: 산업데이터시각화',
    '이수구분: 전공',
    '교과코드: M04111101',
    '분반: 1',
    '학과: Social Science & AI융합전공',
    '학년: 2',
    '교수: 이동현',
    '학점/강의: 3/3',
    '강의시간: 목 4 5 6 (2108)',
    '제한인원: 60',
    'E-mail: donghyun.lee@hufs.ac.kr'
]
for item in info_items:
    st.markdown(f'<div class="info-text">- {item}</div>', unsafe_allow_html=True)

# 교과목 개요 및 학습목표
st.markdown('<div class="section-header">🎯 교과목개요 및 학습목표</div>', unsafe_allow_html=True)
goal_items = [
    '파이썬을 중심으로 Numpy와 Pandas 라이브러리를 활용한 데이터 전처리 과정을 익힌다.',
    'Matplotlib 라이브러리 등을 활용하여 다양한 데이터를 적합하게 시각화하는 방법을 학습한다.'
]
for goal in goal_items:
    st.markdown(f'<div class="info-text">• {goal}</div>', unsafe_allow_html=True)

# 교재
st.markdown('<div class="section-header">📗 교재</div>', unsafe_allow_html=True)
st.markdown('<div class="info-text">데이터 분석을 위한 전처리와 시각화 with 파이썬</div>', unsafe_allow_html=True)

# 학습 평가 방법 (표 형태로)
st.markdown('<div class="section-header">📝 학습 평가방법</div>', unsafe_allow_html=True)
import pandas as pd

eval_data = {
    '평가 항목': ['중간시험', '기말시험', '출석', '과제물', '기타(발표 및 토론, 프로젝트, 수업참여도 등)'],
    '비율(%)': [30, 30, 10, 0, 30]
}
df_eval = pd.DataFrame(eval_data)
st.table(df_eval)

# 마무리 인사말
st.markdown('<br><center>🎉 열심히 배우고 멋진 결과 얻으시길 바랍니다! 🎉</center>', unsafe_allow_html=True)
