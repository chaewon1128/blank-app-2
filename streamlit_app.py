import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --- 수업 소개 파트 ---
st.title('📊 산업데이터시각화 수업 소개')

st.header('📚 기본 정보')
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
    st.write(f'- {item}')

st.header('🎯 교과목개요 및 학습목표')
goal_items = [
    '파이썬을 중심으로 Numpy와 Pandas 라이브러리를 활용한 데이터 전처리 과정을 익힌다.',
    'Matplotlib 라이브러리 등을 활용하여 다양한 데이터를 적합하게 시각화하는 방법을 학습한다.'
]
for goal in goal_items:
    st.write(f'• {goal}')

st.header('📗 교재')
st.write('데이터 분석을 위한 전처리와 시각화 with 파이썬')

st.header('📝 학습 평가방법')
eval_data = {
    '평가 항목': ['중간시험', '기말시험', '출석', '과제물', '기타(발표 및 토론, 프로젝트, 수업참여도 등)'],
    '비율(%)': [30, 30, 10, 0, 30]
}
df_eval = pd.DataFrame(eval_data)
st.table(df_eval)

st.markdown('---')

# --- 독감 발생률 시각화 파트 ---
st.header('🦠 2025년 현재 독감 발생률 및 발생 장소 시각화')

# 예시 데이터
weeks = pd.date_range(start='2025-09-01', periods=12, freq='W')
flu_rate = [3.9, 5.5, 8.2, 12.1, 18.5, 25.9, 31.6, 34.0, 38.2, 40.1, 42.5, 45.3]
df_time = pd.DataFrame({'Week': weeks, 'FluRatePer1000': flu_rate})

age_groups = ['0-6세', '7-12세', '13-18세', '19-49세', '50-64세', '65세 이상']
age_rates = [25.8, 31.6, 15.8, 11.8, 8.4, 6.9]
df_age = pd.DataFrame({'AgeGroup': age_groups, 'RatePer1000': age_rates})

regions = ['서울', '부산', '대구', '인천', '광주', '대전', '울산']
patients = [1200, 950, 800, 700, 600, 500, 450]
df_region = pd.DataFrame({'Region': regions, 'PatientCount': patients})

# 주별 독감 발생률 (시계열)
st.subheader('주별 독감 발생률 (1000명당 환자 수)')
fig1, ax1 = plt.subplots()
sns.lineplot(data=df_time, x='Week', y='FluRatePer1000', marker='o', color='crimson', ax=ax1)
ax1.set_ylabel('환자 수')
ax1.set_xlabel('')
plt.xticks(rotation=45)
ax1.grid(True)
st.pyplot(fig1)

# 연령대별 독감 발생률
st.subheader('연령대별 독감 발생률 (1000명당 환자 수)')
fig2, ax2 = plt.subplots()
sns.barplot(data=df_age, x='AgeGroup', y='RatePer1000', palette='coolwarm', ax=ax2)
ax2.set_ylabel('발생률')
ax2.set_xlabel('연령대')
st.pyplot(fig2)

# 지역별 독감 환자수
st.subheader('지역별 독감 환자 수')
fig3, ax3 = plt.subplots()
sns.barplot(data=df_region, x='PatientCount', y='Region', palette='viridis', ax=ax3)
ax3.set_xlabel('환자 수')
ax3.set_ylabel('지역')
st.pyplot(fig3)

st.markdown('<center>🎉 산업데이터시각화 수업과 연계한 실제 데이터 시각화 예시였습니다! 🎉</center>', unsafe_allow_html=True)
