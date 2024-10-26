import numpy as np
import time

def counting_sort(A, B, k):
    C = np.zeros(k+1, dtype=int)

    for j in range(0, A.shape[0]):
        C[A[j]] += 1

    for i in range(1, k+1):
        C[i] = C[i] + C[i -1]

    for j in reversed(range(0,A.shape[0])):
        C[A[j]] -= 1
        B[C[A[j]]] = A[j]






if __name__=='__main__':
    k = 1000000 #max value
    size = 10000 # vector size
    A = np.random.randint(0, k, size)
    B = np.zeros_like(A)
    start = time.time()
    counting_sort(A,B,k)
    end = time.time()
    print(f'Running time for vector sorting: {end - start}')


