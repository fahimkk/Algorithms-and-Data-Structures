
# normal recursive fib 
# exponential time complexity
def fib(n):
    if n <=2:
        return 1
    else:
        return fib(n-1)+fib(n-2)
print(fib(10))
        
# memorized dp algorithm
# timecomplexity is polynomial
memo = {}
def fib_memo(n):
    if n in memo:
        return memo[n]
    else:
        if n <=2:
            return 1
        else:
            memo[n] = fib(n-1)+fib(n-2)
            return memo[n]
print(fib_memo(10))

# bottom_up dp algorithm
# timecomplexity is same as memorized type
# but practically faster, no recursion
fib_table = {}
def fib_bottom(n):
    for k in range(1,n+1):
        if k<=2:
            f = 1
        else:
           f = fib_table[k-1]+fib_table[k-2]
           # del will help to delete non required keys
           # we only need last two elements
           # wich help to decrease storage 
           del fib_table[k-2]
        fib_table[k] = f

    return fib_table[n]
print(fib_bottom(10))

