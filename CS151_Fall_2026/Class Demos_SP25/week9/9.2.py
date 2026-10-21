A = [i * 4 for i in "Oct 21, 2026" if not i.isalpha() and not i.isspace()]
print(A)