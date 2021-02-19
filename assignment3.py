"""
CHESS GAME
This is a chess application that implements a subset of rules of the chess game.
"""
import sys
f=open(sys.argv[1],"r")
command=[line.split() for line in f.readlines()]
f.close()
def initialize():#It load the pieces to the board.
    global location
    global find_location
    location = {"a8": "R1", "b8": "N1", "c8": "B1", "d8": "QU", "e8": "KI", "f8": "B2", "g8": "N2", "h8": "R2",
           "a1": "r1", "b1": "n1", "c1": "b1", "d1": "qu", "e1": "ki", "f1": "b2", "g1": "n2", "h1": "r2",
           "a7": "P1", "b7": "P2", "c7": "P3", "d7": "P4", "e7": "P5", "f7": "P6", "g7": "P7", "h7": "P8",
           "a2": "p1", "b2": "p2", "c2": "p3", "d2": "p4", "e2": "p5", "f2": "p6", "g2": "p7", "h2": "p8"}
    find_location = {v: k for k, v in location.items()}
    return printboard()
def answ(a, b, player_x, player_y, right, squares_to_go):
    if location[column[a] + str(b)] in player_x or location[column[a] + str(b)] in kings :
        return "stop"
    if location[column[a] + str(b)] in player_y:
        right -= 1
        squares_to_go.append(column[a] + str(b))
    else:
        squares_to_go.append(column[a] + str(b))
    return right
def rook(check, player_x, player_y):
    squares_to_go=[]
    column_index=column.index(check[0])
    b,a,right = int(check[1]), column_index, 1
    while b > 1:
        b -= 1
        answ1= answ(a, b, player_x, player_y, right, squares_to_go)
        if answ1 == "stop" or answ1==0: break
    right,b  = 1,int(check[1])
    while b < 8:
        b += 1
        answ1= answ(a, b, player_x, player_y, right, squares_to_go)
        if answ1 == "stop" or answ1==0: break
    a,right,b= column_index, 1, check[1]
    while a > 0:
        a -= 1
        answ1 = answ(a, b, player_x, player_y, right, squares_to_go)
        if answ1 == "stop" or answ1==0: break
    a,right = column_index,1
    while a < 7:
        a += 1
        answ1 = answ(a, b, player_x, player_y, right, squares_to_go)
        if answ1 == "stop" or answ1==0: break
    return squares_to_go
def bishop1(check, player_x, player_y):
    squares_to_go=[]
    column_index = column.index(check[0])
    b,a,right = int(check[1]), column_index, 1
    while b > 1 and a < 7:
        b -= 1
        a += 1
        answ1 = answ(a, b, player_x, player_y, right, squares_to_go)
        if answ1 == "stop" or answ1==0: break
    b,a,right = int(check[1]), column_index, 1
    while b > 1 and a > 0:
        b -= 1
        a -= 1
        answ1 = answ(a, b, player_x, player_y, right, squares_to_go)
        if answ1 == "stop" or answ1==0: break
    return squares_to_go
def bishop2(check, player_x, player_y):
    squares_to_go = []
    sutunun_indeksi = column.index(check[0])
    b,a,right = int(check[1]), sutunun_indeksi, 1
    while b < 8 and a > 0:
        a -= 1
        b += 1
        answ1 = answ(a, b, player_x, player_y, right, squares_to_go)
        if answ1 == "stop" or answ1==0: break
    b,a,right = int(check[1]), sutunun_indeksi, 1
    while b < 8 and a < 7:
        a += 1
        b += 1
        answ1=answ(a, b, player_x, player_y, right, squares_to_go)
        if answ1 == "stop" or answ1==0: break
    return squares_to_go
def pawn(check, player_x, x):
    squares_to_go=[]
    b= int(check[1]) + x
    column_index=column.index(check[0])
    a=column_index
    if a<8 and a>-1 and b<9 and b>0 and location[column[a] + str(b)] not in player_x and location[column[a] + str(b)] not in kings and b>0:
        check[1]=str(b)
        squares_to_go.append(column[a] + check[1])
    return squares_to_go
