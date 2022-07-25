# Write the algorithm for selection sort

def selectionSort(some_list):
    for i in range(len(some_list)):
        minIndx = i
        for j in range(i+1, len(some_list)):
            if some_list[j] < some_list[minIndx]:
                minIndx = j
        some_list[i], some_list[minIndx] = some_list[minIndx], some_list[i]
    return some_list
    

print(selectionSort([5,4,8,2,9,1,0]))
print(selectionSort([10,30,-9,0,5,100,-15,98]))