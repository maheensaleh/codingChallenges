T = int(input())
for t in range(T):
    n,k= map(int, input().split())
    all = []
    least=27
    for i in range(n):
        s = input()
        all.append(s)
        if len(s)<least:
            least =len(s)

    tester=[]
    for i in all:
        tester.append(i[0:least])

    print(tester)
    tmp=[]
    for i in range(least):
        tmp.append([])
        for j in tester:
            tmp[-1].append(j[i])
    tmp = tmp[0:least]
    print(tmp)



    # print("Case #{}: {}".format(t+1,sum(selected)))







