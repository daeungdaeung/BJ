def chk_bingo(brd, brd_t):
    bingo = 0
    # 가로로 빙고인지 검사
    for i in range(5):
        if sum(brd[i]) == 0:
            bingo += 1
    # 세로 빙고인지 검사
    for i in range(5):
        if sum(brd_t[i]) == 0:
            bingo += 1
    # left-top, right-bottom 대각선 검사
    tmp = 0
    for i in range(5):
        tmp += brd[i][i]
    if tmp == 0:
        bingo += 1
    # left-bottom, right-top 대각선 검사
    tmp = 0
    for i in range(5):
        tmp += brd[i][4-i]
    if tmp == 0:
        bingo += 1

    if bingo >= 3:
        return True
    return False

brd = [list(map(int, input().split())) for _ in range(5)]
# 빙고판을 transpose
# 그러면 세로를 검사하는데, 가로에 사용했던 방법을 사용할 수 있음
brd_t = []
for i in range(5):
    tmp = []
    for j in range(5):
        tmp.append(brd[j][i])
    brd_t.append(tmp)
# 사회자가 숫자를 불렀을 때, 빙고판을 매번 검색하기보다는
# 딕셔너리로 저장해서 해당 위치를 불러내자.
brd_dict = {}
for i in range(5):
    for j in range(5):
        brd_dict[brd[i][j]] = (i, j)

mc = []
for i in range(5):
    mc += list(map(int, input().split()))
# 몇개 이상 부르면 빙고가 나올 수 있을까?
# -> 직선의 특성상, 직선이 3개일때 최대로 가질 수 있는 교점의 개수는 3
# 따라서, 빙고는 사회자가 최소 12개 이상 불렀을때 가능
for i in range(25):
    r, c = brd_dict[mc[i]]
    # 빙고판과 transpose된 빙고판 모두 0으로 체크
    brd[r][c] = 0
    brd_t[c][r] = 0
    if i >= 11:
        if chk_bingo(brd, brd_t):
            break
print(i+1)