from pig_latin import word2piglatin

# And then you have it from here!
with open("moby_dick.txt") as fh:
    data = fh.read()
# data = data.splitlines()
# print(" ".join(data))
# data = data.replace('\n', ' ')

# 2B problems
words = data.split("\n")
print(words)
    
new_words = [word2piglatin(word) for word in words]
# Pidwords = " ".join(new_words)
# print(" ".join(new_words))
pig_store = " ".join(new_words)

with open("piglatin_words.txt", "a") as fh:
    fh.write(pig_store)