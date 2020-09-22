# 'c'가 들어간 단어 찾기

with open ('word.txt', 'r') as file:
    word = file.read()
    words = word.split()

    for w in words:
        if w.find('c') != -1:
            print(w.strip(',.'))