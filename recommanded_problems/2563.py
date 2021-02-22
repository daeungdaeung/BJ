brd = [[0 for _ in range(100)] for __ in range(100)]

for c_p in range(int(input())):
    # c는 왼벽과의 거리 -> column index로 활용
    # r은 아래벽과의 거리 -> row index로 활용
    c_idx, r_idx = map(int, input().split())
    c_idx -= 1
    r_idx -= 1
    # 도화지의 row 방향으로 순회하면서 column 방향으로 10개씩 색칠
    # 색종이의 세로 길이는 10으로 고정
    for r in range(10):
        # 색종이의 가로 길이도 10으로 고정
        brd[r_idx+r][c_idx:c_idx+10] = [1] * 10

# 색칠된 곳 개수 세기
cnt = 0
for i in range(100):
    for j in range(100):
        if brd[i][j] == 1:
            cnt += 1

print(cnt)