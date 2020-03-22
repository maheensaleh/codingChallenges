################ ALGO ####################
#
# kick
# start
# code:
#
# k - total
# wakeup
# calls #######
# A - vallues in the
# array
# ith
# call
# means
# ith
# power
# N - no
# of
# values in aray
#
# algo:
#
# read
# T
#
# repeat
# T
# times:
# read
# n, k, X1, Y2, c, d, E1, E2, f
#
# -------------
# A = [a1 = formula]
# for N - 1:
#     Xn, yn =
#     A.append(formula)
# ------------
# make
# subsets
# --------------
# power = 0
# for i in k:
#     for each subset:
#         for j in range(subset):
#             power += subset[j] * ((j + 1) ** i)
#
# test
# case and output
#
#####################
T= int(input())
for t in range(T):
    n,k,x1,y1,c,d,e1,e2,f= map(int, input().split())
    #################
    a = [(x1+y1)%f]
    for _ in range(n-1):
        x1,y1 = (c*x1 + d*y1 + e1)%f, (d*x1 + c*y1 + e2)%f
        a.append((x1+y1)%f)
    # print(a)
    subsets =[]
    for i in range(len(a)):
        for j in range(i + 1, len(a) + 1):
            subsets.append(a[i:j])

    # print(subsets)

    power = 0
    for i in range(k):
        # print(i)
        for subset in subsets:
            for j in range(len(subset)):
                power+=subset[j]*((j+1)**(i+1))
                # print(i,subset,j,power)
    print("Case #{}: {}".format(t+1,power%1000000007))

