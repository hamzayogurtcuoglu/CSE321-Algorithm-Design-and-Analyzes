
def recursiveExhaustiveSearchAlgorithm(A,rightSide,index,subarr):

    optimalSubArray ,optimalSubArray2= [] , []

    if index == len(A):
        if len(subarr) != 0:
            return subarr
    else:
        optimalSubArray = recursiveExhaustiveSearchAlgorithm(A,rightSide ,index + 1, subarr)
        optimalSubArray2 = recursiveExhaustiveSearchAlgorithm(A,rightSide, index + 1, subarr + [A[index]])
    return findOptimal(optimalSubArray,optimalSubArray2,rightSide)


def findOptimal(optimalSubArray,optimalSubArray2,rightSide):
    if len(optimalSubArray) == 0 and len(optimalSubArray2) == 0:
        return []
    elif len(optimalSubArray) != 0 and len(optimalSubArray2) == 0:
        if sumOfArray(optimalSubArray) >= rightSide:
            return optimalSubArray
        else:
            return []
    elif len(optimalSubArray) == 0 and len(optimalSubArray2) != 0:
        if sumOfArray(optimalSubArray2) >= rightSide:
            return optimalSubArray2
        else:
            return []
    else:
        if sumOfArray(optimalSubArray2) >= rightSide and sumOfArray(optimalSubArray) >= rightSide:
            multi1 = multiplicationOfItems(optimalSubArray)
            multi2 = multiplicationOfItems(optimalSubArray2)
            return optimalSubArray if multi1<multi2 else optimalSubArray2
        elif sumOfArray(optimalSubArray2) >= rightSide and sumOfArray(optimalSubArray) < rightSide:
            return optimalSubArray2
        elif sumOfArray(optimalSubArray2) < rightSide and sumOfArray(optimalSubArray) >= rightSide:
            return optimalSubArray
        else:
            return []


def multiplicationOfItems(array):
    multiplication = 1
    for i in range(len(array)):
        multiplication = multiplication*array[i]
    return multiplication


def sumOfArray(array):
    sum = 0
    for i in range(len(array)):
        sum = sum + array[i]
    return sum

def findSubArray(A):
    rightSide = rightSideEqualization(A)
    return recursiveExhaustiveSearchAlgorithm(A,rightSide,0,[])

def rightSideEqualization(A):
    max = A[0]
    min = A[0]
    for i in range(1, len(A)):
        if max < A[i]:
            max = A[i]

    for i in range(1, len(A)):
        if min > A[i]:
            min = A[i]

    rightSide = (max + min) * (len(A) / 4)
    return  rightSide
print("")
print(" Total Array : ")
A = [2, 4, 7, 5, 22, 11]
print(" {}".format(A) )
print("")
optimalSubArray = findSubArray(A)
print(" Optimal Sub-Array : ")
print(" {}".format(optimalSubArray) )
print("")

