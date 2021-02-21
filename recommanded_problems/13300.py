N, K = map(int, input().split())
students = [list(map(int, input().split())) for _ in range(N)]
# 학생들이
# 1. 여자인지 남자인지 구별
# 2. 성별 구별 후, 학년을 기준으로 구분
# 어차피 성별은 2개고 학년은 6개이니까 -> arr의 길이가 12개이면 충분할 것
# 편한 인덱싱을 위해서 2x6로 배열 선언
arr = [[0]*6 for _ in range(2)]  # 성별, 학년별 구분
for student in students:
    arr[student[0]][student[1]-1] += 1
# 성별, 학년별로 구별 후
# 방이 몇개나 필요한지 조사해보자
total = 0
for s in range(2):
    for g in range(6):
        q, r = divmod(arr[s][g], K)
        if r > 0:
            total += q + 1
        else:
            total += q
print(total)