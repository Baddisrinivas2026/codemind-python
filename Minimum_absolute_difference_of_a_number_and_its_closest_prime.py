n=int(input())
v=n
t=n
s=0
c=0
while(n!=0):
    c+=1
    for i in range(2,int(n**0.5)+1):
        if(n%i==0):
            break
    else:
        break
    n-=1
while(t!=0):
    s+=1
    for i in range(2,int(t**0.5)+1):
        if(t%i==0):
            break
    else:
        break
    t+=1
if(s>=c):
    print(v-n)
else:
    print(t-v)
