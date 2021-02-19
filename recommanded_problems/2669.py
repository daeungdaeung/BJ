from pprint import pprint
m = [[0]*100 for _ in range(100)]
for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    x = x2 - x1
    y = y2 - y1
    for i in range(x1, x1+x):
        for j in range(y1, y1+y):
            m[i][j] = 1
cnt = 0
for i in range(100):
    for j in range(100):
        if m[i][j] == 1:
            cnt += 1
print(cnt)
