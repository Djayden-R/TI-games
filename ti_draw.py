#This is a spoof ti_draw library to remove "function not defined" errors

def draw_line(x1, y1, x2, y2):
    print(f"draw_line({x1}, {y1}, {x2}, {y2})")

def draw_rect(x, y, w, h):
    print(f"draw_rect({x}, {y}, {w}, {h})")

def fill_rect(x, y, w, h):
    print(f"fill_rect({x}, {y}, {w}, {h})")

def draw_circle(x, y, r):
    print(f"draw_circle({x}, {y}, {r})")

def fill_circle(x, y, r):
    print(f"fill_circle({x}, {y}, {r})")

def draw_text(x, y, text):
    print(f"draw_text({x}, {y}, \"{text}\")")

def draw_poly(x_list, y_list):
    print(f"draw_poly({x_list}, {y_list})")

def fill_poly(x_list, y_list):
    print(f"fill_poly({x_list}, {y_list})")

def poly_xy(x, y, sh):
    print(f"poly_xy({x}, {y}, {sh})")

def clear():
    print("clear()")

def clear_rect(x, y, w, h):
    print(f"clear_rect({x}, {y}, {w}, {h})")

def set_color(r, g, b):
    print(f"set_color({r}, {g}, {b})")

def set_pen(size="thin", style="solid"):
    print(f"set_pen({size}, {style})")

def set_window(xmin, xmax, ymin, ymax):
    print(f"set_window({xmin}, {xmax}, {ymin}, {ymax})")

def show_draw():
    print("show_draw()")
