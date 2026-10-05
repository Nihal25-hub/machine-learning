import streamlit as st
import pandas as pd

st.title('💕Machine learning App')

st.info('This is app builds a machine learning model!')

df = pd.read_csv("https://raw.githubusercontent.com/Nihal25-hub/machine-learning/master/data/penguins_cleaned.csv")
df
