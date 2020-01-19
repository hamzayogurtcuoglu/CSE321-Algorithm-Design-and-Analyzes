
def unSortedArrayFindMedian(arr, l, r, k):
    if (k > 0 and k <= r - l + 1):
        n = r - l + 1
        median = []
        i = 0
        while (i < n // 5):
            median.append(findMedian(arr, l + i * 5, 5))
            i += 1

        if (i * 5 < n):
            median.append(findMedian(arr, l + i * 5,
                                     n % 5))
            i += 1
        if i == 1:
            medOfMed = median[i - 1]
        else:
            medOfMed = unSortedArrayFindMedian(median, 0,
                                   i - 1, i // 2)
        pos = partition(arr, l, r, medOfMed)

        if (pos - l == k - 1):
            return arr[pos]
        if (pos - l > k - 1):  # If position is more,
            return unSortedArrayFindMedian(arr, l, pos - 1, k)

        return unSortedArrayFindMedian(arr, pos + 1, r,
                           k - pos + l - 1)
    return 1000000000000000

def swap(arr, a, b):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp

def partition(arr, l, r, x):
    for i in range(l, r):
        if arr[i] == x:
            swap(arr, r, i)
            break

    x = arr[r]
    i = l
    for j in range(l, r):
        if (arr[j] <= x):
            swap(arr, i, j)
            i += 1
    swap(arr, i, r)
    return i

def findMedian(arr, l, n):
    lis = []
    for i in range(l, l + n):
        lis.append(arr[i])
    lis.sort()
    return lis[n // 2]

arr = [1, 9, 8, 7,2]
n = len(arr)
print()
print(" Unsorted Array : {}".format(arr))
print()
print(" Median of Array : ",unSortedArrayFindMedian(arr, 0, n - 1,int(n/2)+1))
print()