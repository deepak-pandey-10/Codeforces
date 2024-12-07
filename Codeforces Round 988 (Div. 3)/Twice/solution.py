t=int(input())
for i in range(t):
    a=int(input())
    c=0
    ls=list(map(int,input().split()))
    for i in range(len(ls)):
        for j in range(i+1,len(ls)):
            if ls[i]==ls[j]:
                c+=1
                ls.pop(j)
                
                break
    print(c)