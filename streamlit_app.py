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
with st.sidebar:
    st.header('Input Features')
    island = st.selectbox('Island' ,('Biscode','Dream' , 'Torgersen'))
    gender = st.selectbox('Gender',('male','female'))
    bill_length = st.slider('Bill length (mm)', 32.1 , 59.8 , 43.9)
    bill_depth = st.slider('Bill depth (mm)' , 13.1 , 21.5 , 17.2)
    flipper_length = st.slider('Flipper Length (mm)' , 172.0 , 231.0 , 201.0)
    body_mass_g = st.slider('Body Mass (g)' , 2700.0 , 6300.0 , 4207.0)

data = {
    "island": island,
    "bill_length_mm": bill_length,
    "bill_depth_mm": bill_depth,
    "flipper_length_mm": flipper_length,
    "body_mass_g": body_mass,
    "sex": gender
}

input_df = pd.DataFrame([data])
        
        
        
    
    
    
