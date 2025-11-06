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
import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

# 이태원 주요 지점 좌표 (예시)
locations = {
    '진입로': (37.534, 126.994),
    '핵심 골목 A': (37.533, 126.995),
    '핵심 골목 B': (37.532, 126.993),
    '광장 입구': (37.5345, 126.992),
    '주점 밀집 지역': (37.5335, 126.996)
}

# 시간대별 인파 밀집도 데이터 (0~100 척도, 가상 데이터)
data = {
    '17시': [20, 30, 25, 15, 10],
    '18시': [35, 50, 45, 30, 25],
    '19시': [60, 80, 75, 50, 40],
    '20시': [90, 100, 95, 80, 70],
    '21시': [85, 95, 90, 75, 65],
    '22시': [60, 70, 65, 50, 45],
    '23시': [30, 40, 35, 25, 20]
}

time_slots = list(data.keys())

st.title('이태원 참사 인파 밀집도 시각화 (시간대별)')

# 시간대 선택
selected_time = st.selectbox('시간대를 선택하세요', time_slots)

# 선택된 시간대 데이터
densities = data[selected_time]

# 지도 생성 - 이태원 중심 좌표
m = folium.Map(location=[37.5335, 126.994], zoom_start=17)

# 밀집도 기반 마커 추가
for place, density in zip(locations.keys(), densities):
    lat, lon = locations[place]

    # 마커 크기와 색상 조절 (밀집도가 높을수록 붉고 크게)
    radius = density / 2  # 크기 조절용
    if density >= 80:
        color = 'red'
    elif density >= 50:
        color = 'orange'
    else:
        color = 'green'

    folium.CircleMarker(
        location=(lat, lon),
        radius=radius,
        color=color,
        fill=True,
        fill_color=color,
        fill_opacity=0.6,
        popup=f'{place}: 밀집도 {density}%'
    ).add_to(m)

# 스트림릿에 지도 표시
st_folium(m, width=700, height=500)


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
