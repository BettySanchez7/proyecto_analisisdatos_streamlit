
import pandas as pd
import numpy as np


#Lectura de los Datos
CO_mensual = pd.read_csv('CO_mensual.csv')
NO2_mensual = pd.read_csv('NO2_mensual.csv')
O3_mensual = pd.read_csv('O3_mensual.csv')
PM10_mensual = pd.read_csv('PM10_mensual.csv')
SO2_mensual = pd.read_csv('SO2_mensual.csv')

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

lista=['noreste','noroeste','sureste',
       'suroeste', 'centro']

#############lectura para visualizaciones jesus
#Lectura de los Datos
CO_mensual2 = pd.read_csv('CO_mensual.csv', index_col=0)
NO2_mensual2 = pd.read_csv('NO2_mensual.csv', index_col=0)
O3_mensual2 = pd.read_csv('O3_mensual.csv', index_col=0)
PM10_mensual2 = pd.read_csv('PM10_mensual.csv', index_col=0)
SO2_mensual2 = pd.read_csv('SO2_mensual.csv', index_col=0)

#Obteniendo promedios generales (2005-2020)
CO_promedios = CO_mensual2.mean()
NO2_promedios = NO2_mensual2.mean()
O3_promedios = O3_mensual2.mean()
PM10_promedios = PM10_mensual2.mean()
SO2_promedios = SO2_mensual2.mean()

###########################lectura para visualizaciones leo
url_1="https://raw.githubusercontent.com/BettySanchez7/Proyecto_AnalisisDatosConPython/main/datos/datos_limpios_imeca/CO.csv"
url_2 = "https://raw.githubusercontent.com/BettySanchez7/Proyecto_AnalisisDatosConPython/main/datos/datos_limpios_imeca/NO2.csv"
url_3 = "https://raw.githubusercontent.com/BettySanchez7/Proyecto_AnalisisDatosConPython/main/datos/datos_limpios_imeca/O3.csv"
url_4 = "https://raw.githubusercontent.com/BettySanchez7/Proyecto_AnalisisDatosConPython/main/datos/datos_limpios_imeca/SO2.csv"
url_5 = "https://raw.githubusercontent.com/BettySanchez7/Proyecto_AnalisisDatosConPython/main/datos/datos_limpios_imeca/PM10.csv"

df_Co=pd.read_csv(url_1)
df_No2 = pd.read_csv(url_2)
df_O3 = pd.read_csv(url_3)
df_So2 = pd.read_csv(url_4)
df_Pm10 = pd.read_csv(url_5)

#Filtrado por año
df_Co=df_Co[df_Co['fecha']>='2020-01-01']
df_No2=df_No2[df_No2['fecha']>='2020-01-01']
df_O3=df_O3[df_O3['fecha']>='2020-01-01']
df_So2=df_So2[df_So2['fecha']>='2020-01-01']
df_Pm10=df_Pm10[df_Pm10['fecha']>='2020-01-01']

#Fijamos los decimales a 2, para acortar los números
df_Co=round(df_Co.groupby('fecha').mean(),2)
df_No2=round(df_No2.groupby('fecha').mean(),2)
df_O3=round(df_O3.groupby('fecha').mean(),2)
df_So2=round(df_So2.groupby('fecha').mean(),2)
df_Pm10=round(df_Pm10.groupby('fecha').mean(),2)

#Agregamos una columns de categoría para poder unir después todas las tablas
df_Co['Categoría']='CO'
df_No2['Categoría']='No2'
df_O3['Categoría']='O3'
df_So2['Categoría']='So2'
df_Pm10['Categoría']='Pm10'
lista = [df_Co,df_No2,df_O3,df_So2,df_Pm10]
#renombramos las columnas
for i in lista:
  i.columns = ['hora','noreste','suroeste','noroeste','sureste','centro','categoria']

#unimos todos los DataFrames
df_all = pd.concat(lista)
#La ZMVM esta conformada por 5 zonas, las cuales son:
zonas = ['noreste','suroeste','noroeste','sureste','centro']

#Convertimos los datos numéricos agregando su índice correspondiente
for i in zonas:
  df_all.loc[df_all[i] <=50, f'cat_{i}'] = 'Bueno'
  df_all.loc[(df_all[i] >50) & (df_all[i] <=100), f'cat_{i}'] = 'Regular'
  df_all.loc[(df_all[i] >100) & (df_all[i] <=150), f'cat_{i}'] = 'Mala'
  df_all.loc[(df_all[i] >150) & (df_all[i] <=200), f'cat_{i}'] = 'Muy mala'
  df_all.loc[(df_all[i] >200), f'cat_{i}'] = 'Extremadamente mala'

