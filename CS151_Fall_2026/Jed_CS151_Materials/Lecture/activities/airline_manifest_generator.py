import faker
from itertools import product
import random
from datetime import datetime

TARGET_PEOPLE = 100

fake = faker.Faker()

cols = ["A", "B", "C", "D", "E", "F"]
rows = [str(i) for i in range(1,29)]
perms = product(rows, cols)
seats = ["".join(p) for p in perms]
random.shuffle(seats)

print("MANIFEST = [")
for n in range(TARGET_PEOPLE):
    person = fake.profile()
    print(f'"{person['name']}",')
    print(f"{datetime.now().year - person['birthdate'].year},")
    print(f'"{seats[n]}",')
print("]")



