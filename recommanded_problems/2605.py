N = int(input())
numbers = list(map(int, input().split()))
result = []
for idx, number in enumerate(numbers):
    if number == 0:
        # 학생이 뽑은 숫자가 0 이면 자리를 옮길 수 없다.
        # 따라서 그 학생은 맨 뒤에 추가해주면 된다.
        result.append(idx+1)
    else:
        # 학생이 앞으로 옮길 수 있는 카드를 뽑으면 (1 이상)
        # 그 숫자만큼 앞으로 갈 수 있다.
        # 리스트 슬라이싱을 통해서
        # 학생이 뽑은 숫자만큼 앞으로 옮겨주었다.
        result = result[:len(result)-number] + [idx+1] + result[len(result)-number:]
print(*result)