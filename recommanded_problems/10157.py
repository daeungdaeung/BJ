def find_next_position(r, c, direction_idx, C, R, arr, result):
    # 방향: 상->우->하->좌
    dxy = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    # 출력 좌표를 위한 방향값
    d_result = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    n_r = r + dxy[direction_idx][0]
    n_c = c + dxy[direction_idx][1]
    n_r_l = result[0] + d_result[direction_idx][0]
    n_r_r = result[1] + d_result[direction_idx][1]
    n_result = [n_r_l, n_r_r]
    # x는 row, y는 column 의
    if n_r < 0 or n_r >= R or n_c < 0 or n_c >= C or arr[n_r][n_c] != 0:
        direction_idx = (direction_idx + 1) % 4
        n_r = r + dxy[direction_idx][0]
        n_c = c + dxy[direction_idx][1]
        n_r_l = result[0] + d_result[direction_idx][0]
        n_r_r = result[1] + d_result[direction_idx][1]
        n_result = [n_r_l, n_r_r]
    return n_r, n_c, direction_idx, n_result


# C는 column 개수
# R은 row 개수
C, R = map(int, input().split())
K = int(input())

if K > C*R:
    print('0')
else:
    # 모든 좌석을 0으로 초기화
    arr = [[0 for i in range(C)] for j in range(R)]
    # 시작은 무조건 좌측 하단
    # r, c 는 각각 row, column을 의
    r, c = R-1, 0
    # result는 나중에 반환할 좌표값이다.
    result = [1, 1]
    direction_idx = 0
    # K에 도달할때까지 좌석 채우기
    seat = 1
    while seat < K:
        # 현재 위치에 관객을 배정
        arr[r][c] = seat
        r, c, direction_idx, result = find_next_position(r, c, direction_idx, C, R, arr, result)
        seat += 1
    # 위에서 종료되면 x, y는 K가 들어가야할 위치 값을 가진다.
    # x, y는 python list index이므로 정답으로 요구하는
    # 값으로 변경해야한다.
    # 계산으로 해결하려 했으나, 그냥 처음부터 더해가면서 찾는게
    # 조금 더 쉬울것 같아서...
    print(*result)