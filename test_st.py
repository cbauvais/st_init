import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

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