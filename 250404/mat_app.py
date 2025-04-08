import streamlit as st
import pandas as pd 
import matplotlib as mpl 
import matplotlib.pyplot as plt 
import seaborn as sns 
import matplotlib.font_manager as fm 


# 한글폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic' 
plt.rcParams['axes.unicode_minus'] = False 
sns.set(font='Malgun Gothic', 
        rc={'axes.unicode_minus' : False}, 
        style='darkgrid')

# 페이지 설정
st.set_page_config(page_title="Matplotlib & Seaborn 튜토리얼", layout="wide") 
st.title("Matplotlib & Seaborn 튜토리얼") 

# 데이터셋 불러오기 
tips = sns.load_dataset('tips') 

# 데이터 미리보기 
st.subheader('데이터 미리보기')
st.dataframe(tips.head())

# 기본 막대 그래프, matplotlit + seaborn 
st.subheader("1. 기본 막대 그래프")
fig, ax = plt.subplots(figsize=(10, 6)) # 객체지향방식으로방식으로 차트 작성하는이유 : 그래프를 그리는목적 (이쁘게) 잘 나오라고 (세부옵션 설정가능)
# matplotlib 문법
sns.barplot(data=tips, x='day', y='total_bill', ax=ax) # seaborn 문법 : 통계와 관련된 시각화
ax.set_title('요일별 평균 지불 금액') # matplotlib 문법
ax.set_xlabel('요일') # matplotlib 문법
ax.set_ylabel('평균 지불 금액($)') # matplotlib 문법

# plt.show() ==>\ 주피터 놋북, 구글 코랩 에서 활용할때 사용하는 문법 
st.pyplot(fig) #streamlit 문법

#산점도
#x,y축이 연속형 변수여야합니다.
st.subheader("2. 산점도")
fig1, ax1 = plt.subplots(figsize=(10, 6))

sns.barplot(data=tips, x='day', y='total_bill', ax=ax) 
sns.scatterplot(data=tips,
                 x='total_bill', 
                 y='tip', 
                 hue='day' ,
                 size='size',
                 ax=ax1)
st.pyplot(fig1)

#히트맵
st.subheader("3. 히트맵")

#요일과 시간별 평균 팁 계산
pivot_df = tips.pivot_table(values='tip', index='day', columns='time', aggfunc='mean')
fig2, ax2 = plt.subplots(figsize=(10, 6)) 
sns.heatmap(pivot_df, annot=True, fmt='.2f', ax=ax2)
st.pyplot(fig2)

#회귀선이 있는 산점도 
st.subheader("4.회귀선이 있는 산점도")
fig3, ax3 = plt.subplots(figsize=(10,6))
sns.regplot(data=tips, x='total_bill', y='tip' , scatter_kws={'alpha':0.5}, ax=ax3)
st.pyplot(fig3)

# 지피티 =  fig , ax = plt.suvplots() 이런방식으로 만드세여