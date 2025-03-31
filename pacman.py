from ti_draw import *
from time import *
from ti_system import *

"""
Pacman

Version: beta 1.1

Made by:
    DjaydenR
    
Description:
    It's just pacman (ghosts are a work-in-progress)
    
How to share this game: 
    1. Connect two calculators using a cable.
    2. On both calculators, press [2nd] + [x,t,0,n].
    3. On the sending calculator, select 2: All-... 
    4. On the receiving calculator, press RECEIVE 
    5. Find the game in the file list and press send.
"""

maze = [[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], 
        [2, 1, 1, 1, 1, 1, 1, 1, 2, 1, 5, 5, 1, 2, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2], 
        [2, 1, 0, 0, 0, 0, 0, 1, 2, 1, 4, 4, 1, 2, 1, 0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 2], 
        [2, 1, 0, 1, 1, 1, 0, 1, 2, 1, 4, 4, 1, 2, 1, 0, 1, 1, 1, 0, 1, 2, 2, 2, 2, 2], 
        [2, 1, 0, 0, 1, 0, 0, 1, 1, 1, 4, 4, 1, 1, 1, 0, 0, 1, 0, 0, 1, 2, 2, 2, 2, 2], 
        [2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 2, 2, 2, 2, 2], 
        [2, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 2], 
        [2, 1, 0, 0, 0, 0, 0, 1, 0, 1, 4, 4, 1, 0, 1, 0, 1, 0, 0, 0, 1, 2, 2, 2, 2, 2], 
        [2, 1, 1, 1, 0, 1, 0, 1, 0, 1, 4, 4, 4, 0, 1, 0, 1, 0, 1, 1, 1, 2, 2, 2, 2, 2], 
        [2, 1, 0, 3, 0, 1, 0, 1, 0, 1, 4, 4, 1, 0, 1, 0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 2], 
        [2, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 2, 2, 2, 2, 2], 
        [2, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 2], 
        [2, 1, 0, 1, 0, 0, 0, 1, 1, 1, 4, 4, 1, 1, 1, 0, 1, 1, 1, 0, 1, 2, 2, 2, 2, 2], 
        [2, 1, 0, 1, 1, 1, 0, 1, 2, 1, 4, 4, 1, 2, 1, 0, 0, 0, 1, 0, 1, 2, 2, 2, 2, 2], 
        [2, 1, 0, 0, 0, 0, 0, 1, 2, 1, 4, 4, 1, 2, 1, 0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 2], 
        [2, 1, 1, 1, 1, 1, 1, 1, 2, 1, 6, 6, 1, 2, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2], 
        [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]]

points = 0
total_points = sum(row.count(0) for row in maze)
portal_1_y = portal_2_y = 0

def draw_maze():
    set_color(0,0,0)
    fill_rect(-1,-1,321,220)
    set_color(255,255,255)
    draw_text(255,20,"Score: ")
    draw_text(255,35,"0")
    for id_row, row in enumerate(maze):
        for id_column, column in enumerate(row):
            global portal_1_y, portal_2_y
            x = id_column * 12
            y = id_row * 12
            if column == 0: #draw path (with points)
                set_color(255,255,255)
                fill_circle(x+6,y+6,2.5)
            elif column == 1: #draw walls
                set_color(25,25,166)
                fill_rect(x,y,12,12)
            elif column == 4: #path (without points)
                pass
            elif column == 5: #portal 1 or 2
                portal_1_y = y + 6
            elif column == 6: #portal 1 or 2
                portal_2_y = y + 6
            elif column == 3: #draw pacman
                p_x, p_y = x+6, y+6
                set_color(255,255,0)
                fill_circle(x+6,y+6,6)
    return p_x, p_y


def detect_controls(x,y):
    current = [x, y]
    target = [x, y]
    while True:
        key = wait_key()
        if key == 1: #right
            target[0] += 12
        elif key == 2: #left
            target[0] -= 12
        elif key == 3: #up
            target[1] -= 12
        elif key == 4: #down
            target[1] += 12
        elif key in [9, 10, 64]: #clear (exit)
            clear()
            break
        else:
            print("Key not recognised: " + str(key))
            continue
        current, target = verify_controls(current, target)
        sleep(0.001) #delay is needed (I think)

def verify_controls(current, target):
    if detect_colision(target[0], target[1]):
        if target[1] == portal_1_y:
            prev = current.copy()
            target = [current[0], portal_2_y]
            current = target.copy()
        elif target[1] == portal_2_y:
            prev = current.copy()
            target = [current[0], portal_1_y]
            current = target.copy()
        else:
            prev = current.copy()
            current = target.copy()
        draw_pacman(current, prev)
        return current, target
    else:
        target = current.copy()
        return current, target

def detect_colision(p_x, p_y):
    global points, maze

    row = int((p_y - 6 ) / 12)
    column = int((p_x - 6) / 12)

    cell = maze[row][column]

    if cell == 0: #point
        points += 1
        maze[row][column] = 4
        change_score(points)
        return True
    elif cell == 1: #wall
        return False
    elif cell in [3,4]: #claimed point or pacman's starting place
        return True
    elif cell in [5,6]:
        return True
    elif cell == 2: #out of map
        return False
    else:
        print("Position not recognised: " + str(cell))

def draw_pacman(current, prev):
    set_color(0,0,0)
    fill_circle(prev[0],prev[1],6)
    set_color(255,255,0)
    fill_circle(current[0],current[1],6)

def change_score(new_score):
    set_color(0,0,0)
    draw_text(255,35,str(new_score-1))
    set_color(255,255,255)
    draw_text(255,35,str(new_score))
    if new_score == total_points:
        print("Game won!")

def game():
    p_x, p_y = draw_maze() #save location of pacman after drawing maze
    detect_controls(p_x, p_y)

game()