def Base(a, b):
    if b == 0:
        return a
    else:
        return a * Base(a, b - 1)


print(Base(5, 3))
