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

# 마름모

for i in range(num // 2):
    for j in range(num):
        if j < (num // 2) - i:
            print(' ', end='')
        elif j > (num // 2) + i:
            print(' ', end='')
        else:
            print('*', end='')
    print()
    
for i in range(num - (num // 2)):
    for j in range(num):
        if j < i:
            print(' ', end='')
        elif j >= num - i:
            print(' ', end='')
        else:
            print('*', end='')
    print()