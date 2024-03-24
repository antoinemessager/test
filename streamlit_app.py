import streamlit as st 
import pandas as pd
import numpy as np
voc = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSeARXO3MT92XWpg2IwyQOQ8Wi2upeEkqJvNJz5i3bRqHdJIrTchGBBclVu-3Jd1ohYKM4IxecgV64I/pub?output=csv')
l = voc.shape[0]
indices = np.random.choice(l, size=4, replace=False)
j = np.random.choice(indices)
word_fr=voc['Définition'].values[j]
st.write('Traduis: '+word_fr)
def is_correct(i, j):
  if i==j:
    st.write("Bien joué !")
  else:
    st.write("Perdu !")

col1, col2 = st.columns(2) 
with col1:
    for i in range(2):
        st.button(voc["Hanzi"].values[indices[i]], on_click= is_correct, args=(indices[i],j))
with col2:
    for i in range(2,4):
        st.button(voc["Hanzi"].values[indices[i]], on_click= is_correct, args=(indices[i],j))

st.markdown(""" div.stButton > button:first-child {
background-color: #00cc00;color:white;font-size:20px;height:3em;width:30em;border-radius:10px 10px 10px 10px;
}
""", unsafe_allow_html=True)