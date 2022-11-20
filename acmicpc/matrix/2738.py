import numpy as np

def sum_matrix(A, B):
    A = np.array(A)
    B = np.array(B)
    return (A + B).tolist()

if __name__ == '__main__':
    x, y = map(int, input().split())
    arr1 = []
    arr2 = []

    for row in range(x):
        column = list(map(int, input().split()))
        arr1.append(column)

    for row in range(x):
        column = list(map(int, input().split()))
        arr2.append(column)

    sum = sum_matrix(arr1, arr2)

    for arr in sum:
        print(' '.join(map(str, arr)))
