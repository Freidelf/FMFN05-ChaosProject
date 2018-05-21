import random
import sys

#strogatz nonlinear dynamics and chaos
class Water:
    xpos = X
    ypos = Y
    moved = 0
    
    def __init__(self, X, Y):
        self.xpos = X
        self.ypos = Y
        self.moved = 0
        
    def move(self):
        return
    
    def isFish(self):
        return False
    
    def isShark(self):
        return False
    
    def isWater(self):
        return True

cols, rows = 200,200;
Dim = 1000; 
SET_INIT_COND = 0;
Fishes = 0
Sharks = 0
PLOT_LENGTH = 500
SHOW_PLOT = 0
FishArray = [0]*PLOT_LENGTH
SharkArray = [0]*PLOT_LENGTH
counter = 0

file = open('nbr_of_animals.txt', "w")

CURRENTmatrix = [[Water(x,y) for x in range(cols)] for y in range(rows)];

def setup():
    size(Dim, Dim)
    background(255)
    
    
def draw():
    global Sharks
    global Fishes
    global counter
    global FishArray
    global SharkArray
    counter = (counter + 1)%PLOT_LENGTH
    print("antal hajar: " + str(Sharks) + "antal fiskar: " + str(Fishes))
    file.writelines(str(Sharks) + "," + str(Fishes) + "\n" )
    if SET_INIT_COND == 0:
        initCondition()
    else:
        frameRate(60)
        t = random.randint(1,4)
        for i in range(cols):
            for j in range(rows):
                if t == 1:
                    i = -i
                if t == 2:
                    j = -j
                if t == 3:
                    i = -i
                    j = -j
                chronon(i,j)
        
        for i in range(cols):
            for j in range(rows):
                temp = CURRENTmatrix[i][j]
                CURRENTmatrix[i][j].moved = 0
                if temp.isWater():
                    fill(0)
                elif temp.isFish():
                    fill(0,0,255)
                elif temp.isShark(): 
                    fill(0,255,0)
                rectMode(CORNER)
                rect(i*Dim/cols,j*Dim/rows,Dim/cols,Dim/rows)
    FishArray[counter] = Fishes
    SharkArray[counter] = Sharks
    
    if SHOW_PLOT == 1:
        # fill(255)
        # rect(Dim/2,2*Dim/4,Dim/2,Dim/4)
        # for i in range(PLOT_LENGTH):
        #     fill(255,0,0)
        #     rect(Dim/2 + i, 3*Dim/4 - FishArray[i]/(Dim/5),1,1)
        #     fill(0)
        fill(255)
        rect(Dim/2,2*Dim/4,Dim/2,Dim/4)
        for i in range(PLOT_LENGTH):
            fill(0)
            rect(Dim/2 + 10 + FishArray[i]/(Dim/40), 3*Dim/4 - 10 - SharkArray[i]/(Dim/40),1,1)
            stroke(0)
            line(Dim/2 + 10, 3*Dim/4, Dim/2 + 10, Dim/2)
            line(Dim/2, 3*Dim/4 - 10, Dim, 3*Dim/4 - 10)
            noStroke()         
        
def initCondition():
        noStroke()
        for i in range(cols):
            for j in range(rows):
                temp = CURRENTmatrix[i][j]
                if temp.isWater():
                    fill(0)
                elif temp.isFish():
                    fill(0,0,255)
                elif temp.isShark(): 
                    fill(0,255,0)
                rectMode(CORNER)
                rect(i*Dim/cols,j*Dim/rows,Dim/cols,Dim/rows)

def chronon(x,y):
    if (CURRENTmatrix[x][y].moved == 0):
        CURRENTmatrix[x][y].moved = 1
        CURRENTmatrix[x][y].move()
        
def keyPressed():
    global SET_INIT_COND
    global SHOW_PLOT
    global Fishes
    global Sharks
    if key == BACKSPACE:
        SHOW_PLOT = 1       
    if key == ENTER:
        if SET_INIT_COND == 0:
            SET_INIT_COND = 1
        else:
            SET_INIT_COND = 0
    if key == TAB:
        Fishes = 0
        Sharks = 0
        for i in range(cols):
            for j in range(rows):
                d = random.randint(0,500)
                if d < 400:
                    CURRENTmatrix[i][j] = Water(i,j)
                elif d < 494:
                    CURRENTmatrix[i][j] = Fish(i,j)
                else:
                    CURRENTmatrix[i][j] = Shark(i,j)

def keyReleased():
    global SHOW_PLOT
    if key == BACKSPACE:
        SHOW_PLOT = 0
        
def mousePressed():
    if mouseButton == LEFT:
            temp = CURRENTmatrix[floor(mouseX/(Dim/rows))][floor(mouseY/(Dim/cols))]
            if temp.isWater():
                CURRENTmatrix[floor(mouseX/(Dim/rows))][floor(mouseY/(Dim/cols))] = Shark(floor(mouseX/(Dim/rows)), floor(mouseY/(Dim/cols)))
            elif temp.isShark():
                Sharks -= 1
                CURRENTmatrix[floor(mouseX/(Dim/rows))][floor(mouseY/(Dim/cols))] = Fish(floor(mouseX/(Dim/rows)), floor(mouseY/(Dim/cols)))
            elif temp.isFish:
                Fishes -=1
                CURRENTmatrix[floor(mouseX/(Dim/rows))][floor(mouseY/(Dim/cols))] = Water(floor(mouseX/(Dim/rows)), floor(mouseY/(Dim/cols)))
                
