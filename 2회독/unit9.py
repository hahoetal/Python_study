# Unit9_문자열 사용하기

# 연습문제: 여러 줄로 된 문자열 사용하기(practice_multiline_string.py)
# 실행 결과
# Python is a programming language that lets you work quickly
# and
# intergrate systems more effectively.

s = '''Python is a programming language that lets you work quickly
and
intergrate systems more effectively.''' # """문자열"""

print(s)

# 심사문제: 여러 줄로 된 문자열 사용하기(judge_multiline_string.py)
# 표준 출력
# 'Python' is a "programming language"
# that lets you work quickly
# and
# intergrate systems more effectively.

s = ''''Python' is a "programming language"
that lets you work quickly
and
intergrate systems more effectively.''' # """문자열""" 여러 줄로 된 문장이 아니라면, 작은 따옴표나 큰 따옴표로 문자열을 감싸고 앞에 \ 붙이기.

print(s)