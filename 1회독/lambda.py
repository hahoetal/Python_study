files = input().split()

print(list(map(lambda f : '{0:03d}{1}'.format(int(f[:f.find('.')]),f[f.find('.'):]), files))) # 내가 작성

print(list(map(lambda f: '{0:03d}.{1}'.format(int(f.split('.')[0]),f.split('.')[1]),files))) # 코드 검사 후 받은 코드