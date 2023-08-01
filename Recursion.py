def SumOf(n):
    if n > 0:
        return n + SumOf(n - 1)
    else:
        return 0


print(SumOf(5))


def fact(v):
    if v > 0:
        return v * fact(v - 1)
    else:
        return 1


print(fact(5))
