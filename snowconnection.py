import streamlit
import pandas
import snowflake.connector
streamlit.header('Snowflake Healthcare App')
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
