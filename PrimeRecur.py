def Prime(a, i=2):
    if a == i:
        return True
    elif a == 1:
        return False
    elif a % i == 0:
        return False
    else:
        return Prime(a, i + 1)


print(Prime(5))
