import math
s = 0
for n in range(1,31):
    f=1
    for i in range(1,2 * n + 1):
        f=f*i 
    s = s+1.2 ** (2*n +1)/ f * math.log(n+1)
math.log(n+1)
print("Сумма =", s)