
def check_insertion(arr, target, k):
    low = 0
    high = len(arr)
    while low < high:
        mid = (low+high)//2  # from n//2 leaf nodes starts
        if abs(arr[mid]-target) > k:
            if arr[mid] > target :
                high = mid - 1  
            if arr[mid] < target :
                low = mid +1
        else: return False
    #at this point low = high, ie reaches leaf node
    if abs(arr[low]-target)>k:
        if arr[low] > target: 
            arr.insert(low, target)
        else: 
            arr.insert(low+1, target)
        return arr


def check_insertion_normal(arr, now,time ,k,):
    if time < now: return False
    for i in range(len(arr)):
        if abs(time-arr[i]) < k: return False
    arr.append(time)
    arr.sort()
    return arr
data =[35,56,60,68,90,95,110]
check_insertion(data,72,3)
print(check_insertion(data,76,3))


