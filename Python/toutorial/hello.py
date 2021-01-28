n=int(input())
x=list(map(int,input().split()))
x.sort()
ans=list()
ans.insert(0,x[n-1])
f=True
for i in range(n-2,-1,-1):
    if f :
        ans.append(x[i]); f=False
    else:
        ans.insert(0,x[i]); f=True
print(' '.join(map(str,ans)))


