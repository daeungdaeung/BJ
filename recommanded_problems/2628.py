# hor: 종이의 가로 길이
# ver: 종이의 세로 길이
w, h = map(int, input().split())
n = int(input())

# d_w: 종이를 가로 방향으로 몇번째에서 자르는지 저장
d_w = []
d_h = []
for _ in range(n):
    d, num = map(int, input().split())
    if d == 0:
        d_w.append(num)
    else:
        d_h.append(num)

d_w = sorted(d_w)
d_h = sorted(d_h)

# 가로 방향으로 자르기
rep = 0
result_w = []
# 잘랐을 때 나누어진 길이가 발생
# 그 길이를 저장
for i in range(len(d_w)):
    result_w.append(d_w[i] - rep)
    rep = d_w[i]
# 두번을 자르면 총 세개의 종이가 생성됨
# 따라서 마지막에 발생한 종이를 추가해줌
# 전체 길이는 height이므로 h에서 빼줘야함
result_w.append(h - rep)

# 세로 방향으로 자르기
rep = 0
result_h = []
for i in range(len(d_h)):
    result_h.append(d_h[i] - rep)
    rep = d_h[i]
# 전체 길이는 width이므로 h에서 빼줘야함
result_h.append(w - rep)

# 마지막으로 사각형 넓이중 가장 넓은 것을 찾으면 됨
# 가로 길이와 세로 길이를 구했으므로
# 각각을 곱해서 최대값을 찾으면 됨
max_v = -1e+10
for i in range(len(result_w)):
    for j in range(len(result_h)):
        if max_v < result_w[i]*result_h[j]:
            max_v = result_w[i]*result_h[j]
print(max_v)