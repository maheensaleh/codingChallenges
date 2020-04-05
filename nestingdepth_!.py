T = int(input())
for t in range(T):
  n= input()
  c=0
  an=n
  i=0

  while i<len(n):
    if n[i]=="1":
      an = an[0:i+c]+"("+an[i+c:]
      c+=1
      s=i+1
      if s==len(n):
        an = an+")"
        break
      else:
        while n[s]=="1" and s+1<len(n):
          s+=1
        if s+1<len(n):
          an = an[0:s+c]+")"+an[s+c:]
          c+=1
          i=s
        else:
          if an[-1]=="1":
            an = an+")"
          else:
            an = an[0:-1]+")"+an[-1:]
          break
    i+=1



  print("Case #{}: {}".format(t + 1, an))
  #
  # n= "10110"
  # an = n
  # c=0
  # for i in range(len(n)):
  #   if n[i]=="1":
  #     an = an[0:i+c]+"("+an[i+c:]
  #     c+=1
  #
  # c=0
  # ann= an
  # for i in range(len(an)):
  #   if an[i]=="(":
  #     s=i+1
  #     while an[s]=="0":
  #       s+=1
  #     ann = ann[0:s+c+1]+")"+ann[s+c+1:]
  #     c+=1
