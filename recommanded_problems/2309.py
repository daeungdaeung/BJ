import itertools
def chk_sum(arr):
    total = 100
    for num in arr:
        total -= num
    if total == 0:
        return True
    return False

dwarfs = sorted([int(input()) for _ in range(9)])
# 9개 중에서 7개 조합을 구하기위해 itertools.combinations를 활용
# 함수말고 bit operation을 활용해서 프로그래밍 가능
cases = itertools.combinations(dwarfs, 7)
for i in cases:
    if chk_sum(i):
        break
for num in i:
    print(num)
