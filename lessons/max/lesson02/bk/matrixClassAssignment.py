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
