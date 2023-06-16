# import sympy 
from sympy import * 
import math
#######--- ECIWAO
print("RATDAS01")
M = Matrix([[2.5853, 0.0, 0.0429], [0.0, 2.3892, 0.0], [0.0429, 0.0, 2.4238]])
# Use sympy.diagonalize() method 
P, D = M.diagonalize()        
#print("Diagonal of a matrix : {}".format(D)) 
print(D[0],D[4],D[8])
print("nx=",round(math.sqrt(D[0]),8))
print("ny=",round(math.sqrt(D[4]),8))
print("nz=",round(math.sqrt(D[8]),8))

M = Matrix([[2.6587, 0.0, 0.0465], [0.0, 2.4489, 0.0], [0.0465, 0.0, 2.4862]])
#Use sympy.diagonalize() method 
P, D = M.diagonalize()       
#print("Diagonal of a matrix : {}".format(D)) 
print(D[0],D[4],D[8])
print("nx=",round(math.sqrt(D[0]),8))
print("ny=",round(math.sqrt(D[4]),8))
print("nz=",round(math.sqrt(D[8]),8))
#######################################
print("TAKRIJ")
M = Matrix([[2.8397, 0.0, 0.0415], [0.0, 2.5087, 0.0], [0.0415, 0.0, 2.6008]])
# Use sympy.diagonalize() method
P, D = M.diagonalize()
#print("Diagonal of a matrix : {}".format(D))
print(D[0],D[4],D[8])
print("nx=",round(math.sqrt(D[0]),8))
print("ny=",round(math.sqrt(D[4]),8))
print("nz=",round(math.sqrt(D[8]),8))

M = Matrix([[2.9234, 0.0, 0.0470], [0.0, 2.5661, 0.0], [0.0470, 0.0, 2.6615]])
#Use sympy.diagonalize() method
P, D = M.diagonalize()
#print("Diagonal of a matrix : {}".format(D))
print(D[0],D[4],D[8])
print("nx=",round(math.sqrt(D[0]),8))
print("ny=",round(math.sqrt(D[4]),8))
print("nz=",round(math.sqrt(D[8]),8))
#######################################
print("LASPZN")
M = Matrix([[2.6665, 0.0, -0.0971], [0.0, 2.5286, 0.0], [-0.0971, 0.0, 2.8723]])
# Use sympy.diagonalize() method
P, D = M.diagonalize()
#print("Diagonal of a matrix : {}".format(D))
print(D[0],D[4],D[8])
print("nx=",round(math.sqrt(D[0]),8))
print("ny=",round(math.sqrt(D[4]),8))
print("nz=",round(math.sqrt(D[8]),8))

M = Matrix([[2.7427, 0.0, -0.1068], [0.0, 2.5888, 0.0], [-0.1068, 0.0, 2.9583]])
#Use sympy.diagonalize() method
P, D = M.diagonalize()
#print("Diagonal of a matrix : {}".format(D))
print(D[0],D[4],D[8])
print("nx=",round(math.sqrt(D[0]),8))
print("ny=",round(math.sqrt(D[4]),8))
print("nz=",round(math.sqrt(D[8]),8))
#######################################
print("OFUWIV")
M = Matrix([[2.8132, 0.0, 0.2049], [0.0, 2.5176, 0.0], [0.2049, 0.0, 2.5746]])
# Use sympy.diagonalize() method
P, D = M.diagonalize()
#print("Diagonal of a matrix : {}".format(D))
print(D[0],D[4],D[8])
print("nx=",round(math.sqrt(D[0]),8))
print("ny=",round(math.sqrt(D[4]),8))
print("nz=",round(math.sqrt(D[8]),8))

M = Matrix([[2.8985, 0.0, 0.2173], [0.0, 2.5807, 0.0], [0.2173, 0.0, 2.6371]])
#Use sympy.diagonalize() method
P, D = M.diagonalize()
#print("Diagonal of a matrix : {}".format(D))
print(D[0],D[4],D[8])
print("nx=",round(math.sqrt(D[0]),8))
print("ny=",round(math.sqrt(D[4]),8))
print("nz=",round(math.sqrt(D[8]),8))
#######################################
print("FIRZIP")
M = Matrix([[2.8547, 0.0, -0.0275], [0.0, 2.7254, 0.0], [-0.0275, 0.0, 2.8071]])
# Use sympy.diagonalize() method
P, D = M.diagonalize()
#print("Diagonal of a matrix : {}".format(D))
print(D[0],D[4],D[8])
print("nx=",round(math.sqrt(D[0]),8))
print("ny=",round(math.sqrt(D[4]),8))
print("nz=",round(math.sqrt(D[8]),8))

