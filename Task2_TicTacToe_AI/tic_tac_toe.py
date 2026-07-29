board = [
    [' ',' ',' '],[' ',' ',' '],[' ',' ',' ']                      # initially the board is empty
]

def print_board(board): 
    print()
    for row in board:                          
        print(" " + "|".join(row))
        print("-" * 9)
    print()
                        
current_player = "X"


#----------CHECKING WINNER------------
def check_winner(board):
     for row in board:                       
          if row[0] == row[1] == row[2] and row[0]!= " ":
               return row[0]

     for column in range(3):                 
          if board[0][column] == board[1][column] == board[2][column] and board[0][column]!=" ":
               return board[0][column]

     if board[0][0] == board[1][1] == board[2][2] != " ":         
          return board[0][0]

     if board[0][2] == board[1][1] == board[2][0] and board[0][2]!=" ":      
          return board[0][2]

     return None          
    

#--------CHECKING IF BOARD IS FULL OR NOT-----------
def check_draw(board):
     for row in board:
          for cell in row:
               if cell == " ":            
                    return False
     return True


#-----------CHECKING AVAIALBLE MOVES--------
def get_available_moves(board):             
     moves=[]
     for row in range(3):
          for column in range(3):
               if board[row][column] == " ":
                    moves.append((row,column))
     return moves


#----------MINIMAX ALGORITHM-----------
def minimax(board, is_ai_turn):                 
    winner = check_winner(board)           

    # Base Cases                
    if winner == "X":             
        return -1
    if winner == "O":            
        return 1
    if check_draw(board):
        return 0

    # AI's Turn (Maximizer)
    if is_ai_turn:                
        best_score = -1000      

        for row, col in get_available_moves(board):
            board[row][col] = "O"  
            score = minimax(board, False)               
            board[row][col] = " "
            best_score = max(best_score, score)
        return best_score

    # Human's Turn (Minimizer)
    else:
        best_score = 1000

        for row, col in get_available_moves(board):
            board[row][col] = "X"
            score = minimax(board, True)
            board[row][col] = " "
            best_score = min(best_score, score)
        return best_score


#----------FINDING BEST MOVE-----------
def find_best_move(board):
    best_score = -1000
    best_move = None

    for row, col in get_available_moves(board):
        board[row][col] = "O"
        score = minimax(board, False)
        board[row][col] = " "
        if score > best_score:
            best_score = score
            best_move = (row, col)
    return best_move


# ----GAME LOOP-------
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Tic Tac Toe AI")
root.geometry("400x560")
root.configure(bg="#dff6ff")
root.resizable(False, False)

current_player = "X"
buttons = []

title = tk.Label(root,text="Tic Tac Toe AI",font=("Arial",20,"bold"),bg="#dff6ff",fg="#0077b6")
title.pack(pady=10)

status = tk.Label(root,text="Your Turn (X)",font=("Arial",14,"bold"),bg="#dff6ff",fg="green")
status.pack()

frame = tk.Frame(root,bg="#dff6ff")
frame.pack(pady=15)


def update_buttons():
    for i in range(3):
        for j in range(3):
            buttons[i][j]["text"] = board[i][j]

            if board[i][j] == "X":
                buttons[i][j]["fg"] = "red"

            elif board[i][j] == "O":
                buttons[i][j]["fg"] = "blue"


def disable_board():
    for row in buttons:
        for btn in row:
            btn.config(state="disabled")


def ai_move():
    global current_player
    status.config(text="AI Thinking...",fg="blue")
    root.update()

    move = find_best_move(board)

    if move is None:
        return
    row,column = move
    board[row][column] = "O"
    update_buttons()
    winner = check_winner(board)

    if winner:
        messagebox.showinfo("Winner","AI Wins!")
        disable_board()
        return

    if check_draw(board):
        messagebox.showinfo("Game Over","It's a Draw!")
        disable_board()
        return

    current_player = "X"
    status.config(text="Your Turn (X)",fg="green")


def click(row,column):
    global current_player

    if current_player != "X":
        return

    if board[row][column] != " ":
        messagebox.showwarning("Oops","Cell already occupied!")
        return

    board[row][column] = "X"
    update_buttons()
    winner = check_winner(board)

    if winner:
        messagebox.showinfo("Winner","You Win!")
        disable_board()
        return

    if check_draw(board):
        messagebox.showinfo("Game Over","It's a Draw!")
        disable_board()
        return

    current_player="O"
    root.after(500,ai_move)


def restart():
    global board,current_player
    board=[
        [' ',' ',' '],[' ',' ',' '],[' ',' ',' ']
    ]

    current_player="X"
    status.config(text="Your Turn (X)",fg="green")

    for row in buttons:
        for btn in row:
            btn.config(text=" ",fg="black",state="normal")


for i in range(3):
    temp=[]
    for j in range(3):
        btn=tk.Button(frame,text=" ",width=4,height=2,font=("Arial",24,"bold"),bg="white",relief="raised",bd=3,command=lambda r=i,c=j:click(r,c))
        btn.grid(row=i,column=j,padx=5,pady=5)
        temp.append(btn)
    buttons.append(temp)


restart_btn=tk.Button(root,text="🔄 Restart",font=("Arial",14,"bold"),bg="#28a745",fg="white",width=15,command=restart)
restart_btn.pack(pady=5)

root.mainloop()
