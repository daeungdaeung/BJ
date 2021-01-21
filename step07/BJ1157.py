s = input().lower()
import collections

dic = collections.defaultdict(int)

for char in s:
    dic[char] = s.count(char)

dic_list = sorted(dic.items(), key=lambda x: x[1], reverse=True)

if len(dic) == 1:
    print(dic_list[0][0].upper())
else:
    if dic_list[0][1] != dic_list[1][1]:
        print(dic_list[0][0].upper())
    else:
        print('?')