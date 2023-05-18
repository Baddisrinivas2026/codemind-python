n=int(input())
vk=[]
while n:
    vk.append(n%10)
    n=n//10
for r in range(len(vk)-1,-1,-1):
    if vk[r]==6:
        vk[r]=9
        break
vk=vk[::-1]
print(*vk,sep='')
