import streamlit as st
import pandas as pd

st.title('💕Machine learning App')

st.info('This is app builds a machine learning model!')

with st.expander("data"):
    st.write("**Raw Data**")
    df = pd.read_csv("https://raw.githubusercontent.com/Nihal25-hub/machine-learning/master/penguins_cleaned%20%281%29.csv")
    df

with st.expander("📊 Data", expanded=False):
    st.subheader("X — Features")
    st.dataframe(X, use_container_width=True)

    st.subheader("Y — Target")
    st.dataframe(y, use_container_width=True)

with st.expander('data visualisation'):
    st.scatter_chart(data=df, x='bill_length_mm' , y='bill_length_mm' , color='species')
    
