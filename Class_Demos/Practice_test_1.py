
from english import ENGLISH_WORDS, is_english_word
#print(8 * 5 + 7 % 4 - 9 // 3 ** 2 + 0 / 6)

"""def positive(N):
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
print(positive(5))"""
def one_off(word):


    number_of_words = 0    


    for i in range(len(word)):


        letter = word[i]


        alphabet = 'abcdefghijklmnopqrstuvwxyz'


        for i in range(len(alphabet)):


            new_word = word


            new_word.replace(letter, i)


            if new_word in is_english_word:


                print(new_word)


                number_of_words += 1


    return number_of_words

if __name__ =="__main__":
    print(one_off("money"))