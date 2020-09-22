# 지뢰 찾기_ 수정

row, col = map(int, input().split()) # 가로와 세로 길이 입력

matrix = [] # 빈 리스트를 만들고

# 2차원 리스트 만들기
for r in range(row):
    matrix.append(list(input())) # 사용자가 입력한 값을 리스트로 만든 다음에 matrix에 추가

# 지뢰가 아닌 곳에 0을 집어넣기
for i in range(row):
    for j in range(col):
        if matrix[i][j] == '*': # '*'이면 넘어가고
            continue
        
        matrix[i][j] = 0 # 아니면 0을 대입
    
        # 주변에 있는 지뢰 찾기
        for x in range(i - 1, i + 2):
            for y in range(j - 1, j + 2):
                if x < 0 or y < 0 or x >= row or y >= col: 
                    continue # x 또는 y 값이 인덱스 범위를 벗어나면 넘어가고

                if matrix[x][y] == '*': # '*'을 발견하면
                    matrix[i][j] += 1 # 1 더하기

# 결과 출력
for r in range(row):
    for c in range(col):
        print(matrix[r][c], end='')
    print()