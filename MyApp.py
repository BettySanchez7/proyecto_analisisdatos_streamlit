import streamlit as st
import pandas as pd
import numpy as np

import seaborn as sns
import matplotlib.pyplot as plt
from transformacion import *

import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import folium
from streamlit_folium import folium_static

selection = st.sidebar.selectbox(
    label="Elige la visualización",
    options=["Información general del proyecto","Mapa de zonas","Concentración anual", "Valores atipicos y distribuciones(Boxplots)", "Correlaciones", "Niveles de concentración","Treemap"],
    index=0,
)

if selection == "Información general del proyecto":
    st.markdown('''## :chart_with_upwards_trend: Analisis de calidad de Aire en la Ciudad de México 2016-2020
_________________________________________________________________________________________________

En la lista que tienes a tu izquierda podrás elegir la visualización que quieras ver, en cada una de ella encontraras información relavante del tema. 

:point_left: :bar_chart:

** INFORMACIÓN GENERAL DEL PROYECTO. ** :point_down: :point_down: :point_down: :point_down: :point_down: :point_down:


La Organización Mundial de la Salud estima que en 2012 aconteció un aproximado de 3.7 millones de muertes prematuras derivadas de enfermedades atribuidas a la contaminación del aire. Esto se refleja en su discurso del 2014: “La contaminación del aire es el riesgo para la salud ambiental número uno del mundo”.
  
Los problemas que aquejan a la incomparable urbanización no son pocos, desde crimen organizado, alcoholismo, inundaciones periódicas, fríos intensos y el que concierne a esta investigación, la contaminación del aire. De las majestuosas vistas que los primeros españoles hallaron en aquel valle, no queda nada. Incluso el propio cielo se esconde entre una densa nube de vapores tóxicos.

Los contaminantes criterio son aquellos que afectan el bienestar y la salud humana, por lo que cuentan con criterios para establecer o revisar límites máximos permisibles por medio de las Normas Oficiales Mexicanas. La concentración de estos contaminantes sirve para indicar la calidad del aire.

Dentro del grupo de contaminantes criterio se encuentran el dióxido de azufre (SO2), el dióxido de nitrógeno (NO2), el monóxido de carbono (CO), el ozono (O3) y las partículas en suspensión (PM10 y PM2.5). Durante nuestra investigación preliminar encontramos información sobre estos contaminantes, como sus afectaciones a la salud y presencia en el Valle de México, que consideramos útil para nuestro análisis:
Todos estos contaminantes tienen graves afectaciones a la salud por lo que es necesario no solo monitorear su concentración, sino también obtener con ellos un índice que nos permita clasificar la calidad del aire para así comunicarlo a la población en general. 

Con este objetivo en mente, en 1982 se diseñó el Índice Metropolitano de la Calidad del Aire (IMECA), cuya metodología transforma a una escala adimensional las concentraciones de los contaminantes criterio; así podemos entender que tan buena o mala es la calidad del aire observando el valor IMECA de dicho contaminante e incluso compararlo con otro, ya que tienen la misma escala. En la figura 1 se muestra esta escala de clasificación de los valores IMECA.

  
![](https://lh5.googleusercontent.com/07HClik8fpzXOVvVHCpbBIsc_ku2rtnSCv2p07o0JHnHgUkJp02HyDIQXY0dt8j-ISiy0Rh-wJ-YaKGbYCaPjuk2qQiNh-puh-JleOWb-Fj4z-xp9CrghqKhtReMHtEGzXDHun8a)

Figura 1. Clasificación IMECA


** Durante nuestra investigación nos dimos cuenta que la información sobre la calidad del aire en la Zona Metropolitana del Valle de México no es tan accesible: existen los datos y están abiertos al público, sin embargo, hay muy poca difusión sobre sus resultados, el último informe anual de la calidad del aire en ciudad de méxico se realizó en el 2018. Por lo tanto el objetivo de este proyecto es primero que nada analizar los datos disponibles para entender la problemática de la contaminación del aire en el Valle de México, y hacer que esta información sea más accesible, para luego proponer posibles soluciones. ** 

[SI QUIERES COLABORAR O VER MÁS ACERCA DEL PROYECTO PUEDES IR A NUESTRO REPOSITORIO]() :page_with_curl:

[O VER NUESTRO VÍDEO EXPLICANDO UN POCO MÁS NUESTRAS VISUALIZACIONES]() :video_camera:

''')

elif selection == "Mapa de zonas":
    m = folium.Map(location = [19.4325,-99.1330],zoom_start=10, width='100%',height='100%')

    folium.Choropleth(
        geo_data=zonas_zmvm,
        name='Monóxido + Dióxido de carbono, promedio anual',
        data=df_Co,
        columns=['index','Promedio'],
        key_on = 'feature.id',
        fill_color='YlGn',
        fill_opacity=0.7,
        line_opacity=0.8,
        legend_name='IMECA'
    ).add_to(m)
    folium_static(m)

