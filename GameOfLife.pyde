cols, rows = 50,50;
Dim = 1000; 
SET_INIT_COND = 0;
SHOW_COUNT = 0;

ANIMALmatrix = [[0 for x in range(cols)] for y in range(rows)];
PREVIOUSmatrix = [[0 for x in range(cols)] for y in range(rows)];
def setup():
    size(Dim, Dim)
    background(255)

def draw():
    animalCount = countAnimals()
    if SET_INIT_COND == 0:
        initCondition()
    else:
        frameRate(2)
        Play()
    if SHOW_COUNT == 1:
        fill(255)
        rect(5,5,5*Dim/cols, Dim/rows)
        textSize(20)
        fill(0)
        text(str(animalCount) + " animals", Dim/(2*cols),  Dim/cols -3)
    
def initCondition():
        stroke(150)
        for i in range(cols):
            for j in range(rows):
                temp = ANIMALmatrix[i][j]
                if temp == 0:
                    fill(255)
                else:
                    fill(0)
                rectMode(CORNER)
                rect(i*Dim/cols,j*Dim/rows,Dim/cols,Dim/rows)

def Play():
    TEMPmatrix = [[0 for x in range(cols)] for y in range(rows)];
    for i in range(cols):
            for j in range(rows):
                global ANIMALmatrix
                n = neighbourCount(i,j);
                if n == 3:
                    TEMPmatrix[i][j] = 1
                elif n == 2:
                    TEMPmatrix[i][j] = ANIMALmatrix[i][j]
                else:
                    TEMPmatrix[i][j] = 0
    PREVIOUSmatrix = ANIMALmatrix
    ANIMALmatrix = TEMPmatrix
    for i in range(cols):
            for j in range(rows):
                temp = ANIMALmatrix[i][j]
                if temp == 0:
                    fill(255)
                else:
                    fill(0)
                rectMode(CORNER)
                rect(i*Dim/cols,j*Dim/rows,Dim/cols,Dim/rows)

def neighbourCount(posX, posY):
    temp = ANIMALmatrix[posX][posY]
    #print("i = " + str(posX) + ", j = " + str(posY))
    if temp == 1:
        N = -1
    else:
        N = 0  
    for i in range(3):
            for j in range(3):
                if ANIMALmatrix[(posX + i - 1)%rows][(posY + j - 1)%cols] == 1:
     #               print(str((posX + i - 1)%rows) + str((posY + j - 1)%cols))
                    N = N + 1
    if N>0:
        print(str(N))
    
    return N


def keyPressed():
    global SET_INIT_COND
    global SHOW_COUNT
    if key == ENTER:
        SET_INIT_COND = 1
    if key == TAB:
        SHOW_COUNT = 1
            
def keyReleased():
    global SHOW_COUNT
    if key == TAB:
        SHOW_COUNT = 0
            
def mouseClicked():
    if mouseButton == LEFT:
        ANIMALmatrix[floor(mouseX/(Dim/rows))][floor(mouseY/(Dim/cols))] = 1
    else:
        ANIMALmatrix[floor(mouseX/(Dim/rows))][floor(mouseY/(Dim/cols))] = 0
            
def countAnimals():
    sum = 0;
    for i in range(cols):
            for j in range(rows):
                sum = sum + ANIMALmatrix[i][j]
    return sum
