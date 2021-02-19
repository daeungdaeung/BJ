def fn(top, dice):
    # 주사위 주위를 보면서 아래 주사위의 윗면과
    # 동일한 값을 찾아야한다.
    for i in range(3):
        for j in range(2):
            if top == dice[i][j]:
                bot_idx = i
                # 아래 주사위의 윗면과 동일한 값을 찾았을 때
                # 지금 이 주사위의 윗면은
                # 윗면과 동일한 값의 pair이다.
                if j == 0:
                    n_top = dice[i][1]
                else:
                    n_top = dice[i][0]
    # 위에서 위 아래면을 찾았으니
    # 옆면을 순회하면서 최대값을 찾아야한다.
    max_side = 0
    for i in range(3):
        if i != bot_idx:
            for j in range(2):
                if max_side < dice[i][j]:
                    max_side = dice[i][j]
    # 다음 주사위에게 알려줄 지금 현재 주사위의
    # 윗면과, 옆면들 중에서의 최대값을 반환
    return n_top, max_side

n = int(input())
dices = []
for i in range(n):
    a, b, c, d, e, f = map(int, input().split())
    # 주사위 위-아래 면을 짝지어 저장
    dices.append([(a, f), (b, d), (c, e)])

# 첫번째 주사위의 윗면을 결정하자.
# 만약 첫번째 주사위의 윗면을 고정하면,
# 그 이후로는 모든 주사위의 위 아랫면이 고정된다.
# 따라서, 모든 경우의 수는 첫번째 주사위의 윗면이 가질 수 있는
# 6가지이다.
max_v = 0
for i in range(3):
    for j in range(2):
        total = 0
        # 첫번째 주사위의 윗면 선택
        top = dices[0][i][j]
        # 첫번째 주사위의 사이드 중에서 최대값 찾기
        for i1 in range(3):
            if i1 != i:
                for j1 in range(2):
                    if total < dices[0][i1][j1]:
                        total = dices[0][i1][j1]
        # 두번째 주사위부터 순회하면서
        # 최대값을 찾아보자.
        for k in range(1, n):
            top, max_side = fn(top, dices[k])
            total += max_side
        if max_v < total:
            max_v = total
print(max_v)