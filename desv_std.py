import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib

ListaEmpleados=pd.read_csv('empleados.csv')
select=ListaEmpleados['TotalAtaque']

media=select.mean()[0]
desvStd=np.std(select)[0]
mediana=np.median(select)[0]
varianza=np.median(select)[0]

print("Media="+str(media))
print("Desviacion std = "+str(desvStd))
print("Mediana="+str(mediana))
print("Varianza="+str(varianza))

sd=select.as_matrix()

#histograma
cuenta, cajas, ignorar = plt.hist(sd,20)
plt.axvline(media,color='b')
plt.axvline(media-desvStd,color='r')
plt.axvline(media+desvStd,color='r')
