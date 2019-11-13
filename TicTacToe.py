#Programming Python 1 & 2
#Tic-Tac-Toe
#Kaydon Payne
#11/11/19

#Global Constants
X = "☘️"
O = "©"
Empty = " "
Num_Squares = 9

#Working
def intro():
    """Display Game Instructions"""
    print("""
    Welcome to the greatest intellectual challenge of all time: Tic-Tac-Toe.
    This will be a showdown between your human brain and my silicon processor.

    You will make your move known by by entering a number 1-9. The number
    will correspond to the board position as illustrated:

                            1 | 2 | 3
                           -----------
                            4 | 5 | 6
                           -----------
                            7 | 8 | 9


    Prepare yourself, human. The Ultimate Battle is about to begin.\n
""")
# Working
def new_board():
    board = []
    for i in range (Num_Squares):
        board.append(Empty)
    return board

#Working
def display_board():
    """ display Game Board On Screen"""
    print(str.format("""

                        {0} | {1} | {2}
                       ------------------
                        {3} | {4} | {5}
                       ------------------
                        {6} | {7} | {8}
""",board[0],board[1],board[2],
        board[3],board[4],board[5],
        board[6],board[7],board[8]))


#Working
def ask_yes_no(question):
    """ ask a yes no question and give a one letter response"""
    response = None
    while response not in ("y","n","yes","no"):
        response = input(question).lower()
    x = response[0]    
    return x


#Working
def ask_number(question, low, high):
    response = None
    while response not in range(low, high):
       try:
           response = int(input(question))
       except:
           print("Invalid Input, Not a Number")
    return response




def assign_piece():
    go_first = ask_yes_no("Do You Want to Go First")
    if go_first == "y":
        human = X
        comp  = O
    else:
        comp = X
        human = O
    return comp, human
comp, player = assign_piece()
print (player)
print (comp)
