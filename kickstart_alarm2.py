
T= int(input())
for t in range(T):
    n,k,x1,y1,c,d,e1,e2,f= map(int, input().split())
    #################
    a = [(x1+y1)%f]
    for _ in range(n-1):
        x1,y1 = (c*x1 + d*y1 + e1)%f, (d*x1 + c*y1 + e2)%f
        a.append((x1+y1)%f)
    # print(a)
    # print(subsets)
    result = 0
    gp = k
    mod = 1000000007
    for x in range(1,n+1):
        if x!=1:
            gp = gp + (pow(x,k+1)-1)*pow(x-1,-1)
            gp%= mod
        result = result+gp+a[x-1]
        result%=mod

    # power = a[0]*gp
    # print(power)
    # for p in range(2,len(a)+1):
    #     print(a[p-1])
    #     gp+= (((p)**(k+1)-1)*pow(p-1,1000000007-2))
    #     power+=a[p-1] *gp
    #     print(power)
    print("Case #{}: {}".format(t+1,result%1000000007))

