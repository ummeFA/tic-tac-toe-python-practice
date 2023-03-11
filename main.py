from tkinter import*
from tkinter import messagebox

import random

def nextMove(row, column):
    global player
    if buttons[row][column]['text'] =="" and checkWinner() is False:
        if player == players[0]:
            buttons[row][column]['text']=player
            
            if checkWinner() is False:
                player = players[1]
                label.config(text=(players[1]+" turn"))
                
            elif checkWinner() is True:
                label.config(text=(players[0]+" wins"))
            
            elif checkWinner() =="Tie":
                # label.config(text="Tie!")
                messagebox.showinfo("", "Tie!")
                label.config(text=(""))
                
        
        else:
            buttons[row][column]['text']=player
            
            if checkWinner() is False:
                player = players[0]
                label.config(text=(players[0]+" turn"))
                
            elif checkWinner() is True:
                label.config(text=(players[1]+" wins"))
            
            elif checkWinner() =="Tie":
                # label.config(text=("Tie!"))
                messagebox.showinfo("", "Tie!") 
                label.config(text=(""))
                

def checkWinner():
    # Vertical and Horizontal checking
    for row in range(3):
        if buttons[row][0]['text']==buttons[row][1]['text'] ==buttons[row][2]['text']!="":
            return True
        
    for column in range(3):
        if buttons[0][column]['text']==buttons[1][column]['text'] ==buttons[2][column]['text']!="":
            return True
        
    # Diagonal checking
    if buttons[0][0]['text']==buttons[1][1]['text']==buttons[2][2]['text']!="":
        return True
    
    elif buttons[0][2]['text']==buttons[1][1]['text']==buttons[2][0]['text']!="":
        return True
    
    # If there is no empty space even after not finding any matching row or column
    elif emptySpaces() is False:
        return "Tie"
    
    # No winner or tie
    else:
        return False
    
                       

def emptySpaces():
    spaces = 9
    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != "":
                spaces-=1
                
    if spaces==0:
        # When match ties
        return False
    else:
        return True            

def newGame():
    global player
    player = random.choice(players)
    label.config(text=player+ " turn")

    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="",bg="#F0F0F0")
  
        
window = Tk()
window.title("Tic Tac Toe")
players = ["X", "O"]

# Starting with a random player
player = random.choice(players)

# Creating buttons/ board
buttons = [[0,0,0],[0,0,0],[0,0,0]]

label = Label(text=player +" turn", background="lightgray",padx=20, font=('Centaur',35))
label.pack(side="top")

resetButton = Button(text="Reset Game", font=('Centaur', 20),command=newGame)
resetButton.pack(side="top")

frame = Frame(window)
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, background="lightgray",text="", font=('Centaur',35), width=5, height=2, padx=20, pady=15, command = lambda row=row, column=column:nextMove(row,column))
        buttons[row][column].grid(row=row, column=column)
        
window.mainloop()