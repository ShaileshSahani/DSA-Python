import time

# Normal
n = int(input("Enter A Number: "))
sm = time.time()
s = 0
for i in range(n + 1):
    s += i**2
print(s)
print(time.time() - sm)


# DSA
n = int(input("Enter A Number: "))
s1 = time.time()
s = (n * ((n + 1) * (2 * n + 1))) / 6
print(s)
print(time.time() - s1)
