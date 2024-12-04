from english import ENGLISH_WORDS

count = 0
for word in ENGLISH_WORDS:
    if len(word) == 2:
        count += 1
        print(word)
print(count)