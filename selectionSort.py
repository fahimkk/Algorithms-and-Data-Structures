data = [30,-50,20,8,16,15,10]

def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min_val = arr[i]
        min_index = i
        for j in range(i+1,n):
            if arr[j] < min_val:
                min_val = arr[j]
                min_index = j
        arr[i],arr[min_index] = arr[min_index], arr[i] 

print(data)
selection_sort(data)
print(data)