T = int(input())
for t in range(T):
  n= int(input())
  slots=[]
  for _ in range(n):
    slot=[int(x) for x in input().split()]
    slots.append(slot)

  j=[]
  c=[]
  schedule=""
  print(slots)

  done=True
  for s in slots:
    J = True
    C = True
    period=[]
    for i in range(s[0],s[1]):
      period.append(i)
      if i in c and C==True:
        C = False
      if i in j and J==True:
        J=False

    if C:
      c=c+period
      schedule=schedule+"C"
    elif J:
      j=j+period
      schedule=schedule+"J"

    else:
      done=False
      schedule="IMPOSSIBLE"
      break

  print("Case #{}: {}".format(t + 1, schedule))


