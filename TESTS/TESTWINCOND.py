from scipy.signal import convolve2d
import numpy as np
from Settings import *

horizontal_kernel = np.ones((1,JUEGODE), dtype=int)
vertical_kernel = np.transpose(horizontal_kernel)
diag1_kernel = np.eye(JUEGODE, dtype=np.uint8)
diag2_kernel = np.fliplr(diag1_kernel)
detection_kernels = [horizontal_kernel, vertical_kernel, diag1_kernel, diag2_kernel]


#Busqueda Horizontal
print(horizontal_kernel)
Matrix1 = np.matrix('5 0 0 0 0 0 0;5 0 0 0 0 0 0;5 0 5 5 0 5 0;5 0 0 0 0 0 0;0 5 3 3 3 3 0;0 3 0 0 0 0 0')
print(Matrix1,'\n')

arr1 = np.asanyarray(convolve2d(Matrix1, horizontal_kernel, mode="valid"),'\n')
if num1 in arr1:
    print('hay', JUEGODE, ', 5 juntos de manera Horizontal!')
if num2 in arr1:
    print('hay', JUEGODE, ', 3 juntos de manera Horizontal!')

#Busqueda vertical
print(vertical_kernel)
Matrix2 = np.matrix('5 0 0 0 0 0 0;5 0 0 0 0 0 0;5 0 0 5 5 5 0;5 0 0 0 0 0 0;0 5 5 3 3 3 0;0 3 0 0 0 0 0')
print(Matrix2,'\n')

arr2 = np.asanyarray(convolve2d(Matrix2, vertical_kernel, mode="valid"), '\n')
if num1 in arr2:
    print('hay', JUEGODE, ', 5 juntos de manera vertical!')
if num2 in arr2:
    print('hay', JUEGODE, ', 3 juntos de manera vertical!')
#Busqueda diagonal negativa
print(diag1_kernel)
Matrix3 = np.matrix('0 0 0 0 0 0 0;5 5 0 0 0 0 0;5 0 5 5 5 5 0;5 0 0 5 0 0 0;0 5 5 3 5 3 0;0 3 0 0 0 0 0')
print(Matrix3,'\n')

arr3 = np.asanyarray(convolve2d(Matrix3, diag1_kernel, mode="valid"), '\n')
print(arr3)
if num1 in arr3:
    print('hay', JUEGODE, ', 5 juntos de manera diagonal negativa!')
if num2 in arr3:
    print('hay', JUEGODE, ', 3 juntos de manera diagonal negativa!')

#Busqueda diagonal positiva
print(diag2_kernel)
Matrix4 = np.matrix('0 0 0 5 0 0 0;5 3 5 0 0 0 3;5 5 5 3 3 5 0;5 0 0 3 0 0 0;0 5 3 3 5 3 0;0 3 0 0 0 0 0;3 3 0 0 0 0 0')
print(Matrix4,'\n')

arr4 = np.asanyarray(convolve2d(Matrix4, diag2_kernel, mode="valid"), '\n')
print(arr4)
if num1 in arr4:
    print('hay', JUEGODE, ', 5 juntos de manera diagonal positiva!')
if num2 in arr4:
    print('hay', JUEGODE, ', 3 juntos de manera diagonal positiva!')