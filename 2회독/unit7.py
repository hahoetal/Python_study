# Unit7_출력 방법 알아보기

# 연습문제: 날짜와 시간 출력하기(practice_print.py)
# 실행 결과: 2000/10/27 11:43:59
year = 2000
month = 10
day = 27
hour = 11
minute = 43
second = 59

print(year, month, day, sep='/', end=' ')
print(hour, minute, second, sep=':')

# 심사문제: 날짜와 시간 출력하기(judge_print.py)
# 표준 입력: 2017 10 27 11 43 59
# 표준 출력: 2017-10-27T11:43:59

year, month, day, hour, minute, second = input().split()
print(year, month, day, sep='-', end='T')
print(hour, minute, second, sep=':')