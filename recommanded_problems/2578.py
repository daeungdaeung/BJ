def find_num(num, bingo_map, mapping):
    i, j = mapping[num]
    # 사회자가 부른 숫자를 찾아서
    # 빙고판에 표시
    # 나는 0으로 표시함
    bingo_map[i][j] = 0
    return bingo_map

def chk_bingo(bingo_map):
    bingo = 0
    # 가로가 빙고인지 검사
    for row in bingo_map:
        if [0, 0, 0, 0, 0] == row:
            bingo += 1
        if bingo == 3:
            return True
    # 세로가 빙고인지 검사
    for col in range(5):
        total = 0
        for row in range(5):
            total += bingo_map[row][col]
        if total == 0:
            bingo += 1
        if bingo == 3:
            return True

    # 우하향 대각선이 빙고인지 검사
    total = 0
    for x in range(5):
        total += bingo_map[x][x]
    if total == 0:
        bingo += 1
    if bingo == 3:
        return True
    # 우상향 대각선이 빙고인지 검
    total = 0
    for x in range(5):
        total += bingo_map[x][4-x]
    if total == 0:
        bingo += 1
    if bingo == 3:
        return True
    return False


bingo_map = [list(map(int, input().split())) for i in range(5)]
mc = []
# 각 값이 빙고판 어디에 존재하는지 저장
# 이렇게 하면 빠르게 빙고판에 동그라미 칠 수 있다.
mapping = {}
for i in range(5):
    for j in range(5):
        mapping[bingo_map[i][j]] = (i, j)

for i in range(5):
    mc.extend(list(map(int, input().split())))

# 빙고판에 동그라미를 그리면서 빙고를 외쳐보자
for idx, num in enumerate(mc):
    bingo_map = find_num(num, bingo_map, mapping)
    if chk_bingo(bingo_map):
        break
print(idx+1)
