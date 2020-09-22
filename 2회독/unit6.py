# Unit_변수와 입력 사용하기

# 연습문제: 정수 세 개를 입력받고 합계 출력하기(practice_input_split.py)
a, b, c = map(int, input('정수 세 개를 입력해주세요: ').split())
print(a + b + c)

# 심사문제: 변수 만들기(judge_variable.py)
# 50, 100, None이 출력되도록 만들기
a = 50
b = 100
c = None

print(a)
print(b)
print(c)

# 심사문제: 평균 점수 구하기(judge_average.py)
# 정수로 출력.
# 표준 입력: 32 53 22 95
# 표준 출력: 50
korean, english, math, science = map(int, input().split())
print((korean + english + math + science) // 4)
