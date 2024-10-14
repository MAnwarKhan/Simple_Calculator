git init
git add .
git commit -m "Initial commit with calculator code"
git branch -M main
git remote add origin <your-github-repository-url>
git push -u origin main

pip install streamlit

import streamlit as st

def calculate(operation, num1, num2):
    if operation == 'Add':
        return num1 + num2
    elif operation == 'Subtract':
        return num1 - num2
    elif operation == 'Multiply':
        return num1 * num2
    elif operation == 'Divide':
        return num1 / num2

st.title("Generative Calculator")
operation = st.selectbox('Select Operation', ['Add', 'Subtract', 'Multiply', 'Divide'])
num1 = st.number_input('Enter first number')
num2 = st.number_input('Enter second number')

if st.button('Calculate'):
    result = calculate(operation, num1, num2)
    st.write(f"The result of {operation} is: {result}")

