a = [int(x) for x in input().split()]
idx=0
i=0
smallest = 0
print(a)
for i in range(0,len(a)):
    smallest=min(a[i:])
    idx=a.index(smallest)
    a[i],a[idx]=a[idx],a[i]
print (a)
