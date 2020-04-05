T = int(input())
for t in range(T):
  n= int(input())
  mat =[]
  for _ in range(n):
    rows=[int(x) for x in input().split()]
    mat.append(rows)

  sum=0
  for i in range(n):
    sum+=mat[i][i]
  # print(sum)

  r,c=0,0
  for i in mat:
    chk=[]
    for j in i:
      if j not in chk:
        chk.append(j)
      else:
        r+=1
        break

  # print(r)

  for i in range(n):
    chkc = []
    for j in range(n):
      if mat[j][i] not in chkc:
        chkc.append(mat[j][i])
      else:
        c+=1
        break
  # print(c)
  print("Case #{}: {} {} {}".format(t + 1, sum,r,c))

