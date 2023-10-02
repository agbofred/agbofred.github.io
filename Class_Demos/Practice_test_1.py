#print(8 * 5 + 7 % 4 - 9 // 3 ** 2 + 0 / 6)

def positive(N):
    sum =0
    i =1
    check= 1
    stop = False
    while not stop:
        if (i%2!=0):
            if (check<=N):
                print(i)
                sum = sum+i
                check=check+1
                i = i+1
            else:
                stop = True
        else:
            i = i+1
    return sum
print(positive(5))

