import random
Feld=[[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "]]
Snake=[[3,10],[3,10],[3,10]]
Gameon=True
Food = False
while not Food:
    random1 = random.randint(0, 5)
    random2 = random.randint(0, 20)
    if random1 != 3 or random2 != 10:
        Feld[random1][random2] = "*"
        Food = True
while Gameon:
    Feld[Snake[-1][0]][Snake[-1][1]] = "#"
    moved = False
    while not moved:
        v = 0
        h = 0
        for a in Feld:
            for a in Feld[v]:
                print (Feld[v][h],end="")
                h+=1
            v+=1
            h=0
            print()
        move = input("#"*21)
        if move == "8":
            if Snake[-1][0]>0:
                Snake.append([Snake[-1][0]-1,Snake[-1][1]])
                moved = True
            else:
                Gameon = False
                moved = True
        elif move == "6":
            if  Snake[-1][1]<20:
                Snake.append([Snake[-1][0],Snake[-1][1]+1])
                moved = True
            else:
                Gameon = False
                moved = True
        elif move == "2":
            if Snake[-1][0]<5:
                Snake.append([Snake[-1][0]+1,Snake[-1][1]])
                moved = True
            else:
                Gameon = False
                moved = True
        elif move == "4":
            if Snake[-1][1]>0:
                Snake.append([Snake[-1][0],Snake[-1][1]-1])
                moved = True
            else:
                Gameon = False
                moved = True
    if Feld[Snake[-1][0]][Snake[-1][1]] == "*":
        Food = False
        while not Food:
            random1 = random.randint(0, 5)
            random2 = random.randint(0, 20)
            if Feld[random1][random2] != "#":
                Feld[random1][random2] = "*"
                Food = True 
    else:
        Feld[Snake[0][0]][Snake[0][1]] = " "
        Snake.pop(0)
    if Feld[Snake[-1][0]][Snake[-1][1]] == "#":
        Gameon = False
    
print("\n"*6 +"Du hast verloren lol")