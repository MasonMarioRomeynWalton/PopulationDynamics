#!/usr/bin/python3
from tkinter import *
import random
from math import *
import time
import sys
import traceback

##Keep running after traceback
def show_exception_and_exit(exc_type, exc_value, tb):
    traceback.print_exception(exc_type, exc_value, tb)
    print("Press any key to exit.")
    input()
    sys.exit(-1)
sys.excepthook = show_exception_and_exit

##Input function
def get_input(nums):
    while True:
        h = input()
        if h=='':
            h = nums
            return float(h)
        try:
            return float(h)
        except ValueError:
            print('Try again.')

##Inputs
print('Size of creatures')
size = int(get_input(20))
print('Size vertically:')
rows = int(get_input(1000))
print('Size horizontally:')
columns = int(get_input(1000))
print('Number of creatures:')
number_of_creatures = int(get_input(40))
print('Percentage of carnivores:')
per = int(get_input(7))
print('Speed of creatures relative to size:')
spc = get_input(0.3)
spc = size*spc
print('Lifespan:')
life = int(get_input(200))
half_life = int(life/2)
print('Randomness of movement:')
vertex = int(get_input(3))
print('Number of plants:')
number_of_plants = int(get_input(20))
print('Percentage of plant spread:')
perplant = get_input(10)
print('Speed(s)(0.1-5):')
speed = get_input(0.01)

##Board creation
sim = Tk()
canvas = Canvas(sim, width=2000, height=2000)
canvas.pack()
canvas.create_rectangle(10,10,columns,rows)

##Creature creation
class creature:
    def init(self,x,y,age):
        self.x = x
        self.y = y
        self.gx = self.x
        self.gy = self.y
        self.movenum = 0
        self.age = age
    ##Creature movement
    def move(self):
        while True:
            if ((self.x-self.gx)**2+(self.y-self.gy)**2)**(1/float(2))<spc:
                self.movenum = self.movenum+1
                self.gx = random.randint(10, columns-size)
                self.gy = random.randint(10, rows-size)
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
                        if self.gx3 > 10 and self.gx3 < columns-size and self.gy3 > 10 and self.gy3 < rows-size:
                            break
                    if self.gx2 > 10 and self.gx2 < columns-size and self.gy2 > 10 and self.gy2 < rows-size:
                        break
#                canvas.create_rectangle(self.gx3,self.gy3,self.gx3+2,self.gy3+2,outline='blue')
            elif ((self.x-self.gx2)**2+(self.y-self.gy2)**2)**(1/float(2))<spc:
                self.movenum = self.movenum+1
                self.u = atan2(self.gy-self.y,self.gx-self.x)
                while True:
                    self.dis3 = random.randint(int(-(((self.x-self.gx)**2+(self.y-self.gy)**2)**(1/float(2)))/2), int((((self.x-self.gx)**2+(self.y-self.gy)**2)**(1/float(2)))/2))
                    self.gx3 = (self.x+self.gx)/2+self.dis3*cos(self.u+pi/2)
                    self.gy3 = (self.y+self.gy)/2+self.dis3*sin(self.u+pi/2)
                    self.u = atan2(self.gy3-self.y,self.gx3-self.x)
                    if self.gx3 > 10 and self.gx3 < columns-size and self.gy3 > 10 and self.gy3 < rows-size:
                        break
