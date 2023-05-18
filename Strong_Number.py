n=int(input())
t=n
k=0
while n>0:
    r=n%10
    v=1
    for i in range(r,0,-1):
        v=v*i
    k+=v
    n=n//10
if k==t:
    print('The number',t,'is a strong number')
else:
    print('The number',t,'is not a strong number')
