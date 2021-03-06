import tkinter as tk
import maze_maker as mm

def key_down(event):
    global key #キー入力
    key = event.keysym
    #print(f"{key}キーが押されました")

def key_up(event):
    global key #キー入力
    key = ""

def main_proc():
    global cx, cy, mx, my #キーを入力したときに進む大きさ
    delta = {#キー：押されているキーkey/値：移動幅リスト[x,y]
        ""     : [0, 0],
        "Up"   : [0, -1],
        "Down" : [0, +1],
        "Left" : [-1, 0],
        "Right": [+1, 0],
    }
    try:
        if maze_bg[my+delta[key][1]][mx+delta[key][0]] == 0:#床
            my, mx = my+delta[key][1], mx+delta[key][0]
    except:
        pass
    cx, cy = mx*50+25, my*50+25
    canvas.coords("tori", cx, cy)
    root.after(100, main_proc)
    

if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")
    
    canvas = tk.Canvas(root, width = 1500, height = 900, bg = "black")
    canvas.pack()
    maze_bg = mm.make_maze(30, 18) #1:壁/0:床を表す二次元リスト
    mm.show_maze(canvas, maze_bg) #canvaにmaze_bgを描く

    tori = tk.PhotoImage(file="fig/4 (1).png")
    mx, my = 1, 1
    cx, cy = mx*50+25, my*50+25
    canvas.create_image(cx, cy, image=tori, tag="tori")
    #if cx == 250:
        #tori = tk.PhotoImage(file="fig/don.png")


    key = ""
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)

    main_proc()
    root.mainloop()