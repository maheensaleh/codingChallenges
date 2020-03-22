#  ####### ALGO ######
#
# N - total numbers
# p - selections
# si - skill level of ith
#
# make a dic to save differencesof all levels
#  for i in range(n):
#      for j in range(i+1,n):
#          diff [] = [ith elemnt, jth element]



# T = int(input())
for t in range(1):
    # n,p= map(int, input().split())
    # skills=[int(x) for x in input().split()]
    n,p,skills = 6,2,[5,5,1,2,3,4]
    print(skills)

    levels= []
    repeated = []
    for x in skills:
        if x not in levels:
            levels.append(x)
        else:
            repeated.append(x)

    print(repeated)
    diff={}
    for i in range(n):
        for j in range(i+1,n):
            change = abs(skills[i]-skills[j])
            if change not in diff.keys():
                diff[change] = [skills[i],skills[j]]
            else:
                diff[change].append(skills[i])
                diff[change].append(skills[j])



    print(diff)
    # diff_keys = diff_keys
    sort_diff = sorted(diff.keys())
    print("sorted : ",sort_diff)

    selected_levels = []
    for i in sort_diff:
        # taken = levels[diff[i]]
        print("this : ",diff[i])
        for k in range(len(diff[i])):
            if len(selected_levels)<p and diff[i][k] in skills:
                selected_levels.append(diff[i][k])
                skills.pop(skills.index(diff[i][k]))

    print(selected_levels)

    max = selected_levels.max()
    result =0
    for i in selected_levels:
        result  += max-selected_levels[i]

    print("Case #{}: {}",t+1,result)












