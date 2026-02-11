import streamlit as st

st.title("Temperature Converter")

celsius = st.number_input("Enter temperature in Celsius:", value=0.0)

if st.button("Convert"):
    fahrenheit = (celsius * 9/5) + 32
    st.success(f"{celsius}°C = {fahrenheit}°F")
