import streamlit as st

# 앱 타이틀
st.title('산업데이터시각화 수업 소개')

# 교과목 기본 정보
st.header('기본 정보')
st.text('교과목명: 산업데이터시각화')
st.text('이수구분: 전공')
st.text('교과코드: M04111101')
st.text('분반: 1')
st.text('학과: Social Science & AI융합전공')
st.text('학년: 2')
st.text('교수: 이동현')
st.text('학점/강의: 3/3')
st.text('강의시간: 목 4 5 6 (2108)')
st.text('제한인원: 60')
st.text('E-mail: donghyun.lee@hufs.ac.kr')

# 교과목 개요 및 학습목표
st.header('교과목개요 및 학습목표')
st.write('- 파이썬을 중심으로 Numpy와 Pandas 라이브러리를 활용한 데이터 전처리 과정을 익힌다.')
st.write('- Matplotlib 라이브러리 등을 활용하여 다양한 데이터를 적합하게 시각화하는 방법을 학습한다.')

# 교재
st.header('교재')
st.text('데이터 분석을 위한 전처리와 시각화 with 파이썬')

# 학습 평가 방법
st.header('학습 평가방법')
st.write('(1) 중간시험(%): 30')
st.write('(2) 기말시험(%): 30')
st.write('(3) 출석(%): 10')
st.write('(4) 과제물(%): 0')
st.write('(5) 기타(%)(발표 및 토론, 프로젝트, 수업참여도 등): 30')
