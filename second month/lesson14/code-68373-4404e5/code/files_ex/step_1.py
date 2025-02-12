f_path = 'data/hello.txt'
f = open(f_path, 'r', encoding='utf-8')
print(dir(f))

f.write('good evening')
# print(type(f))
# print(dir(f))
# print(f.closed)
# f.close()
# print(f.closed)
