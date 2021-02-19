n, k = map(int, input().split())
temperatures = list(map(int, input().split()))
max_v = sum(temperatures[0:k])
tmp_v = max_v
idx = 0
# 매번 리스트 슬라이싱으로 합을 구하는것보다
# 기존의 합에서 맨 앞의 원소를 빼고
# 맨뒤의 원소를 더하면
# 속도가 더 빠를것으로 생각된다.
while idx+k <= n-1:
    tmp_v -= temperatures[idx]
    tmp_v += temperatures[k+idx]
    if max_v < tmp_v:
        max_v = tmp_v
    idx += 1

print(max_v)