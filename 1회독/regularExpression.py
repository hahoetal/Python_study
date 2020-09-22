# 정규표현식_입력받은 url이 올바른지 판단하기

# http:// 또는 https://로 시작
# 도메인은 도메인.최상위 도메인 형식, 영문 대소문자, 숫자 -로 구성
# 도메인 이하 경로는 /로 구분, 영문 대소문자, 숫자, -, _, ., ?, =을 사용
# ex) http://www.exaple.com/hello/world.do?key=python

import re # 정규표현식은 re 모듈을 사용

url = input()
m = re.match('^https?://[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+/[a-zA-Z0-9-_.?=]*',url)

# ^https? => http 또는 https로 시작하는지.
# ^문자열은 해당 문자열이 맨 앞에 오는지 판단
# 문자? 문자가 0개 또는 1개인지 판단

# [a-zA-Z0-9-]+ => 영문 대소문자, 숫자, -을 1개 이상 포함하는지.
# [범위]로 포함할 범위를 지정 / 범위는 0-9 또는 a-z 처럼 시작-끝
# +는 해당 범위의 문자가 1개 이상 있는지 판단
# *는 문자가 0개 이사아 있는지 판단

if m != None:
    print(True)
else:
    print(False)
