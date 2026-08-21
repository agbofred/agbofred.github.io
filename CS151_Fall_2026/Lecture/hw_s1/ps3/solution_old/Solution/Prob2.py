
import random

def consecutive_heads(n):
    count = 0
    tot_flips = 0
    while count < n:
        flip = random.randint(0,1)
        tot_flips += 1
        if flip == 1:
            print("heads")
            count += 1
        else:
            print("tails")
            count = 0
    print(f"It took {tot_flips} flips to get {count} heads!")
    return tot_flips

if __name__ == '__main__':
    print(consecutive_heads(4))
