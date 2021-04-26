import streamlit as st
import pandas as pd
import numpy as np

import seaborn as sns
import matplotlib.pyplot as plt
from transformacion import *

import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

st.title("Analisis de calidad de Aire en la Ciudad de México 2016-2020")

st.write('\n')


selection = st.sidebar.selectbox(
    label="Elige la visualización",
    options=["Medidas estadisticas", "Grafica de tiempo 2016-2020", "Boxplots", "Treemap"],
    index=0,
)

if selection == "Grafica de tiempo 2016-2020":

    #PROMEDIO ANUAL
    st.write('\n')
    st.markdown('** CONCENTRACIÓN PROMEDIO ANUAL DE CADA CONTAMINANTE POR ZONA **')
    fig, axes = plt.subplots(5, 1, figsize=(10, 30), sharex=True, sharey=True)
    sns.lineplot(data=CO_mensual.resample('Y', on='fecha').mean(), ax=axes[0])
    axes[0].set(title='Promedio anual de conaminación CO por zonas',ylabel='Concentración de contaminación',xlabel="Año")

    sns.lineplot(data=NO2_mensual.resample('Y', on='fecha').mean(), ax=axes[1])
    axes[1].set(title='Promedio anual de conaminación NO2 por zonas',ylabel='Concentración de contaminación',xlabel="Año")

    sns.lineplot(data=O3_mensual.resample('Y', on='fecha').mean(), ax=axes[2])
    axes[2].set(title='Promedio anual de conaminación O3 por zonas',ylabel='Concentración de contaminación',xlabel="Año")

    sns.lineplot(data=PM10_mensual.resample('Y', on='fecha').mean(), ax=axes[3])
    axes[3].set(title='Promedio anual de conaminación PM10 por zonas',ylabel='Concentración de contaminación',xlabel="Año")

    sns.lineplot(data=SO2_mensual.resample('Y', on='fecha').mean(), ax=axes[4])
    axes[4].set(title='Promedio anual de conaminación SO2 por zonas',ylabel='Concentración de contaminación',xlabel="Año")
    st.pyplot(fig)
if selection == "Boxplots":
    fig, ax = plt.subplots() #solved by add this line 
    ax = CO_mensual.boxplot(vert=False,color='r')
    ax.set(title="CO")
    st.pyplot(fig)
    
    fig, ax = plt.subplots() #solved by add this line 
    ax = NO2_mensual.boxplot(vert=False,color='b')
    ax.set(title="NO2")
    st.pyplot(fig)
    
    fig, ax = plt.subplots() #solved by add this line 
    ax = O3_mensual.boxplot(vert=False,color='g')
    ax.set(title="O3")
    st.pyplot(fig)
    
    fig, ax = plt.subplots() #solved by add this line 
    ax = PM10_mensual.boxplot(vert=False,color='y')
    ax.set(title="PM10")
    st.pyplot(fig)
    
    fig, ax = plt.subplots() #solved by add this line 
    ax = SO2_mensual.boxplot(vert=False,color='b')
    ax.set(title="SO2")
    st.pyplot(fig)

if selection == "Treemap":
    lista_zonas = ['suroeste','sureste','noreste','noroeste','centro']
for zona in lista_zonas:
    fig = px.treemap( Df_total_anual, path=['fecha','categoria'], values=zona, title=zona)
    st.plotly_chart(fig)