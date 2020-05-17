T = int(input())
for t in range(T):
    n = int(input())
    ints = input()
    ints = [int(i) for i in ints.split(' ') if i.isdigit()]
    # print("array ",ints)
    count=0


    for i in range(n):
      for j in range(i + 1, n + 1):
        s = sum(ints[i:j])
        r = int(s ** (1 / 2))
        if r * r == s:
          count += 1





    print("Case #{}: {}".format(t+1,count))



