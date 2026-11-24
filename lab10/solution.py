import numpy as np

def make_table(rows, columns):
    table = np.arange(rows * columns).reshape(rows, columns)
    return table.tolist()

def rectangle(matrix, row_start, row_end, column_start, column_stop):
    sub_matrix = np.array(matrix)[row_start:row_end, column_start:column_stop]
    return sub_matrix.tolist()

def replace_rectangle(matrix, row_start, row_end, column_start, column_stop, value):
    modified_matrix = np.array(matrix, copy=True)
    modified_matrix[row_start:row_end, column_start:column_stop] = value
    return modified_matrix.tolist()

def matrix_vector_product(matrix, vector):
    product = np.array(matrix) @ np.array(vector)
    return product.tolist()

def matrix_multiply(left, right):
    product = np.array(left) @ np.array(right)
    return product.tolist()

def transpose_matrix(matrix):
    transposed = np.array(matrix).T
    return transposed.tolist()

def solve_system(matrix, vector):
    solution = np.linalg.solve(np.array(matrix), np.array(vector))
    return solution.tolist()

def tensor_channel_mean(tensor):
    mean_values = np.mean(np.array(tensor), axis=-1)
    return mean_values.tolist()

def point_distance(first, second):
    distance = np.linalg.norm(np.array(first) - np.array(second))
    return distance

