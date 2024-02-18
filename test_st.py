import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from datetime import time, datetime

## Exo 1: st.button
st.header('st.button') ## Création d'un titre, 

if st.button('say hello'): ## Say hello: texte affiché sur le bouton (label)
    st.write('Hello, *world!* :sunglasses:') ## Si le bouton est cliqué, retourne True si le boutton est cliqué, False sinon
else:
    st.write('goodbye') ## Sinon


## Exo 2: st.write
st.header('st.write')
st.subheader('display numbers')
st.write(1234)

st.subheader('display dataframe')
df_test = pd.DataFrame()
df_test['first columns'] = np.random.randint(10, size = 5)
df_test['second columns'] = np.random.randint(100, size = 5)
st.write(df_test)

st.subheader('Accept multpiple arguments')
st.write('below is a dataframe', df_test, 'Above is a dataframe')

st.subheader('Display charts')
c = alt.Chart(df_test).mark_circle().encode(
    x='first columns', y="second columns"
)
st.write(c)

## Exo 3: st.slider
# Types de données pris en charge: int, float, date, time, datetime
st.header('st.slider')

st.subheader('Slider')
age = st.slider(min_value = 0, max_value = 130, label = "How old are you ?", value = 10)
st.write('I\'m', age, 'years old')

st.subheader("Range slider")
range_values = st.slider(label = "select a range of values", min_value = 0.0, max_value = 100.0, value = (10.0, 15.0))
st.write('Values : ', range_values)

st.subheader("Range time slider")
appointment = st.slider(label = "schedule your appointment", min_value = datetime.time(00, 00), 
                        max_value = datetime.time(23, 59), value = (datetime.time(8, 00), datetime.time(18, 00)))
st.write('You are scheduled for : ', appointment)

st.subheader("Datetime slider")
# Ne fonctionne plus ??


## Exo 4: st.line_chart
# graphique linéaire

st.header("st.line_chart")

st.subheader("Line Chart")

my_df = pd.DataFrame()
my_df['a'] = np.random.randint(28, size = 5)
my_df['b'] = np.random.randint(28, size = 5)
my_df['c'] = np.random.randint(28, size = 5)

st.line_chart(my_df)

