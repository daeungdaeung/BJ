def f(a1, a2, arr):
    if a1 < a2:
        return ''
    arr.append(a1-a2)
    f(a2, a1-a2, arr)
    return arr

N = int(input())
max_len = -1e+10
max_arr = []
# 처음에 range(1, N)으로 했더니 통과 못했음...
#
for i in range(1, N+1):
    tmp_arr = f(N, i, [N, i])
    if max_len < len(tmp_arr):
        max_arr = tmp_arr
        max_len = len(tmp_arr)

print(len(max_arr))
print(*max_arr)