def knight(check, player_x, player_y):
    squares_to_go=[]
    column_index=column.index(check[0])
    a= int(check[1]) + 2
    b= int(check[1]) - 2
    c=column_index-1
    hak=0
    while a<10 and c<8 and c>-1 and hak!=2:
        if a!=9:
            if location[column[c] + str(a)] not in player_x and location[column[c] + str(a)] not in kings:
                squares_to_go.append(column[c] + str(a))
        a-=1
        hak+=1
        c-=1
    c=column_index-1
    hak=0
    while c<8 and c>-1 and b>-1 and hak!=2:
        if b!=0:
            if location[column[c] + str(b)] not in player_x and location[column[c] + str(b)] not in kings:
                squares_to_go.append(column[c] + str(b))
        c-=1
        b+=1
        hak+=1
    d=column_index+1
    hak=0
    a = int(check[1]) + 2
    while a<10  and d<8 and d>-1 and hak!=2 :
        if a!=9:
            if location[column[d] + str(a)] not in player_x and location[column[d] + str(a)] not in kings:
                squares_to_go.append(column[d] + str(a))
        d+=1
        a-=1
        hak+=1
    d=column_index+1
    hak=0
    b = int(check[1]) - 2
    while d<8 and d>-1 and b>-1 and hak!=2:
        if b!=0:
            if location[column[d] + str(b)] not in player_x and location[column[d] + str(b)] not in kings:
                squares_to_go.append(column[d] + str(b))
        d+=1
        b+=1
        hak+=1
    a= column.index(check[0]) - 1
    b= column.index(check[0]) + 1
    c= int(check[1]) - 1
    d= int(check[1]) + 1
    check_list=[]
    if a>-1 and d<9:
        check_list.append(column[a] + str(d))
    if a>-1 and c>0:
        check_list.append(column[a] + str(c))
    if b<8 and d<9:
        check_list.append(column[b] + str(d))
    if b<8 and c>0:
        check_list.append(column[b] + str(c))
    for i in check_list:
        if (location[i] not in player_x) and (location[i] not in player_y) and location[i] not in kings:
            squares_to_go.append(i)
    return squares_to_go
def king(check, player_x, x):
    squares_to_go=[]
    b = int(check[1]) + x
    if b > 0 and b<9 and location[check[0] + str(b)] not in player_x  and location[check[0] + str(b)] not in kings :
        squares_to_go.append(check[0] + str(b))
    a = column.index(check[0]) - 1
    c = column.index(check[0]) + 1
    if c<8 and b>0 and b<9 and location[column[c] + str(b)] not in player_x and location[column[c] + str(b)] not in kings:
        squares_to_go.append(column[c] + str(b))
    if a>-1 and b>0 and b<9 and location[column[a] + str(b)] not in player_x and location[column[a] + str(b)] not in kings:
        squares_to_go.append((column[a] + str(b)))
    if c < 8 and b>0 and b<9 and location[column[c] + str(check[1])] not in player_x and location[column[c] + str(check[1])] not in kings:
        squares_to_go.append(column[c] + check[1])
    if a > -1 and  b>0 and b<9 and location[column[a] + str(check[1])] not in player_x and location[column[c] + str(check[1])] not in kings:
        squares_to_go.append(column[a] + check[1])
    return squares_to_go
def queen(check, player_x, player_y):
    a=rook(check, player_x, player_y)
    b=bishop1(check, player_x, player_y)
    c=bishop2(check, player_x, player_y)
    return a+b+c
def printboard():#It prints the status of the board to the console.
    list1=[]
    print("------------------------")
    for i in range(8,0,-1):
        list2=[]
        for j in column:
            x=j+str(i)
            list2.append(x)
            if x not in location:
                location[x]= "  "
        list1.append(list2)
    for i in list1:
        for j in i:
            print(location[j], end=" ")
        print()
    print("------------------------")
