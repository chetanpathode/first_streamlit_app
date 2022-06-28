import streamlit

streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfast Favorites')
streamlit.text('🥣Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗Kale,Spinach & Rocket Smoothie')
streamlit.text('🐔Hard Boiled Free-range Egg')
streamlit.text('🥑Avocado Toast')

streamlit.header('🍇🍓Build Your Own Fruit Smoothie🍌🥭')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
Fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
Fruits_show=my_fruit_list.loc[Fruits_selected]

streamlit.dataframe(Fruits_show)

streamlit.header("Fruityvice Fruit Advice!")
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
#normalizes json objects
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
#converts nirmalised file to dataframe
streamlit.dataframe(fruityvice_normalized)

import snowflake.connector

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from fruit_load_list")
my_data_row = my_cur.fetchall()
streamlit.header("The fruit Load list contains")
streamlit.dataframe(my_data_row)

add_my_fruit=streamlit.text_input('Which fruit you want to add',)


my_cur.execute("insert into fruit_load_list (Fruit_name) values (?)",(add_my_fruit,))

streamlit.header("insert into fruit_load_list (Fruit_name) values (?)",(add_my_fruit))

