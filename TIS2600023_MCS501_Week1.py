"""
MCS501 Programming Principles
Week 1 Tutorial Activities
"""


# Tutorial 1a - Task 3
print("1. 4 ** 2 =", 4 ** 2)
print("2. 8 * 5 =", 8 * 5)
print("3. 18 / 12 =", 18 / 12)
print("4. 12 / 18 =", 12 / 18)
print("5. 18 // 12 =", 18 // 12)
print("6. 12 // 18 =", 12 // 18)
print("7. 9 % 2 =", 9 % 2)
print("8. 12 % 5 =", 12 % 5)


# Tutorial 1a - Task 4
expression_1 = (3 + 7) / (5 % 3)
expression_2 = 5 * 9 ** (1 / 2) // (3 * 2)
expression_3 = 4 / (3 * (3 - 1))

print("\nOperator precedence results:")
print("Expression 1:", expression_1)
print("Expression 2:", expression_2)
print("Expression 3:", expression_3)


# Tutorial 1b - Task 1
x = 10
y = 5
z = 0

boolean_result = (x > y) and not (z == 0) or (y < x and z != 1)
print("\nBoolean result:", boolean_result)


# Tutorial 1b - Task 2
full_name = input("\nEnter your full name: ")
age = int(input("Enter your age: "))
years_until_100 = 100 - age

print(f"Hello, {full_name}!")
print(f"You will turn 100 in {years_until_100} years.")


# Tutorial 1b - Task 3
celsius = float(input("\nEnter the temperature in Celsius: "))
fahrenheit = (celsius * 9 / 5) + 32

print(f"{celsius:.2f}°C is equal to {fahrenheit:.2f}°F.")


# Tutorial 1b - Task 4
import math

radius = 7
circle_area = math.pi * radius ** 2
logarithm = math.log10(1000)
rounded_pi = round(math.pi, 3)

print(f"\nArea of the circle: {circle_area:.2f}")
print("Log base 10 of 1000:", logarithm)
print("Pi rounded to three decimal places:", rounded_pi)


# Tutorial 1b - Task 5
num = "10"
total = int(num) + 5

print("\nTotal:", total)