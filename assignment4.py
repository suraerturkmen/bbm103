import sys
import os
def matrix_product(matrix1, matrix2):
    result=[]
    for i in range(len(matrix2)):
        result.append([0])
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j]+=matrix1[i][k]*matrix2[k][j]
    return result
def enc(key):#this function have matched the letters with numbers
    my_dict={"A":1,"a":1,"B":2,"b":2,"C":3,"c":3,"D":4,"d":4,"E":5,"e":5,"F":6,"f":6,"G":7,"g":7,"H":8,"h":8,"I":9,"i":9,"J":10,"j":10,
            "K":11,"k":11,"L":12,"l":12,"M":13,"m":13,"N":14,"n":14,"O":15,"o":15,"P":16,"p":16,"Q":17,"q":17,"R":18,"r":18,"S":19,"s":19,
            "T":20,"t":20,"U":21,"u":21,"V":22,"v":22,"W":23,"w":23,"X":24,"x":24,"Y":25,"y":25,"Z":26,"z":26," ":27}
    length_key=len(key)
    f=open(sys.argv[3],"r")
    input=f.readlines()
    a=0
    new_input=[]
    for i in input:#I append space to string for this the length can divide by length key.txt
        if len(i)%length_key!=0:
            remain=len(i) % length_key
            difference=length_key-remain
            i=i+difference*" "
        add_new_input=[]
        for j in i:#I convert numbers to letters
            a+=1
            letter=my_dict[j]
            add_new_input.append([letter])
            if a%length_key==0:#I separate the letters when "a" is the multiple of the key
                new_input.append(add_new_input)
                add_new_input=[]
    return new_input
def dec(key):#this function convert string input to integer list
    length_key=len(key)
    file=open(sys.argv[3],"r")
    input=file.readlines()
    file.close()
    input=input[0].split(",")
    a = 0
    add_new_input = []
    input_file = []
    for i in input:#I separate the numbers when "a" is the multiple of the key
        a += 1
        add_new_input.append([int(i)])
        if a % length_key == 0:
            input_file.append(add_new_input)
            add_new_input = []
    return input_file
def determinant(matrix):
    if len(matrix)==2:#the base of recursion
        return (matrix[0][0] * matrix[1][1]) - (matrix[1][0] * matrix[0][1])
    row=matrix[0].copy()
    a=0
    det=0
    for i in range(len(row)):
        if a%2==1:
            row[i]=-row[i]
        minor=[]
        for k in matrix[1:]:#with this loop I have found minor
            add=k[:i]+k[i+1:]
            minor.append(add)
        det+=row[i]*determinant(minor)
        a+=1
    return det
def submatrix_determinant(matrix):
    if len(matrix)==2:#the base of recursion
        return (matrix[0][0] * matrix[1][1]) - (matrix[1][0] * matrix[0][1])
    number=11
    my_dict={}
    for i in range(len(matrix)):#I have created submatrix
        for t in range(len(matrix)):
            minor=[]
            submatrix=matrix[:i]+matrix[i+1:]
            for k in submatrix:
                add=k[:t]+k[t+1:]
                minor.append(add)
            determinant_minor=determinant(minor)#I have calculated determinant of minors of submatrix
            my_dict[number]=determinant_minor
            number+=1
        number=number+10-len(matrix)
    return my_dict#this dictionary include the cofactor of the key
def inverse_matrix(new_key_submatrix,matrix):
    det=determinant(matrix)
    other_number = 11#I have used "other_number" for create adjugate matrix
    inverse = []
    add_inverse=[]
    for i in range(len(key) * len(key)):
        t = 0
        for j in str(other_number):
            t += int(j)
        print(int((str(other_number)[::-1])))
        print(new_key_submatrix)
        x = new_key_submatrix[int((str(other_number)[::-1]))]#I select the dictionary value for adjugate matrix
        add_inverse.append(((-1) ** (t) * x) / det)#this result equal to one element of inverse
        if (i + 1) % len(key) == 0:
            inverse.append(add_inverse)
            add_inverse = []
            other_number = other_number + 10 - len(key)
        other_number += 1
    return inverse

characters=["A", "a", "B", "b", "C", "c", "D", "d", "E", "e", "F", "f", "G", "g", "H", "h", "I", "i",
           "J","j","K","k","L","l","M","m","N","n","O","o","P","p","Q","q","R","r",
           "S","s","T","t","U","u","V","v","W","w","X","x","Y","y","Z","z"," "]
try:
    assert len(sys.argv)==5
except AssertionError:
    print("Parameter number error")
else:
    try:
        assert os.path.exists(sys.argv[2])
        if sys.argv[2][-3:] != "txt":
            raise IOError
        try:
            f = open(sys.argv[2], "r")
            key = [line.split() for line in f.readlines()]
            assert key != []
            f.close()
            for i in range(len(key)):#check the key
                key[i] = key[i][0].split(",")
                a = 0
                for k in key[i]:
                    key[i][a] = int(k)
                    a += 1
        except (IndexError,ValueError) :
            print("Invalid character in key file error")
            exit()
        except AssertionError:
            print("Key file is empty error")
            exit()
    except AssertionError:
        print("Key file not found error")
    except IOError:
        print("Key file could not be read error")
    else:
        try:
            if sys.argv[1]=="enc":
                try:
                    assert os.path.exists(sys.argv[3])
                    if sys.argv[3][-3:]!="txt":
                        raise Exception
                except AssertionError:
                    print("Input file not found error")
                except:
                    print("The input file could not be read error")
                else:
                    try:
                        f=open(sys.argv[3],"r")
                        file=f.readlines()
                        assert file!=[]
                        try:
                            for i in file:#check the input
                                for j in i:
                                    assert j in characters
                            f.close()
                        except AssertionError:
                            print("Invalid character in input file error")
                            exit()
                    except AssertionError:
                        print("Input file is empty error")
                    else:
                        enc_number = enc(key)#I have matched the letters with the numbers
                        encrypted = []
                        for i in enc_number:
                            result = matrix_product(key, i)
                            encrypted.append(result)
                        output = open(sys.argv[4], "w")
                        write_this = ""
                        for i in encrypted:
                            for k in i:
                                write_this += str(k[0]) + ","
                        output.write(write_this[:-1])
                        output.close()
            elif sys.argv[1]=="dec":
                t=submatrix_determinant(key)#I have found submatrix determinant for calculate inverse
                inverse=inverse_matrix(t, key)
                my_dict = {1: "A", 2: "B", 3: "C", 4: "D", 5: "E", 6: "F", 7: "G", 8: "H", 9: "I",
                            10: "J", 11: "K",12: "L",13: "M", 14: "N", 15: "O", 16: "P", 17: "Q", 18: "R",
                           19: "S", 20: "T", 21: "U", 22: "V", 23: "W", 24: "X", 25: "Y", 26: "Z", 27: " "}
                decrypted = []
                dec_number = (dec(key))
                for i in dec_number:
                    result = matrix_product(inverse, i)
                    decrypted.append(result)
                output = open(sys.argv[4], "w")
                for k in decrypted:
                    for j in k:
                        for t in j:
                            output.write(my_dict[round(j[0])])
                output.close()
            else:
                raise IOError
        except IOError:
            print("Undefined parameter error")