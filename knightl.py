# Complete the knightlOnAChessboard function below.
def knightlOnAChessboard(n):

    # get possible move sizes sets (a,b)
    move_size = []
    for i in range(1,n):
        row = []
        for j in range(1,n):
            row.append((i,j))
        move_size.append(row)

    # print("moves sizes -- {}".format(move_size))

    # step_size = (1,2)
    # step_size = (3,3)
    for i in move_size:
        for step_size in i:
            print(for_ab(step_size,n),end=" ")
        print("")



def for_ab(step_size,n):


    # generate bfs for (a,b)==(1,2)
    found = False
    explored=[]
    generated=[(0,0)]
    tree = [
        [(0,0)] #root
        ]

    a,b = step_size[0], step_size[1]
    
    while True:
        last_level = tree[-1] #
        new_level = []
        for node in last_level:
            if  (node not in explored )  :
                new_nodes = [
                    (node[0]+a,node[1]+b),  (node[0]+b,node[1]+a),  (node[0]-a,node[1]-b),  (node[0]-b,node[1]-a),
                    (node[0]+a,node[1]-b),  (node[0]+b,node[1]-a),  (node[0]-a,node[1]+b),  (node[0]-b,node[1]+a),
                ]
                filtered_nodes=[]

                for ntc in new_nodes:
                    # print("debug",ntc)

                    if (ntc not in generated) and -1<ntc[0]<n and -1<ntc[1]<n:
                        filtered_nodes.append(ntc)
                        # check for goal state
                        if ntc == (n-1,n-1):
                            # print("***** YIPWEE *******")
                        
                            new_level.extend(filtered_nodes)
                            generated.extend(filtered_nodes)
                            explored.append(node)
                            tree.append(new_level)

                            # print("tree levels are : ")
                            # for level in tree:
                            #     print("")
                            #     print("length : {} => {}".format(len(level),level))

                            return (len(tree)-1)

                # print("filtered nodes {}".format(filtered_nodes))

                new_level.extend(filtered_nodes)
                generated.extend(filtered_nodes)
                explored.append(node)

        if len(new_level)==0:
            return -1

        tree.append(new_level)

    #tree generated !!
    # print("tree levels are : ")
    # for level in tree:
    #     print("")
    #     print("length : {} => {}".format(len(level),level))




if __name__=="__main__":
    # print("minimum moves = {}".format(knightlOnAChessboard(5)))    

   knightlOnAChessboard(5)
