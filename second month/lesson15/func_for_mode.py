# Стрелочка нужна для указания того что будет возвращено по выполнению функции.
def model(val: list) -> tuple[bool, tuple[int]]:
    res = all(v >= 0 for v in val)
    if res:
        idx = []
    else:
        idx = [index for index, value in enumerate(val) if value < 0]
    return res, idx