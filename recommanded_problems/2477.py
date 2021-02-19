K = int(input()) # 평당 참외수
arr = []
for i in range(6):
    arr.append(list(map(int, input().split())))
# 북쪽 -> 서쪽이 고정으로 나오게 arr 배열의 원소 순서를 변경하자
for i in range(5):
    if arr[0][0] == 4 and arr[1][0] == 2 and arr[2][0] == 3:
        break
    else:
        tmp = arr.pop()
        arr = [tmp] + arr

cnts = [0]*5
for elem in arr:
    cnts[elem[0]] += 1

# 총 네가지가 나올 수 있다.
# case01
# 북 방향 1번 동 방향 2번
if cnts == [0, 2, 1, 2, 1]:
    area = arr[0][1] * arr[1][1] - arr[3][1] * arr[4][1]
# 북 방향 2번, 서 방향 2번
elif cnts == [0, 1, 2, 1, 2]:
    area = arr[2][1] * arr[3][1] - arr[0][1] * arr[5][1]
# 북 방향 1번, 서 방향 2번
elif cnts == [0, 1, 2, 2, 1]:
    area = arr[0][1] * arr[5][1] - arr[2][1] * arr[3][1]
# 북 방향 2번, 동 방향 2번
else:
    area = arr[1][1] * arr[2][1] - arr[4][1] * arr[5][1]

print(K*area)