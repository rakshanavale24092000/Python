# If the list contains 0,0,7 in order then the function returns true
# examples:  [1,2,5,0,0,7] ->True
#            [1, 4, 2, 0, 7, 5, 0, 6, 7] -> True
#            [2, 7, 0, 0, 3] -> False


def spy_game(num):
    code = [0, 0, 7, 'x']
    for i in num:
        if i==code[0]:
            code.pop(0)

    return len(code) == 1


nums = [1, 0, 0, 6, 7]
print(spy_game(nums))
#output-> True

# iteration 1
#     i = 1 , False

# iteration 2
#     i = 0 , True
#     0 from code is poped therefore code=[0, 7, 'x']

# iteration 3
#     i = 0 , True
#     0 from code is poped therefore code=[7, 'x']

# iteration 4
#     i = 6 , False

# iteration 5
#     i = 7 , True
#     0 from code is poped therefore code=['x']
#for loop breaks and length is 1 and hence True is returned
