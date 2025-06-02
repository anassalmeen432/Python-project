import tkinter as tk
from tkinter import messagebox

# Initialize game state
xstate = [0] * 9
zstate = [0] * 9
turn = [1]  # Use list to make it mutable in nested functions

# Check for win
def checkwin():
    wins = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    for win in wins:
        if xstate[win[0]] + xstate[win[1]] + xstate[win[2]] == 3:
            messagebox.showinfo("Game Over", "Player X Wins!")
            return True
        if zstate[win[0]] + zstate[win[1]] + zstate[win[2]] == 3:
            messagebox.showinfo("Game Over", "Player O Wins!")
            return True
    if sum(xstate) + sum(zstate) == 9:
        messagebox.showinfo("Game Over", "It's a Draw!")
        return True
    return False

# Handle button click
def on_click(i):
    if xstate[i] == 0 and zstate[i] == 0:
        if turn[0] == 1:
            buttons[i].config(text="X", state='disabled')
            xstate[i] = 1
        else:
            buttons[i].config(text="O", state='disabled')
            zstate[i] = 1

        if checkwin():
            for btn in buttons:
                btn.config(state='disabled')
        else:
            turn[0] = 1 - turn[0]  # Switch turn
    else:
        messagebox.showwarning("Invalid Move", "Cell already taken!")

# Restart game
def reset_game():
    global xstate, zstate
    xstate = [0] * 9
    zstate = [0] * 9
    turn[0] = 1
    for btn in buttons:
        btn.config(text="", state='normal')

# Create main window
root = tk.Tk()
root.title("Tic Tac Toe")

buttons = []

# Create 3x3 grid of buttons
for i in range(9):
    btn = tk.Button(root, text="", font='Helvetica 20', width=5, height=2,
                    command=lambda i=i: on_click(i))
    btn.grid(row=i//3, column=i%3)
    buttons.append(btn)

# Restart button
reset_btn = tk.Button(root, text="Restart", font='Helvetica 12', command=reset_game)
reset_btn.grid(row=3, column=0, columnspan=3, sticky='nsew', pady=10)

root.mainloop()