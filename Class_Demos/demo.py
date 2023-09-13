def add ():
    sum = 0
    finish = False
    while not finish:
        num = int(input("Enter integer to sum, Enter zero to stop!  "))
        if num ==0:
            finish = True
        else:
            sum += num
    return sum


if __name__ == '__main__':
    print(add())

