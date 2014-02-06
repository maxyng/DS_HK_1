#!/usr/bin/python
# Import required libraries
from __future__ import division
import sys

def MatrixMult(matrix1, matrix2):
	row=[0]
	resultMatrix = [ row * len(matrix1[0]) for cols in range(len(matrix2)) ]
	#print resultMatrix
	if len(matrix1[0]) != len(matrix2):
		print "cannot multiply the two matrices. Incorrect dimensions."
		return
	"""
	Looping through the resulting matrix and adding the multiplied pairs from matrix1 and matrix2
	"""
	for i in range(len(matrix1)):
		for j in range(len(matrix2[0])):
			for k in range(len(matrix1[0])):
				#print matrix1[i][k] * matrix2[k][j]
				resultMatrix[i][j] += matrix1[i][k] * matrix2[k][j]
			#resultMatrix.append(row)
	return resultMatrix

def VectorMatrix(vector, matrix):
	result = [0] * len(matrix[0])
	for i in range(len(vector)):
		for j in range(len(matrix)):
			result[i] += vector[i] * matrix[i][j]
	return result

def isIdentityMatrix(matrix):
	numRows = len(matrix[0])
	numCols = len(matrix)
	if numRows != numCols:
		return False

	for i in range(numRows):
		for j in range(numCols):
			if i != j and matrix[i][j] != 0:
				return False
			if i == j and matrix[i][j] != 1:
				return False
	return True


test1 = [ [1, 2, 3, 4],[1, 2, 3, 4],[1, 2, 3, 4],[1, 2, 3, 4] ]
test2 = [ [1, 0, 0, 0],[0, 1, 0, 0],[0, 0, 1, 0],[0, 0, 0, 1] ]
print MatrixMult(test1,test2)

test3 = [1,2,3,4]
print VectorMatrix(test3,test1)

print isIdentityMatrix(test1)
print isIdentityMatrix(test2)

"""
 Adding numpy library from lesson 3 to compare speed with original implementation
also test matrix multiply test
"""
from numpy import array, matrix,dot,eye

a1 = array([ [1, 2], [3, 4] ])
a2 = array([ [1, 3], [2, 4] ])
m1 = matrix('1 2; 3 4')
m2 = matrix('1 3; 2 4')
a1 * a2
m1 * m2

print 'isIdentityMatrix with eye(5): '+ str(isIdentityMatrix(eye(5)))
print 'isIdentityMatrix with eye(6): '+ str(isIdentityMatrix(eye(6)))

import timeit as t
print
print 'Time to run numpy.dot on a1 and a2'
print t.timeit('dot(a1, a2)', setup="from __main__ import dot, a1, a2", number = 100000)
print 'Time to run my python implementation on a1 and a2'
print t.timeit('MatrixMult(a1,a2)',setup="from __main__ import MatrixMult, a1, a2",number = 100000)