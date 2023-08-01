x = [[0, 0, 0],
     [0, 0, 0],
     [0, 0, 0]]
y = [[0, 0, 0],
     [0, 0, 0],
     [0, 0, 0]]
for i in range(len(x)):
    for j in range(len(x)):
        print(f"Enter {i},{j} element of Matrix X:", end=" ")
        n = int(input())
        x[i][j] = n
for i in x:
    print(i)
for i in range(len(x)):
    for j in range(len(x)):
        print(f"Enter {i},{j} element of Matrix Y:", end=" ")
        n = int(input())
        y[i][j] = n
for i in y:
    print(i)
z = [[0, 0, 0],
     [0, 0, 0],
     [0, 0, 0]]
for i in range(len(x)):
    for j in range(len(y[0])):
        for k in range(len(y)):
            z[i][j] += x[i][k] * y[k][j]
print("Resultant Matrix Z:\n")
for i in z:
    print(i)
