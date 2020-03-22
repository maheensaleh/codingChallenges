T = int(input())
for t in range(T):
    n,k,p= map(int, input().split())
    stacks=[]
    for _ in range(n):
        vals=[int(x) for x in input().split()]
        stacks.append(vals)

    max_stack_i = None
    ii=None
    maxi = 0
    for i in range(len(stacks)):
        if max(stacks[i])>maxi:
            maxi = max(stacks[i])
            max_stack_i= i
            tmp = max(stacks[i])
            ii = stacks[i].index(tmp)+1

    beauty=0
    selected=[]
    if p>ii:
        for y in range(ii):
            selected.append(stacks[max_stack_i].pop(0))
    max2=0

    while len(selected)<p:
        print("stacks",stacks)
        tester=[]
        for i in range(len(stacks)):
            if len(stacks[i])>0:
                tester.append(stacks[i][0])
        
        max2 = max(tester)
        selected.append(max2)
        indexx = tester.index(max2)
        stacks[indexx].pop(0)

    print("Case #{}: {}".format(t+1,sum(selected)))