elif selection == "Concentración anual":


    #PROMEDIO ANUAL
    st.write('\n')
    st.markdown('''** CONCENTRACIÓN PROMEDIO ANUAL DE CADA CONTAMINANTE POR ZONA **
                
Las siguientes graficas de tiempo tienen como objetivo mostrarte la concentración de cada contaminante 
( CO, NO2, PM10, O3 y SO2) por zona a lo largo del tiempo durante los años del 2005 al 2020).  :chart_with_upwards_trend:''')
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
    
    st.markdown(''' Con base en lo anterior podemos observar que el PM10 es el que tiene mas cambios a lo largo
                del tiempo y que en los dos ultimos años tiene un crecimiento mayor''')
elif selection == "Valores atipicos y distribuciones(Boxplots)":
    st.markdown('''** VALORES ATIPICOS Y DISTRIBUCIONES DE CONTAMINANTES**
                
Las graficas de cajas a continuación permiten observar valores atipicos y comparar distribuciones entre cada zona por contaminante
( CO, NO2, PM10, O3 y SO2).  :chart_with_upwards_trend:''')
    
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
    
    st.markdown(''' De las visualizaciones anteriores podemos decir que existe una mayoría de datos atipicos en
                el contaminante SO2, una de las conclusiones de las graficas anteriores es que se observa que la concentración del NO2
                en la zona centro es mayor que en las otras 4 zonas
                ''')

elif selection == "Correlaciones":
    st.markdown('** CORRELACIÓN ENTRE ZONAS POR CADA CONTAMINANTE**')
    for i in listacontam:
        fig, ax= plt.subplots()
        ax = sns.heatmap(i.corr())
        st.write(fig)
