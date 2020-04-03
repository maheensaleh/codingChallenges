T = int(input())
for t in range(T):
  # n,l= map(int, input().split())
  # prods=[int(x) for x in input().split()]
  n,l = 103 , 31
  prods = [217 ,1891 ,4819, 2291, 2987, 3811, 1739, 2491, 4717, 445, 65 ,1079, 8383, 5353 ,901,187,649,1003,697,3239,7663,291,123,779,1007,3551,1943,2117,1679,989,3053]
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
  # primes = sorted(primes)
  # print(primes)
  # print(alphas)
  # print(len(primes))
  # print(len(primes)==len(alphas))

  # get the factors of prods:
  facs=[]
  for i in prods:
    done = False
    c=0
    while not done:
      rem = i%primes[c]
      if rem ==0:
        facs.append((primes[c],int(i/primes[c])))
        done  = True
      c+=1
  # for

  print(facs)
  prime_code=[]
  codes =[]

  for i in facs[0]:
    if i not in facs[1]:
      prime_code.append(i)
      codes.append(i)

  for i in range(len(facs)-1):
    at = facs[i][0]
    if at in facs[i+1]:
      prime_code.append(at)
      if at not in codes:
        codes.append(at)
    else:
      other = facs[i][1]
      prime_code.append(other)
      if other not in codes:
        codes.append(other)

    # for j in facs[i]:
    #   if j in facs[i+1]:
    #     prime_code.append(j)
    #     if j not in codes:
    #       codes.append(j)
  # print(prime_code)
  # print(len(prime_code))

  for i in facs[-1]:
    if i not in facs[-2]:
      prime_code.append(i)
      if i not in codes:
        codes.append(i)


  codes = sorted(codes)
  ans = ""
  # print(prime_code,codes)
  for i in prime_code:
    # print(i)
    ans=ans+alphas[codes.index(i)]
  # print(ans,len(ans))
  print("Case #{}: {} ".format(t + 1, ans.upper()))








