import random
import string

def generate_candidate(num_low, num_high, dirt_options, chance_dirty):
    num = str(random.randint(num_low, num_high))
    if random.random() < chance_dirty:
        n_dirt_lead = random.randint(0,3)
        if n_dirt_lead == 0:
            n_dirt_trail = random.randint(1,3)
        else:
            n_dirt_trail = random.randint(0,3)
        lead = "".join(random.choices(dirt_options, k=n_dirt_lead))
        trail = "".join(random.choices(dirt_options, k=n_dirt_trail))
        return (lead + num + trail).replace('"', '')
    return num





if __name__ == '__main__':
    dirt = string.ascii_letters + "!#$%&()*+,-./:;<=>?@[]^_{|}~"
    print("DATA = [")
    for _ in range(500):
        print(f'\t"{generate_candidate(0, 25, dirt, 0.25)}",')
    print("]")
