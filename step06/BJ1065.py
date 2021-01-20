def fn(n):
    if n < 100:
        return n
    
    cnt = 99

    for i in range(100, n+1):
        each_value = list(map(int, list(str(i))))
        differences = []
        for j in range(len(each_value)-1):
            differences.append(each_value[j]-each_value[j+1])
        
        if differences.count(differences[0]) == len(differences):
            cnt += 1
    
    return cnt

value = int(input())

print(fn(value))