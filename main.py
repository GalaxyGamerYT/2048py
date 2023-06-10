from random import randint
from colorama import Fore, init
from copy import deepcopy
from time import sleep
import keyboard
from sys import exit

from support import linearAddCheck, linearCheck, linearCompressCheck

init(autoreset=True)

class Game:
    def __init__(self, width:int, height:int):
        self.width = width
        self.height = height
        
        self.board = [[0 for _ in range(self.width)] for _ in range(self.height)]
        # self.board = [[0,0,1,2],[0,2,1,0],[0,0,0,1],[2,0,4,2]]
        # self.printBoard()
        
        self.running = True
    
    def printBoard(self):
        colouredBoard = self.checkColours()
        for col in colouredBoard:
            print("┼───"*self.width+"┼")
            r = ""
            for row in col:
                r += f"│ {row} "
            print(r+"│")
        print("┼───"*self.width+"┼")
    
    def checkColours(self) -> list:
        board = deepcopy(self.board)
        colours = [Fore.WHITE, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA, Fore.RED]
        for colIndex,col in enumerate(self.board):
            for rowIndex,row in enumerate(col):
                if row == 0:
                    board[colIndex][rowIndex] = colours[row]+" "+Fore.RESET
                else:
                    board[colIndex][rowIndex] = colours[row]+str(row)+Fore.RESET
        return board
    
    def place(self):
        if linearCheck(self.board,0):
            counter = 0
            while counter < 2:
                added = (randint(0,3),randint(0,3))
                if linearAddCheck(self.board,added):
                    self.board[added[0]][added[1]] = 1
                    counter += 1
            self.printBoard()
    
    def compress(self, direction:str):
        linearCompressCheck(self.board,direction)
    
    def combine(self, direction:str):
        self.compress(direction)
    
    def checkInput(self):
        eventCatching = True
        while eventCatching:
            event = keyboard.read_event()
            key = event.name
            if event.event_type == keyboard.KEY_UP:
                if key == "up":
                    print("UP KEY PRESSED")
                    eventCatching = False
                    self.combine("up")
                if key == "right":
                    print("RIGHT KEY PRESSED")
                    eventCatching = False
                    self.combine("right")
                if key == "down":
                    print("DOWN KEY PRESSED")
                    eventCatching = False
                    self.combine("down")
                if key == "left":
                    print("LEFT KEY PRESSED")
                    eventCatching = False
                    self.combine("left")
                if key == "esc":
                    exit()
    
    def play(self):
        while self.running:
            self.place()
            self.checkInput()

def menu():
    while True:
        print("-----MENU-----\nOption 1: Play\nOption 2: Quit\n--------------\nChoose an option[1-2]:")
        choice = input()
        try:
            choice = int(choice)
        except:
            print(f"{Fore.BLUE}{choice}{Fore.RED} is not an option")
        else:
            if choice == 1:
                game = Game(4,4)
                game.play()
            elif choice == 2:
                exit()
            else:
                print(f"{Fore.BLUE}{choice}{Fore.RED} is not an option")

if __name__ == "__main__":
    # game = Game(4,4)
    # print("\n")
    # game.play()
    menu()