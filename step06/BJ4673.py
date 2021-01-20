def fn(n):
    summation = n
    while n > 0:
        q, r = divmod(n, 10)
        summation += r
        n = q

    return summation

dn = [0]*10000
for i in range(10000):
    dn[i] = fn(i+1)

for i in range(1, 10000):
    if not(i in dn):
        print(i)

