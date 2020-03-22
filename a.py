
T = int(input())
for t in range(T):
    n,b= map(int, input().split())
    prices=[int(x) for x in input().split()]

    sorted_p = sorted(prices)
    # print(sorted)

    count=0
    for i in sorted_p:
        b= b-i
        if b>-1:
            count+=1
        else:
            break

    print("Case #{}: {}".format(t+1,count))















