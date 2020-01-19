###############-------- Insertion Sort---------########
def insertionSort(arr):
    count = 0;
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            count = count + 1
            arr[j + 1] = arr[j]
            j -= 1
        count = count + 1     
        arr[j + 1] = key
    return count

#################------QuickSort---------#############

def partition(arr, low, high,count):
    i = (low - 1)
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
            count = count + 1
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    count = count + 1
    return (i + 1),count

def quickSort(arr, low, high,count):
    if low < high:
        pi ,count = partition(arr, low, high,count)
        count = quickSort(arr, low, pi - 1,count)
        count = quickSort(arr, pi + 1, high,count)
        return count
    return count
#################--------QuickSort------#############


arr = [12, 11, 13, 5, 6]
n = len(arr)
swapQuickSort = quickSort(arr, 0, n - 1,0)
print("QuickSort Swap Count ->  {}".format(swapQuickSort))
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i])


arr = [12, 11, 13, 5, 6]
swapInsertion = insertionSort(arr)
print("Insertion Swap Count ->  {}".format(swapInsertion))
print("Sorted array is:")
for i in range(len(arr)):
    print("%d" % arr[i])



arr = [1,2,3,4,5,6,7,8,9,10]
n = len(arr)
swapQuickSort = quickSort(arr, 0, n - 1,0)
print("QuickSort Swap Count ->  {}".format(swapQuickSort))
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i])


arr = [1,2,3,4,5,6,7,8,9,10]
swapInsertion = insertionSort(arr)
print("Insertion Swap Count ->  {}".format(swapInsertion))
print("Sorted array is:")
for i in range(len(arr)):
    print("%d" % arr[i])

