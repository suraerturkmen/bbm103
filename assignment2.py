"""
Feeding the rabbit game
In this game, the rabbit(*) which is placed in a board will move according to the commands and collect
points according to the food it eats. The foods have a point like that:
Apple(A)= 5 point Carrot(C)= 10 point Meat(M)= -5 point
If the rabbit eats the posion(P),it will be die.
"""
feeding_map_input=input("Please enter feeding map as a list:\n")
direction_input=input("\nPlease enter direction of movements as a list:\n")
creation_list=[]
feeding_map_list=[]
score=0
for i in feeding_map_input:#our map input is include unnecessary things so it selects necessary things
    if i=="M" or i=="C" or i=="*" or i=="X" or i=="W" or i=="A" or i=="P":
        creation_list.append(i)
    if i=="]":#it seperates the lists
        feeding_map_list.append(creation_list)
        creation_list=[]
feeding_map_list.pop()
direction_list=[]
for i in direction_input:#our direction input is include unnecessary things so it selects necessary things
    if i=="U" or i=="D" or i=="L" or i=="R":
        direction_list.append(i)
row_up_limit = len(feeding_map_list) - 1#I have to prevent the rabbit from going outside
column_up_limit = len(feeding_map_list[0]) - 1#I have to prevent the rabbit from going outside
def board(feeding_map_list):#it converts 1D array into 2D array
    for i in feeding_map_list:
        for j in i:
            print(j,end = " ")
        print()
def conditions(a,b,c,d):#with this function rabbit can move on the board and collect points
    global feeding_map_list
    global score
    if d<=row_up_limit and d>=0 and c<=column_up_limit and c>=0:
        if feeding_map_list[d][c]== "A":
            score+=5
            feeding_map_list[d][c]= "*"
            feeding_map_list[b][a] = "X"
            return "go"
        elif feeding_map_list[d][c]== "M":
            score-=5
            feeding_map_list[d][c]= "*"
            feeding_map_list[b][a]= "X"
            return "go"
        elif feeding_map_list[d][c]== "C":
            score+=10
            feeding_map_list[d][c]= "*"
            feeding_map_list[b][a] = "X"
            return "go"
        elif feeding_map_list[d][c]== "P":
            feeding_map_list[d][c]= "*"
            feeding_map_list[b][a] = "X"
            return "stop"
        elif feeding_map_list[d][c]== "X":
            feeding_map_list[d][c]= "*"
            feeding_map_list[b][a]= "X"
        elif feeding_map_list[d][c]== "W":
            return "continue"
    else:
        return "continue"
print("Your board is:")
board(feeding_map_list)
print()
number_list=0
for i in feeding_map_list:#with this loop I find the rabbit(*)
    number_sublist=0
    for j in i:
        if j=="*":
            index_list=number_list
            index_sublist=number_sublist
        number_sublist+=1
    number_list+=1
for i in direction_list:#this loop evaluate the direction
    if i=="U":
        new_index_sublist = index_sublist
        new_index_list = index_list - 1
        go_or_stop=conditions(index_sublist, index_list, new_index_sublist, new_index_list)
        if go_or_stop== "stop":
            break
        elif go_or_stop== "continue":
            continue
    elif i=="D":
        new_index_sublist = index_sublist
        new_index_list = index_list + 1
        go_or_stop =conditions(index_sublist, index_list, new_index_sublist, new_index_list)
        if go_or_stop== "stop":
            break
        elif go_or_stop== "continue":
            continue
    elif i=="L":
        new_index_sublist = index_sublist - 1
        new_index_list = index_list
        go_or_stop=conditions(index_sublist, index_list, new_index_sublist, new_index_list)
        if go_or_stop== "stop":
            break
        elif go_or_stop== "continue":
            continue
    elif i=="R":
        new_index_sublist = index_sublist + 1
        new_index_list = index_list
        go_or_stop=conditions(index_sublist, index_list, new_index_sublist, new_index_list)
        if go_or_stop== "stop":
            break
        elif go_or_stop== "continue":
            continue
    index_list=new_index_list
    index_sublist=new_index_sublist
print("Your output should be like this:")
board(feeding_map_list)
print("Your score is:", score)