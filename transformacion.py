
import pandas as pd
import numpy as np



#Lectura de los Datos
CO_mensual = pd.read_csv('datos/promedios_mensuales/CO_mensual.csv')
NO2_mensual = pd.read_csv('datos/promedios_mensuales/NO2_mensual.csv')
O3_mensual = pd.read_csv('datos/promedios_mensuales/O3_mensual.csv')
PM10_mensual = pd.read_csv('datos/promedios_mensuales/PM10_mensual.csv')
SO2_mensual = pd.read_csv('datos/promedios_mensuales/SO2_mensual.csv')

listacontam = [CO_mensual,NO2_mensual,O3_mensual,PM10_mensual,SO2_mensual]
for contam in listacontam:
    contam.columns= ['fecha', 'noreste', 'suroeste', 'noroeste', 'sureste', 'centro']

#Realizando el Casting correspondiente

casting={
    "fecha":"datetime64[ns]"
}

CO_mensual=CO_mensual.astype(casting)
NO2_mensual = NO2_mensual.astype(casting)
O3_mensual = O3_mensual.astype(casting)
PM10_mensual= PM10_mensual.astype(casting)
SO2_mensual= SO2_mensual.astype(casting)

CO_anual=CO_mensual.resample('Y', on='fecha').mean()
NO2_anual=NO2_mensual.resample('Y', on='fecha').mean()
O3_anual=O3_mensual.resample('Y', on='fecha').mean()
PM10_anual=PM10_mensual.resample('Y', on='fecha').mean()
SO2_anual=SO2_mensual.resample('Y', on='fecha').mean()

CO_anual['categoria'] = "CO"
NO2_anual['categoria'] = "NO2"
O3_anual['categoria'] = "O3"
PM10_anual['categoria'] = "PM10"
SO2_anual['categoria'] = "SO2"

listacontam2=[CO_anual,NO2_anual,O3_anual,PM10_anual,SO2_anual]

Df_total_anual = pd.concat(listacontam2)

Df_total_anual['fecha'] = Df_total_anual.index