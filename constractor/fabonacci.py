def fabonacci(n):
    if n <= 1:  # Base case: n is 0 or 1
        return 1
    return(fabonacci(n-1) + fabonacci(n-2))

n = int(input())
fabonaci = fabonacci(n)
print(fabonaci)