T = int(input())
for t in range(T):
  n,l= map(int, input().split())
  prods=[int(x) for x in input().split()]
  # n,l = 103 , 31
  # prods = [217 ,1891 ,4819, 2291, 2987, 3811, 1739, 2491, 4717, 445, 65 ,1079, 8383, 5353 ,901,187,649,1003,697,3239,7663,291,123,779,1007,3551,1943,2117,1679,989,3053]
  primes = []
  alphas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  p=2
  primes.append(p)
  while p<n:
    p+=1
    ok = True
    for i in range(2,p//2):
      rem = p%i
      if rem==0:
        ok = False
        break
      else:
        continue
    if ok:
      primes.append(p)

  prime_codes=[]
  codes=[]
  status =[]
  for i in range(len(prods)):
    done = False
    c=0
    while not done:
      rem = prods[i]%primes[c]
      if rem ==0:
        done = True
        this_prod = [primes[c], int(prods[i] / primes[c])]

        if i==0:
          status.append(this_prod)

        elif i == 1:
          status.append(this_prod)
          if status[0][0] not in status[1]:
            prime_codes.append(status[0][0])
            if prime_codes[-1] not  in codes:
              codes.append(prime_codes[-1])
            prime_codes.append(status[0][1])
            if prime_codes[-1] not  in codes:
              codes.append(prime_codes[-1])
          else:
            prime_codes.append(status[0][1])
            if prime_codes[-1] not  in codes:
              codes.append(prime_codes[-1])
            prime_codes.append(status[0][0])
            if prime_codes[-1] not  in codes:
              codes.append(prime_codes[-1])
          status.pop(0)

        else:
          status.append(this_prod)
          if status[0][0] in status[1]:
            prime_codes.append(status[0][0])
            if prime_codes[-1] not  in codes:
              codes.append(prime_codes[-1])
          else:
            prime_codes.append(status[0][1])
            if prime_codes[-1] not  in codes:
              codes.append(prime_codes[-1])
          status.pop(0)
      c+=1
    if i == len(prods)-1:
      status[-1].pop(status[-1].index(prime_codes[-1]))
      prime_codes.append(status[-1][0])
      if prime_codes[-1] not in codes:
        codes.append(prime_codes[-1])

    # print(prime_codes)
    codes = sorted(codes)
    # print(codes,len(codes))

  ans = ""
  for i in prime_codes:
    # print(i)
    ans=ans+alphas[codes.index(i)]
  # print(ans,len(ans))
  print("Case #{}: {} ".format(t + 1, ans.upper()))
