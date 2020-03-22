a = [1,2,3,4]
subsets=[]
for i in range(len(a)):
    for j in range(i+1,len(a)+1):
        subsets.append(a[i:j])

print(subsets)