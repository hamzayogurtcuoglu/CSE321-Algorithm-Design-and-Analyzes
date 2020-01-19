def kthElementStart(A,B,k):
     kth = kthElement(A, B, 0,0,len(A), len(B), k)
     return kth
def kthElement(A,B,beginA,beginB,endA,endB,k):
    if (beginA == endA):
        return B[k]
    if (beginB == endB):
        return A[k]
    mid1 =int( (endA - beginA) / 2)
    mid2 =int( (endB - beginB) / 2)
    if (mid1 + mid2 < k):
        if (A[mid1] > B[mid2]):
            return kthElement(A,B, beginA ,beginB + mid2 + 1,endA,endB,k - mid2 - 1)
        else:
            return kthElement(A,B, beginA+mid1+1 ,beginB,endA,endB,k - mid1 - 1)
    else:
        if (A[mid1] > B[mid2]):
            return  kthElement(A,B, beginA ,beginB,beginA+mid1,endB,k)
        else:
            return  kthElement(A,B, beginA ,beginB,endA,beginB+mid2,k)

#TEST DRIVER
A = [4, 9 , 11 , 15 , 100]
B = [1, 2, 8, 16, 990, 50000]
print()
print("First Sorted Array : ",A)
print()
print("Second Sorted Array : ",B)
print()
k = 3
print("kth element : ",kthElementStart(A,B,k))
print()
print(sorted(A+B))