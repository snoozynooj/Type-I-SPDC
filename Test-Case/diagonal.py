# import sympy 
from sympy import * 
import math
#######--- ECIWAO
##########################################
#BIBO
print("BIBO1064")
M = Matrix([[3.9890, 0.0,-0.3181], [0.0, 3.3663, 0.0], [-0.3181, 0.0, 3.6717]])
# Use sympy.diagonalize() method 
P, D = M.diagonalize()        
#print("Diagonal of a matrix : {}".format(D)) 
print(D[0],D[4],D[8])
print("nx=",round(math.sqrt(D[0]),8))
print("ny=",round(math.sqrt(D[4]),8))
print("nz=",round(math.sqrt(D[8]),8))

M = Matrix([[4.2363, 0.0, -0.3535], [0.0, 3.5202, 0.0], [-0.3535, 0.0, 3.8696]])
#Use sympy.diagonalize() method 
P, D = M.diagonalize()       
#print("Diagonal of a matrix : {}".format(D)) 
print(D[0],D[4],D[8])
print("nx=",round(math.sqrt(D[0]),8))
print("ny=",round(math.sqrt(D[4]),8))
print("nz=",round(math.sqrt(D[8]),8))
###########################################
print("BIBO810")
M = Matrix([[4.0434, 0.0,-0.3260], [0.0, 3.4006, 0.0], [-0.3260, 0.0, 3.7153]])
# Use sympy.diagonalize() method 
P, D = M.diagonalize()        
#print("Diagonal of a matrix : {}".format(D)) 
print(D[0],D[4],D[8])
print("nx=",round(math.sqrt(D[0]),8))
print("ny=",round(math.sqrt(D[4]),8))
print("nz=",round(math.sqrt(D[8]),8))

M = Matrix([[4.5522, 0.0, -0.3977], [0.0, 3.7075, 0.0], [-0.3977, 0.0, 4.1200]])
#Use sympy.diagonalize() method 
P, D = M.diagonalize()       
#print("Diagonal of a matrix : {}".format(D)) 
print(D[0],D[4],D[8])
print("nx=",round(math.sqrt(D[0]),8))
print("ny=",round(math.sqrt(D[4]),8))
print("nz=",round(math.sqrt(D[8]),8))
###########################################
