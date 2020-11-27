# Insertion Sort

data =[21,22,36,54,1,45,27,63,28,14,16,98,74,12,36,35,34,89,65,25,87,45]

def insertion_sort(data):
    for i in range(1,len(data)):
        # -------------
        """ for j in range(i-1,-1,-1):
            if data[j] > data[j+1]:
                data[j],data[j+1] = data[j+1], data[j]
            else:
                break """
        j=i-1
        while data[j] > data[j+1] and j>=0:
                data[j],data[j+1] = data[j+1], data[j]
                j -=1

    return data
 

def insertion_sort_withou_swap(data):
    # first element at the 0th index considered as sorted.
    for i in range(1,len(data)):
        #current element is the first element of the unsorted part.
        curNum = data[i] 
        # pos -  is used to compare the curNum whith sorted elements
        pos = i
        # to compare current element to sorted part element we need a loop
        #----------------------------
        while curNum < data[pos - 1] and pos >0:
            data[pos] = data [pos-1]
            pos -=1 
        data[pos] = curNum

    
        """ for j in range(i-1,0,-1):
            if data[j]>curNum:
                data[j+1] = data[j]
            else:
                data[j+1] = curNum
                break """
    return data
print(insertion_sort_withou_swap(data))