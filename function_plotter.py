
import numpy as np
import matplotlib.pyplot as plt


def number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a number.")


def roots(a, b, c):
    if a == 0:
        if b != 0:
            return [-c / b]
        else:
            return []
    d = b**2 - 4*a*c
    if d > 0:
        r1 = (-b + np.sqrt(d)) / (2*a)
        r2 = (-b - np.sqrt(d)) / (2*a)
        return [r1, r2]
    elif d == 0:
        return [-b / (2*a)]
    else:
        return []


a = number("Enter a: ")
b = number("Enter b: ")
c = number("Enter c: ")

if a == 0 and b == 0 and c == 0:
    print("Every x is a solution.")
    raise SystemExit

result = roots(a, b, c)

vertex = -b / (2*a) if a != 0 else 0
points = result + [vertex]
x_min = min(points) - 5
x_max = max(points) + 5

x = np.linspace(x_min, x_max, 200)
y = a * x**2 + b * x + c

plt.figure("Graph of a function")
plt.title(f"f(x) = {a:g}x^2 {b:+g}x {c:+g}")
plt.grid(True)
plt.axhline(0, color="black")
plt.axvline(0, color="black")
plt.xlabel("x")
plt.ylabel("y")
plt.plot(x, y)

if result:
    plt.scatter(result, [0] * len(result), color="red", zorder=5)
    print([float(r) for r in result])
else:
    print("There are no real roots.")

plt.show()