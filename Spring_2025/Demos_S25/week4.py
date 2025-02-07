# A = 1000000
# B ="*"
# for i in range(10):
#     star = 2*i +1
#     print(f"The value of A is {B*star:0^40}")

from english import ENGLISH_WORDS


def tenletterwords():
    count =0
    for w in ENGLISH_WORDS:
        if len(w)==10:
            print(w)
            count +=1
    return count

print(f"{tenletterwords():,}")