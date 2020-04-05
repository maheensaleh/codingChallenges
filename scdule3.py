T = int(input())
for t in range(T):
  n= int(input())
  slots=[]
  for _ in range(n):
    slot=[int(x) for x in input().split()]
    slots.append(slot)

  period=[]
  all_period=[]
  for i in slots:
    for j in range(i[0],i[1]):
      period.append(j)
    all_period.append(period)

  done=True
  overlap=[]
  for i in slots:
    o=1
    for j in all_period:
      if i[0] in j:
        overlap.append((slots.index(i),all_period.index(j)))
        o+=1
        if o==3:
          done = False
          break
    if not done:
      print("impossible")
      break
  print(overlap)
