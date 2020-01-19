
def findingContiguousSubset(A,begin,end):
    if begin == end:
        return (begin, end)
    mid = int((begin + end) / 2)
    lLargest = findingContiguousSubset(A, begin, mid)
    rRightest = findingContiguousSubset(A, mid + 1, end)
    Lsum = sum(A[lLargest[0]:lLargest[1] + 1])
    Rsum = sum(A[rRightest[0]:rRightest[1] + 1])

    if (rRightest[0] - lLargest[1]) == 1:
        total = Lsum + Rsum
        if Rsum <= total and Lsum <= total:
            return (lLargest[0], rRightest[1])
    else:
        rangeSum = sum(A[lLargest[0]:rRightest[1] + 1])
        if Rsum <= rangeSum and Lsum <= rangeSum:
            return (lLargest[0], rRightest[1])
    return rRightest if Lsum < Rsum else lLargest

def largestSum(A):
    begin, end = findingContiguousSubset(A, 0, len(A) - 1)
    largestSumArray = A[begin:end+1]
    return largestSumArray

A = [5, -6, 6, 7, -6, 7, -4, 3]
print()
print("Array -> " ,A)
print()
print("Largest Sum Array: ")
largestSumArray = largestSum(A)
print(largestSumArray , " - Sum -> " , sum(largestSumArray))