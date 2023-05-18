for l in range(int(input())):
    n,s=map(int,input().split())
    arr=list(map(int,input().split()))
    for i in range(n):
        for j in range(n):
            vk,b=sum(arr[i:j+1]),0
            if vk==s:
                print(i+1,j+1)
                b=1
                break
        if b==1:
            break
    else:
        print(-1)
