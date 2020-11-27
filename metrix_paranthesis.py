import heapq

m_dict= {'m1':(3,2),'m2':(2,4),'m3':(4,2),'m4':(2,5)}
metrix_order = ['m1','m2','m3','m4']

def metrix_multiplication(metrix_dict,multiplication_order):
    """ metrix_dict, 
            key - metrix name
            value - metrix order (mxn)
        metric multiplication is not commutative,
        multiplication_order - list matrix name in multiplication order"""
    # for time complexity
    time_dict = {}
    # to track order of multiplication
    order_dict={}

    size_list = []
    size_list.append(metrix_dict[multiplication_order[0]][0])
    for metrix in multiplication_order:
        size_list.append(metrix_dict[metrix][1])

    start = 1
    end = len(multiplication_order)

    # where m & n are metrix number 
    # from where to where we want to multiply
    # to multiply 1st metrix to 4th metrix, m=1 and n=4
    def metrix_time_complexity(m,n):
        # multiplying a metrix with itself
        if m == n:
            return 0
        # taking from memorize
        elif (m,n) in time_dict:
            return time_dict[(m,n)]
        else:
            time_list = []
            for k in range (m,n):
                # equation
                a = metrix_time_complexity(m,k)+metrix_time_complexity(k+1,n)\
                    + size_list[m-1] * size_list[k] * size_list[n]

                heapq.heappush(time_list,(a,k))
                heapq.heapify(time_list)
            # take min time complextiy, and trace k value to
            # get the order of multiplication
            min_tup = heapq.heappop(time_list)
            time_dict[(m,n)] = min_tup[0]
            order_dict[(m,n)] = min_tup[1]
            return time_dict[(m,n)]
    metrix_time_complexity(start,end)
    return time_dict, order_dict

print(metrix_multiplication(m_dict,metrix_order))
