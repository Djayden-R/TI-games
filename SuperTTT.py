from ti_draw import *
from time import *
from ti_system import *
"""
Super-Tic-Tac-TI

Version: beta 1.0

Made by:
    DjaydenR
    
Description:
    You play on a 3x3 grid of Tic-Tac-Toe boards.
    The square in which you place you shape will decide where the next person will play.
    To win you must win 3 boards in a row (vertical, horizontal, or diagonal).
    If the square is already won you get to choose a field yourself.

    
How to share this game: 
    1. Connect two calculator with a cable.
    2. On both calculators, press [2nd] + [x,t,0,n].
    3. On the sending calculator, choose 2: All-... 
    4. On the receiving calculator, press RECEIVE 
    5. Find the game in the file list.
"""

list_xcords = [90,160,230]
list_ycords = [40,110,180]

list_cleared_fields = [0,1,2,3,4,5,6,7,8] #all big fields with place holders, will get replaced if won

x_turn = True
debug_mode = False

all_moves = [
[0,1,2,3,4,5,6,7,8], #field 1 
[0,1,2,3,4,5,6,7,8], #field 2
[0,1,2,3,4,5,6,7,8], #numbers are placeholders
[0,1,2,3,4,5,6,7,8],
[0,1,2,3,4,5,6,7,8],
[0,1,2,3,4,5,6,7,8],
[0,1,2,3,4,5,6,7,8],
[0,1,2,3,4,5,6,7,8],
[0,1,2,3,4,5,6,7,8]]

winning_moves = [
    [0, 1, 2],  # Row 1
    [3, 4, 5],  # Row 2
    [6, 7, 8],  # Row 3
    [0, 3, 6],  # Column 1
    [1, 4, 7],  # Column 2
    [2, 5, 8],  # Column 3
    [0, 4, 8],  # Diagonal 1
    [2, 4, 6]   # Diagonal 2
]

def check_winning(field, big=False):
    global x_turn
    for moves in winning_moves:
        if big == False:
            if all_moves[field][moves[0]] == all_moves[field][moves[1]] == all_moves[field][moves[2]]:
                if all_moves[field][moves[0]] == "x":
                    draw_shape(0,0,big=True,field=field,won="x")
                else:
                    draw_shape(0,0,big=True,field=field,won="o")
        else:
            if list_cleared_fields[moves[0]] == list_cleared_fields[moves[1]] == list_cleared_fields[moves[2]]:
                if list_cleared_fields[moves[0]] == "x":
                    print("Game won by X")
                    sleep(5)
                    raise SystemExit
                else:
                    print("Game won by O")
                    sleep(5)
                    raise SystemExit


def draw_field(mid_point_x,mid_point_y,size):
    mpy = mid_point_y
    mpx = mid_point_x
    s = size

    #all big squares should be 70 x 70 pixels
    #small squares get devided by 3.5 to create a 20 x 20 pixel square
    
    set_color(0,0,0)
    #vertical lines
    draw_line(mpx+s*35,mpy-s*90,mpx+s*35,mpy+s*90) #x1,y1,x2,y2
    draw_line(mpx-s*35,mpy-s*90,mpx-s*35,mpy+s*90)
    #horizontal lines
    draw_line(mpx-s*105,mpy-s*35,mpx+s*105,mpy-s*35)
    draw_line(mpx-s*105,mpy+s*35,mpx+s*105,mpy+s*35)

def draw_small_fields():
    for x in list_xcords:
        for y in list_ycords:
            draw_field(x,y,0.2857) #multiply with 1/3.5 to create a 20*20 square

def draw_shape(x,y,big=False,field=None,won=None):
    global x_turn
    
    #check if shape should be small or big
    if not big:
        s = 6
    else:
        x,y = get_cords(field,4) #get middle point of field
        set_color(255,255,255)
        fill_rect(x-32,y-32,64,64) #clear small field
        s = 21 #make size of shape 
        x_turn = not x_turn
        list_cleared_fields[field] = "x" if x_turn else "o"
        
    
    if x_turn:
        #draw red x
        set_color(255,6,55)
        draw_line(x-s,y+s,x+s,y-s)
        draw_line(x-s,y-s,x+s,y+s)
    else:
        #draw blue circle
        set_color(4,30,255)
        draw_circle(x,y,s)
    x_turn = not x_turn

    if big:
        check_winning(field,True)

def draw_cursor(type,x,y):
    color = (255,6,55) if x_turn else (4,30,255)
    if type == "normal": #to avoid drawing over the shapes a square has been 
        set_color(color[0],color[1],color[2])
        draw_rect(x-8,y-8,15,15)
    elif type == "fill":
        set_color(255,255,255)
        draw_rect(x-8,y-8,15,15)

def get_cords(field,square):
    #160, 110

    x = ((field % 3)-1) * 70 + 160
    y = ((field // 3)-1) * 70 + 110

    x += ((square % 3)-1) * 20
    y += ((square // 3)-1) * 20

    return x,y


def clear():
    set_color(255,255,255)
    fill_rect(-1,-1,321,220)

def start_choosing(forced_field=None):
    global debug_mode
    #free choice of location
    field = 4 if forced_field is None else forced_field #if there is not forced field is defaults to 
    position = [field, 4] #field,square

    for i in range(2):
        while True:
            x, y = get_cords(position[0], position[1])
            draw_cursor("normal", x, y)

            if i == 0:
                if forced_field is not None and type(list_cleared_fields[forced_field]) == int: #check if there is a forced field, if the field is not won and if the field has not ended in a draw
                    if [move for move in all_moves[forced_field] if type(move) == int] < 9:
                        break
                    else:
                        list_cleared_fields[forced_field] = ""

            key = wait_key()

            if key == 1: #right
                position[i] = check_move(position[i],1)
            elif key == 2: #left
                position[i] = check_move(position[i],-1)
            elif key == 3: #up
                position[i] = check_move(position[i],-3)
            elif key == 4: #down
                position[i] = check_move(position[i],3)
            elif key == 5: #enter
                if type(list_cleared_fields[position[0]]) == int:
                    draw_cursor("fill", x, y)
                    break
            # elif key == 146: #4 key
            #     for row in all_moves:
            #         print(row + "\n")
            # elif key == 147: #5 key
            #     debug_mode = True
            elif key in[9, 10, 64]: #del, clear, quit
                raise SystemExit
            draw_cursor("fill", x, y)
    
    x, y = get_cords(position[0], position[1])

    #save position
    if type(all_moves[position[0]][position[1]]) == int:
        if x_turn:
            all_moves[position[0]][position[1]] = "x"
        else:
            all_moves[position[0]][position[1]] = "o"
    else:
        start_choosing(forced_field=forced_field) #still force field even if square is occupied
    
    
    draw_shape(x,y)

    if forced_field is not None and type(list_cleared_fields[position[0]]) == int: #use current field instead of forced field for when user has free and they differ
        check_winning(position[0])

    return position[1] #return square (which will be the next field)

def check_move(position,move):
    end_result = position + move
    if end_result > 8:
        return position
    elif end_result < 0:
        return position
    else:
        return end_result

def main():
    clear()
    draw_field(160,110,1)
    draw_small_fields()

    next_field = start_choosing()

    while True:
        next_field = start_choosing(next_field)
    

main()


