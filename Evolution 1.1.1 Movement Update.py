#!/usr/bin/python3
from tkinter import *
import random
from math import *
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
s = int(inputa(30))
print('Size vertically:')
rows = int(inputa(500))
print('Size horizontally:')
columns = int(inputa(500))

canvas.create_rectangle(10,10,columns,rows)

#Creature creation
print('Number of creatures:')
e = int(inputa(3))
print('Percentage of carnivores(0-100):')
per = inputa(30)
print('Speed of creatures relative to size:')
spc = inputa(0.5)
spc = s*spc

class creature:
    def init(self,x,y,age):
        self.x = x
        self.y = y
        self.age = age
    def move(self):
        while True:
            self.w = random.randint(1,int(2000*pi))
            self.w = self.w/1000
            self.xa = self.x+spc*cos(self.w)
            self.xb = self.y+spc*sin(self.w)
            if self.xa > 10 and self.xa+s < columns and self.xb > 10 and self.xb+s < rows:
                break
        self.x = self.xa
        self.y = self.xb
        canvas.coords(self.n, int(self.x), int(self.y), int(self.x)+s, int(self.y)+s)
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
    def breed(self):
        for u in range(0,len(cre)):
            if ((self.x-cre[u].x)**2+(self.y-cre[u].y)**2)**(1/float(2))<s and self.n != cre[u].n and self.n < cre[u].n and cre[u].typ == 'carn' and self.age < hl and cre[u].age < hl:
                self.age = self.age + hl
                cre[u].age = cre[u].age + hl
                self.v = random.randint(1,2)
                while True:
                    self.w = random.randint(1,int(2000*pi))
                    self.w = self.w/1000
                    if self.v == 1:
                        self.xa = self.x+s*cos(self.w)
                        self.xb = self.y+s*sin(self.w)
                    if self.v == 2:
                        self.xa = cre[u].x+s*cos(self.w)
                        self.xb = cre[u].y+s*sin(self.w)
                    if self.xa > 10 and self.xa+s < columns and self.xb > 10 and self.xb+s < rows:
                        cre.append(carn(self.xa,self.xb,hl))
                        break
                print('romantic')
    def eat(self):
        for u in range(0,len(cre)): 
            if ((self.x-cre[u].x)**2+(self.y-cre[u].y)**2)**(1/float(2))<s and self.n != cre[u].n and cre[u].typ == 'herb':
                canvas.itemconfig(self.n, fill='red')
                self.age = 1
                canvas.delete(cre[u].n)
                cre[u].x = -1
                print('kill')

class herb(creature):
    def __init__(self,x,y,age):
        self.init(x,y,age)
        self.typ = 'herb'
        self.n = canvas.create_oval(self.x, self.y, self.x+s, self.y+s, fill='blue', outline='#008080')
    def breed(self):
        for u in range(0,len(cre)):
            if ((self.x-cre[u].x)**2+(self.y-cre[u].y)**2)**(1/float(2))<s and self.n != cre[u].n and self.n < cre[u].n and cre[u].typ == 'herb' and self.age < hl and cre[u].age < hl:
                self.age = self.age + hl
                cre[u].age = cre[u].age + hl
                self.v = random.randint(1,2)
                while True:
                    self.w = random.randint(1,int(2000*pi))
                    self.w = self.w/1000
                    if self.v == 1:
                        self.xa = self.x+s*cos(self.w)
                        self.xb = self.y+s*sin(self.w)
                    if self.v == 2:
                        self.xa = cre[u].x+s*cos(self.w)
                        self.xb = cre[u].y+s*sin(self.w)
                    if self.xa > 10 and self.xa+s < columns and self.xb > 10 and self.xb+s < rows:
                        cre.append(herb(self.xa,self.xb,hl))
                        break
                print('romantic')
    def eat(self):
        for u in range(0,len(pla)):
            if ((self.x-pla[u].x)**2+(self.y-pla[u].y)**2)**(1/float(2))<s: 
                canvas.itemconfig(self.n, fill='blue')
                self.age = 1
                canvas.delete(pla[u].n)
                pla[u].x = -1
                print('tasty')

cre = []
for u in range(0, e):
    zz = random.randint(1, 100)
    x = random.randint(1, columns-s)
    y = random.randint(1, rows-s)
    if zz <= per:
        cre.append(carn(x,y,1))
    elif zz >= per:
        cre.append(herb(x,y,1))

#Plant creation
print('Number of plants:')
f = int(inputa(1))

class plant():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.n = canvas.create_oval(self.x, self.y, self.x+s ,self.y+s, fill='lime',)
    def breed(self):
        x = random.randint(1,100)
        if x <= perplant:
            while True:
                self.w = random.randint(1,int(2000*pi))
                self.w = self.w/1000
                self.xa = self.x+s*cos(self.w)
                self.xb = self.y+s*sin(self.w)
                if self.xa > 10 and self.xa+s < columns and self.xb > 10 and self.xb+s < rows:
                    pla.append(plant(self.xa,self.xb))
                    break

pla = []
for d in range(0, f):
    x = random.randint(1, columns-s)
    y = random.randint(1, rows-s)
    pla.append(plant(x,y))

#One round
def move():
    for u in range(0, len(cre)):
        cre[u].move()
    for u in range(0, len(pla)):
        pla[u].breed()
    for u in range(0, len(cre)):
        cre[u].breed()
    for u in range(0, len(cre)):
        cre[u].eat()
    for u in range(0, len(cre)):
        if cre[len(cre)-u-1].x == -1:
            del cre[len(cre)-u-1]
    if len(pla) != 0:
        for u in range(0, len(pla)):
            if pla[len(pla)-u-1].x == -1:
                del pla[len(pla)-u-1]
    for u in range(0, len(cre)):
        cre[u].die()
    if len(cre) != 0:
        for u in range(0, len(cre)):
            try:
                if cre[len(cre)-u-1].x == -1:
                    del cre[len(cre)-u-1]
            except:
                print(cre)

#Plantspread
print('Percentage of plant spread:')
perplant = (inputa(2))

#Lifespan
print('Lifespan:')
life = int(inputa(500))
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
