import streamlit as st 
import pandas as pd
import numpy as np
voc = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSeARXO3MT92XWpg2IwyQOQ8Wi2upeEkqJvNJz5i3bRqHdJIrTchGBBclVu-3Jd1ohYKM4IxecgV64I/pub?output=csv')
l = voc.shape[0]
word_fr = voc['Définition'].values[i]
st.write("Traduis : "+word_fr)
indices = np.random.choice(l, size=4, replace=False)
j = np.random.choice(indices)

def is_correct(i, j):
  if i==j:
    st.write("Bien joué !")
  else:
    st.write("Perdu !")

for i in range(4):
  st.button(voc["Hanzi"].values[indices[i]], on_click= is_correct, args=(indices[i],j))