#In fibonacci series the first 2 digits are 0,1 and the next digit is sum of previous two digits.
#0,1,1,2,3,5,8 here the third digit is sum of 1st and 2nd digit i.e 0+1


value = int(input("Enter a integer"))
#input returns string and must be typecasted to integer
#input->50
x = 0
y = 1
while x <= value:
    print(x)
    x,y = y,x+y
    
#output:

# 0
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34


