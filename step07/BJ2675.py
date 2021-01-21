num_case = int(input())
for i in range(num_case):
    num_iter, s = input().split()

    out = ''
    for char in s:
        out += char*int(num_iter)

    print(out)