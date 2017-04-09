# Matrix Algebra

import numpy

A = numpy.array([[1,2,3],[2,7,4]])
transposeA = [list(i) for i in zip(*A)]
B = numpy.array([[1,-1],[0,1]])
C = numpy.array([[5,-1],[9,1],[6,0]])
transposeC = [list(i) for i in zip(*C)]
D = numpy.array([[3,-2,-1],[1,2,3]])
u = numpy.array([[6,2,-3,5]])
v = numpy.array([[3,5,-1,4]])
w = numpy.array([[1],[8],[0],[5]])

#question 1

print(A.shape) #(2, 3)
print(B.shape) #(2, 2)
print(C.shape) #(3, 2)
print(D.shape) #(2, 3)
print(u.shape) #(1, 4)
print(w.shape) #(4, 1)

#question 2

print(u+v) #[[ 9  7 -4  9]]
print(u-v) #[[ 3 -3 -2  1]]
print((6*u)) #[[ 36  12 -18  30]]
print(u*v) #[[18 10  3 20]]
print(numpy.linalg.norm(u)) #8.60232526704

#question 3

#print(A+C) not defined
print(A-transposeC) #[[-4 -7 -3]
 					#[ 3  6  4]]
print(transposeC+(3*D)) #[[14  3  3]
						#[ 2  7  9]]
print(numpy.dot(B, A)) #[[-1 -5 -1]
						#[ 2  7  4]]

#not defined