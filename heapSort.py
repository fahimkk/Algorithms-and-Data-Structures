heap_list = [50,30,20,15,10,8,16]

data = [30,50,20,8,16,15,10,32,86,54]

def heapify(arr,n,i):
    largest = i
    l = i*2 +1
    r = i*2 + 2
    if (l<n and arr[i] < arr [l]):
        largest = l
    if (r<n and arr[largest] < arr [r]):
        largest = r
    if largest !=i :
        arr[largest],arr[i] = arr[i], arr[largest]
        heapify (arr,n,largest)
    return arr
    
def heapSort(arr):
    n = len(arr)
    for i in range(n//2-1,-1,-1):
        heapify(arr,n,i)
    print(arr)
    # this for loop is for deleting, ie delete the i=0 th element
    # which is the max element, and swap it with the last element
    # and then heapify without including that element.
    for i in range(n-1, 0,-1):
        arr[i],arr[0]== arr[0],arr[i]
        heapify(arr,i,0)

print(data)
heapSort(data)
print(data)