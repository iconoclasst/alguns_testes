import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv("pizzas.csv")
modelo = LinearRegression()

x = df[['diametro']]
y = df[['preco']]

modelo.fit(x, y)

st.title("Prevendo valor de pizzas ;-;")
st.divider()

diam = st.number_input("Diametro da pizza: ")

if diam:
    preco_prev = modelo.predict([[diam]])[0][0]
    st.write(f"Valor previsto: {preco_prev:.2f}")