p,r,t=input().split()
p=int(p)
r=int(r)
t=int(t)
import math
a=p*math.pow((1+r/100),t)
print("%.2f"%(a))
