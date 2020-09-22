# 지뢰 찾기

# 크기 입력
row, col = map(int, input('가로 세로 길이 입력 : ').split())

# 빈 리스트 생성
matrix = []

# 사용자가 입력한 문자를 2차원 리스트로 만듦
print("'*' 또는 '.'을 입력한 가로, 세로 길이만큼 입력해주세요.")
for r in range(row):
    matrix.append(list(input()))
    
print()

# 입력한 가로 길이만큼의 리스트를 원래 리스트의 위와 아래에 추가
matrix.insert(0, ['.'] * row)
matrix.insert(len(matrix), ['.'] * row)

# 안쪽 리스트의 맨 앞과 끝에 요소를 하나씩 추가
for m in matrix:
    m.insert(0, '.')
    m.insert(len(matrix), '.')

# 결과를 담을 리스트(지뢰가 있는 곳은 '*', 지뢰가 없는 곳은 주변에 있는 지뢰 개수 출력)
result = []

for i in range(1, row + 1):
    resultCount = [] # 주변에 있는 지뢰 개수를 찾아서 추가하기 위한 리스트

    for j in range(1, col + 1): # 사용자가 입력한 문자가 담긴 2차원 리스트 중 한 요소를 찍고
        if matrix[i][j] == '.': # 지뢰가 없으면 
            count = 0

            for k in range(i - 1, i + 2):

                for z in range(j - 1, j + 2): # 찍은 리스트 요소 중 하나의 주변 요소들을 반복하면서
                    if matrix[k][z] == '*': # 지뢰가 발견되면
                        count += 1 # count 값을 하나 올리기

            resultCount.append(count) # 주변에 있는 지뢰 개수를 리스트에 추가 

        else: # 지뢰가 아니면
            resultCount.append('*') # '*'을 추가하고
    result.append(resultCount) # 주변 지뢰 개수 또는 '*'로 이루어진 리스트를 결과 리스트에 추가

# 결과 출력하기
for r in range(len(result)):
    for c in range(len(result[r])):
        print(result[r][c], end='')
    print()