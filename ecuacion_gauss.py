#SISTEMA DE ECUACION LINEAL USANDO LA REGLA DE GAUSS JORDAN
import matplotlib.pyplot as plt

import numpy as np

#sistema de ecucaiones definido
A = np.array([[2, 1], [1, -3]])
B = np.array([5, 2])

#Definimos la variable x
X = np.linalg.solve(A, B)

#Graficamos las ecuaciones a resolver.
X_vals = np.linspace(-10, 10, 100)
Y1 = (5 - 2 * X_vals) / 1
Y2 = (X_vals -2) / -3

plt.figure(figsize=(6, 5))
plt.plot(X_vals,Y1, label='2X + y = 5')
plt.plot(X_vals,Y2, label='X - 3y = 2')
plt.xlim(-10, 10)
plt.ylim(-10,10)

#Solucion grafica
plt.scatter(X[0], X[1], color="red", label='solucion (X, Y)')

plt.xlabel('X')
plt.xlabel('Y')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth=0.5)
plt.legend()
plt.title('SISTEMA DE ECUACIONES LINEALES DE GAUSS JORDAN DE 2*2')
plt.show()
print(f"La solución es X = {X[0]}, Y = {X[1]}")