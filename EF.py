import numpy as np
import numpy.linalg as la

# Datos iniciales
k1 = 1000.0
k2 = 2000.0
k3 = 3000.0
P = 5000.0

# Matrices por elemento
K1 = np.array([[k1,-k1],[-k1,k1]])
K2 = np.array([[k2,-k2],[-k2,k2]])
K3 = np.array([[k3,-k3],[-k3,k3]])

# Matriz global 
K = np.array([[  K1[0,0],        0,           K1[0,1],                0],
               [      0 ,  K3[0,0],                 0,          K3[0,1]],
               [ K1[1,0],        0,   K1[1,1]+K2[0,0],          K2[0,1]],
               [       0,  K3[1,0],           K2[1,0],  K2[1,1]+K3[1,1]]])

F = np.array([0, 0, 0, P])

# Condiciones de frontera
# Nodos 1 y 2 conocidos -> UX = 0
KS = K[2:,2:]
FS = F[2:]

# Resolviendo
USOL = la.solve(KS, FS)

# Vector de desplazamientos
USOL = np.concatenate(([0,0],USOL))

# Obteniendo las fuerzas nodales
NF = np.dot(K,USOL)

# Presentando los resultados
for nodo in range(4):
    print("%g  UX = %-8.4f    FX = %-8.4f"%(nodo+1, USOL[nodo], NF[nodo]))