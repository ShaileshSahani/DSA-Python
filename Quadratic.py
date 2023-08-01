import math
import re


def Solve(a, b, c):
    discriminant = (b * b - (4 * a * c))
    if discriminant > 0 or discriminant == 0:
        value = math.sqrt(discriminant)
        if value == 0:
            print(f"Roots Are Real And Equal\n"
                  f"Result: {(-b / 2 * a)}")
        elif value > 0:
            print(f"Roots Are Real And Equal\n"
                  f"Positive: {((-b + value) / (2 * a))} and Negative: {((-b - value) / (2 * a))}")
    elif discriminant < 0:
        print(f"Root Are Imagery\nSolution: {(-b / (2 * a))} + {math.sqrt(abs(discriminant))} i")


ans = input("1.Coefficient\n2.Equation\nEnter the Entry method: ")
if ans == "1":
    a1 = float(input())
    b1 = float(input())
    c1 = float(input())
    if a1 == 0:
        print("No Solution")
    else:
        Solve(a1, b1, c1)
elif ans == "2":
    try:
        print("Give Input In 1x^2-1x-1")
        x = input()
        x1 = re.findall(r"\d", x)
        x2 = re.findall(r"\W", x)
        if (x1[1] != "2") or (x2[0] != "^"):
            print("Invalid Input")
        else:
            a1 = x1[0]
            b1 = x2[1] + x1[2]
            c1 = x2[2] + x1[3]
            if a1 == 0:
                print("No Solution")
            else:
                Solve(int(a1), int(b1), int(c1))
    except Exception as r:
        print(r)
