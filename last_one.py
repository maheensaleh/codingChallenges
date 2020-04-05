T = int(input())
for t in range(T):
  n,k= map(int, input().split())

  # n,k = 4,10
  nums=[]
  for i in range(1,n+1):
    nums.append(i)
  # print("nums : ",nums)

  poss_sums =[]
  for i in nums:
    poss_sums.append(i*n)
  # print("poss_sums : ",poss_sums)
  # poss_sums.append(sum(nums))

  possible= False
  if k in poss_sums:
    possible=True

  if possible:
    combs= [nums]
    for i in range(n-1):
      a = combs[-1]
      b = [a[-1]]+a[0:-1]
      combs.append(b)
    # print("combinations : ",combs)

    mat=[]
    for i in combs:
      if i[0]*n==k:
        key = i[0]
        row = combs.pop(combs.index(i))
        mat.append(row)
        break

    for i in range(1,n):
      for j in combs:
        if j[i]==key:
          row = j
          mat.append(row)


  elif possible==False:
    # print("two")
    combs= [nums]
    for i in range(n-1):
      a = combs[-1]
      b = [a[-1]]+a[0:-1]
      combs.append(b)
    # print("combinations : ",combs)

    mat=[]
    st=-1
    for i in range(1,n+1):
      st = -1
      mat=[]
      while st>=-(n):
        for j in combs:
          if j[st]==i:
            mat.append(j)
            st-=1
            break
      chk_sum=0
      for i in range(n):
        chk_sum+=mat[i][i]
      # print(chk_sum,k)
      if chk_sum==k:
        possible=True
        break

  if possible:
    print("Case #{}: {}".format(t + 1, "POSSIBLE"))
    for i in mat:
      for j in i:
        print(j, end=" ")
      print("")
  else:
    print("Case #{}: {}".format(t + 1, "IMPOSSIBLE"))








