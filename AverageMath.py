n = int(input("Enter Number Of Element: "))
val = []
for i in range(n):
    print("Enter Element ", i, " : ", end=" ")
    s = int(input())
    val.append(s)
print("Elements You Entered: ", val)
s = 0
for i in range(len(val)):
    s += val[i]
print("Average: ", s / len(val))


def solve(v):
    return sum(v) / len(v)


l1 = [1, 3, 6, 4, 8, 9]

print(round(solve(l1), 2))
