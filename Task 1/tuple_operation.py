c = (10, 28, 3, 28, 18, 23, 47, 19, 29, 17, 40)
y = list(c)

print(f"initial value : {c}")

y.append(49)
print(f"append 49 : {y}")

y.insert(5, 99)
print(f"insert 99 on index 5 : {y}")

y.pop(2)
print(f"delete index 2 : {y}")

c = tuple(y)
print(f"final result : {c}")