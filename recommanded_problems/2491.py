N = int(input())
numbers = list(map(int, input().split()))
# 수열의 길이가 1인경우에는 무조건 최대길이는 1이다.
if N == 1:
    max_l = 1
else:
    max_l = 0
    # 배열의 원소가 증가하거나 같은 구간의 최대 길이 찾기
    cnt = 1
    # 원래 배열에 -1을 추가함으로써
    # 원래 배열의 마지막 원소가 증가인 경우도 카운트할 수 있다.
    numbers_p = numbers[:] + [-1]
    for i in range(N):
        if numbers_p[i] <= numbers_p[i+1]:
            cnt += 1
        else:
            if max_l < cnt:
                max_l = cnt
            cnt = 1
    # 배열의 원소가 감소하거나 같은 구간의 최대길이 찾기
    cnt = 1
    # 원래 배열에 10을 추가함으로써
    # 원래 배열의 마지막 원소가 감소인 경우도 카운트할 수 있다.
    numbers_n = numbers[:] + [10]
    for i in range(N):
        if numbers_n[i] >= numbers_n[i+1]:
            cnt += 1
        else:
            if max_l < cnt:
                max_l = cnt
            cnt = 1

print(max_l)