from tkinter import *
import random
import time

#Global Varibles

paddleSpeed = 7
x = 1
Score = 0
BallSpeed = 7
Score_Mutiplyer = 1
#Game Body


#This where all of the stuff concernig the ball is held
class Ball:

    #this initiats the ball on the canvas at the start of the game
    def __init__(self, canvas, paddle, color):
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)
        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False
        print(self.canvas.coords(self.id))

    #This function handels ball paddle conntact
    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos [3] <= paddle_pos[3]:
                return True
        return False
        
    #this draws the ball every frame in the game loop
    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = BallSpeed
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
        if self.hit_paddle(pos) == True:
            if paddle.x != 0:
                if paddleSpeed >=1:
                    self.y = -BallSpeed + -paddleSpeed
                    self.x = -paddleSpeed + 1
                if paddleSpeed <=-1:
                    self.y = -BallSpeed + -paddleSpeed
                    self.x = paddleSpeed - 1
            if paddle.x == 0:
                self.y = -BallSpeed
        if pos[0] <= 0:
            self.x = BallSpeed
        if pos[2] >= self.canvas_width:
            self.x = -BallSpeed
        print(self.canvas.coords(self.id))



#This is where all of the stuuf concernig the paddle is held


class Paddle:
    #This draws the paddle at the beginging of the game
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 200, 300)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Right>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Left>', self.turn_right)
        print(self.canvas.coords(self.id))
    #This draws the paddle every frame in the game loop
    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= self.canvas_width:
            self.x = 0
        print(self.canvas.coords(self.id))

    #these two function controll left to right movement
    def turn_left(self, evt):
        self.x = paddleSpeed

    def turn_right(self, evt):
        self.x = -paddleSpeed

#Window setup



tk = Tk()
tk.title("Game(Bounce V 0.1.2)")
tk.resizable(0,0)
tk.wm_attributes("-topmost",1)
canvas = Canvas(tk,width=500, height=400, bd=0,highlightthickness=0)
canvas.pack()
tk.update()




#Game Paramiters

Ball_Colors = ['red', 'blue', 'yellow', 'green', 'purple', 'pink', 'orange']
random.shuffle(Ball_Colors)

paddle = Paddle(canvas, Ball_Colors[1])
ball = Ball(canvas, paddle, Ball_Colors[0])




    


#Game Loop. The Game is running at 100 frames per second

while x == 1:
    
    if ball.hit_bottom == False:
        ball.draw()
        paddle.draw()
    elif ball.hit_bottom == True:
        print('''           Game over
            Score %s''' % int(Score/10))
        canvas.create_text(250, 150, text='Game Over', font=('Helvetica', 30))
        canvas.create_text(250, 200, text='Your Score is:', font=('Helvetica', 20))
        canvas.create_text(250, 250, text=int(Score/10), font=('Helvetica', 30))
        x = 2
        #print(text)
    tk.update_idletasks()
    Score = (Score + 1)#*Score_Multiplyer
    tk.update()
    time.sleep(0.01)
