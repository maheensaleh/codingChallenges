T = int(input())

for t in range(T):
  n = int(input())
  p = input()
  # n,p = 5 ,"SEEESSES"
  mp=""
  pe,ps,mpe,mps = 0,0,0,0
  path = list(p)
  # print(path)
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
  # print(pes)
  if p[0]=="E":
    mp= mp+"S"
    mps+=1
  else:
    mp = mp +"E"
    mpe+=1
  if p[-1]=="E":
    mp = mp+"S"
    mps+=1
    while mps!=n-1:
      mps+=1
      s  = len(p)-1
      mp = mp[0:s]+"S"+mp[s:]
  else:
    mp = mp +"E"
    mpe+=1
    while mpe!=n-1:
      mpe+=1
      s  = len(p)-1
      mp = mp[0:s]+"E"+mp[s:]

  if mpe!=n-1:
    while mpe!=n-1:
      mpe+=1
      mp = mp[0:1]+"E"+mp[1:]
  else:
    while mps!=n-1:
      mps+=1
      s  = len(p)-1
      mp = mp[0:1]+"S"+mp[1:]

  print("Case #{}: {}".format(t + 1, mp))
#
# if ((mpe, mps) not in pes) or (mpe, mps) == pes[-1]:
#   if p[c] == 'E' and (mpe + 1, mps) != pes[-1]:
#     mpe += 1
#     mp = mp + "E"
#   elif (mpe, mps + 1) != pes[-1]:
#     mps += 1
#     mp = mp + "S"
#   c += 1
# else:
#   ind = pes.index((mpe, mps)) + 1
#   if p[ind] == 'E' and (mpe, mps + 1) != pes[-1]:
#     mps += 1
#     mp = mp + "S"
#   elif (mpe + 1, mps) != pes[-1]:
#     mpe += 1
#     mp = mp + "E"


