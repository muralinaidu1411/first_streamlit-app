import streamlit 
import pandas as pd
import requests
import snowflake.connector

streamlit.title('my parents new healthy diner')

streamlit.header('BreakFast Menu')

streamlit.text(' 🥣 omega 3')

streamlit.text('🐔 omlette')
my_fruit_list=pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
my_fruit_list=my_fruit_list.set_index('Fruit')

#pick up some fruits you want
fruits_selected=streamlit.multiselect("pick some fruits:",list(my_fruit_list.index),['Apple','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)


fruits_selected1=streamlit.multiselect("pick some fruits:",list(my_fruit_list.index),[])
fruits_to_show1 = my_fruit_list.loc[fruits_selected1]
streamlit.dataframe(fruits_to_show1)
#show the fruit list 
streamlit.dataframe(my_fruit_list)




fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
streamlit.text(fruityvice_response)

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)
