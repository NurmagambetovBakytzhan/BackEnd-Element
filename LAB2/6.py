
def power(a,b):
    if(b == 0):
        return 1

    return(a * power(a,b-1))

a = list(map(int, input().split()))
fi = a[0]
se = a[1]
print(power(fi,se))