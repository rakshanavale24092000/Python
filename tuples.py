tuple = (4,10,20,15,80)
a,b,c,d,e = tuple
sum = a+b+c+d+e
print(sum)
tuple = tuple + (sum,)
print(tuple)
tuple = tuple[-1:]
print(tuple)