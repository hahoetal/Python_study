def fibo(num):
    if num < 3:
        return 1
    return fibo(num - 1) + fibo(num - 2)

n = int(input())
print(fibo(n))