M = Matrix([[2.9958, 0.0, -0.0345], [0.0, 2.8391, 0.0], [-0.0345, 0.0, 2.9418]])
#Use sympy.diagonalize() method
P, D = M.diagonalize()
#print("Diagonal of a matrix : {}".format(D))
print(D[0],D[4],D[8])
print("nx=",round(math.sqrt(D[0]),8))
print("ny=",round(math.sqrt(D[4]),8))
print("nz=",round(math.sqrt(D[8]),8))
#######################################
print("FIPWUY")
M = Matrix([[2.0981, 0.0, -0.0329], [0.0, 2.3724, 0.0], [-0.0329, 0.0, 2.4463]])
# Use sympy.diagonalize() method
P, D = M.diagonalize()
#print("Diagonal of a matrix : {}".format(D))
print(D[0],D[4],D[8])
print("nx=",round(math.sqrt(D[0]),8))
print("ny=",round(math.sqrt(D[4]),8))
print("nz=",round(math.sqrt(D[8]),8))

M = Matrix([[2.1494, 0.0, -0.0401], [0.0, 2.4358, 0.0], [-0.0401, 0.0, 2.5343]])
#Use sympy.diagonalize() method
P, D = M.diagonalize()
#print("Diagonal of a matrix : {}".format(D))
print(D[0],D[4],D[8])
print("nx=",round(math.sqrt(D[0]),8))
print("ny=",round(math.sqrt(D[4]),8))
print("nz=",round(math.sqrt(D[8]),8))
#######################################
print("PODREH")
M = Matrix([[3.4362, 0.0, 0.4005], [0.0, 3.5672, 0.0], [0.4005, 0.0, 2.8468]])
# Use sympy.diagonalize() method
P, D = M.diagonalize()
#print("Diagonal of a matrix : {}".format(D))
print(D[0],D[4],D[8])
print("nx=",round(math.sqrt(D[0]),8))
print("ny=",round(math.sqrt(D[4]),8))
print("nz=",round(math.sqrt(D[8]),8))

M = Matrix([[3.7448, 0.0, 0.5146], [0.0, 3.8596, 0.0], [0.5146, 0.0, 3.0234]])
#Use sympy.diagonalize() method
P, D = M.diagonalize()
#print("Diagonal of a matrix : {}".format(D))
print(D[0],D[4],D[8])
print("nx=",round(math.sqrt(D[0]),8))
print("ny=",round(math.sqrt(D[4]),8))
print("nz=",round(math.sqrt(D[8]),8))
#######################################
print("RUVBAN")
M = Matrix([[2.3705, 0.0, -0.3149], [0.0, 3.3561, 0.0], [-0.3149, 0.0, 3.2545]])
# Use sympy.diagonalize() method
P, D = M.diagonalize()
#print("Diagonal of a matrix : {}".format(D))
print(D[0],D[4],D[8])
print("nx=",round(math.sqrt(D[0]),8))
print("ny=",round(math.sqrt(D[4]),8))
print("nz=",round(math.sqrt(D[8]),8))

M = Matrix([[2.4574, 0.0, -0.3627], [0.0, 3.6360, 0.0], [-0.3627, 0.0, 3.5002]])
#Use sympy.diagonalize() method
P, D = M.diagonalize()
#print("Diagonal of a matrix : {}".format(D))
print(D[0],D[4],D[8])
print("nx=",round(math.sqrt(D[0]),8))
print("ny=",round(math.sqrt(D[4]),8))
print("nz=",round(math.sqrt(D[8]),8))
#######################################
print("MUYGOE")
M = Matrix([[2.6561, 0.0, -0.0406], [0.0, 2.8360, 0.0], [-0.0406, 0.0, 2.9551]])
# Use sympy.diagonalize() method
P, D = M.diagonalize()
#print("Diagonal of a matrix : {}".format(D))
print(D[0],D[4],D[8])
print("nx=",round(math.sqrt(D[0]),8))
print("ny=",round(math.sqrt(D[4]),8))
print("nz=",round(math.sqrt(D[8]),8))

M = Matrix([[2.7499, 0.0, -0.0539], [0.0, 2.9416, 0.0], [-0.0539, 0.0, 3.0800]])
#Use sympy.diagonalize() method
P, D = M.diagonalize()
#print("Diagonal of a matrix : {}".format(D))
print(D[0],D[4],D[8])
print("nx=",round(math.sqrt(D[0]),8))
print("ny=",round(math.sqrt(D[4]),8))
print("nz=",round(math.sqrt(D[8]),8))
#######################################
print("NELWUY")
M = Matrix([[2.3971, 0.0, -0.0076], [0.0, 2.3501, 0.0], [-0.0076, 0.0, 2.2818]])
# Use sympy.diagonalize() method
P, D = M.diagonalize()
#print("Diagonal of a matrix : {}".format(D))
print(D[0],D[4],D[8])
print("nx=",round(math.sqrt(D[0]),8))
print("ny=",round(math.sqrt(D[4]),8))
print("nz=",round(math.sqrt(D[8]),8))

M = Matrix([[2.4514, 0.0, -0.0078], [0.0, 2.4147, 0.0], [-0.0078, 0.0, 2.3323]])
#Use sympy.diagonalize() method
P, D = M.diagonalize()
#print("Diagonal of a matrix : {}".format(D))
print(D[0],D[4],D[8])
print("nx=",round(math.sqrt(D[0]),8))
print("ny=",round(math.sqrt(D[4]),8))
print("nz=",round(math.sqrt(D[8]),8))
