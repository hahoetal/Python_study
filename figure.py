num = int(input('세로 길이 : '))
print()

# 사각형
for i in range(num):
    for j in range(num):
        print('*', end='')
    print()
    
print()

# 직각 삼각형
for i in range(num):
    for j in range(num):
        if j <= i:
            print('*', end='')
        else:
            print(' ', end='')
    print()

print()

# 뒤집어진 직각 삼각형
for i in range(num):
    for j in range(num):
        if i <= j:
            print('*', end='')
        else:
            print(' ', end='')
    print()

print()

#for i in range(num):
#    for j in range(num):
#        if j < i:
#            print(' ', end='')
#        else:
#            print('*', end='')
#    print()

# 사다리꼴

for i in range(num):
    for j in range(2 * num - 1):
        if j < (num - 1) - i:
            print(' ', end='')
        else:
            print('*', end='')
    print()
    
print()

# 이등변 삼각형

for i in range(num):
    for j in range(2 * num - 1):
        if j < (num - 1) - i:
            print(' ', end='')
        elif j >= (num + i):
            print(' ', end='')
        else:
            print('*', end='')
    print()
print()

# 마름모(홀수만)
# 위에 산 모양, 아래 역삼각형으로 두 개로 쪼개서 만들어 봄.


for i in range(num // 2):
    for j in range(num):
        if j < (num // 2) - i:
            print(' ', end='')
        elif j > (num // 2) + i:
            print(' ', end='')
        else:
            print('*', end='')
    print() # 산 모양
    
for i in range(num - (num // 2)):
    for j in range(num):
        if j < i:
            print(' ', end='')
        elif j >= num - i:
            print(' ', end='')
        else:
            print('*', end='')
    print() # 역삼각형
print()

# 하트
h = num
w = num + 2

for i in range(w):
    if i == 0: 
        print(' ', end='')
    elif i == (w // 2) - 1:
        print(' ', end='')
    elif i == w // 2:
        print(' ', end='')
    elif i == (w // 2) + 1:
        print(' ', end='')
    elif i == w - 1:
        print(' ', end='')
    else:
        print('*', end='')
print()

for i in range(w):
    if i == w // 2:
        print(' ', end='')
    else:
        print('*', end='')
print()   

for i in range(h - 2):
    for j in range(w):
        if j < i:
            print(' ', end='')
        elif j >= w - i:
            print(' ', end='')
        else:
            print('*', end='')
    print()
print()
