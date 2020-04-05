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
  done=True

  for s in slots:
    J = False
    C = False
    if s[0] not in j and (s[1]-1) not in j:
      period = []
      for i in range(s[0],s[1]):
        period.append(i)
        if i not  in j:
          J=True
        else:
          J=False
          break
      if J==True:
        schedule=schedule+"J"
        j=j+period
    elif s[0] not in c and (s[1]-1) not in c and J==False :
      period = []
      for i in range(s[0],s[1]):
        period.append(i)
        if i not  in c:
          C=True
        else:
          C=False
          break
      if C==True:
        schedule=schedule+"C"
        c=c+period
    if J==False and C==False:
      done = False
      break

  if done:
    # print(schedule)
    print("Case #{}: {}".format(t + 1, schedule.upper()))

  else:
    # print("not possible")
    print("Case #{}: {}".format(t + 1,"IMPOSSIBLE"))




