with open("tweets.csv") as fh:
    # print(fh.read())
    dic = {}
    for line in fh:
        part = line.strip().split('","')
        username = part[0][1:]
        tweet = part[1][:-1]
        print(f"{username} ---------> {tweet}")