import streamlit as st
import pandas as pd

st.title('💕 Machine Learning App')

st.info('This app builds a machine learning model!')

df = pd.read_csv("penguins_cleaned (1).csv")

with st.expander("📊 Data", expanded=False):

    st.write("**Raw Data**")
    st.dataframe(df, use_container_width=True)

    X = df.drop('species', axis=1)

    st.write("**X — Features**")
    st.dataframe(X, use_container_width=True)

    y = df['species']

    st.write("**y — Target**")
    st.dataframe(y, use_container_width=True)


with st.expander("📈 Data Visualisation", expanded=False):

    st.scatter_chart(
        data=df,
        x='bill_length_mm',
        y='flipper_length_mm',
        color='species'
    )
