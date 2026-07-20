#Find Second Largest in Array
a=list(map(int,input().split()))
s=max(tuple(a))
a.remove(s)
print(max(a))