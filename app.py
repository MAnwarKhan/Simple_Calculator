import streamlit as st
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model

# Load the pre-trained model
model = load_model('calculator_model.h5')

# Title of the app
st.title("Simple Calculator with Generative Model")

# Input fields for the two numbers
num1 = st.number_input("Enter first number", min_value=0)
num2 = st.number_input("Enter second number", min_value=0)

# Predict button
if st.button('Calculate'):
    # Create input data for the model
    input_data = np.array([[num1, num2]])
    
    # Use the model to predict the sum
    result = model.predict(input_data)
    
    # Display the result
    st.write(f'The predicted sum is: {result[0][0]}')
