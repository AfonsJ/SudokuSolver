import random

class Board:
    def __init__(self):
        self.Board = [[0 for _ in range(9)] for __ in range(9)]
        self.Difficulty = 1
        self.genBoard()
        self.pokeHole()

    def __str__(self):
        ret = ""

        ret += "-" * 37 + "\n"
        for row in range(9):
            for col in range(9):
                ret += "| "+str(self.Board[row][col]) + " "
                if col == 8:
                    ret += "|"
            ret += "\n"
            ret += "-"*37 + "\n"
        return ret
    
    def setDifficulty(self, newDiff):
        self.Difficulty = newDiff  

    def setBoard(self, newBoard):
        self.Board = newBoard   
    
    def getBoard(self):
        return self.Board
    
    def getAllSquares(self):
        ret = [[],[],[],[],[],[],[],[],[]]
        for row in range(9):
            for col in range(9):
                tc = col//3
                tr = row//3

                ret[tr*3+tc].append(self.Board[row][col])

        return ret
    
    def getCell(self, row, col):
        return self.Board[row][col]

    def genBoard(self):
        nums = [1,2,3,4,5,6,7,8,9]
        random.shuffle(nums)

        for row in range(9):
            for col in range(9):
                if self.Board[row][col] == 0:
                    for num in nums:
                        if self.checkAll(row, col, num):
                            self.Board[row][col] = num
                            if self.genBoard():
                                return True
                            self.Board[row][col] = 0
                    return False
        return True 

    def pokeHole (self):
        toPoke = 0
        match self.Difficulty:
            case 1:
                toPoke = random.randint(30,40)
            case 2:
                toPoke = random.randint(40,50)
            case 3:
                toPoke = random.randint(50,64)

        for i in range(toPoke):
            row = random.randint(0,8)
            col = random.randint(0,8)
            self.Board[row][col] = 0    

    def refreshBoard(self):
        self.Board = [[0 for _ in range(9)] for __ in range(9)]
        self.genBoard()
        self.pokeHole()

    def checkAll(self, row, col, num):
        if(self.validSquare(row, col, num) and self.validRow(row, num) and self.validCol(col, num)):
            return True
        return False
    
    def validSquare(self, row, col, num):
        tempR = row//3 *3
        tempR2 = tempR + 3
        tempC = col//3 *3
        tempC2 = tempC + 3

        for i in range(tempR, tempR2):
            for j in range(tempC, tempC2):
                if self.Board[i][j] == num:
                    return False
        return True
    
    def validRow(self, row, num):
        for i in range(9):
            if self.Board[row][i] == num:
                return False
        return True

    def validCol(self, col, num):
        for i in range(9):
            if self.Board[i][col] == num:
                return False
        return True