#                canvas.create_rectangle(self.gx3,self.gy3,self.gx3+2,self.gy3+2,outline='blue')
            elif ((self.x-self.gx3)**2+(self.y-self.gy3)**2)**(1/float(2))<spc:
                self.movenum = self.movenum+1
                if (self.movenum//2)%2 == 1:
                    self.u = atan2(self.gy2-self.y,self.gx2-self.x)
#                    canvas.create_rectangle(self.gx2,self.gy2,self.gx2+2,self.gy2+2,outline='red')
                elif (self.movenum//2)%2 == 0:
                    self.u = atan2(self.gy-self.y,self.gx-self.x)
#                    canvas.create_rectangle(self.gx,self.gy,self.gx+2,self.gy+2,outline='orange')
            self.xa = self.x+spc*cos(self.u)
            self.ya = self.y+spc*sin(self.u)
            if self.xa >= 10 and self.xa+size <= columns and self.ya >= 10 and self.ya+size <= rows:
                break
            ##If it were to go off the screen
            else:
                self.movenum = self.movenum+1
                self.gx = random.randint(10+spc, columns-size)
                self.gy = random.randint(10+spc, rows-size)
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
                        if self.gx3 > 10 and self.gx3 < columns-size and self.gy3 > 10 and self.gy3 < rows-size:
                            break
                    if self.gx2 > 10 and self.gx2 < columns-size and self.gy2 > 10 and self.gy2 < rows-size:
                        break
#                canvas.create_rectangle(self.gx3,self.gy3,self.gx3+2,self.gy3+2,outline='blue')
        self.x = self.xa
        self.y = self.ya
        canvas.coords(self.n, int(self.x), int(self.y), int(self.x)+size, int(self.y)+size)
    def tick(self):
        if self.age < life:
            self.age = self.age+1
            if self.type == 'carn':
                canvas.itemconfig(self.n, fill=llh[self.age])
            if self.type == 'herb':
                canvas.itemconfig(self.n, fill=llc[self.age])
        else:
            canvas.delete(self.n)
            return True

##Carnivore creation
class carn(creature):
    def __init__(self,x,y,age):
        self.init(x,y,age)
        self.type = 'carn'
        ## Tag of some sort
        self.n = canvas.create_oval(self.x, self.y, self.x+size, self.y+size, fill='red')
    ## carnivore eating
    def eat(self):
        for creature in cre:
            if dist([self.x,self.y],[creature.x,creature.y]) < size and creature.type == 'herb':
                canvas.itemconfig(self.n, fill='red')
                self.age = 1
                canvas.delete(creature.n)
                cre.remove(creature)

##Herbivore creation
class herb(creature):
    def __init__(self,x,y,age):
        self.init(x,y,age)
        self.type = 'herb'
        ## Tag of some sort
        self.n = canvas.create_oval(self.x, self.y, self.x+size, self.y+size, fill='blue', outline='#008080')
    ## Herbivore eating
    def eat(self):
        for plant in plants:
            if dist([self.x,self.y],[plant.x,plant.y]) < size:
                canvas.itemconfig(self.n, fill='blue')
                self.age = 1
                canvas.delete(plant.n)
                plants.remove(plant)

def breed(creature1,creature2):
    ## Check if it's possible to breed
    possible_to_breed = [dist([creature1.x,creature1.y],[creature2.x,creature2.y])<size,
                        creature1.n < creature2.n,
                        creature1.type == creature2.type,
                        creature1.age < half_life,
                        creature2.age < half_life]

    if not all(possible_to_breed):
        return

    creature1.age = creature1.age + half_life
    creature2.age = creature2.age + half_life

    ## Randomly generate which it'll spawn next to or something
    which_parent = random.randint(1,2)
    while True:
        ## Generate between 0 and 2pi
        direction = random.randint(1,int(2000*pi))/1000
        if which_parent == 1:
            new_x = creature1.x+size*cos(direction)
            new_y = creature1.y+size*sin(direction)
        if which_parent == 2:
            new_x = creature2.x+size*cos(direction)
            new_y = creature2.y+size*sin(direction)
        if new_x > 10 and new_x+size < columns and new_y > 10 and new_y+size < rows:
            if creature1.type == 'herb':
                cre.append(herb(new_x,new_y,half_life))
            elif creature1.type == 'carn':
                cre.append(carn(new_x,new_y,half_life))
            break



##Plant creation
class Plant():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.n = canvas.create_oval(self.x, self.y, self.x+size ,self.y+size, fill='lime',)
    ## Plant spread
    def breed(self):
        x = random.randint(1,100000)
        if x <= perplant*1000:
            direction = random.randint(1,int(2000*pi))/1000
            new_x = self.x+size*cos(direction)
            new_y = self.y+size*sin(direction)
            if new_x > 10 and new_x+size < columns and new_y > 10 and new_y+size < rows:
                for plant in plants:
                    if dist([new_x,new_y],[plant.x,plant.y]) < size and self.n != plant.n:
                        return
                plants.append(Plant(new_x,new_y))

## List of creatures
cre= []
for _ in range(0, number_of_creatures):
    zz = random.randint(1, 100)
    x = random.randint(10, columns-size)
    y = random.randint(10, rows-size)
    if zz <= per:
        cre.append(carn(x,y,1))
    elif zz >= per:
        cre.append(herb(x,y,1))

## List of plants
plants = []
for _ in range(0, number_of_plants):
    x = random.randint(10, columns-size)
    y = random.randint(10, rows-size)
    plants.append(Plant(x,y))

##One round
def move():
    for u in range(0, len(cre)):
        cre[u].move()
    for plant in plants:
        plant.breed()
    for creature1 in cre:
        for creature2 in cre:
            breed(creature1,creature2)
    for creature in cre:
        creature.eat()
    for creature in cre:
        if(creature.tick()):
            cre.remove(creature)

##Lifespan
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

##Controls
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
