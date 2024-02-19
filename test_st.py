import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import datetime
# import pandas_profiling
# from streamlit_pandas_profiling import st_profile_report

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

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

# st.write(chart_data)

st.line_chart(chart_data)

## Exo 5: st.selectbox
# affichage d'un widget de sélection

st.header("st.selectbox")
fav_color = st.selectbox("What is your favorite color?", ("Blue", "Red", "Green"))
st.write("Your favorite color is", fav_color)

## Exo 6: st.multiselect
# Affiche un widget multiselect

st.header("st.multiselect")
fav_colors = st.multiselect("What are your favorite colors?", ["Yellow", "Red", "Blue", "Green"], ["Yellow", "Red"])
st.write("You selected:", fav_colors)

## Exo 7: st.checkbox
# Widget de type checkbox

st.header("st.checkbox")

st.write("What would you like to order?")

ice_cream = st.checkbox("Ice cream")
coffee = st.checkbox("Coffee")
cola = st.checkbox("Cola")

if ice_cream:
    st.write("Great! here is some more")
if coffee:
    st.write("Ok for coffee")
if cola:
    st.write("Here you go")

# ## Exo 8: Components
# st.header('`streamlit_pandas_profiling`')

# df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')

# pr = df.profile_report()
# st_profile_report(pr)
    

## Exo 9: st.latex
# Affiche des expressions mathématiques au format LaTeX
    
st.header("st.latex")

st.latex(r'''
     ar + ar^2 + ar^3 + \cdots + ar^{n-1} =
     \sum_{k=0}^{n-1} ar^k =
     a \left(\frac{1-r^{n}}{1-r}\right)
     ''')


## Créer une side bar (menu)
number = st.sidebar.slider('Select a number:', 0, 10, 5)
st.write('Selected number from slider widget is:', number)

## Exo 10: st.secrets
# permet de stocker des informations confidentielles

st.header("st.secrets")
st.write(st.secrets["message"])
