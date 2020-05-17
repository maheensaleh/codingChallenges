T = int(input())
for t in range(T):
    n,k= map(int, input().split())
    ints = input()
    ints = [int(i) for i in ints.split(' ') if i.isdigit()]
    # print(ints)
    possible = True
    count=0

    # while possible:

    for i in range(n):
      # print("i--",ints[i])
      if k==ints[i]:
        # print("equals")
        pos = i
        for j in range(k-1,0,-1):
          pos+=1
          if pos<len(ints):
            # print(j,"and",ints[pos])
            if j==ints[pos]:
              # print("true")
              if j==1:
                count+=1
            else:
              break

    print("Case #{}: {}".format(t+1,count))





