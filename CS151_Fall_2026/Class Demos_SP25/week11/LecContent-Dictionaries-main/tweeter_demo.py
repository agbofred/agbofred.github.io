

with open("tweets.csv") as fh:
    #print(fh.read())
    dic = {}
    for line in fh:
        part = line.strip().split('","')
        username = part[0][1:]
        tweet = part[1][:-1]
        # print(f"{username} ---------> {tweet}")
        for word in tweet.split(','):
            if word.startswith("#"):
                if word in dic:
                    dic[word].append(username)
                else:
                    dic[word] = [username]
    for w, val in dic.items():
        print(w, val)
# print(dic)
        
        