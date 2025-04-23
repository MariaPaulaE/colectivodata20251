import pandas as pd

#Leyendo datos de ususarios
usuariosDataFrame = pd.read_excel("./data/usuarios_sistema_completo.xlsx")
#print(usuariosDataFrame)

print(usuariosDataFrame.isnull().sum())#verifica cuantos datos estan vacios

