def firstn(n):
    """ A generator that yields items instead of returning a list"""
    num = 0
    while num < n:
        yield num
        num +=1

print(sum(firstn(10)))