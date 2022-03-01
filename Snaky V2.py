try:
    import keyboard
except:
    import pip
    pip.main(["install","keyboard"])
    import keyboard
import random
import time
repeat = True
def Snaky():
    Feld=[[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "]]
    Snake=[[3,10],[3,10],[3,10]]
    Gameon=True
    Food = False
    move = ""
    hardness = 1/float(input("geben sie die Geschwindigkeit an:\n"))
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
            print("\n"*100)
            print("_"*23)
            for a in Feld:
                print("|", end="")
                for a in Feld[v]:
                    print (Feld[v][h],end="")
                    h+=1
                v+=1
                h=0
                print("|", end="\n")
            print("^"*23)
            time.sleep(hardness)
            if keyboard.is_pressed("up"):
               move = "up"
            elif keyboard.is_pressed("right"):
                move = "right"
            elif keyboard.is_pressed("down"):
                move = "down"
            elif keyboard.is_pressed("left"):
                move = "left"
            if move == "up":
                if Snake[-1][0]>0:
                    Snake.append([Snake[-1][0]-1,Snake[-1][1]])
                    moved = True
                else:
                    Gameon = False
                    moved = True
            elif move == "right":
                if  Snake[-1][1]<20:
                    Snake.append([Snake[-1][0],Snake[-1][1]+1])
                    moved = True
                else:
                    Gameon = False
                    moved = True
            elif move == "down":
                if Snake[-1][0]<5:
                    Snake.append([Snake[-1][0]+1,Snake[-1][1]])
                    moved = True
                else:
                    Gameon = False
                    moved = True
            elif move == "left":
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
    input()
while(repeat):
    Snaky()
    eingabe = True
    while(eingabe == True):
        inp = input("Gib 'y' ein um weiter zu spielen und 'n'\n")
        if(inp=="n"):
            eingabe = False
            repeat = False
        elif(inp=="y"):
            eingabe = False