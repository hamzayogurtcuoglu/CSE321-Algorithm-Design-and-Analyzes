
def decrease_and_conquer(arr):
    for i in range(int(len(arr)/2)):
        # 		moves       #
        if i % 2 == 1:
            temp = arr[i]
            arr[i] = arr[int(len(arr))-1-i]
            arr[int(len(arr)) - 1 - i] = temp
    return arr

#################################################################################################
#                                       Test                                                    # 

arr = ['black' ,'black','black' ,'black','white','white','white','white']
print("2n boxes standing in a row : \n")
print(arr)
print("\n")
print("Designed array is:")
arr = decrease_and_conquer(arr)
print(arr)
for i in range(len(arr)):
   print(arr[i])