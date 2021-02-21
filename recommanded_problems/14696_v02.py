def who_win(c1, c2):
    for x in range(3, -1, -1):
        # 카운트 함수 사용 x
        if c1[x] > c2[x]:
            return 'A'
        elif c1[x] < c2[x]:
            return 'B'
        else:
            pass
    return 'D'

N = int(input())
for turn in range(N):
    tmp1 = list(map(int, input().split()))
    tmp2 = list(map(int, input().split()))
    n1, child1 = tmp1[0], tmp1[1:]
    n2, child2 = tmp2[0], tmp2[1:]
    # 딱지에 적힌 그림의 각 개수를 아래 변수에 저장할거다.
    # 0번째 인덱스는 활용 안할거다.
    p1 = [0]*5
    p2 = [0]*5
    # 첫번째 아이의 딱지부터
    for i in range(n1):
        # child1[i]는 딱지에 적힌 모양이 나온다.
        # 모양에서 1을 뺀 인덱스를 활용
        p1[child1[i]] += 1
    # 두번째 아이의 딱지
    for i in range(n2):
        p2[child2[i]] += 1

    print(who_win(p1[1:], p2[1:]))