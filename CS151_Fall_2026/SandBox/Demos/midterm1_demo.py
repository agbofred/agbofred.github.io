def problem1(s):
    r = ""
    for i in range(len(s)):
        if i % 2 != 0:
            r += s[i]
        else :
            r = s[i] + r
    return r



if __name__ == '__main__':

    print(problem1("ressets"))