data = [30,50,20,8,16,15,10,32,86,34,4,-49,92,17,-33,12,12,2,36,8,1,5,9]
sample=[23,29,15,19,31,7,9,5,2]
sampledict = {0:23, 1:29, 2:15, 3:19, 4:31, 5:7, 6:9, 8:5, 9:2}

def shell_sort(arr):
    gap = len(arr)//2
    while gap >0:
        i=0
        j = gap
        while j < len(arr): 
            if arr[i] > arr[j]:
                #arr[i],arr[j]=arr[j],arr[i]
                temp = arr[j]
                arr[j]=arr[i]
                if i-gap >=0 and arr[i-gap] >temp:
                    arr[i] = arr[i-gap]
                    arr[i-gap]=temp
                else: arr[i] = temp

            i+=1
            j+=1
        gap = gap//2
    return arr


#print(shell_sort(sample))

def shellsort(arr): 
    n = len(arr)
    gap = n//2
    while gap >0:
        for i in range(gap,n):
            temp = arr[i]
            j=i
            while j>=gap and arr[j-gap] > temp:
                arr[j] = arr[j-gap]
                j -=gap
            arr[j] = temp
        gap //=2
    return arr
print(shell_sort(data))
