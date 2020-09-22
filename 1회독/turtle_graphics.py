import turtle as t # turtle 모듈 가져오기
t.shape('turtle') # 거북이 모양이 나타나도록 설정

# 거북이 속도 -> t.speed(숫자 또는 문자열), 숫자는 0.5 ~ 10 숫자가 작을수록 빠름, 문자열은 fastest, fast, normal, slow, slowest

# 사각형

t.forward(100) # 앞으로 100픽셀만큼 이동
t.right(90) # 오른쪽으로 90도 회전
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)

# 오각형
for i in range(5):
    t.left((360 / 5) * 2)
    t.forward(100)
    t.right(360 / 5)

# 다각형 그리기
# 다각형에서 외각의 합은 항상 360도...

num = int(input('정수 입력 : '))

t.color('orange') # 펜의 색 설정
t.begin_fill() # 색칠할 준비

# 다각형을 그리고
for i in range(num):
    t.forward(100)
    t.left(360 / num) # 360을 num으로 나눈 각도만큼 왼쪽으로 회전하면서..

t.end_fill() # 현재 지정된 색으로 도형 색칠하기

# 원 그리기
t.color('green')
t.begin_fill()
t.circle(50) # 반지름이 50인 원 그리기
t.end_fill()

# 별
for i in range(5):
    t.forward(80)
    t.right((360 / 5) * 2)
    t.forward(80)
    t.left(360 / 5)

# 꼭짓점과 길이를 입력받아 별을 그려주는 코드
dot, line = map(int, input('별의 꼭짓점과 길이 : ').split())

if 5 <= dot <= 10 and 50 <= line <=100:
    for i in range(dot):
        t.forward(line)
        t.right((360 / dot) * 2)
        t.forward(line)
        t.left(360 / dot)
else:
    print('잘못된 값입니다.')

input() # 안 적어주면 모듈이 켜졌다가 바로 껴짐!! python ide을 사용하지 않는 경우 꼭 쓰기
# t.mainloop()