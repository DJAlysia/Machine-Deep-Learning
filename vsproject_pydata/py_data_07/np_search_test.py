import numpy as np

py_2d = [
    [1,0,1,0],
    [0,1,0,1],
    [1,0,1,0],
    [0,1,0,1]
]
# print(py_2d)
np_arr2 = np.array(py_2d)
print('red:', np_arr2[:,3])
print('orange:', np_arr2[2,0:3])
print('yellow:', np_arr2[0:2,1])
print('green:', np_arr2[3,2])
