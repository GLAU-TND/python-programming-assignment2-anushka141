a=int(input())
b=bin(a)
b=b[2:]
c=[]
d=0
for i in b:
    if int(i)==0:
        d=0
    if int(i)==1:
        d+=1
    if d>0:
        c.append(d)
print(max(c))
