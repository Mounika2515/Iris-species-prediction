import streamlit as st
import pickle
import numpy as np

# Load saved model
model = pickle.load(open('iris_model1.pkl', 'rb'))

# Title
st.title("Iris Flower Prediction App")

st.write("Enter flower measurements below:")

# Input boxes
sepal_length = st.number_input("Sepal Length")
sepal_width = st.number_input("Sepal Width")
petal_length = st.number_input("Petal Length")
petal_width = st.number_input("Petal Width")

# Prediction button
if st.button("Predict"):

    features = np.array([
        [sepal_length,
         sepal_width,
         petal_length,
         petal_width]
    ])

    prediction = model.predict(features)

    st.success(f"Predicted Flower: {prediction[0]}")