N = int(input())
# 색종이가 놓이는 평면 -> 가로 최대 101, 세로 최대 101
brd = [[-1 for _ in range(101)] for __ in range(101)]
# N -> 색종이 수
for i in range(N):
    # 내 생각에는 좌표를 리스트 인덱스로 사용해도
    # 결국 모든 사각형에 적용되므로 결과값은 똑같을 것이라 생각한다.
    r, c, r_l, c_l = map(int, input().split())
    for p_r in range(r, r+r_l):
        for p_c in range(c, c+c_l):
            brd[p_r][p_c] = i

# 색칠이 모두 끝났으면 어떻게 색칠이 되었는지 확인
dic = {}
for i in range(101):
    for j in range(101):
        if brd[i][j] >= 0:
            dic[brd[i][j]] = dic.get(brd[i][j], 0) + 1
# 색칠이 덮어 씌워져 사라진 색이 있다.
# 사라진 색도 출력해
for i in range(N):
    print(dic.get(i, 0))
