import streamlit as st
import pandas as pd
import pickle

st.write("""
# Sale Prediction Value

This app predicts the **Sale Prediction Value** in TV, Radio & Newspaper!
""")

st.sidebar.header('User Input Parameters')

def user_input_advertising():
        tv = st.sidebar.slider('TV ', 0.0, 25.0, 5.4)
        radio = st.sidebar.slider('Radio', 0.0, 25.0, 3.4)
        newspaper = st.sidebar.slider('Newspaper', 0.0, 25.0, 1.3)
        data = {'TV': tv,
                'Radio': radio,
                'Newspaper': newspaper}
        sale = pd.DataFrame(data, index=[0])
        return sale

df = user_input_advertising()

st.subheader('User Input values')
st.write(df)

loaded_model = pickle.load(open("modelSvrRegressions.h5", "rb"))

prediction = loaded_model.predict(df)
# prediction.columns = ['Sales']
# st.write(type(prediction))
sales = pd.DataFrame(prediction, columns=['Sales'])

st.subheader('Sales Prediction')
st.write(sales) 
