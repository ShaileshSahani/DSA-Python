import time

# Normal
n = int(input("Enter A Number: "))
sat = time.time()
s = 0
for i in range(n + 1):
    s += i**3

print(s)
print(time.time() - sat)


# DSA
n = int(input("Enter A Number: "))
sat1 = time.time()
s = ((n * n)*((n + 1) * (n + 1))) / 4
print(s)
print(time.time() - sat1)



