##

from tkinter import *
import random
import time

game_widths = 500
game_heights = 500
snake_item = 10
snake_color1 = "red"
snake_color2 = "yellow"

present_color1= "green"
present_color2 = "black"

virtual_game_x = game_widths//snake_item
virtual_game_y = game_heights//snake_item

snake_x = virtual_game_x//2
snake_y = virtual_game_y//2

snake_x_nav = 0
snake_y_nav = 0

snake_list = []
snake_size = 3

presents_list = []
present_size = 50

Game_Run = True

tk = Tk()
tk.title("Змейка на питоне")

## нельзя маштабировать
tk.resizable(0, 0)
## повер всех окон
tk.wm_attributes("-topmost", 1)

## объект bd  - границы окна тонкие
gameWindows = Canvas(tk, width=game_widths, height=game_heights, bd=0, highlightthickness=0)
gameWindows.pack()
tk.update()

##Подарки
for i in range(present_size):
    x = random.randrange(virtual_game_x)
    y = random.randrange(virtual_game_y)
    id1 = gameWindows.create_oval(x * snake_item, y * snake_item, x * snake_item + snake_item,
                                 y * snake_item + snake_item, fill=present_color1)
    id2 = gameWindows.create_oval(x * snake_item + 2, y * snake_item + 2, x * snake_item + snake_item - 2,
                                 y * snake_item + snake_item - 2, fill=present_color2)
    presents_list.append([x, y, id1, id2])
print(presents_list)


##Рисуем змею
def snake_paint_item(gameWindows, x, y):
    global snake_list
    id1 = gameWindows.create_rectangle(x * snake_item, y * snake_item, x * snake_item + snake_item,
                                 y * snake_item + snake_item, fill=snake_color1)
    id2 = gameWindows.create_rectangle(x * snake_item + 2, y * snake_item + 2, x * snake_item + snake_item - 2,
                                 y * snake_item + snake_item - 2, fill=snake_color2)
    snake_list.append([x,y,id1,id2])
    print(snake_list)

def delete_shadow_of_snake():
    if len(snake_list) >= snake_size:
        temp_item = snake_list.pop(0)
        gameWindows.delete(temp_item[2])
        gameWindows.delete(temp_item[3])

def chek_present():
    global snake_size
    for i in range(len(presents_list)):
        if presents_list[i][0] == snake_x and presents_list[i][1] == snake_y:
            snake_size = snake_size +1
            gameWindows.delete(presents_list[i][2])
            gameWindows.delete(presents_list[i][3])
           # print("found")
    #print(snake_x, snake_y)
   

##def это функция
def snake_move(event):
    global snake_x
    global snake_y
    global snake_x_nav
    global snake_y_nav
    if event.keysym == "Up":
        snake_x_nav = 0
        snake_y_nav = -1
        delete_shadow_of_snake()
    elif event.keysym == "Down":
        snake_x_nav = 0
        snake_y_nav = 1
        delete_shadow_of_snake()
    elif event.keysym == "Left":
        snake_x_nav = -1
        snake_y_nav = 0
        delete_shadow_of_snake()
    elif event.keysym == "Right":
        snake_x_nav = 1
        snake_y_nav = 0
        delete_shadow_of_snake()
    snake_x = snake_x + snake_x_nav
    snake_y = snake_y + snake_y_nav
    snake_paint_item(gameWindows, snake_x, snake_y)
    chek_present()


snake_paint_item(gameWindows, snake_x, snake_y)

def game_over():
    global Game_Run
    Game_Run = False

def chek_borders():
    if snake_x>virtual_game_x or snake_x<0 or snake_y>virtual_game_y or snake_y<0:
        game_over()


gameWindows.bind_all("<KeyPress-Left>", snake_move)
gameWindows.bind_all("<KeyPress-Right>", snake_move)
gameWindows.bind_all("<KeyPress-Up>", snake_move)
gameWindows.bind_all("<KeyPress-Down>", snake_move)

#нельзя врезаться в себя
def chek_touch_snake(f_x,f_y):    
    global Game_Run
    if not (snake_x_nav ==0 and snake_y_nav ==0):
        for i in range(len(snake_list)):
            if snake_list[i][0] == f_x and snake_list[i][1] == f_y:
                Game_Run = False
           

while Game_Run:
    delete_shadow_of_snake()
    chek_present()
    chek_borders()
    chek_touch_snake(snake_x + snake_x_nav, snake_y + snake_y_nav)
    snake_x = snake_x + snake_x_nav
    snake_y = snake_y + snake_y_nav
    snake_paint_item(gameWindows, snake_x, snake_y)
    tk.update_idletasks()
    tk.update()
    time.sleep(0.07)

def fun_nothing(event):
    pass
gameWindows.bind_all("<KeyPress-Left>", fun_nothing)
gameWindows.bind_all("<KeyPress-Right>", fun_nothing)
gameWindows.bind_all("<KeyPress-Up>", fun_nothing)
gameWindows.bind_all("<KeyPress-Down>", fun_nothing)
