t=int(input())
for i in range(t):
    k=int(input())
    ls=list(map(int,input().split()))
    p=k-2
    for m in range(1,p+1):
        if p%m==0:
            n=p//m 
            if (n in ls):
                if (m in ls):
                    a=m
                    b=n
    print(a,b)