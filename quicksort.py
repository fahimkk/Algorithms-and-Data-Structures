data = [45,67,90,-66,89,23,45,-77,90,15,95,35]

def partition(arr, low, high):
    pivot_index = low 
    pivot = arr[pivot_index]
    low+=1

    while low<high:
        while arr[low] <= pivot: 
            low += 1
        while arr[high] > pivot: 
            high -= 1
        if low < high:
            arr[low], arr[high] = arr[high], arr[low]
    arr[pivot_index],arr[high]=arr[high], arr[pivot_index]
    return high
    
def quick_sort(arr,low,high):
    if low < high: 
        j = partition(arr, low, high)
        quick_sort(arr, low, j-1)
        quick_sort(arr, j+1, high)


print(data)
quick_sort(data, 0, len(data)-1)
print(data)
