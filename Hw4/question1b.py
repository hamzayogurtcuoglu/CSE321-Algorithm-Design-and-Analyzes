
# I used A[i, j ] + A[i + 1, j + 1] ≤ A[i, j + 1] + A[i + 1, j ] equalization
def changeSinglePoint2DArray(array):
    distance = 0
    points = [[0, 0], [0, 0]]
    for i in range(len(array)-1):
        for j in range(len(array[0])-1):
            if array[i][j] + array[i+1][j+1] > array[i][j+1] + array[i+1][j]:
                points[0][0] = i
                points[0][1] = j+1
                points[1][0] = i+1
                points[1][1] = j
                distance = array[i][j] + array[i+1][j+1] - array[i][j+1] - array[i+1][j]
                break

    specialArray = True
    array[points[0][0]][points[0][1]] = array[points[0][0]][points[0][1]] + distance

    for i in range(len(array)-1):
        for j in range(len(array[0])-1):
            if array[i][j] + array[i+1][j+1] > array[i][j+1] + array[i+1][j]:
                specialArray = False
                break
    if not specialArray:
        array[points[0][0]][points[0][1]] = array[points[0][0]][points[0][1]] -  distance
        array[points[1][0]][points[1][1]] = array[points[1][0]][points[1][1]] +  distance
        return array

    return array

# I used A[i, j ] + A[i + 1, j + 1] ≤ A[i, j + 1] + A[i + 1, j ] equalization in the function
print("Not Special Array ")
array = [[10,17,13,28,23],[17,22,16,29,23],[24,28,22,34,24],[11,13,6,17,7],
         [45,44,32,37,23],[36,33,19,1,6],[75,66,51,53,34]]
for i in range(len(array)):
    print(array[i])
print("---------------------")
print("Special Array ")
array = changeSinglePoint2DArray(array)
for i in range(len(array)):
    print(array[i])