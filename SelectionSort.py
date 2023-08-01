values = list(map(int, input("Enter Elements: ").split()))
print("The Values You Entered", values)
for step in range(len(values)):
    min_idx = step
    for i in range(step + 1, len(values)):
        if values[min_idx] > values[i]:
            min_idx = i
            values[min_idx], values[step] = values[step], values[min_idx]
print(values)


# Selection sort in Python


def selectionSort(array, size):
    for step in range(size):
        min_idx = step
        for i in range(step + 1, size):
            if array[i] < array[min_idx]:
                min_idx = i
        (array[step], array[min_idx]) = (array[min_idx], array[step])


data = [-2, 45, 0, 11, -9]
size = len(data)
selectionSort(data, size)
print('Sorted Array in Ascending Order:')
print(data)