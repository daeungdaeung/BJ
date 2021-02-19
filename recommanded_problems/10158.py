w, h = map(int, input().split())
x, y = map(int, input().split())
cnt = int(input())

dx = [1, -1]
dx_idx = 0
dy = [1, -1]
dy_idx = 0

while cnt > 0:
    # 개미가 왼벽을 넘어가려하거나 오른벽을 넘어가려하면
    # dx_idx를 변경하여 방향을 바꿔준다.
    # 예를 들면
    # 왼벽을 넘어가려하면 delta x의 값을 1로 변경
    # 오른벽을 넘어가려하면 delta x의 값을 -1로 변경
    if x + dx[dx_idx] > w or x + dx[dx_idx] < 0:
        dx_idx = (dx_idx + 1) % 2
    # 개미가 윗벽과 아랫벽을 넘어가지 않도록
    # x와 유사하게 처리해준다.
    if y + dy[dy_idx] > h or y + dy[dy_idx] < 0:
        dy_idx = (dy_idx + 1) % 2
    x += dx[dx_idx]
    y += dy[dy_idx]

    cnt -= 1
print(x, y)