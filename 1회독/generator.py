# 입력한 두 정수 사이에 있는 소수를 생성하는 제너레이터

def prime_number_generator(start, stop):
    for num in range(start + 1, stop):
        isPrime = True
        for n in range(2, num):
            if num % n == 0:
                isPrime = False
                break
        if isPrime:
            yield num

start, stop = map(int, input().split())

g = prime_number_generator(start, stop)
print(type(g))

for i in g:
    print(i, end=' ')