elif selection == "Niveles de concentración":

    st.markdown(''' ** CALIDAD DE AIRE DE ACUERDO A LOS VALORES IMECA **

El indice metropolitano de calidad de Aire califica los puntajes de calidad de aire con un 
código de colores que indica un rango de valor entre 0- 200 o más, En la figura 1 se muestra esta escala de clasificación de los valores IMECA.
            
![](https://lh5.googleusercontent.com/07HClik8fpzXOVvVHCpbBIsc_ku2rtnSCv2p07o0JHnHgUkJp02HyDIQXY0dt8j-ISiy0Rh-wJ-YaKGbYCaPjuk2qQiNh-puh-JleOWb-Fj4z-xp9CrghqKhtReMHtEGzXDHun8a)

Figura 1. Clasificación IMECA''')
    
    st.markdown('Clasificación por contaminantes')
                    
    fig, axes = plt.subplots(2, 3, figsize=(16, 10));
    ax = sns.barplot(x=cross_ne.index,y=cross_ne['Bueno']+cross_ne['Regular']+cross_ne['Mala'],color = 'red',ax=axes[0,0])
    sns.barplot(x=cross_ne.index,y=cross_ne['Bueno']+cross_ne['Regular'],color = 'yellow',ax=axes[0,0])
    sns.barplot(x=cross_ne.index,y=cross_ne['Bueno'],color = 'green',ax=axes[0,0])
    ax.set_title('Zona Noreste')
    ax.set(ylabel = 'Número de días')
    ax.set_xticklabels(ax.get_xticklabels(), rotation=5);
    ax2 = sns.barplot(x=cross_so.index,y=cross_so['Bueno']+cross_so['Regular']+cross_so['Mala'],color = 'red',ax=axes[0,1])
    sns.barplot(x=cross_so.index,y=cross_so['Bueno']+cross_so['Regular'],color = 'yellow',ax=axes[0,1])
    sns.barplot(x=cross_so.index,y=cross_so['Bueno'],color = 'green',ax=axes[0,1])
    ax2.set_title('Zona Suroeste')
    ax2.set(ylabel = 'Número de días')
    ax2.set_xticklabels(ax.get_xticklabels(), rotation=5);
    ax3 = sns.barplot(x=cross_no.index,y=cross_no['Bueno']+cross_no['Regular']+cross_no['Mala'],color = 'red',ax=axes[0,2])
    sns.barplot(x=cross_no.index,y=cross_no['Bueno']+cross_no['Regular'],color = 'yellow',ax=axes[0,2])
    sns.barplot(x=cross_no.index,y=cross_no['Bueno'],color = 'green',ax=axes[0,2])
    ax3.set_title('Zona Noroeste')
    ax3.set(ylabel = 'Número de días')
    ax3.set_xticklabels(ax.get_xticklabels(), rotation=5);
    ax4 = sns.barplot(x=cross_se.index,y=cross_se['Bueno']+cross_se['Regular']+cross_se['Mala'],color = 'red',ax=axes[1,0])
    sns.barplot(x=cross_se.index,y=cross_se['Bueno']+cross_se['Regular'],color = 'yellow',ax=axes[1,0])
    sns.barplot(x=cross_se.index,y=cross_se['Bueno'],color = 'green',ax=axes[1,0])
    ax4.set_title('Zona Sureste')
    ax4.set(ylabel = 'Número de días')
    ax4.set_xticklabels(ax.get_xticklabels(), rotation=5);
    ax5 = sns.barplot(x=cross_ce.index,y=cross_ce['Bueno']+cross_ce['Regular']+cross_ce['Mala'],color = 'red',ax=axes[1,2])
    sns.barplot(x=cross_ce.index,y=cross_ce['Bueno']+cross_ce['Regular'],color = 'yellow',ax=axes[1,2])
    sns.barplot(x=cross_ce.index,y=cross_no['Bueno'],color = 'green',ax=axes[1,2])
    ax5.set_title('Zona Centro')
    ax5.set(ylabel = 'Número de días')
    ax5.set_xticklabels(ax.get_xticklabels(), rotation=5);
    
    st.write(fig)
    
    st.markdown('''Como se puede observar, de las 5 zonas, las zonas del norte (noreste y noroeste), 
                presentan las peor calidad del aire en comparación con las otras 3 zonas. Además la 
                zona suroeste es la que prenta una mejor calidad del aire. Gráficas nos muestran de 
                los 366 días que tuvo el año 2020, cuantos de estos tuvieron un índice IMECA, bueno, 
                regular o malo.''')
       
    st.markdown('Clasificación por zonas')
    
    fig, axes = plt.subplots(2, 3, figsize=(16, 10), sharey=True)
    ax = sns.barplot(x=df_Co_redux.index,y=df_Co_redux['Bueno'] ,color = 'green',ax=axes[0,0])
    ax.set_title('Monóxido + dióxido de carbono')
    ax.set(ylabel = 'Número de días')
    ax.set_xticklabels(ax.get_xticklabels(), rotation=20);

    ax2 = sns.barplot(x=df_No2_redux.index,y=df_No2_redux['Bueno'] ,color = 'green',ax=axes[0,1])
    ax2.set_title('Dióxido de nitrógeno')
    ax2.set(ylabel = 'Número de días')
    ax2.set_xticklabels(ax.get_xticklabels(), rotation=20);

    ax3 = sns.barplot(x=df_O3_redux.index,y=df_O3_redux['Bueno']+df_O3_redux['Regular'] ,color = 'yellow',ax=axes[0,2])
    ax3 = sns.barplot(x=df_O3_redux.index,y=df_O3_redux['Bueno'] ,color = 'green',ax=axes[0,2])
    ax3.set_title('Ozono')
    ax3.set(ylabel = 'Número de días')
    ax3.set_xticklabels(ax.get_xticklabels(), rotation=20);

    ax4 = sns.barplot(x=df_Pm10_redux.index,y=df_Pm10_redux['Bueno']+df_Pm10_redux['Regular']+df_Pm10_redux['Mala']  ,color = 'red',ax=axes[1,0])
    ax4 = sns.barplot(x=df_Pm10_redux.index,y=df_Pm10_redux['Bueno']+df_Pm10_redux['Regular'] ,color = 'yellow',ax=axes[1,0])
    ax4 = sns.barplot(x=df_Pm10_redux.index,y=df_Pm10_redux['Bueno'] ,color = 'green',ax=axes[1,0])
    ax4.set_title('Partículas menores a 10 micras')
    ax4.set(ylabel = 'Número de días')
    ax4.set_xticklabels(ax.get_xticklabels(), rotation=20);

    ax5 = sns.barplot(x=df_So2_redux.index,y=df_So2_redux['Bueno']+df_So2_redux['Regular'] ,color = 'yellow',ax=axes[1,2])
    ax5 = sns.barplot(x=df_So2_redux.index,y=df_So2_redux['Bueno'] ,color = 'green',ax=axes[1,2])
    ax5.set_title('Dióxido de asufre')
    ax5.set(ylabel = 'Número de días')
    ax5.set_xticklabels(ax.get_xticklabels(), rotation=20);
    
    st.write(fig)
    
    st.markdown('''El monóxido+dióxido de nitrógeno y el dióxido de nitrógeno en promedio diario, 
                presentaron valores buenos de concentración. De igual manera el dióxido de asufre, 
                con muy pocos días de calidad de aire regular. Después le sigue el ozono que presenta 
                peor calidad en el suroeste, siendo aquí la única vez que destaca por mala calidad.
                Donde se observa las peores concentraciones es en las particulas menores de 10 micras, 
                donde en promedio, se tuvieron varios días con índices malos de calidad de aire.''')

elif selection == "Treemap":
    st.markdown(''' ** DISTRIBUCIÓN DE CONCENTRACIÓN DE CONTAMINANTES POR AÑO Y CONTAMINANTE **
                
    Las siguientes visualizaciones son graficas dinámicas, te permiten observar cual fue
    la distribución de cada contaminante por año. 
                ''')
    lista_zonas = ['suroeste','sureste','noreste','noroeste','centro']
    for zona in lista_zonas:
        fig = px.treemap( Df_total_anual, path=['fecha','categoria'], values=zona, title=zona)
        st.plotly_chart(fig)

