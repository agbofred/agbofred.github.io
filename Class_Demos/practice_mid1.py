from english import is_english_word, ENGLISH_WORDS
"""def tracer(n):
    total = 0
    while n > 0:# start tracing here
        digit = n % 10
        total += digit
        n //= 10
    return total"""


"""def mystery (x):
    def enigma (s, t):
        t -= 1
        return s [::12] + s[t]
    y = len(x)
    z = x[3 - y]
    z += enigma (x, y)
    #z += enigma (x, 9-y)
    return z
if __name__ == "__main__":
    print(mystery("abcdefghijklmn")) # Answer damn"""

#50 % 5 + 3 * 4 - 1 * (4 - 3 ** 3 + 5) + 13 // 7  #Answer `31`
#print(2 + 2 * 2 // 2 ** 2 - 2 % 2) # Answer 3

#print(7 < 9 - 5 and 3 % 0 == 3) # Answer False

#a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#print(a[5:15:3] * 3)

def problem3 (s): ## Answer is sesrest
    r = ""
    for i in range ( len(s)):
        if i % 2 != 0:
            r += s[i]
        else :
            r = s[i] + r
    return r

# Another Quesition
def prob4a (s): ## with s = "Hit tie why wish noon rip lord ding" output will be "Hi world"
    r = 0
    new = ""
    for i in range ( len(s)):
        if s[i]. isspace () and is_english_word (s[r:i]):
            new += prob4b (s[r:i])
            r = i + 1
    new += prob4b (s[r:])
    return new

def prob4b (y):
    done = False
    for r in y [:: -1]:
        if done :
            return r
        if r. lower () in " aeiou ":
            done = True
    return " "

# Another Programming tracing 

def func (a, b=5, c= False ): ## The answer is 6
    if c:
        return a + c
    else:
        return a * b
print(func (5,False,True))

#-------------
#Another Question

def puzzle (t): # Answer is cfadg
    def mystery (r,x):
        x += 1
        def enigma (s):
            return r[s::x]
        return enigma
    x = 2
    y = mystery (t,x)
    return y(x) + y(0)


# Question on Programming 
def one_off(word):
    counter=0
    for w in ENGLISH_WORDS:
        if len(word)== len(w):
            count = 0
            for i in range(len(w)):
                if w[i]== word[i]:
                    count +=1
            if count == len(word)-1:
                print(w)
                counter +=1
    return counter
            

if __name__ == "__main__":
    #print(problem3("ressets"))
    #print(prob4a("Hit tie why wish noon rip lord ding"))
    #print( puzzle ("abcdefg"))
    print(one_off("money"))