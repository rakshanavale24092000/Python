
value = int(input("Enter a integer"))

x = 0
y = 1
while x <= value:
    print(x)
    x,y = y,x+y

