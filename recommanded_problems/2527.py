def chk_unoverlab(s1, s2):
    # 아래 4가지의 경우는 두 사각형이
    # 어느 한 점도 겹치지 않음을 의미함
    # -> 코드 문자 d
    if s1[3] < s2[1]:
        return True
    if s1[1] > s2[3]:
        return True
    if s1[2] < s2[0]:
        return True
    if s1[0] > s2[2]:
        return True
    return False

# 어느 한점에서만 딱 겹치는 경우 -> 코드 문자 c
def chk_point(s1, s2):
    if s1[2] == s2[0] and s1[3] == s2[1]:
        return True
    if s1[0] == s2[2] and s1[1] == s2[3]:
        return True
    if s1[0] == s2[2] and s1[3] == s2[1]:
        return True
    if s1[2] == s2[0] and s1[1] == s2[3]:
        return True
    return False

# 한 선분에서만 딱 겹치는 경우 -> 코드 문자 b
def chk_line(s1, s2):
    if s1[2] == s2[0] and s2[1] < s1[3] and s2[3] > s1[1]:
        return True
    if s1[0] == s2[2] and s2[1] < s1[3] and s2[3] > s1[1]:
        return True
    if s1[1] == s2[3] and s2[2] > s1[0] and s2[0] < s1[2]:
        return True
    if s1[3] == s2[1] and s2[2] > s1[0] and s2[0] < s1[2]:
        return True

    return False

def find_code(s1, s2):
    if chk_unoverlab(s1, s2):
        return 'd'
    if chk_point(s1, s2):
        return 'c'
    if chk_line(s1, s2):
        return 'b'
    return 'a'

for i in range(4):
    x1, y1, x2, y2, X1, Y1, X2, Y2 = map(int, input().split())
    s1 = [x1, y1, x2, y2]
    s2 = [X1, Y1, X2, Y2]
    # 두번째 사각형의 꼭짓점이 첫번째 사각형의 내부에 있는 경우
    # 위의 경우는 무조건 직사각형이 생긴다. -> 코드문자 a
    print(find_code(s1, s2))

