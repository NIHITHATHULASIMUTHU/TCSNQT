#Linear Search
l=list(map(int,input().split()))
e=int(input("enter the number"))
for i in range(len(l)):
    if l[i]==e:
        print(i)
        break