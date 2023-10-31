#mULTIPLICASION DE MATRIZ
def multiplicacion_matrices(matriz1, matriz2):
    if len(matriz1[0])!= len(matriz2):
        return
    
    resultado = [[0 for _ in range(len(matriz2[0]))] for _ in range(len(matriz1))]

    for i in range(len(matriz1)):
        for j in range(len(matriz2[0])):
                       for k in range(len(matriz2)):
                           resultado[i][j] += matriz1[i][k]* matriz2[k][j]

    return resultado

#describimos las matrices
matriz1 = ([[1, 6],
           [0, 4],
           [-2, 3]])


matriz2 = ([[7, 1, 4],
           [2, -3, 5]])
      


resultado = multiplicacion_matrices(matriz1, matriz2)

print("Matrices originales")
print(matriz1, matriz2)

print("La multiplicacion de matrices es: \n")
for row in resultado:
     
      print(row)
      

    