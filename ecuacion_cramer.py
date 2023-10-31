#SISTEMA DE ECUACION LINEAL USANDO LA REGLA DE GRAMER
import matplotlib.pyplot as plt

import numpy as np

#sistema de ecucaiones definido
A = np.array([[2, 1, 1],
              [3, -2, -3],
              [8, 2, 5]])


B = np.array([6, 5, 11])


#Funcion con regla de cramer
def cramer_rule(A, B):
    det_A = np.linalg.det(A)
    X = []

    for i in range(A.shape[1]):
        A_temp = A.copy()
        A_temp[:, i] = B
        det_A_temp = np.linalg.det(A_temp)
        X.append(det_A_temp / det_A)
        
    return X
#aca se resuelve el sistema
solution = cramer_rule(A, B)

for i, sol  in enumerate(solution):
    print(f'x{i+1} = {sol}')

#funcion de grafica
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.quiver(0, 0, 0, solution[0], solution[1], solution[2], color='m')
ax.set_xlim(0, solution[0])
ax.set_ylim(0, solution[1])
ax.set_zlim(0, solution[2])


ax.set_xlabel('Eje X')
ax.set_ylabel('Eje Y')
ax.set_zlabel('Eje Z')
plt.title('SISTEMA DE ECUACIONES LINEALES CON LA REGLA DE GRAMER')

plt.show()




