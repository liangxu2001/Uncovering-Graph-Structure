import scipy.io
import matplotlib.pyplot as plt
from scipy.linalg import svd
import numpy as np
from numpy.linalg import eig


mat = scipy.io.loadmat('graphs.mat')


graphA = mat['A']
graphB = mat['B']
graphC = mat['C']


def displayMatrix(matrix):
    w,v = eig(matrix)

    eigenvalueList = list(enumerate(w))
    sortEigenvalueList = sorted(eigenvalueList, key=lambda x: x[1])

    secondLargestEigenvalue = sortEigenvalueList[-2]
    eigenvector = v[secondLargestEigenvalue[0]]

    randomPerm = np.random.randint(2, size=(200, 200))

    pv = np.matmul(randomPerm, eigenvector.T)

    
    tuplelist = list(enumerate(pv))
    sort = sorted(tuplelist, key=lambda x: x[1])


    index_list = [i[0] for i in sort]

    output = randomPerm[:, index_list]
    output = output[index_list, :]

    orderedA = np.matmul(np.matmul(output.T, matrix), output)

    print(index_list)

        

        
    
    plt.imshow(orderedA, cmap='Blues')
    plt.show()


displayMatrix(graphA)
displayMatrix(graphB)
displayMatrix(graphC)
