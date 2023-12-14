import streamlit as st
import pandas as pd
import pickle

st.write("""
# Advertising Prediction Value

This app predicts the **Advertiding channel** type!
""")

st.sidebar.header('User Input Parameters')

def user_input_advertising():
        tv = st.sidebar.slider('TV ', 4.3, 7.9, 5.4)
        radio = st.sidebar.slider('Radio', 2.0, 4.4, 3.4)
        newspaper = st.sidebar.slider('Newspaper', 1.0, 6.9, 1.3)
        data = {'tv': tv,
                'sradio': radio,
                'newspaper': newspaper}
        sale = pd.DataFrame(data, index=[0])
        return sale

df = user_input_sale()

st.subheader('User Input parameters')
st.write(df)

loaded_model = pickle.load(open("modelSvrRegression.h5", "rb"))

prediction = loaded_model.predict(df)

st.subheader('Prediction')
st.write(prediction)
