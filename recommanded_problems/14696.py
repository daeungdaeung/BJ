def who_win(c1, c2):
    for x in range(4, 0, -1):
        # 만약 카운트 함수를 쓸 수 없다면
        # 딕셔너리를 활용하면 된다.
        s1 = c1.count(x)
        s2 = c2.count(x)
        if s1 > s2:
            return 'A'
        elif s1 < s2:
            return 'B'
        else:
            pass
    return 'D'

N = int(input())
for turn in range(N):
    child1 = list(map(int, input().split()))[1:]
    child2 = list(map(int, input().split()))[1:]

    print(who_win(child1, child2))