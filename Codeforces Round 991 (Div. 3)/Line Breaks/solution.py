t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    ls=[]
    for i in range(n):
        s=input()
        ls.append(s)
    l=0
    c=0
    for i in ls:
        l+=len(i)
        if l<=m:
            c+=1
        else:
            break
    print(c)