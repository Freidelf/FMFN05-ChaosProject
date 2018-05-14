cols, rows = 20,20;
Dim = 640; 
SET_INIT_COND = 0;
SHOW_COUNT = 0;

LANDmatrix = [[0 for x in range(cols)] for y in range(rows)];
ANIMALmatrix = [[0 for x in range(cols)] for y in range(rows)];
def setup():
    size(Dim, Dim)
    background(255)

def draw():
    animalCount = countAnimals()
    if SET_INIT_COND == 0:
        initCondition()
    else:
        fill(255)
        rect(5,5,Dim/cols,Dim/rows)
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
                temp1 = LANDmatrix[i][j]
                temp2 = ANIMALmatrix[i][j]
                if temp1 == 0:
                    fill(255, 204, 102)
                elif temp1 == 1:
                    fill(0, 102, 255)
                elif temp1 == 2:
                    fill(51, 153, 51)
                elif temp1 == 3:
                    fill(153, 255, 153)
                if temp2 == 1:
                    fill(0)
                rectMode(CORNER)
                rect(i*Dim/cols,j*Dim/rows,Dim/cols,Dim/rows)

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
        temp = LANDmatrix[floor(mouseX/(Dim/rows))][floor(mouseY/(Dim/cols))];
        if temp == 0:
            LANDmatrix[floor(mouseX/(Dim/rows))][floor(mouseY/(Dim/cols))] = 1
        elif temp == 1:
            LANDmatrix[floor(mouseX/(Dim/rows))][floor(mouseY/(Dim/cols))] = 2
        elif temp == 2:
            LANDmatrix[floor(mouseX/(Dim/rows))][floor(mouseY/(Dim/cols))] = 3
        elif temp == 3:
            LANDmatrix[floor(mouseX/(Dim/rows))][floor(mouseY/(Dim/cols))] = 0
    else:
        temp = ANIMALmatrix[floor(mouseX/(Dim/rows))][floor(mouseY/(Dim/cols))];
        if temp == 0:
            ANIMALmatrix[floor(mouseX/(Dim/rows))][floor(mouseY/(Dim/cols))] = 1
        else:
            ANIMALmatrix[floor(mouseX/(Dim/rows))][floor(mouseY/(Dim/cols))] = 0
            
def countAnimals():
    sum = 0;
    for i in range(cols):
            for j in range(rows):
                sum = sum + ANIMALmatrix[i][j]
    return sum
