# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 15:02:08 2023

@author: 86319
"""
import numpy as np

A = np.array([[2, 3], [3, -5], [1, 2], [4, 2]])
b = np.array([11, 3, 6, 14])

A_transpose = np.transpose(A)
x = np.linalg.inv(A_transpose @ A) @ A_transpose @ b

print("近似解为:", x)
