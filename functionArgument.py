korean, english, mathmatics, science = map(int, input().split())

def get_min_max_score(*args): # args는 튜플, 가변 인수 함수 + 위치 인수
    return min(args), max(args)

def get_average(**kwargs): # kwargs는 딕셔너리, 가변 인수 함수 + 키워드 인수
    hap = 0
    for s in kwargs.values():
        hap += s
    return hap / len(kwargs)

min_score, max_score = get_min_max_score(korean, english, mathmatics, science)
average_score = get_average(korean=korean, english=english, mathmatics=mathmatics, science=science)
print('낮은 점수 : {0:.2f}, 높은 점수 : {1:.2f}, 평균 점수 : {2:.2f}'.format(min_score, max_score, average_score))

min_score, max_score = get_min_max_score(english, science)
average_score = get_average(english=english, science=science)
print('낮은 점수 : {0:.2f}, 높은 점수 : {1:.2f}, 평균 점수 : {2:.2f}'.format(min_score, max_score, average_score))
