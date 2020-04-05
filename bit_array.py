import sys
T,b= map(int, input().split())
for t in range(T):
  bit_array = input() #input by judge
  stored = bit_array
  original=bit_array
  for i in range(1,151):
    p = 1 #can be any integer between 1 and B
    print(p)
    sys.stdout.flush()
    # if ends with 1 , make changes:
    # turn = str(i)
    if i%10==1:
      print("changed")
      sys.stdout.flush()
      stored = stored[::-1] #reversal

    chr = input() #input by judge

  print(stored)
  sys.stdout.flush()

  accuracy  = input() #judge tells whether same or not
  if accuracy=='N':
    break



