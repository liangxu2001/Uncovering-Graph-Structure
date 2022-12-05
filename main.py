import scipy.io
import matplotlib.pyplot as plt
from numpy.linalg import eig

mat = scipy.io.loadmat('graphs.mat')

graphA = mat['A']
graphB = mat['B']
graphC = mat['C']


def displayMatrix(matrix):
    #Grab all the eigenvectors
    vals, vects = eig(matrix)

    #Find the second largest eigenvalue
    eigenvalueList = list(enumerate(vals))
    sortEigenvalueList = sorted(eigenvalueList, key=lambda x: x[1])
    eigVal = sortEigenvalueList[-2][1] 

    #Find second largest eigenvalue's eigenvector
    maxcol = list(vals).index(eigVal)
    eigenVect = vects[:,maxcol]

    #Sorted the Eigenvector values from largest to smallest
    tuplelist = list(enumerate(eigenVect))
    sort = sorted(tuplelist, key=lambda x: x[1])
    index_list = [i[0] for i in sort]

    #Re order the matrix according to new ordering
    output = matrix[:, index_list]
    output = output[index_list, :]

    #Plot Matrix
    plt.imshow(output, cmap='Blues')
    plt.show()

displayMatrix(graphA)
displayMatrix(graphB)
displayMatrix(graphC)
