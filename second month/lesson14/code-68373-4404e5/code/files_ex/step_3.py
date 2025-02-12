f_path = 'data/hello.txt'

with open(f_path, 'r', encoding='utf-8') as f:
    # data = f.read()
    data = f.read(4)
    # data = f.readline()
    # data = f.readlines()
    # data = list(
    #     map(
    #         str.strip,
    #         f.readlines(),
    #     )
    # )
    # data = f.read()
    # data = data.splitlines()
    print(data)
    # for el in f:
    #     print(el)
