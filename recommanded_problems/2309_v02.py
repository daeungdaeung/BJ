def my_min(arr):
    minv = arr[0]
    for num in arr:
        if minv > num:
            minv = num
    return minv

def my_sum(arr):
    total = 0
    for num in arr:
        total += num
    return total

dwarfs = [int(input()) for _ in range(9)]
# bit operation 활용하기 -> itertools.combinations 사용 x
# 2진수로 생각하면 아래와 같다.
# [0, 0, 1, 1, 1, 1, 1, 1, 1] => 2**8 - 1
# [1, 1, 1, 1, 1, 1, 1, 0, 0] => 2**10 -1 - 2**1 - 2**0
for i in range(2**8-1, 2**10 - 1 - 2**1 - 2**0 + 1):
    # result => 각 난장이가 포함되면 result에 저장
    result = []
    for j in range(0, 9):
        # 각 난장이가 포함되는지 확인
        if i & (1<<j):
            result.append(dwarfs[j])
    # 가능한 정답이 여러가지인 경우에는 아무거나 출력이므로
    # 처음 정답을 발견하면 반복문 종료
    if my_sum(result) == 100 and len(result) == 7:
        break
# 오름 차순 출력이므로
# 작은 수부터 출력
while result:
    min_v = my_min(result)
    print(min_v)
    # 가장 작은 수 출력 후, 리스트에서 삭제
    result.remove(min_v)