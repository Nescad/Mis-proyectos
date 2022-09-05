import matplotlib.pyplot as plt
plt.style.use('seaborn-white')
import numpy as np

#Función utilizada
def funcion(x,y,z):
    return 2*x**3*y**2 + 3*x**2*y**3 - 10*y**2*z**4 + 2

#Gradiente de la función
def Grad(x,y,z):
    g1 = 6*x**2*y**2 + 6*x*y**3
    g2 = 9*x**2*y**2 + 4*x**3*y - 20*y*z**4
    g3 = -40*y**2*z**3
    return np.array([g1,g2,g3])

#Matriz Hessiana

def Hessian(x,y,z):
    h11 = 12*x*y**2 + 6*y**3
    h12 = 12*x**2*y + 18*x*y**2
    h13 = 0
    h21 = 12*x**2*y + 18*x*y**2
    h22 = 18*x**2*y + 4*x**3 - 20*z**4
    h23 = -80*y*z**3
    h31 = 0
    h32 = -80*y*z**3
    h33 = -120*y**2*z**2
    return np.array([[h11,h12,h13],[h21,h22,h23],[h31,h32,h33]])

def Newton_Raphson_Optimize(Grad, Hess, x,y,z, epsilon=0.0001, nMax = 100):
    #Inicialización
    i = 0
    iter_x, iter_y, iter_z, iter_count = np.empty(0),np.empty(0), np.empty(0), np.empty(0)
    error = 10
    X = np.array([x,y,z])
    
    #Se realizan las iteraciones hasta que el error sea mas grande que epsilon
    while np.linalg.norm(error) > epsilon and i < nMax:
        i +=1
        iter_x = np.append(iter_x,x)
        iter_y = np.append(iter_y,y)
        iter_z = np.append(iter_z,z)
        iter_count = np.append(iter_count ,i)   
        print(X) 
        
        X_prev = X
        X = X - np.linalg.inv(Hess(x,y,z)) @ Grad(x,y,z)
        error = X - X_prev
        x,y,z = X[0], X[1], X[2]
          
    return X, iter_x,iter_y, iter_z, iter_count

from scipy.optimize import minimize, rosen, rosen_der, rosen_hess
x0 = [-2,4,-2]
res = minimize(rosen, x0, method='trust-exact', jac=rosen_der, hess = rosen_hess, tol = 0.0001, callback = print)