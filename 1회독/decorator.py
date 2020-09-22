# 데코레이터_html 태그 이름을 입력하면 문자열에 해당 태그를 붙어서 출력
def html_tag(tag_name):
    def real_decorator(func):
        def wrapper():
            html = '<{0}>{1}</{0}>'.format(tag_name, func())
            return html
        return wrapper
    return real_decorator

a, b = input().split()

@html_tag(a)
@html_tag(b)
def hello():
    return 'Hello, world'

print(hello())