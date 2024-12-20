def print_board(board):
    for i in range(len(board)):
        print(" ".join([str(x) for x in board[i]]))

my_list=[]
for i in range(8):
    my_list.append([0]*8)
for row in range(8):
    for column in range(8):
        if row<3 or row>4:
            if (row+column)%2==1:
                my_list[row][column]=1
print_board(my_list)
