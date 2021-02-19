w, h = map(int, input().split())
x, y = map(int, input().split())
cnt = int(input())

# 가로로 왔다갔다 반복하면 제자리 -> 세로도 마찬가
cnt_x = cnt % (2*w)
cnt_y = cnt % (2*h)

dx = [1, -1]
dx_idx = 0
dy = [1, -1]
dy_idx = 0

# 가로로 왔다갔다하다가 어디에 멈출까?
while cnt_x > 0:
    # 왼벽 또는 오른쪽 벽을 만나면 진행방향을 바꾼다.
    if x + dx[dx_idx] > w or x + dx[dx_idx] < 0:
        dx_idx = (dx_idx + 1) % 2
    x += dx[dx_idx]
    cnt_x -= 1
# 세로로 왔다갔다가 어디에 멈출까?
while cnt_y > 0:
    if y + dy[dy_idx] > h or y + dy[dy_idx] < 0:
        dy_idx = (dy_idx + 1) % 2
    y += dy[dy_idx]
    cnt_y -= 1

print(x, y)