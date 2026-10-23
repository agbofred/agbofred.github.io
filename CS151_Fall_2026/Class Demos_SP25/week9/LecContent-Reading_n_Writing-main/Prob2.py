from pig_latin import word2piglatin

# And then you have it from here!
with open("moby_dick.txt") as fh:
    data = fh.read()
# data = data.splitlines()
# print(" ".join(data))
data = data.replace('\n', ' ')

# 2B problems
words = data.split()
    
new_words = [word2piglatin(word) for word in words]
Pidwords = " ".join(new_words)
# print(" ".join(new_words))

#2C Problem
with open("moby_bacon.txt", "w") as fh:
    
    fh.writelines(Pidwords)
