T = int(input())
for tt in range(T):
  account=0
  n= input()
  an=n
  c=0
  for i in range(len(n)):
    t=int(n[i])
    an = an[0:i+c]+ "("*t +an[i+c] + ")"*t + an[i+c+1:]
    c += t*2
    account+=t*2
  # print(an)

  ann=an
  c=0
  for _ in range(account):
    c=0
    an=ann
    for i in range(len(an)-1):
      if an[i]==")" and an[i+1]=="(":
        ann = an[0:i]+an[i+2:]
        c-=2
    # print(ann)
  print("Case #{}: {}".format(tt + 1,ann))





