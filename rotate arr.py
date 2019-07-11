# rotate-array
m,n=map(int,input().split())
t=list(map(int,input().split()))[:m]

for i in range(0,n):
    t=[t[-1]]+t[:-1]
    
print(t)
