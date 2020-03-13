# 함수가 호출될 때마다 1씩 감소

def countdown(n):
    number = n + 1 # 입력받은 숫자부터 시작해 값이 1씩 감소해야 하니까 1을 더함.
    def count():
        nonlocal number # countdown 함수의 지역변수 number 값을 변경할 수 있도록 만들어줌.
        number -= 1
        return number
    return count # 함수를 반환할 때는 이름만 반환

n = int(input())

c = countdown(n) # 여기서 c는 클로저 함수 / 함수 count를 둘러싼 환경(지역변수, 코드 등)을 유지하고 있다가 함수가 호출될 때 꺼내서 사용!
for i in range(n):
    print(c(), end=' ')