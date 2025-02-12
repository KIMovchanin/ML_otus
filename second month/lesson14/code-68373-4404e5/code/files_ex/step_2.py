f_path = 'data/hello.txt'

with open(f_path, 'r', encoding='utf-8') as f:
    # print(dir(f))
    # print(f.closed)
    # IOPS
    for el in f:  # next(f) -> next row
        el = el.strip()
        if el == 'hello, world!':
            print(el)
        else:
            print(f'!{el}')

print(f.closed)
