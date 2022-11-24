import streamlit
import pandas as pd


streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfast Favorites')

streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinacle & Rocket Smoothie')
strealit.text('Hard-Boiled Free-Range Egg')

streamlit.header(' Build Your Own Fruit Smoothie ')

my_fruit_list = pd.read.csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
streamlit.dataframe(my_fruit_list)
