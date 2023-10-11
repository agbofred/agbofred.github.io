
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
def one_off(the_word):


    result_words = ""


    for word in ENGLISH_WORDS:


        if len(word)== len(the_word):


            diff_count=0


            for i in range(len(word)):


                if word[i] != the_word[i]:


                    diff_count += 1

                if diff_count == 1:


                    #(I froze I dont remember this part)


                    result_words


                    #print(results)


    return len(result_words) 
   

if __name__ =="__main__":
    print(one_off("money"))