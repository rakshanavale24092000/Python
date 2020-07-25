#Tuples are similar to lists but are immutable 

tuple = (4,10,20,15,80)
#unpacking of tuples
a,b,c,d,e = tuple
sum = a+b+c+d+e
print(sum)
#output->129

#tuples are immutable thats the reason to add elements at the end concatination is used.
#tuples are constructed by comma operators with or without being enclosed by parantheses
tuple = tuple + (sum,)
print(tuple)
#output-> (4, 10, 20, 15, 80, 129)

#tuple containing only sum
tuple = tuple[-1:]
print(tuple)
#output->(129,)
