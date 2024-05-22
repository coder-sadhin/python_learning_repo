def fac(n):
    if n <= 1:  # Base case: n is 0 or 1
        return 1
    return n * fac(n - 1)

n = int(input())
factorial = fac(n)
print(factorial)