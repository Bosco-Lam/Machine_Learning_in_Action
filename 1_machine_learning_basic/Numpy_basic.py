# !/usr/bin/python3
# -*- coding:utf8 -*-

import numpy as np

# create array
array = np.random.rand(4,4)

# array turn into matrix
randMat = np.mat(array)
print(randMat)

# inverse matrix 
invRandMat = randMat.I
print(invRandMat)

# eye(4) create 4X4 Unit matrix
myEye = randMat * invRandMat
print(myEye)
print(myEye - np.eye(4))
