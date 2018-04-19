a=[int(x) for x in input().split()]
n=int(input("Enter the number you want to search: "))
for i in range(len(a)):
    if a[i]==n:
        print("%s found at index: %s"%(n, i))
    if i==len(a)-1:
        print("%s not found"%(n))
