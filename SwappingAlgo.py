a = 10
b = 20
print(f'Before Swapping a = {a}, b = {b}')

# m-1
a, b = b, a
print(f'M-1 a = {a}, b = {b}')

# m-2
a = 10
b = 20
tem = a
a = b
b = tem
print(f'M-2 a = {a}, b = {b}')

# m-3
a = 10
b = 20
[a, b] = [b, a]
print(f'M-3 a = {a}, b = {b}')

# m-4
a = 10
b = 20
a = a + b
b = a - b
a = a - b
print(f'M-4 a = {a}, b = {b}')

# m-5
a = 10
b = 20
a = a ^ b
b = a ^ b
a = a ^ b
print(f'M-5 a = {a}, b = {b}')

# m-6
a = 10
b = 20
a = a * b
b = a / b
a = a / b
print(f'M-6 a = {a}, b = {b}')