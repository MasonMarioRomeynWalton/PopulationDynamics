#!/usr/bin/python3
from tkinter import *
import random
from math import *
import time
import sys
import traceback

#Keep running after traceback
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

#Inputs
print('Size of creatures')
s = int(inputa(30))
print('Size vertically:')
rows = int(inputa(1000))
print('Size horizontally:')
columns = int(inputa(1000))
print('Number of creatures:')
e = int(inputa(20))
print('Percentage of carnivores:')
per = int(inputa(10))
print('Speed of creatures relative to size:')
spc = inputa(0.3)
spc = s*spc
print('Lifespan:')
life = int(inputa(1000))
hl = int(life/2)
print('Randomness of movement:')
vertex = int(inputa(3))
print('Number of plants:')
f = int(inputa(500))
print('Percentage of plant spread:')
perplant = int((inputa(1)))
print('Speed(s)(0.1-5):')
speed = inputa(0.01)

#Board creation
sim = Tk()
canvas = Canvas(sim, width=2000, height=2000)
canvas.pack()
canvas.create_rectangle(10,10,columns,rows)

#Creature creation
class creature:
    def init(self,x,y,age):
        self.x = x
        self.y = y
        self.gx = self.x
        self.gy = self.y
        self.movenum = 0
        self.age = age
    def move(self):
        while True:
            if abs(((self.x-self.gx)**2+(self.y-self.gy)**2)**(1/float(2)))<spc/2:
                self.movenum = self.movenum+1
##random x guess
                self.gx = random.randint(10+spc, columns-s)
##random y guess
                self.gy = random.randint(10+spc, rows-s)
##atan2 of delta points
                self.u = atan2(self.gy-self.y,self.gx-self.x)
                while True:
