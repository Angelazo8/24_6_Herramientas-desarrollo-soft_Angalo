import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')  # leer los datos

st.header('Caracteristicas de Autos en venta 2024')

# crear una casilla de verificación
build_histogram = st.checkbox('Construir un histograma')

if build_histogram:  # si la casilla de verificación está seleccionada
    st.write('Construir un histograma para la columna odómetro')
    fig = px.histogram(car_data, x="odometer")  # crear un histograma
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

bar_button = st.button('Construir un grafico de barras')  # Crear boton

if bar_button:  # al hacer clic en el boton 2
    # escribir un mensaje
    st.write('Creacion de grafico de barras')
    fig2 = px.bar(car_data, x="type", color="fuel",
                  title="Condition of cars per type")  # Crear un grafico de barras
    st.plotly_chart(fig2)  # Mostrar un grafico de plotly
