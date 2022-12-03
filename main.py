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

    
    tuplelist = list(enumerate(eigenvector))
    sort = sorted(tuplelist, key=lambda x: x[1])

    index_list = [i[0] for i in sort]
    print(w)

    output = matrix[:, index_list]
    output = output[index_list, :]


        

        
    
    
    plt.imshow(randomPerm, cmap='Blues')
    plt.show()



displayMatrix(graphC)
