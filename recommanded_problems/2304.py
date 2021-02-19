def find_max_pillar(pillars):
    max_h = 0
    max_idx = -1
    for i in range(len(pillars)):
        if max_h < pillars[i][1]:
            max_h = pillars[i][1]
            max_idx = i
    return max_idx


N = int(input())

pillars = []
for i in range(N):
    L, H = map(int, input().split())
    pillars.append((L, H))

pillars = sorted(pillars)
max_idx = find_max_pillar(pillars)
area = pillars[max_idx][1]
# 가장 큰 기둥의 왼쪽 영역 넓이 구하기
l = max_idx
while l > 0:
    n_l = find_max_pillar(pillars[:l])
    area += (pillars[l][0] - pillars[n_l][0]) * pillars[n_l][1]
    l = n_l

# 가장 큰 기둥의 오른쪽 영역 넓이 구하기
r = max_idx + 1
while True:
    n_r = find_max_pillar(pillars[r:])
    area += (pillars[r + n_r][0] - pillars[r-1][0]) * pillars[r + n_r][1]
    r += n_r + 1

    if r > len(pillars)-1:
        break
print(area)