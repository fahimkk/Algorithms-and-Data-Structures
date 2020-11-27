data = [30,50,-20,8,16,15,10]
data1 = []

def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        # after each iteration next larger number reaches to its postion
        for j in range(1,n-i):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1],arr[j]

print(data)
bubble_sort(data)
print(data)
