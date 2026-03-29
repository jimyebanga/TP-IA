import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.title("File uploader")
st.subheader("Input_csv")
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.subheader('DataFrame')
    st.write(df)
    col1,col2= st.columns(2)
    with col1:
        fig1 = plt.figure()
        sns.scatterplot(x='EstimatedSalary', y='Age', hue = 'Purchased',data=df)
        st.pyplot(fig1)
    with col2:
        fig2 = plt.figure()
        sns.histplot(df.Age)
        st.pyplot(fig2)