##Random distance
                    self.dis2 = random.randint(int(-(((self.x-self.gx)**2+(self.y-self.gy)**2)**(1/float(2)))/2), int((((self.x-self.gx)**2+(self.y-self.gy)**2)**(1/float(2)))/2))
                    self.gx2 = (self.x+self.gx)/2+self.dis2*cos(self.u+pi/2)
                    self.gy2 = (self.y+self.gy)/2+self.dis2*sin(self.u+pi/2)
                    self.u = atan2(self.gy2-self.y,self.gx2-self.x)
                    while True:
                        self.dis3 = random.randint(int(-(((self.x-self.gx2)**2+(self.y-self.gy2)**2)**(1/float(2)))/2), int((((self.x-self.gx2)**2+(self.y-self.gy2)**2)**(1/float(2)))/2))
                        self.gx3 = (self.x+self.gx2)/2+self.dis3*cos(self.u+pi/2)
                        self.gy3 = (self.y+self.gy2)/2+self.dis3*sin(self.u+pi/2)
                        self.u = atan2(self.gy3-self.y,self.gx3-self.x)
                        if self.gx3 > 10 and self.gx3 < columns-s and self.gy3 > 10 and self.gy3 < rows-s:
                            break
                    if self.gx2 > 10 and self.gx2 < columns-s and self.gy2 > 10 and self.gy2 < rows-s:
                        break
                canvas.create_rectangle(self.gx3,self.gy3,self.gx3+2,self.gy3+2,outline='blue')
            elif abs(((self.x-self.gx2)**2+(self.y-self.gy2)**2)**(1/float(2)))<spc/2:
                self.movenum = self.movenum+1
                self.u = atan2(self.gy-self.y,self.gx-self.x)
                while True:
                    self.dis3 = random.randint(int(-(((self.x-self.gx)**2+(self.y-self.gy)**2)**(1/float(2)))/2), int((((self.x-self.gx)**2+(self.y-self.gy)**2)**(1/float(2)))/2))
                    self.gx3 = (self.x+self.gx)/2+self.dis3*cos(self.u+pi/2)
                    self.gy3 = (self.y+self.gy)/2+self.dis3*sin(self.u+pi/2)
                    self.u = atan2(self.gy3-self.y,self.gx3-self.x)
                    if self.gx3 > 10 and self.gx3 < columns-s and self.gy3 > 10 and self.gy3 < rows-s:
                        break
                canvas.create_rectangle(self.gx3,self.gy3,self.gx3+2,self.gy3+2,outline='blue')
            elif abs(((self.x-self.gx3)**2+(self.y-self.gy3)**2)**(1/float(2)))<spc/2:
                self.movenum = self.movenum+1
                if (self.movenum//2)%2 == 1:
                    self.u = atan2(self.gy2-self.y,self.gx2-self.x)
                    canvas.create_rectangle(self.gx2,self.gy2,self.gx2+2,self.gy2+2,outline='red')
                elif (self.movenum//2)%2 == 0:
                    self.u = atan2(self.gy-self.y,self.gx-self.x)
                    canvas.create_rectangle(self.gx,self.gy,self.gx+2,self.gy+2,outline='orange')
            self.xa = self.x+spc*cos(self.u)
            self.xb = self.y+spc*sin(self.u)
            if self.xa >= 10 and self.xa+s <= columns and self.xb >= 10 and self.xb+s <= rows:
                break
            ##If it were to go off the screen
            else:
                self.movenum = self.movenum+1
                self.gx = random.randint(10+spc, columns-s)
                self.gy = random.randint(10+spc, rows-s)
                self.u = atan2(self.gy-self.y,self.gx-self.x)
                while True:
                    self.dis2 = random.randint(int(-(((self.x-self.gx)**2+(self.y-self.gy)**2)**(1/float(2)))/2), int((((self.x-self.gx)**2+(self.y-self.gy)**2)**(1/float(2)))/2))
                    self.gx2 = (self.x+self.gx)/2+self.dis2*cos(self.u+pi/2)
                    self.gy2 = (self.y+self.gy)/2+self.dis2*sin(self.u+pi/2)
                    self.u = atan2(self.gy2-self.y,self.gx2-self.x)
                    while True:
                        self.dis3 = random.randint(int(-(((self.x-self.gx2)**2+(self.y-self.gy2)**2)**(1/float(2)))/2), int((((self.x-self.gx2)**2+(self.y-self.gy2)**2)**(1/float(2)))/2))
                        self.gx3 = (self.x+self.gx2)/2+self.dis3*cos(self.u+pi/2)
                        self.gy3 = (self.y+self.gy2)/2+self.dis3*sin(self.u+pi/2)
                        self.u = atan2(self.gy3-self.y,self.gx3-self.x)
                        if self.gx3 > 10 and self.gx3 < columns-s and self.gy3 > 10 and self.gy3 < rows-s:
                            break
                    if self.gx2 > 10 and self.gx2 < columns-s and self.gy2 > 10 and self.gy2 < rows-s:
                        break
                canvas.create_rectangle(self.gx3,self.gy3,self.gx3+2,self.gy3+2,outline='blue')
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

#Carnivore creation
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

#Herbivore creation
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
    x = random.randint(10, columns-s)
    y = random.randint(10, rows-s)
    if zz <= per:
        cre.append(carn(x,y,1))
    elif zz >= per:
        cre.append(herb(x,y,1))

#Plant creation
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
    x = random.randint(10, columns-s)
    y = random.randint(10, rows-s)
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
    lencre = len(cre)
    for u in range(0, lencre):
        if cre[lencre-u-1].x == -1:
            del cre[lencre-u-1]
    lenpla = len(pla)
    for u in range(0, lenpla):
        if pla[lenpla-u-1].x == -1:
            del pla[lenpla-u-1]
    for u in range(0, len(cre)):
        cre[u].die()
    lencre = len(cre)
    for u in range(0, lencre):
        if cre[lencre-u-1].x == -1:
            del cre[lencre-u-1]

#Lifespan
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
