board = [ "-","-","-","-","-","-","-","-","-" ]

currentplayer = "X"
winner = None
gamerunning = True

def printboard(board):
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("-----")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("-----")
    print(board[6] + "|" + board[7] + "|" + board[8])

def playerinput(board):
    inp = int(input("Enter position 1-9:"))
    if inp >=1 and inp <=9 and board[inp-1]=="-":
        board[inp-1] = currentplayer
        
    else:
        print("Invalid position!")

#check win or tie
def checkhorizontal(board):
     global winner
     if board[0]==board[1]==board[2] and board[0]!="-":
         winner = board[0]
         return True
     elif board[3]==board[4]==board[5] and board[5]!="-":
         winner = board[3]
         return True
     elif board[6]==board[7]==board[8] and board[8]!="-":
         winner = board[9]
         return True
         
def checkrow(board):
    global winner
    if board[0]==board[3]==board[6] and board[0]!="-":
         winner = board[0]
         return True 
    elif board[1]==board[4]==board[7] and board[1]!="-":
         winner = board[1]
         return True
    elif board[3]==board[6]==board[8] and board[3]!="-":
         winner = board[3]
         return True

def checkdiagonal(board):
    global winner
    if board[0]==board[4]==board[8] and board[0]!="-":
         winner = board[0]
         return True
    elif board[2]==board[4]==board[6] and board[2]!="-":
         winner = board[2]
         return True

def checktie(board):
    global gamerunning
    if "-" not in board:
        printboard(board)
        print("It's a tie!")
        gamerunning = False
        
def checkwin():
    global gamerunning
    if checkdiagonal(board) or checkhorizontal(board) or checkrow(board) :
        print("The winner is " + winner )
        gamerunning = False

#switch player
def switchplayer():
    global currentplayer
    if (currentplayer == "X"):
       currentplayer = "O"
    else:
        currentplayer = "X"

##
while gamerunning:
      printboard(board)
      playerinput(board)
      checkwin()
      checktie(board)
      switchplayer()
    