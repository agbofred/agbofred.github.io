tu = ("grace", 43)
name, age = tu
empty_t =(4,)
tu1 =tu[1:]
tu2 = ("Fred",) + tu1
"""
[print(f'{name}--{age}') for i in range(len(tu)) ]"""
#print(tu2*2)
#print(tu[1], + tu[0],)

# Named tupple

from collections import namedtuple

employee = namedtuple("record", ["name", "age", "salary"])

e1 = employee("Fred", 33, 1000)
e1 = employee("grace", 44,20)
print(employee.count())