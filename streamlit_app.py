import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 제목
st.title('이태원 참사 관련 주요 데이터 및 인파 밀집도 시각화')

# 주요 사상자 및 신고 현황 (예시)
summary_data = {
    '항목': ['사망자 수', '부상자 수', '신고 접수 수', '경찰 출동(명)'],
    '수치': [159, 195, 120, 300]
}
df_summary = pd.DataFrame(summary_data)
st.subheader('주요 데이터 현황')
st.table(df_summary)

# 시간대별 인파 밀집도 (가상의 시각별 데이터)
# 시간은 참사 발생일 10월 29일 17시부터 23시까지 한 시간 단위
time_slots = ['17시', '18시', '19시', '20시', '21시', '22시', '23시']
crowd_density = [30, 50, 85, 100, 95, 70, 40]  # 밀집도는 0~100 척도

df_crowd = pd.DataFrame({'시간대': time_slots, '인파 밀집도(%)': crowd_density})

st.subheader('시간대별 인파 밀집도 변화')
fig, ax = plt.subplots(figsize=(8,4))
ax.plot(df_crowd['시간대'], df_crowd['인파 밀집도(%)'], marker='o', color='red')
ax.set_ylim(0, 110)
ax.set_ylabel('밀집도(%)')
ax.set_xlabel('시간대')
ax.set_title('10월 29일 이태원 참사 당일 인파 밀집도 변화')
ax.grid(True)
st.pyplot(fig)

# 신고 접수 수 시간대별(예시)
report_counts = [1, 3, 7, 20, 25, 30, 34]
df_reports = pd.DataFrame({'시간대': time_slots, '신고 접수 수': report_counts})

st.subheader('시간대별 신고 접수 현황')
fig2, ax2 = plt.subplots(figsize=(8,4))
ax2.bar(df_reports['시간대'], df_reports['신고 접수 수'], color='skyblue')
ax2.set_ylabel('신고 접수 수')
ax2.set_xlabel('시간대')
ax2.set_title('10월 29일 시간대별 압사 사고 관련 신고 접수 수')
ax2.grid(axis='y')
st.pyplot(fig2)
