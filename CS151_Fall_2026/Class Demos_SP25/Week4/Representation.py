from english import ENGLISH_WORDS

def check_word():
    count =0
    for w in ENGLISH_WORDS:
        if len(w) == 20:
            
            print(w)
            #print(f"{len(ENGLISH_WORDS):,}")
            count +=1
    return count

print(f"{check_word():,}")

