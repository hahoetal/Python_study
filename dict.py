# 딕셔너리 표현법

keys = input().split()
values = map(int, input().split())

x = dict(zip(keys, values))

x = {k:v for k, v in x.items() if v != 30}
del x['delta']

print(x)