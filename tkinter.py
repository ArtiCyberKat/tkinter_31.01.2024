from tkinter import *
w = 720
h = 480

c = Canvas(Tk(),width=w,height=h)
c.pack()


x = 10
y = 10
vx = 1
vy = 1
ay = 0.2

accuracy = []





def click(event):
    mx = event.x
    my = event.y
    #print("click at", mx,my)
    if x<mx<x+50 and y-20<my<y+50:
        #print("You hit the character.")
        accuracy.append(1)
        
    else:
        #print("You missed the character.")
        accuracy.append(0)
    print("Your accuracy is",format(sum(accuracy)/len(accuracy),"0.0%"),".")

    
c.bind("<Button-1>", click)
c.bind("<Button-2>", click)



def makeChar(x,y):
    c.create_rectangle(x,y,x+50,y+50,fill="white")
    c.create_oval(x+10,y+10,x+20,y+20,fill="yellow")
    c.create_oval(x+30,y+10,x+40,y+20,fill="yellow")
    c.create_line(x+25,y+25,x+30,y+35,x+20,y+35,x+25,y+25,fill="orange")
    c.create_arc(x+10,y+35,x+40,y+45,start=180,extent=180)
    c.create_line(x,y,x+10,y-20,x+20,y,fill="red")
    c.create_line(x+30,y,x+40,y-20,x+50,y,fill="red")

#x=50
#y=50
    
    


def render():
    global x,y,vx,vy,ay
    c.delete("all")
    makeChar(x,y)

    x = x + vx
    y = y + vy
    vy = vy + ay
    #vy = vy = 0.05

    #x,y = x + vx, y + vy    short hand of what is above

    if x < 0 or x > w - 50:
        x = x - vx - 1
        vx = -0.9*vx

    if y < 0 or y > h - 50:
        y = y - vy - 1
        vy = -0.9*vy

    c.after(10,render)


render()
mainloop()
