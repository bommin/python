# streamlit, pandas 라이브러리 불러오기 
import streamlit as st
import pandas as pd


st.title('Unit 3. Data display elements')
st.caption('참조사이트: https://docs.streamlit.io/library/api-reference/data')

st.header(' 1. Metric')
st.metric(label='Temperature', value='30.5')

st.header('2. columns')
st.columns()

st.header('3. Dataframe')
st.caption('10개 행  기준 스크롤, 열 크기조정, 열 정렬, 테이블  확대')
# 파일 위치- https://raw.githubusercontent.com/huhshin/streamlit/master/data_titanic.csv


st.header('4. Table')



# 파일실행: File > New > Terminal(anaconda prompt) - streamlit run streamlit\3.data.py