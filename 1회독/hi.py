# class Student:
#     def __init__(self, name, num):
#         self.name = name
#         self.num = num

#     def hello(self):
#         print("안녕 나는 " + self.name + "학번은 " + self.num + " 이야")

# s = Student("영은", "20170669")
# s.hello()


# class Calculate:
#     def __init__ (self, a, b):
#         self.a = a
#         self.b = b

#     def sum(self):
#         print(self.a + self.b)


# print("숫자를 입력해주세요")

# a,b = map(int, input().split())
# c = Calculate(a,b)
# c.sum()

# def addNum(n1, n2):
#     return n1 + n2

# try:
#     print(addNum(2, 'n'))
# except TypeError:
#     print("오류")

# lst = [0,1,0,1,1,0,1,0]

# to_dic = {}

# for i in lst:
#     try:
#         to_dic[i] += 1
#     except KeyError:
#         to_dic[0] = 0
#         to_dic[1] = 0
        
# print(to_dic)

p = "python"
print(f'hello,{p}') # {} 안에는 변수가 들어가야 함.

print('hello,{0}'.format('python'))