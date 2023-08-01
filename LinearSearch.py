from random import randint
main_lis = []
for i in range(1000):
    main_lis.append(randint(1, 100))
print(main_lis)
for i in range(len(main_lis)):
    for j in range(len(main_lis)):
        if main_lis[i] < main_lis[j]:
            main_lis[i], main_lis[j] = main_lis[j], main_lis[i]
print(main_lis)
n = int(input("Enter A Number: "))
if n in main_lis:
    print("Number Found ")
    r = main_lis.index(n)
    for i in main_lis:
        if n == i:
            print("Index : [", r, "]", i)
            r += 1
else:
    print("No Data")

