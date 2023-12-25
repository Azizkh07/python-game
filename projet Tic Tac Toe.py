from random import randrange
board = [['1','2','3'],['4','X','6'],['7','8','9']]
def display_board(board): 
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   " + board[0][0] +   "   |   " +   board[0][1] +  "   |   " + board[0][2] + "   |")    
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   " + board[1][0] +   "   |   " +   board[1][1] +  "   |   " + board[1][2] + "   |")  
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   " + board[2][0] +   "   |   " +   board[2][1] +  "   |   " + board[2][2] + "   |")  
    print("|       |       |       |")
    print("+-------+-------+-------+")
   
def enter_move(board):
    while True:
        move = int(input("please choose a number within the range of square"))
        if move <1 or move > 9:
            print("please pick a number in range 1 to 9")
            continue
        elif str(move) not in board[0] and str(move) not in board[1] and str(move) not in board[2]:
            print("place taken please select another")
            continue
        elif move ==1:
            board[0][0]='O'
        elif move ==2:
            board[0][1]='O'
        elif move==3:
            board[0][2]='O'
        elif move==4:
            board[1][0]='O'
        elif move==6:
            board[1][2]='O'
        elif move==7:
            board[2][0]='O'
        elif move==8:
            board[2][1]='O'
        elif move==9:
            board[2][2]='O'
        break    
        
        
def make_list_of_free_fields(board):
    global free_squares
    free_squares =[]
    for row in range(0,3):
        for column in range(0,3):
            if board[row][column] == 'X'or board[row][column]=='O':
                pass
            else:
                free_squares.append(([row],[column]))
        print(free_squares)        

def victory_for(board, sign):
    if sign =="O":
        print('checking to see if you are a winner')
    else:
        print('checking to see if the computer is the winner')
    if board[0][0]==sign and board[0][1]==sign and board[0][2]==sign:
        return True
    elif board[1][0]==sign and board[1][1]==sign and board[1][2]==sign:
        return True
    elif board[2][0]==sign and board[2][1]==sign and board[2][2]==sign:
        return True
    elif board[0][0]==sign and board[1][0]==sign and board[2][0]==sign:
        return True
    elif board[0][1]==sign and board[1][1]==sign and board[2][1]==sign:
        return True
    elif board[0][2]==sign and board[1][2]==sign and board[2][2]==sign:
        return True
    elif board[0][0]==sign and board[1][1]==sign and board[2][2]==sign:
        return True
    elif board[2][0]==sign and board[1][1]==sign and board[0][2]==sign:
        return True
    else:
        print("we dont have a winner yet")
        

def draw_move(board):
    while True:
        row = randrange(3)
        column=randrange(3)
        if ([row],[column]) not in free_squares:
            continue
        else:
            board[row][column]='X'
            return 
        
board = [['1','2','3'],['4','X','6'],['7','8','9']]
numberofmoves = 1
human='O'
computer='X'
print("Welcome to tic tac toe")
display_board(board)
print()

while numberofmoves < 9:
    enter_move(board)
    numberofmoves +=1
    display_board(board)
    if victory_for(board, human)==True:
        print('You won!')
        break
    else:
        print('here is the current list of free squares')
        make_list_of_free_fields(board)
        print()
        display_board(board)
        
    print()
    print("time for the computer's move")
    draw_move(board)
    numberofmoves +=1
    display_board(board)
    print()
    
    if victory_for(board, computer)==True:
        print("computer won!")
        break
    else:
        print('here is the current list of free squares')
        make_list_of_free_fields(board)
        print()
        display_board(board)
else:
    print('Tie Game!')
print('thank you for playing!')    


