cnt= 0
def elec(l):

    global cnt
    for i in l:
        if i == 0:
            cnt+=1
 
l = list(map(int, input().split()))
a= l[0]
b= l[1]
c= l[2]
elec(l)
if cnt >= 2:
    print(0)
else:
    print(1)
