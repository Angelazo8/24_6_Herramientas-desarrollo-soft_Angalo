import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv') # leer los datos

st.header('Caracteristicas de Autos en venta 2024')

hist_button = st.button('Construir histograma') # crear un botón
        
        if hist_button: # al hacer clic en el botón
            st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches') # escribir un mensaje
            
            fig = px.histogram(car_data, x="odometer") # crear un histograma
        
            st.plotly_chart(fig, use_container_width=True) # mostrar un gráfico Plotly interactivo
