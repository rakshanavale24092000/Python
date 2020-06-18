def spy_game(num):
    code = [0, 0, 7, 'x']
    for i in num:
        if i==code[0]:
            code.pop(0)

    return len(code) == 1


nums = [1, 4, 2, 0, 0, 7]
print(spy_game(nums))