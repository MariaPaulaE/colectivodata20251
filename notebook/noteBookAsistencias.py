import pandas as pd

#Leyendo los datos de asistencias
asistenciaDataFrame = pd.read_csv("./data/asistencia_estudiantes_completo.csv")
#print(asistenciaDataFrame)

#Obteniendo informacion basica del dataframe
#print(asistenciaDataFrame.info()) #informacion de todos los dato

#print(asistenciaDataFrame.tail()) #muestra los ultimos 5 registros de la tabla

#print(asistenciaDataFrame.tail(20)) #mustrra los ultimos (N) registros

#print(asistenciaDataFrame.head(20)) # los primeros (N) regitros

#print(asistenciaDataFrame.describe()) #analisis descriptivos de los datos numericos

#print(asistenciaDataFrame.isnull().sum())##verifica cuantos datos estan vacios

#print(asistenciaDataFrame['estado'].value_counts())#selecciono columnas por separado //.value_counts para contar los valores

print(asistenciaDataFrame['estrato'].value_counts().head())
