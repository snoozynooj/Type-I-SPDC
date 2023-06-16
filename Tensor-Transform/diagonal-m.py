# import sympy 
from sympy import * 
import math
#######--- ECIWAO
print("ECIWAO")
M = Matrix([[2.6598, 0.0, -0.3772], [0.0, 3.0728, 0.0], [-0.3772, 0.0, 3.7490]])
# Use sympy.diagonalize() method 
P, D = M.diagonalize()        
#print("Diagonal of a matrix : {}".format(D)) 
print(D[0],D[4],D[8])
print("nx=",round(math.sqrt(D[0]),8))
print("ny=",round(math.sqrt(D[4]),8))
print("nz=",round(math.sqrt(D[8]),8))

M = Matrix([[3.0198, 0.0, -0.5161], [0.0, 3.3777, 0.0], [-0.5161, 0.0, 4.5205]])
#Use sympy.diagonalize() method 
P, D = M.diagonalize()       
#print("Diagonal of a matrix : {}".format(D)) 
print(D[0],D[4],D[8])
print("nx=",round(math.sqrt(D[0]),8))
print("ny=",round(math.sqrt(D[4]),8))
print("nz=",round(math.sqrt(D[8]),8))
#########################################
#AQOROP
print("AQOROP")
M = Matrix([[3.0387, 0.0, -0.6331], [0.0, 4.6711, 0.0], [-0.6331, 0.0, 2.8282]])
# Use sympy.diagonalize() method 
P, D = M.diagonalize()        
#print("Diagonal of a matrix : {}".format(D)) 
print(D[0],D[4],D[8])
print("nx=",round(math.sqrt(D[0]),8))
print("ny=",round(math.sqrt(D[4]),8))
print("nz=",round(math.sqrt(D[8]),8))

M = Matrix([[3.4089, 0.0, -0.8290], [0.0, 5.7395, 0.0], [-0.8290, 0.0, 3.0897]])
#Use sympy.diagonalize() method 
P, D = M.diagonalize()       
#print("Diagonal of a matrix : {}".format(D)) 
print(D[0],D[4],D[8])
print("nx=",round(math.sqrt(D[0]),8))
print("ny=",round(math.sqrt(D[4]),8))
print("nz=",round(math.sqrt(D[8]),8))
##########################################
#BIBO
print("BIBO")
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
print("KOMMII")
M = Matrix([[2.4800, 0.0,0.0773], [0.0, 2.4035, 0.0], [0.0773, 0.0, 2.4847]])
# Use sympy.diagonalize() method
P, D = M.diagonalize()
#print("Diagonal of a matrix : {}".format(D))
print(D[0],D[4],D[8])
print("nx=",round(math.sqrt(D[0]),8))
print("ny=",round(math.sqrt(D[4]),8))
print("nz=",round(math.sqrt(D[8]),8))

M = Matrix([[2.5297, 0.0, 0.0798], [0.0, 2.4548, 0.0], [0.0798, 0.0, 2.5392]])
#Use sympy.diagonalize() method
P, D = M.diagonalize()
#print("Diagonal of a matrix : {}".format(D))
print(D[0],D[4],D[8])
print("nx=",round(math.sqrt(D[0]),8))
print("ny=",round(math.sqrt(D[4]),8))
print("nz=",round(math.sqrt(D[8]),8))
############################################
print("SEYVIC")
M = Matrix([[2.8401, 0.0,0.1656], [0.0, 2.5400, 0.0], [0.1656, 0.0, 2.5009]])
# Use sympy.diagonalize() method
P, D = M.diagonalize()
#print("Diagonal of a matrix : {}".format(D))
print(D[0],D[4],D[8])
print("nx=",round(math.sqrt(D[0]),8))
print("ny=",round(math.sqrt(D[4]),8))
print("nz=",round(math.sqrt(D[8]),8))

M = Matrix([[2.9434, 0.0, 0.1808], [0.0, 2.6161, 0.0], [0.1808, 0.0, 2.5770]])
#Use sympy.diagonalize() method
P, D = M.diagonalize()
#print("Diagonal of a matrix : {}".format(D))
print(D[0],D[4],D[8])
print("nx=",round(math.sqrt(D[0]),8))
print("ny=",round(math.sqrt(D[4]),8))
print("nz=",round(math.sqrt(D[8]),8))
#############################################
print("MOFTIL")
M = Matrix([[3.0535, 0.0,-0.6369], [0.0, 3.7737, 0.0], [-0.6369, 0.0, 2.8552]])
# Use sympy.diagonalize() method
P, D = M.diagonalize()
#print("Diagonal of a matrix : {}".format(D))
print(D[0],D[4],D[8])
print("nx=",round(math.sqrt(D[0]),8))
print("ny=",round(math.sqrt(D[4]),8))
print("nz=",round(math.sqrt(D[8]),8))

M = Matrix([[3.2963, 0.0, -0.7727], [0.0, 4.1830, 0.0], [-0.7727, 0.0, 3.0192]])
#Use sympy.diagonalize() method
P, D = M.diagonalize()
#print("Diagonal of a matrix : {}".format(D))
print(D[0],D[4],D[8])
print("nx=",round(math.sqrt(D[0]),8))
print("ny=",round(math.sqrt(D[4]),8))
print("nz=",round(math.sqrt(D[8]),8))
###################################
print("IDOGIR")
M = Matrix([[2.5729, 0.0,0.1133], [0.0, 2.6581, 0.0], [0.1133, 0.0, 2.4567]])
# Use sympy.diagonalize() method
P, D = M.diagonalize()
#print("Diagonal of a matrix : {}".format(D))
print(D[0],D[4],D[8])
print("nx=",round(math.sqrt(D[0]),8))
print("ny=",round(math.sqrt(D[4]),8))
print("nz=",round(math.sqrt(D[8]),8))

M = Matrix([[2.6350, 0.0, 0.1214], [0.0, 2.7303, 0.0], [0.1214, 0.0, 2.5084]])
#Use sympy.diagonalize() method
P, D = M.diagonalize()
#print("Diagonal of a matrix : {}".format(D))
print(D[0],D[4],D[8])
print("nx=",round(math.sqrt(D[0]),8))
print("ny=",round(math.sqrt(D[4]),8))
print("nz=",round(math.sqrt(D[8]),8))
########################################
print("RUBDOI")
M = Matrix([[2.7559, 0.0,0.1130], [0.0, 3.0667, 0.0], [0.1130, 0.0, 2.6209]])
# Use sympy.diagonalize() method
P, D = M.diagonalize()
#print("Diagonal of a matrix : {}".format(D))
print(D[0],D[4],D[8])
print("nx=",round(math.sqrt(D[0]),8))
print("ny=",round(math.sqrt(D[4]),8))
print("nz=",round(math.sqrt(D[8]),8))

M = Matrix([[2.8916, 0.0, 0.1283], [0.0, 3.2394, 0.0], [0.1283, 0.0, 2.7308]])
#Use sympy.diagonalize() method
P, D = M.diagonalize()
#print("Diagonal of a matrix : {}".format(D))
print(D[0],D[4],D[8])
print("nx=",round(math.sqrt(D[0]),8))
print("ny=",round(math.sqrt(D[4]),8))
print("nz=",round(math.sqrt(D[8]),8))
