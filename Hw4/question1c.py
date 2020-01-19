def startFinding(array):
    print("Special Array ")
    for i in range(len(array)):
        print(array[i])
    print("---------------------")
    print("Leftmost minimum elements each row")
    minimumElements = []
    for i in range(0, len(array)):
        minimumElements.append(0)
    specialArray = Array(len(array[0]), len(array), array, 1)
    findLeftMostMinimums(specialArray, minimumElements)
    for i in range(0, len(array)):
        print(array[i][minimumElements[i]])

def minIndex(A, row,left,right):
    min = left

    for i in range(left,right):
        if (A.array[((row + 1) * A.step - 1)][i] < A.array[((row + 1) * A.step - 1)][min]):
            min = i
    return min

def findLeftMostMinimums(A,mins):
    if (int(A.row/ A.step) == 1):
        mins[0] = minIndex(A, 0, 0, A.column)
    else:
        evens = Array(A.column,A.row,A.array,A.step*2)
        even_minimums = []
        for i in range(0,int (int(evens.row/ evens.step))):
            even_minimums.append(0)

        findLeftMostMinimums(evens, even_minimums)
        leftmost = 0

        for i in range(0,int(evens.row/ evens.step)):
            leftmost = minIndex(A, 2 * i, leftmost, even_minimums[i] + 1)
            mins[2 * i] = leftmost
            mins[2 * i + 1] = even_minimums[i]
        if (int(A.row/ A.step) % 2):
            mins[int(A.row/ A.step) - 1] = minIndex(A, int(A.row/ A.step) - 1, leftmost, A.column)

class Array:
  def __init__(self, column, row, array, step):
    self.column = column
    self.row = row
    self.array = array
    self.step = step

#Test Array
array = [[10,17,13,28,23],[17,22,16,29,23],[24,28,22,34,24],[11,13,6,17,7],
         [45,44,32,37,23],[36,33,19,21,6],[75,66,51,53,34]]
startFinding(array)
