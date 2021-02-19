def change_switch(sex, num, switchs):
    len_switchs = len(switchs)
    # 남자인 경우
    if sex == 1:
        tmp = num
        num = num - 1
        while num < len_switchs:
            switchs[num] = '0' if switchs[num] == '1' else '1'
            num += tmp
    # 여자인 경우
    else:
        num = num - 1
        # 가운데에 위치를 잡고 있는
        # 스위치의 상태를 먼저 바꿔준다.
        switchs[num] = '0' if switchs[num] == '1' else '1'
        l = num - 1
        r = num + 1
        while l > -1 and r < len_switchs and switchs[l] == switchs[r]:
            if switchs[l] == '1':
                switchs[l], switchs[r] = '0', '0'
            else:
                switchs[l], switchs[r] = '1', '1'
            l -= 1
            r += 1
    return switchs

# 스위치의 개수
n = int(input())
switchs = list(input().split())
# 사람 수
k = int(input())
for i in range(k):
    sex, num = map(int, input().split())
    switchs = change_switch(sex, num, switchs)

# 출력 조건에 20개씩 출력하라는게 있어서...
# 하아...
idx = 0
while n > 0:
    if n >= 20:
        tmp = 20
        print(*switchs[idx:idx+20])
    else:
        tmp = len(switchs[idx:])
        print(*switchs[idx:])
    idx += tmp
    n -= tmp
