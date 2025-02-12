a = [1, 2, 4, 3]
b = [2, .4, -.5, 2, -8]

# all - проверяет все условия, что в неё входят
print(all(v > 0 for v in a))
print([index for index, value in enumerate(a) if value <= 0])

# ---
print(all(v > 0 for v in b))
print([index for index, value in enumerate(b) if value <= 0])