def showmove():#Lists the possible target positions of the given piece can move.
    squares_to_go=[]
    if ask_place == "R1" or ask_place == "R2":
        squares_to_go = rook(check, player_one, player_two)
    if ask_place == "r1" or ask_place == "r2":
        squares_to_go = rook(check, player_two, player_one)
    if ask_place == "B1" or ask_place == "B2":
        squares_to_go = bishop1(check, player_one, player_two)
    if ask_place == "b1" or ask_place == "b2":
        squares_to_go = bishop2(check, player_two, player_one)
    if ask_place in pawn_1:
        squares_to_go = pawn(check, player_one, -1)
    if ask_place in pawn_2:
        squares_to_go = pawn(check, player_two, 1)
    if ask_place == "KI":
        squares_to_go = set(king(check, player_one, -1)) | set(king(check, player_one, 1))
        squares_to_go=list(squares_to_go)
    if ask_place == "ki":
        squares_to_go = set(king(check, player_two, -1)) | set(king(check, player_two, 1))
        squares_to_go = list(squares_to_go)
    if ask_place == "QU":
        squares_to_go = queen(check, player_one, player_two)
    if ask_place == "qu":
        squares_to_go = queen(check, player_two, player_one)
    if ask_place == "N1" or ask_place == "N2":
        squares_to_go = knight(check, player_one, player_two)
    if ask_place == "n1" or ask_place == "n2":
        squares_to_go = knight(check, player_two, player_one)
    squares_to_go.sort()
    return squares_to_go
player_one=["R1", "N1", "B1", "QU", "KI","B2", "N2", "R2", "P1", "P2", "P3", "P4", "P5", "P6", "P7", "P8"]
player_two=["r1", "n1", "b1", "qu", "b2","ki","n2", "r2", "p1", "p2", "p3", "p4", "p5", "p6", "p7", "p8"]
kings=["KI","ki"]
pawn_1=["P1", "P2", "P3", "P4", "P5", "P6", "P7", "P8"]
pawn_2=["p1", "p2", "p3", "p4", "p5", "p6", "p7", "p8"]
location={"a8": "R1", "b8": "N1", "c8": "B1", "d8": "QU", "e8": "KI", "f8": "B2", "g8": "N2", "h8": "R2",
        "a1":"r1","b1":"n1","c1":"b1","d1":"qu","e1":"ki","f1":"b2","g1":"n2","h1":"r2",
        "a7":"P1","b7":"P2","c7":"P3","d7":"P4","e7":"P5","f7":"P6","g7":"P7","h7":"P8",
        "a2":"p1","b2":"p2","c2":"p3","d2":"p4","e2":"p5","f2":"p6","g2":"p7","h2":"p8"}
find_location={v: k for k, v in location.items()}
column=["a", "b", "c", "d", "e", "f", "g", "h"]
list1=[]
for i in range(8, 0, -1):
    list2 = []
    for j in column:
        x = j + str(i)
        list2.append(x)
        if x not in location:
            location[x] = "  "
    list1.append(list2)
for i in command:
    a=i[0]
    print(">", end="")
    for k in i:
        print(k,end=" ")
    print()
    if a=="move":#Moves the given piece to the given position
        if i[1] in find_location:
            ask_place=i[1]
            evaluate = find_location[ask_place]
            check = []
            for j in evaluate:
                check.append(j)
            squares_to_go=showmove()
            if i[2] in squares_to_go:
                print("OK")
                moving = i[1]
                place_to_move = i[2]
                a = find_location[i[1]]
                location[a] = "  "
                if i[1] in player_one and location[i[2]] in player_two:
                    del find_location[location[i[2]]]
                if i[1] in player_two and location[i[2]] in player_one:
                    del find_location[location[i[2]]]
                find_location[i[1]] = i[2]
                location[i[2]] = i[1]
            else:
                print("FAILED")
        else:
            print("FAILED")
    if a=="showmoves":
        if i[1] in find_location:
            ask_place=i[1]
            squares_to_go=[]
            evaluate = find_location[ask_place]
            check = []
            for j in evaluate:
                check.append(j)
            squares_to_go=showmove()
            if squares_to_go!=[]:
                for i in squares_to_go:
                    print(i,end=" ")
                print()
            else:
                print("FAILED")
        else:
            print("FAILED")
    if a=="print":
        printboard()
    if a=="initialize":
        print("OK")
        initialize()
    if a=="exit":
        exit()