# 1부터 100까지의 수 중 3의 배수면 Fizz, 5의 배수면 Buzz, 3과 5의 공배수면 FizzBuzz를 출력하는 프로그램

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0: # 3과 5의 공배수, 조건문 중 가장 위에 위치, 그렇지 않으면 공배수일 때, 'FizzBuzz'가 출력 안 됨.
        print('FizzBuzz')
    elif i % 3 == 0: # 3의 배수
        print('Fizz')
    elif i % 5 == 0: # 5의 배수
        print('Buzz')
    else: # 3 또는 5의 배수가 아닌 경우
        print(i)

# 문자열의 특징을 이용해서 한 줄로 작성하면....

for i in range(1, 101):
    print('Fizz' * (i % 3 == 0) + 'Buzz' or i)

# 문자열의 곱셈(문자열 * 정수) -> 정수만큼 반복
# True는 1 False는 0
# 문자열 * 0은 아무 것도 출력하지 않음

# 문자열의 덧셈(문자열 + 문자열) -> 앞 문자열의 끝에 뒷 문자열을 가져다 붙임

# 3의 배수도 5의 배수도 아닌 경우에는 숫자를 출력해야 함... 그래서 논리 연산자 or을 이용

# 정수 두 개를 입력하면 두 정수 사이에 있는 5의 배수는 'Fizz' 7의 배수는 'Buzz' 공배수 'FizzBuzz'를 출력하는 프로그램
# 첫 번째 정수는 1부터 1000까지, 두 번째 정수는 10부터 1000까지, 항상 두 번째 정수가 큼

num1, num2 = map(int, input('정수를 두 개 입력해주세요 : ').split())

if 1 <= num1 <= 1000 and 10 <= num2 <= 1000 and num1 < num2:
    for i in range(num1, num2):
        if i % 5 == 0 and i % 7 == 0:
            print('FizzBuzz')
        elif i % 5 == 0:
            print('Fizz')
        elif i % 7 == 0:
            print('Buzz')
        else:
            print(i)
else:
    print('잘못된 숫자를 입력했습니다.')

# 위의 코드를 단축해서 작성해보기~

n1, n2 = map(int, input('정수 두 개 : ').split())

if 1 <= n1 <= 1000 and 10 <= n2 <= 1000 and n1 < n2:
    for i in range(n1, n2):
        print('Fizz' * (i % 5 == 0) + 'Buzz' * (i % 7 == 0) or i)