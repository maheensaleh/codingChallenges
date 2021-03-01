# read inputs

inp_file = open("inputs/a.txt")
inp_data = inp_file.read()

inp_lines = [x.split(" ") for x in inp_data.split("\n")][:-1]
print(inp_lines)


# code work 
duration = int(inp_lines[0][0])
intersects = int(inp_lines[0][1])
streets  = int(inp_lines[0][2])
cars = int(inp_lines[0][3])
points = int(inp_lines[0][4])

street_desc = inp_lines[1:streets+1]
path_desc = inp_lines[streets+1:]

starts = []
further_streets =[]
unique_starts=[]
req_ints = []

for i in path_desc:
    paths = i[1:]
    further_streets.extend(paths[1:])
    starts.append(paths[0])

for i in starts:
    if i not in further_streets:
        unique_starts.append(i)

print(further_streets)
print(starts)
print(unique_starts)

# required intersects
re_streets=[]
for i in street_desc:
    print(i)
    if i[2] not in unique_starts and i[0] not in req_ints:
        re_streets.append(i[2])
        req_ints.append(i[0])

print("required intersects are : ",req_ints)

# ---------- fo rincoming and itging
ins_outs = {}
for i in range(intersects):
    ins_outs[str(i)]={"in":[], "out":[]}
print(ins_outs)

for path in street_desc:
    print(path)
    ins_outs[path[0]]["out"].append(path[2])
    ins_outs[path[1]]["in"].append(path[2])


print("incoming n outgoing stat :", ins_outs)


# set path acc to duration 
street_durs ={}

for street in street_desc:
    street_durs[street[2]]=street[3]


new_path = []
for path in path_desc:
    temp = [path[0]]
    for street in path[1:]:
        for t in range(int(street_durs[street])):
            temp.append(street)
    new_path.append(temp)

print("new paths : \n",new_path)


#durations loop:
# for i in range(duration):

schedule=[]
car_pos=[]

for i in range(duration):
    car_pos=[]
    for path in new_path:
        car_pos.append(path[1])

    max_path = max(set(car_pos), key = car_pos.count)
    schedule.append(max_path)

    for path in new_path:
            if max_path == path[1]:
                path.pop(1)

    print("******* {} *****".format(i+1))
    print(car_pos)
    print("new paths ", new_path)

print("_____________________")
print(schedule)

out_res = str(len(req_ints))+"\n"
last=""
aa=""
for i in schedule:
    if i == last:
        cnt = int(aa[-2])+1
        out_res+=aa[0:-2]+str(cnt)+"\n"
    else:    
        out_res += aa
        aa = ""
        last = i
        for p in street_desc:
            if p[2]==i:
                print(p)
                print("kk"+p[1])
                aa+=str(p[1])+"\n"
                break
        aa+="1\n"
        aa+=i+" "+"1\n"
print(out_res)
sample_out = "2\n2 1 4\n3 0 2 3"
# write outputs
out_file = open("outputs/out_a.txt","w")
out_file.write(out_res)