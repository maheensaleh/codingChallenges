T = int(input())
def div(num):
  if type(num)==int:
    rev = str(num)[::-1]
    ind = rev.index("4")
    # print(ind)
    subt=pow(10,ind)
    # print(subt)
    rem = num - subt
    if str(rem).__contains__("4"):
      again = div(rem)
      return [again[0],subt+again[1]]
    return [rem,subt]

for t in range(T):
# while True:

  n = int(input())
  ans = div(n)
  print("Case #{}: {} {}".format(t + 1, ans[0],ans[1]))







