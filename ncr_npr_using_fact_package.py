Create a package(folder)  for factorial.
def factorial(n):
    fact = 1
    if n < 0:
        return "Factorial not possible"
    for i in range(1, n + 1):
        fact = fact * i
    return fact
Create a package(folder)  for combination
from factorial.factorial import factorial
def ncr(n, r):
    result = factorial(n) / (factorial(r) * factorial(n-r))
    return result
def npr(n, r):
    result = factorial(n) / factorial(n-r)
    return result
Main Program to use package factorial and combination # main.py
from combination.combin import ncr, npr
n = int(input("Enter n value: "))
r = int(input("Enter r value: "))
print("nCr =", ncr(n, r))
print("nPr =", npr(n, r))
