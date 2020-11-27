data = [45,2,56,4,789,56,324,11,562,55,0,476,10]

def count_sort(arr,pos):
    n = len(arr)
    count_list = [0 for i in range(10)]
    for i in range(n):
        count_list[(arr[i]//pos)%10] +=1
    for i in range(1,10):
        count_list[i] += count_list[i-1]
    sorted_list = [0 for i in range(n)]
    for i in range(n-1, -1, -1):
        index = (arr[i]//pos) %10
        count_list[index] -=1
        sorted_list[count_list[index]] = arr[i]
    for i in range(n):
        arr[i] = sorted_list[i]

def radix_sort(arr):
    #find max digit
    n = len(arr)
    largest_num = arr[0]
    for i in range(n):
        if arr[i] > arr[0]:
            largest_num=arr[i]
    pos = 1
    while largest_num//pos > 0:
        count_sort(arr,pos)    
        pos = pos * 10

print(data)
radix_sort(data)
print(data)