#Seleccionamos solo las columnas con las descripciones de índice para trabajar
df_all_cat = df_all.iloc[:,[6,7,8,9,10,11]]
df_all_cat.columns = ['categoria']+zonas

cross_ce = pd.crosstab(df_all_cat['categoria'],df_all_cat['centro'])
cross_so = pd.crosstab(df_all_cat['categoria'],df_all_cat['suroeste'])
cross_se = pd.crosstab(df_all_cat['categoria'],df_all_cat['sureste'])
cross_no = pd.crosstab(df_all_cat['categoria'],df_all_cat['noroeste'])
cross_ne = pd.crosstab(df_all_cat['categoria'],df_all_cat['noreste'])

zonas_zmvm="https://raw.githubusercontent.com/BettySanchez7/Proyecto_AnalisisDatosConPython/main/map.json"

df_Co_cat = df_all_cat[df_all_cat['categoria']=='CO']
df_No2_cat = df_all_cat[df_all_cat['categoria']=='No2']
df_O3_cat = df_all_cat[df_all_cat['categoria']=='O3']
df_Pm10_cat = df_all_cat[df_all_cat['categoria']=='Pm10']
df_So2_cat = df_all_cat[df_all_cat['categoria']=='So2']

df_Co_redux = pd.DataFrame()
df_No2_redux = pd.DataFrame()
df_O3_redux = pd.DataFrame()
df_Pm10_redux = pd.DataFrame()
df_So2_redux = pd.DataFrame()

for i in zonas:
      df_Co_redux[i] = pd.Series(df_Co_cat[i].value_counts())
for i in zonas:
  df_No2_redux[i] = pd.Series(df_No2_cat[i].value_counts())
for i in zonas:
  df_O3_redux[i] = pd.Series(df_O3_cat[i].value_counts())
for i in zonas:
  df_Pm10_redux[i] = pd.Series(df_Pm10_cat[i].value_counts())
for i in zonas:
  df_So2_redux[i] = pd.Series(df_So2_cat[i].value_counts())

df_Co_redux = df_Co_redux.T
df_No2_redux = df_No2_redux.T
df_O3_redux = df_O3_redux.T
df_Pm10_redux = df_Pm10_redux.T
df_So2_redux = df_So2_redux.T

df_Co_redux.replace(np.nan,0)
df_No2_redux.replace(np.nan,0)
df_O3_redux.replace(np.nan,0)
df_Pm10_redux.replace(np.nan,0)
df_So2_redux.replace(np.nan,0)

df_Co=pd.read_csv(url_1)
df_No2 = pd.read_csv(url_2)
df_O3 = pd.read_csv(url_3)
df_So2 = pd.read_csv(url_4)
df_Pm10 = pd.read_csv(url_5)

df_Pm10.columns=['hora','NE','SO','SE','CE','NO','categoria']
df_Pm10 = pd.DataFrame(df_Pm10.iloc[:,[1,2,3,4,5]].mean(),columns=['Promedio'])
df_Pm10 = df_Pm10.reset_index()

df_No2.columns=['hora','NE','SO','SE','CE','NO','categoria']
df_No2 = pd.DataFrame(df_No2.iloc[:,[1,2,3,4,5]].mean(),columns=['Promedio'])
df_No2 = df_No2.reset_index()

df_O3.columns=['hora','NE','SO','SE','CE','NO','categoria']
df_O3 = pd.DataFrame(df_O3.iloc[:,[1,2,3,4,5]].mean(),columns=['Promedio'])
df_O3 = df_O3.reset_index()

df_So2.columns=['hora','NE','SO','SE','CE','NO','categoria']
df_So2 = pd.DataFrame(df_So2.iloc[:,[1,2,3,4,5]].mean(),columns=['Promedio'])
df_So2 = df_So2.reset_index()

df_Co.columns=['hora','NE','SO','SE','CE','NO','categoria']
df_Co = pd.DataFrame(df_Co.iloc[:,[1,2,3,4,5]].mean(),columns=['Promedio'])
df_Co = df_Co.reset_index()
