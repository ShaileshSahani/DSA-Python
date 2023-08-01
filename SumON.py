import time

# Normal
n = int(input("Enter a Number: "))
t1 = time.time()
s = 0
for i in range(n + 1):
    s += i
print(s)
print(time.time() - t1)


# DSA
n = int(input("Enter A Number: "))
s1 = time.time()
s = (n * (n + 1)) / 2
print(s)
print("Sum of Cube: ", int(s) ** 2)
print(time.time() - s1)

# Method 2
p1 = 0
n1 = 10
for i in range(1, n1 + 1, p1+1):
    p1 = p1 + i
print(p1)


