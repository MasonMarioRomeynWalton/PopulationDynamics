#!/usr/bin/python3
from tkinter import *
import random
import time
import sys
import traceback
 
def show_exception_and_exit(exc_type, exc_value, tb):
    traceback.print_exception(exc_type, exc_value, tb)
    print("Press any key to exit.")
    input()
    sys.exit(-1)
sys.excepthook = show_exception_and_exit

#Input function
def inputa(nums):
    while True:
        h = input()
        if h=='':
            h = nums
            return float(h)
        try:
            return float(h)
        except ValueError:
            print('Try again.')

#Board creation
sim = Tk()
canvas = Canvas(sim, width=2000, height=2000)
canvas.pack()
print('Size of creatures')
s = int(inputa(5))
print('Size vertically:')
rows = int(inputa(1000))
print('Size horizontally:')
columns = int(inputa(1000))

canvas.create_rectangle(10,10,columns,rows)

#Creature creation
print('Number of creatures:')
e = int(inputa(1))
print('Percentage of carnivores(0-100):')
per = inputa(30)

class creature:
    def init(self,x,y,age):
        self.x = x
        self.y = y
        self.age = age
    def move(self):
        while True:
            self.w = random.randint(1,9)
            if self.w == 9:
                self.xa = 0
                self.xb = 0
                break
            elif self.w == 1 or self.w == 2:
                if self.y <= rows:
                    self.xa = 0
                    self.xb = 1
                    self.y = self.y + 1
                    break
            elif self.w == 3 or self.w == 4:
                if self.y > 1:
                    self.xa = 0
                    self.xb = -1
                    self.y = self.y - 1
                    break
            elif self.w == 5 or self.w == 6:
                if self.x <= columns:
                    self.xa = 1
                    self.xb = 0
                    self.x = self.x + 1
                    break
            elif self.w == 7 or self.w == 8:
                if self.x > 1:
                    self.xa = -1
                    self.xb = 0
                    self.x = self.x - 1
                    break
        canvas.move(self.n, self.xa, self.xb)
    def die(self):
        if self.age == life:
            canvas.delete(self.n)
            self.x = -1
            self.y = -1
            print('death')
        if self.age < life:
            if self.typ == 'carn':
                self.age = self.age+1
                canvas.itemconfig(self.n, fill=llh[self.age])
            if self.typ == 'herb':
                self.age = self.age+1
                canvas.itemconfig(self.n, fill=llc[self.age])

class carn(creature):
    def __init__(self,x,y,age):
        self.init(x,y,age)
        self.typ = 'carn'
        self.n = canvas.create_oval(self.x, self.y, self.x+s, self.y+s, fill='red')
##    def breed(self):
##        for u in range(0,len(cre)):
##            if self.x == cre[u].x and self.y == cre[u].y and self.typ == cre[u].typ and self.n != cre[u].n and self.n < cre[u].n and self.age < hl and cre[u].age < hl:
##                self.age = self.age + hl
##                cre[u].age = cre[u].age + hl
##                cre.append(carn(self.x,self.y,hl))
##                print('romantic')
##    def eat(self):
##        for u in range(0,len(cre)): 
##            if self.x == cre[u].x and self.y == cre[u].y and self.n != cre[u].n and cre[u].typ == 'herb':
##                canvas.itemconfig(self.n, fill='red')
##                self.age = 1
##                canvas.delete(cre[u].n)
##                cre[u].x = -1
##                print('kill')

class herb(creature):
    def __init__(self,x,y,age):
        self.init(x,y,age)
        self.typ = 'herb'
        self.n = canvas.create_oval(self.x, self.y, self.x+s, self.y+s, fill='blue', outline='#008080')
##    def breed(self):
##        for u in range(0,len(cre)):
##            if self.x == cre[u].x and self.y == cre[u].y and self.typ == cre[u].typ and self.n != cre[u].n and self.n < cre[u].n and self.age < hl and cre[u].age < hl:
##                self.age = self.age + hl
##                cre[u].age = cre[u].age + hl
##                cre.append(herb(self.x,self.y,hl))
##                print('romantic')
##    def eat(self):
##        for u in range(0,len(pla)):
##            if self.x == pla[u].x and self.y == pla[u].y: 
##                canvas.itemconfig(self.n, fill='blue')
##                self.age = 1
##                canvas.delete(pla[u].n)
##                pla[u].x = -1
##                print('tasty')

cre = []
for u in range(0, e):
    zz = random.randint(1, 100)
    x = random.randint(1, columns)
    y = random.randint(1, rows)
    if zz <= per:
        cre.append(carn(x,y,1))
    elif zz >= per:
        cre.append(herb(x,y,1))

#Plant creation
print('Number of plants:')
f = int(inputa(0))

class plant():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.n = canvas.create_oval(self.x, self.y, self.x+s ,self.y+s, fill='lime',)
##    def breed(self):
##        x = random.randint(1,100)
##        if x <= perplant:
##            self.w = random.randint(1,4)
##            if self.w == 1:
##                self.xa = self.x-1
##                self.xb = self.y
##            if self.w == 2:
##                self.xa = self.x
##                self.xb = self.y+1
##            if self.w == 3:
##                self.xa = self.x+1
##                self.xb = self.y
##            if self.w == 4:
##                self.xa = self.x
##                self.xb = self.y-1
##            if self.xa > 0 and self.xa <= columns and self.xb > 0 and self.xb <= rows:
##                pla.append(plant(self.xa,self.xb))

pla = []
for d in range(0, f):
    x = random.randint(1, columns)
    y = random.randint(1, rows)
    pla.append(plant(x,y))

#One round
def move():
    for u in range(0, len(cre)):
        cre[u].move()
##    for u in range(0, len(cre)):
##        cre[u].breed()
##    for u in range(0, len(cre)):
##        cre[u].eat()
    for u in range(0, len(cre)):
        if cre[len(cre)-u-1].x == -1:
            del cre[len(cre)-u-1]
    if len(pla) != 0:
        for u in range(0, len(pla)):
            if pla[len(pla)-u-1].x == -1:
                del pla[len(pla)-u-1]
    for u in range(0, len(cre)):
        cre[u].die()
    for u in range(0, len(cre)):
        if cre[len(cre)-u-1].x == -1:
            del cre[len(cre)-u-1]
##    for u in range(0, len(pla)):
##        pla[u].breed()

#Plantspread
print('Percentage of plant spread:')
perplant = (inputa(5))

#Lifespan
print('Lifespan:')
life = int(inputa(1000))
hl = int(life/2)
llc=[]
llh=[]
llv = 255/life
for llz in range(0, int(life)+1):
    lly = llv*llz
    llw = (hex(int(lly))[2:])
    if len(llw) == 1:
        llw = '0' + llw
    llc.append('#'+llw+llw+'ff')
    llh.append('#'+'ff'+llw+llw)

#Controls
but = 0
print('Speed(s)(0.1-5):')
speed = inputa(0.5)
def update_clock():
    if but == 1:
        move()
        sim.after(int(speed*1000),update_clock)
def togglemovesquare(event):
    global but
    if but == 0:
        but = 1
        sim.after(int(speed*1000), update_clock)
    elif but == 1:
        but = 0
def movesquare(event):
    move()
canvas.bind_all('<Return>', movesquare)
canvas.bind_all('<space>', togglemovesquare)
def qit(event):
    sim.destroy()
canvas.bind_all('<Escape>', qit)
def dele(event):
    quit()
canvas.bind_all('<Delete>', dele)
sim.mainloop()
