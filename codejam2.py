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
    if i =="E":
      mp = mp +"S"
    else:
      mp = mp+"E"

  print("Case #{}: {}".format(t + 1, mp))



