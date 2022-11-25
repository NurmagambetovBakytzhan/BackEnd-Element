st_hr = 9
st_min = 0

n = int(input())

num_of_evens = (n//2) - (((n+1)%2))
num_of_odds = (n-1)//2 + (n+1)%2
# print(num_of_evens)

a = n * 45
a += (5*num_of_odds + 15*num_of_evens)

st_hr += a//60

st_min += a%60

print(st_hr, st_min)