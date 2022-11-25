a = input()
j = 0
n= 0
for i in range(len(a)-1,-1,-1):
    # print(a[i])
    n += int(a[i]) * 2**j
    j+=1
print(n)
