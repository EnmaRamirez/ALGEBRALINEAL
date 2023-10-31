#ENCONTRAR LA INVERSA DE UNA MATRIZ
import numpy as np

#Definimos la matriz
Matriz = np.array([[2, -2, 2],
                   [2, 1, 0 ],
                   [3, -2, 2]])

#Calcular la inversa
Matriz_inversa = np.linalg.inv(Matriz)

print("Matriz original")
print(Matriz)
print("\nMatriz inversa:")
print(Matriz_inversa)


