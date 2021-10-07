import player


class Game:
    def __init__(self):
        self.player = player.Player(1)
        self.player2 = player.Player(2)
        self.gamestate = [0,0,0,0,0,0,0,0,0]

    def signToPrintable(self, sign):
        if sign == 0:
            return " "
        elif sign == 1:
            return "X"
        else:
            return "O"
    
    def isValidTurn(self, cell):
        if self.gamestate[cell] != 0:
            return False
        return True

    def makeTurn(self, cell, player):
        if self.isValidTurn(cell):
            self.gamestate[cell] = player.sign
            return True
        False

    def isFull(self):
        for i in self.gamestate:
            if i == 0:
                return False
        return True

    def checkWin(self, player):
        sign = player.sign
        if self.gamestate[0] == sign and self.gamestate[1] == sign and self.gamestate[2] == sign:
            return True
        elif self.gamestate[3] == sign and self.gamestate[4] == sign and self.gamestate[5] == sign:
            return True
        elif self.gamestate[6] == sign and self.gamestate[7] == sign and self.gamestate[8] == sign:
            return True
        elif self.gamestate[0] == sign and self.gamestate[3] == sign and self.gamestate[6] == sign:
            return True
        elif self.gamestate[1] == sign and self.gamestate[4] == sign and self.gamestate[7] == sign:
            return True
        elif self.gamestate[2] == sign and self.gamestate[5] == sign and self.gamestate[8] == sign:
            return True
        elif self.gamestate[0] == sign and self.gamestate[4] == sign and self.gamestate[8] == sign:
            return True
        elif self.gamestate[2] == sign and self.gamestate[4] == sign and self.gamestate[6] == sign:
            return True          

    def printBoard(self): 
        print(self.signToPrintable(self.gamestate[0]) + " | " + self.signToPrintable(self.gamestate[1]) + " | " + self.signToPrintable(self.gamestate[2]))
        print("---------")
        print(self.signToPrintable(self.gamestate[3]) + " | " + self.signToPrintable(self.gamestate[4]) + " | " + self.signToPrintable(self.gamestate[5]))
        print("---------")
        print(self.signToPrintable(self.gamestate[6]) + " | " + self.signToPrintable(self.gamestate[7]) + " | " + self.signToPrintable(self.gamestate[8]))  

    def startGame(self):
        currPlayer = self.player
        while not self.isFull():
            self.printBoard()
            
            try:
                cell = int(input("set your sign (1-9): ")) -1
            except ValueError:
                print("only numbers from 1-9")
                continue
            
            if cell > 8 or cell < 0:
                print("only numbers from 1-9")
                continue

            if not self.makeTurn(cell, currPlayer):
                print("cell allready occupied")
                
            if self.checkWin(currPlayer):
                if currPlayer == self.player:
                    print("-----------------------")
                    print("player with sign X won")
                    print("-----------------------")
                else:
                    print("-----------------------")
                    print("player with sign O Won")
                    print("-----------------------")
                self.printBoard()
                break

            if currPlayer == self.player:
                currPlayer = self.player2
            else:
                currPlayer = self.player
