def checkwin(mat):
    for p in range(3):
        for q in range(3):
            print(mat[p][q],end=" ")
        print()
    for m in range(3):
        if ((mat[m][0]=='X' and mat[m][1]=='X' and mat[m][2]=='X')or 
            (mat[0][m]=='X' and mat[1][m]=='X' and mat[2][m]=='X')):
            print("X win")
            return(1)
    if ((mat[0][0]=='X' and mat[1][1]=='X' and mat[2][2]=='X')or 
        (mat[0][2]=='X' and mat[1][1]=='X' and mat[2][0]=='X')):
        print("X win")
        return(1)
    for m in range(3):
        if((mat[m][0]=='O' and mat[m][1]=='O' and mat[m][2]=='O')or
           (mat[0][m]=='O' and mat[1][m]=='O' and mat[2][m]=='O')):
            print("O win")
            return(1)
    if ((mat[0][0]=='O' and mat[1][1]=='O' and mat[2][2]=='O')or 
        (mat[0][2]=='O' and mat[1][1]=='O' and mat[2][0]=='O')):
        print("O win")
        return(1)
    else:
        return (0)
mat=[['-','-','-'],['-','-','-'],['-','-','-']]
for p in range(3):
    for q in range(3):
        print(mat[p][q],end=" ")
    print()
for k in range(9):
    if k%2==0:
        print("player1's turn:")
        print("Ente the position to X(1 to 9)",end=" ")
        pos=int(input())
        pos=pos-1
        i=int(pos/3)
        j=int(pos%3)
        mat[i][j]='X'
        res=checkwin(mat)
        if(res==1):
            break
    if k%2==1:
        print("player2's turn:")
        print("Ente the position to O(1 to 9)")
        pos=int(input())
        pos=pos-1
        i=int(pos/3)
        j=int(pos%3)
        mat[i][j]='O'
        res=checkwin(mat)
        if(res==1):
            break