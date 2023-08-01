values = list(map(int, input("Enter Elements: ").split()))
print("The Values You Entered", values)
for i in range(len(values)):
    for j in range(i + 1, len(values)):
        if values[i] > values[j]:
            values[i], values[j] = values[j], values[i]
print("List After Sorting: ", values)