class Fish:
    xpos = X
    ypos = Y
    ReprodTimer = 0.0
    moved = 0
    
    def __init__(self, X, Y):
        self.xpos = X
        self.ypos = Y
        global Fishes
        Fishes += 1
    
    def move(self):
        self.xpos = self.xpos%cols
        self.ypos = self.ypos%rows
        surrounding = [CURRENTmatrix[self.xpos%cols][(self.ypos + 1)%rows], CURRENTmatrix[(self.xpos + 1)%cols][self.ypos%rows], CURRENTmatrix[self.xpos%cols][(self.ypos - 1)%rows], CURRENTmatrix[(self.xpos - 1)%cols][self.ypos%rows]]
        p = ["down","right","up","left"]
        possibilities = []
        oldx = self.xpos%rows
        oldy = self.ypos%cols
        for i in range(4):
            if surrounding[i].isWater():
                possibilities.append(p[i])
        if possibilities:
            decision = random.choice(possibilities)
            if decision == "up":
                self.ypos -= 1
            elif decision == "right":
                self.xpos += 1
            elif decision == "down":
                self.ypos += 1
            elif decision == "left":
                self.xpos -= 1
            global toDraw
            # toDraw.append((oldx%rows,oldy%cols))
            # toDraw.append((self.xpos%rows,self.ypos%cols))
            CURRENTmatrix[self.xpos%rows][self.ypos%cols] = self
            if self.ReprodTimer > 1:
                CURRENTmatrix[oldx][oldy] = Fish(oldx,oldy)
                self.ReprodTimer = 0.0
            else:
                CURRENTmatrix[oldx][oldy] = Water(oldx,oldy)

        self.ReprodTimer += 0.08
                
    def isFish(self):
        return True
    
    def isShark(self):
        return False
    
    def isWater(self):
        return False
    

class Shark:
    moved = 0
    xpos = X
    ypos = Y
    ReprodTimer = 0.0
    Energy = 0
    global Fishes
    global Sharks
    
    def __init__(self, X, Y):
        self.xpos = X
        self.ypos = Y
        global Sharks
        Sharks += 1
        self.Energy = 0.7
        
    def move(self):
        if self.Energy < 0.0:
            # toDraw.append((self.xpos%rows,self.ypos%cols))
            CURRENTmatrix[self.xpos%cols][self.ypos%rows] = Water(self.xpos%cols, self.ypos%rows)
            global Sharks
            Sharks -= 1
            return
        self.xpos = self.xpos%cols
        self.ypos = self.ypos%rows
        surrounding = [CURRENTmatrix[self.xpos%cols][(self.ypos + 1)%rows], CURRENTmatrix[(self.xpos + 1)%cols][self.ypos%rows], CURRENTmatrix[self.xpos%cols][(self.ypos - 1)%rows], CURRENTmatrix[(self.xpos - 1)%cols][self.ypos%rows]]
        p = ["down","right","up","left"]
        possibilitiesWater = []
        possibilitiesFish = []
        oldx = self.xpos
        oldy = self.ypos
        for i in range(4):
            if surrounding[i].isWater():
                possibilitiesWater.append(p[i])
            if surrounding[i].isFish():
                possibilitiesFish.append(p[i])
        if not possibilitiesFish:
            if possibilitiesWater:
                decision = random.choice(possibilitiesWater)
                if decision == "up":
                    self.ypos -= 1
                elif decision == "right":
                    self.xpos += 1
                elif decision == "down":
                    self.ypos += 1
                elif decision == "left":
                    self.xpos -= 1
                CURRENTmatrix[self.xpos%cols][self.ypos%rows] = self
                # toDraw.append((oldx%rows,oldy%cols))
                # toDraw.append((self.xpos%rows,self.ypos%cols))
                if self.Energy > 0.95:
                    CURRENTmatrix[oldx][oldy] = Shark(oldx,oldy)
                else:
                    CURRENTmatrix[oldx][oldy] = Water(oldx,oldy)
        else:
            decision = random.choice(possibilitiesFish)
            global Fishes
            Fishes -= 1
            if self.Energy < 0.85:
                self.Energy +=0.15
            if decision == "up":
                self.ypos -= 1
            elif decision == "right":
                self.xpos += 1
            elif decision == "down":
                self.ypos += 1
            elif decision == "left":
                self.xpos -= 1
            CURRENTmatrix[self.xpos%cols][self.ypos%rows] = self
            # toDraw.append((oldx%rows,oldy%cols))
            # toDraw.append((self.xpos%rows,self.ypos%cols))
            if self.Energy > 0.98:
                CURRENTmatrix[oldx][oldy] = Shark(oldx,oldy)
            else:
                CURRENTmatrix[oldx][oldy] = Water(oldx,oldy)
        self.Energy -= 0.04

    def isFish(self):
        return False
    
    def isShark(self):
        return True
    
    def isWater(self):
        return False
    
