# 회문 찾기

with open ("words.txt", 'r') as file:
    words = file.readlines()

    for w in words:
        word = w.strip('\n')        
        if word == word[::-1]:
            print(word.strip('\n'))