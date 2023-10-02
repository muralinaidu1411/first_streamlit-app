import streamlit 
import pandas as pd

streamlit.title('my parents new healthy diner')

streamlit.header('BreakFast Menu')

streamlit.text(' 🥣 omega 3')

streamlit.text('🐔 omlette')
my_fruit_list=pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
streamlit.dataframe('my_fruit_list')
