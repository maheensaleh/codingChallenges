# T = int(input())

for t in range(1):
  # n = int(input())
  # p = input()
  n,p = 5 ,"EESSSESE"
  mp=""
  pe,ps,mpe,mps = 0,0,0,0
  pes = []
  mpes=[]
  for i in p:
    if i=='E':
      pe+=1
    else:
      ps+=1
    pes.append((pe,ps))
  pes.pop()
  pes.insert(0,(0,0))
  print(pes)
  c=0
  if pes[1] == (1, 0):
    mpes.append((0, 1))
  else:
    mpes.append((1, 0))

  while mpes!=(n-1,n-1):
    print(mp)
    if (mpe+1,mps) not in pes and mpe<n-1:
      mpe += 1
      mp = mp + "E"
    elif (mpe,mps+1) not in pes and mps<n-1:
      mps += 1
      mp = mp + "S"
    else:
      if mpe<n-1:
        ind = pes.index((mpe+1))



  print("Case #{}: {}".format(t + 1, mp))







