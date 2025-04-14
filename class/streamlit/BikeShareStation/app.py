from helpers import *
import streamlit as st

st.title('Toronto Bike Share Station Status')
st.markdown('This Dashboard tracks bike availability at each bike station in Toronto.')
 
data_df = query_stat