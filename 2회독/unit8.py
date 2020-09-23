# Unit8_불과 비교, 논리 연산자 알아보기

# 연습문제: 합격 여부 출력하기(practice_operator.py)
korean = 92
english = 47
mathematics = 86
science = 81

print(korean >= 50 and english >= 50 and mathematics >= 50 and science >= 50)

# 심사문제: 합격 여부 출력하기(judge_comparison_logical_operator.py)
# 표준 입력: 90 80 85 80
# 표준 출력: False

korean, english, mathematics, science = map(int, input().split())
print(korean >= 90, english > 80, mathematics > 85, science >=80)