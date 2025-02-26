from english import ENGLISH_WORDS, is_english_word

def one_off (x):
    count = 0
    y = ""
    z = "abcdefghijklmnopqrstuvwxyz"
    for i in range(len(x)):
        for j in range(len(z)):
            for k in range(len(x)):
                if k == i:
                    y += z[j]
                else:
                    y += x[k]
            if not(x[i] == y[i]):
                if y[i] in ENGLISH_WORDS:
                    print(y)
                    count += 1
    return count
                    
    print(one_of("word"))