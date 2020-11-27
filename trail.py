data =[21,22,36,54,1,45,27,63,28,14,16,98,74,12,25,87,45]

def check(data):
    og_data = data
    def merge_sort (data):
        if len(data) > 1:
            mid = len(data)//2
            left_list = data[:mid]
            right_list = data[mid:] 

            merge_sort(left_list)
            merge_sort(right_list)

            # merging
            i = 0   # index for left_list
            j = 0   # index for right_list
            k = 0   # index for sort_list   
            
            while i < len(left_list) and j < len(right_list):
                if left_list[i] < right_list[j]:
                    data[k] = left_list[i]
                    i+=1
                    k+=1
                else:
                    data[k] = right_list[j]
                    j+=1
                    k+=1
            
            while i < len(left_list):
                data[k] = left_list[i]
                i+=1
                k+=1
            while j < len(right_list):
                data[k] = right_list[j]
                j+=1
                k+=1
    merge_sort(og_data)
    return og_data 

gap = 50
for i in range(gap,0,lambda x: x//2):
    print(i)
    print(gap)