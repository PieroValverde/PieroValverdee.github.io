import matplotlib.pyplot as plt
x1=[2,4,6,8,10]
y1=[3,5,1,7,4]
x2=[1,3,5,7,9]
y2=[1,3,2,4,9]
plt.bar(x1, y1, label="barra 1" , color="g")
plt.bar(x2, y2, label="barra 2" , color="r")
plt.xlabel("eje x")
plt.ylabel("eje y")
plt.title("grafico de barras")
plt.legend()
plt.show()