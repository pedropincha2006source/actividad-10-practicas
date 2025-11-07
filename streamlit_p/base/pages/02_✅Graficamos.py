import streamlit as st
import pandas as pd

import streamlit as st
import matplotlib.pyplot as plt


areas = pd.read_csv('area_protegida.csv')
st.title("Gráfico")
st.write("El grafico muestra la cantidad de cada tipo de area protegida las reservas siendo mayoria y los monumentos naturales el tipo que menos hay.")
fig,ax = plt.subplots()
areas['tap'] = areas['tap'].replace({
    1: 'Parque', 2: "Reserva", 3: "Monumento Natural", 0: "Informacion no disponible"})

# Crear el gráfico de barras
conteo_tipos = areas['tap'].value_counts()
conteo_tipos.plot(kind='bar', ax=ax, color='skyblue')
# Agregar etiquetas y título
ax.set_xlabel('Tipo de area protegida')
ax.set_ylabel('Cantidad')
ax.set_title('cantidad de cada tipo de Areas protegidas')

# Mostrar el gráfico
st.pyplot(fig)
