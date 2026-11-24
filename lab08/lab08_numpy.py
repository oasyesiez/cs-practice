import numpy as np
# 1
hours = np.arange(0, 22, 3)
line = np.linspace(0, 1, 5)
zeros = np.zeros(6 , dtype=np.int64)
unknown_table = np.full((2,3), -1)
identity = np.ones((3,3), dtype=np.int64)
print(hours, hours.shape, hours.ndim, hours.size, hours.dtype)

# 2
print(hours[2])
print(hours[-1])
print(hours[2:6])
print(hours[::2])
print(hours[::-1])

# 3
temperatures = np.array([
    [12, 14, 13, 15],
    [11, 13, 16, 17],
    [10, 12, 15, 18],
])
print(temperatures.shape)
print(temperatures.ndim)
print(temperatures.size)
print(temperatures[1,2])
print(temperatures[0])
print(temperatures[:,-1])
print(temperatures[:2,1:])
print(temperatures[0:2,1:3])

# 4
matrix = np.arange(1, 26).reshape(5, 5)
print(matrix[:3,:],matrix[:3,:].shape )
print(matrix[-2:,:], matrix[-2:,:].shape )
print(matrix[:,:2], matrix[:,:2].shape)
print(matrix[1:4,2:5], matrix[1:4,2:5].shape)
print(matrix[3:5, 3:5], matrix[3:5, 3:5].shape)

# 5

changed_hours = hours.copy() # .copy() создает копию массива, чтобы изменения не повлияли на исходный массив
changed_hours[2:5] = 99
changed_hours[::2] = -1
print(changed_hours, hours)

changed_matrix = matrix.copy()
changed_matrix[1,:] = 0
changed_matrix[:,-1] = -1
changed_matrix[1:4, 1:4] = 100
print(changed_matrix, matrix)

# 6
numbers = np.arange(12)
table = numbers.reshape(3,4) # для таблицы 5x3 нужно 15 элементов, а у нас 12, поэтому reshape не сработает
transposed = table.T
print(numbers.shape)
print(table.shape)
print(transposed.shape)
