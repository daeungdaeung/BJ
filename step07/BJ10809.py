s = input()

al = 'abcdefghijklmnopqrstuvwxyz'
my_list = [-1]*len(al)

for idx, char in enumerate(s):
    if my_list[al.index(char)] == -1:
        my_list[al.index(char)] = idx

print(' '.join(list(map(str, my_list))))