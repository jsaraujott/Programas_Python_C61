import numpy as np 
import pandas as pd
import argparse 

#Creación de un objeto de conexion
parser = argparse.ArgumentParser(description = "Programa en Python que grafica histograma dados sus parametros") #Igual siempre
parser.add_argument("media", help = "Valor promedio del histograma") #Solamente cambia el argumento
parser.add_argument("desv", help = "Error estandar del histograma") #Solamente cambia el argumento
parser.add_argument("--n", default = 100, help = "Tamaño de la muestra a graficar") #Opcion (--)
args = parser.parse_args() #Igual siempre

n = int(args.n) 
media = float(args.media) 
desv = float(args.desv) 

#Generar datos aleatorios con distribucion normal
datos = np.random.normal(size = n, loc = media, scale = desv) 
datos = datos.round(0).astype(int) 

#Eliminar valores atipicos
datos_trim = [] 
for i in range(len(datos)): 
  if datos[i] <= abs(media) + 2*desv or datos[i] >= abs(media) - 2*desv: 
    datos_trim.append(datos[i]) 

datos_trim = pd.DataFrame(datos_trim) 
datos_trim.columns = ['Datos'] 

#Generar un histograma de los datos
histograma = datos_trim.groupby('Datos').size() 

for i in range(len(histograma)): 
  if histograma.index[i]>=0: 
    s = "+" 
  else: 
    s = "" 
  print( 
    s, 
    histograma.index[i], 
    ' '*(1+len(str(np.max([np.max(histograma.index), 
                           abs(np.min(histograma.index))]))) - 
                           len(str(abs(histograma.index[i])))), 
    '*'*round(100*histograma.iloc[i]/len(datos_trim)), 
    sep = "" 
    )