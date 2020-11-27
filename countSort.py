data = [3,3,4,5,2,-5,2,8,3,8,3,0,-9,3,0,2,4,6,0,6,2]
data1 = [30,50,20,8,16,15,10]
data2 = [45,2,56,4,789,56,324,11,562,55,476,11]

def count_sort(arr):
    n = len(arr)
    k = 0
    # to find the max value in the list to determine the range
    for i in range(n):
        if arr[i] > k:
            k = arr[i]
    # size of count list should be k+1 ie including zero
    count_list = [0 for i in range(k+1)] 
    for i in range(n):
        count_list[arr[i]] +=1
    for i in range(1,k+1):
        count_list[i] += count_list[i-1]
    sort_arr = [0 for i in range(n)] 
    for i in range(n-1, -1, -1):
        count_list[arr[i]] -= 1
        sort_arr[count_list[arr[i]]] = arr[i]
    for i in range(n):
        arr[i] = sort_arr[i]

def count_sort_negative(arr):
    n = len(arr)
    k = 0
    neg_list = []
    neg_factor = 0
    for i in range(n):
        if arr[i] > k:
            k = arr[i]
        if arr[i]< 0:
            neg_list.append(arr[i])
    if neg_list:
        for i in range(len(neg_list)): 
           neg_factor += neg_list[i]
        k -= neg_factor
        # adding negative number to all the numbers wont effect the comparison
        for i in range(n): 
            arr[i] -= neg_factor
    # size of count list should be k+1 ie including zero
    count_list = [0 for i in range(k+1)] 
    for i in range(n):
        count_list[arr[i]] +=1
    for i in range(1,k+1):
        count_list[i] += count_list[i-1]
    sort_arr = [0 for i in range(n)] 
    for i in range(n-1, -1, -1):
        count_list[arr[i]] -= 1
        sort_arr[count_list[arr[i]]] = arr[i]
    for i in range(n):
        arr[i] = sort_arr[i]+neg_factor

print(data2)
count_sort_negative(data2)
print(data2)

    