import matplotlib.pyplot as plt
hombres = [14,25,12,56,34]
mujeres = [22,42,21,63,99]
edades = [0,10,20,30,40,50,60,70,80,90,100]
plt.hist(hombres, edades, histtype='bar', rwidth=0.8,
color='b', label='hombres')
plt.hist(mujeres, edades, histtype='bar', rwidth=0.4,
color='r', label='mujeres')
plt.xlabel('Eje X: Edades')
plt.ylabel('Eje Y: Población')
plt.title('Histograma')
plt.legend()
plt.show()
