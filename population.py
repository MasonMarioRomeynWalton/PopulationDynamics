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
number_of_creatures = int(get_input(8))
print('Percentage of carnivores:')
per = int(get_input(7))
print('Speed of creatures relative to size:')
creature_speed = get_input(0.1)
creature_speed = size*creature_speed
print('Lifespan:')
life = int(get_input(200))
half_life = int(life/2)
print('Randomness of movement:')
vertex = int(get_input(3))
print('Number of plants:')
number_of_plants = int(get_input(50))
print('Percentage of plant spread:')
perplant = get_input(10)
print('Speed(s)(0.1-5):')
game_speed = get_input(0.01)

##Board creation
sim = Tk()
canvas = Canvas(sim, width=2000, height=2000)
canvas.pack()
canvas.create_rectangle(10,10,columns,rows)

##Creature creation
class creature:
    def init(self,x,y,speed,age):
        self.x = x
        self.y = y
        self.dest_x = self.x
        self.dest_y = self.y
        self.speed = speed
        self.age = age
    ##Creature movement
    def move(self):
        while True:
            ## If we have reached the point of destination
            if dist([self.x,self.y],[self.dest_x,self.dest_y]) < self.speed:

                ## New destination
                self.dest_x = random.randint(10, columns-size)
                self.dest_y = random.randint(10, rows-size)

                angle_to_dest = atan2(self.dest_y-self.y,self.dest_x-self.x)

                ## New intermediate destination
                while True:

                    distance_to_dest = dist([self.x,self.y],[self.dest_x,self.dest_y])
                    distance_along = random.randint(1,int(distance_to_dest))

                    point_along_x = self.x+distance_to_dest*cos(angle_to_dest)
                    point_along_y = self.y+distance_to_dest*sin(angle_to_dest)

                    distance_sideways = random.randint(-int(distance_to_dest/2),int(distance_to_dest/2))

                    self.inter_dest_x = point_along_x+distance_sideways*cos(angle_to_dest+pi/2)
                    self.inter_dest_y = point_along_y+distance_sideways*sin(angle_to_dest+pi/2)

                    if self.inter_dest_x >= 10 and self.inter_dest_x <= columns-size and self.inter_dest_y >= 10 and self.inter_dest_y < rows-size:
                        break

                canvas.create_rectangle(self.dest_x, self.dest_y, self.dest_x+5, self.dest_y+5, fill='green')
                canvas.create_rectangle(self.inter_dest_x, self.inter_dest_y, self.inter_dest_x+5, self.inter_dest_y+5, fill='blue')
                self.angle = atan2(self.inter_dest_y-self.y,self.inter_dest_x-self.x)

            ## If we have reached the intermediate point
            elif dist([self.x,self.y],[self.inter_dest_x,self.inter_dest_y]) < self.speed:
                self.angle = atan2(self.dest_y-self.y,self.dest_x-self.x)

            ## Update coordinates
            x_attempt = self.x+self.speed*cos(self.angle)
            y_attempt = self.y+self.speed*sin(self.angle)
            if x_attempt >= 10 and x_attempt+size <= columns and y_attempt >= 10 and y_attempt+size <= rows:
                break
        self.x = x_attempt
        self.y = y_attempt
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
    def __init__(self,x,y,speed,age):
        self.init(x,y,speed,age)
        self.type = 'carn'
        ## Tag of some sort
        self.n = canvas.create_oval(self.x, self.y, self.x+size, self.y+size, fill='red')
    ## carnivore eating
    def eat(self):
        for creature in creatures:
            if dist([self.x,self.y],[creature.x,creature.y]) < size and creature.type == 'herb':
                canvas.itemconfig(self.n, fill='red')
                self.age = 1
                canvas.delete(creature.n)
                creatures.remove(creature)

##Herbivore creation
class herb(creature):
    def __init__(self,x,y,speed,age):
        self.init(x,y,speed,age)
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
        new_speed = random.randint(1,5)*creature_speed
        if new_x > 10 and new_x+size < columns and new_y > 10 and new_y+size < rows:
            if creature1.type == 'herb':
                creatures.append(herb(new_x,new_y,new_speed,half_life))
            elif creature1.type == 'carn':
                creatures.append(carn(new_x,new_y,new_speed,half_life))
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
creatures= []
for _ in range(0, number_of_creatures):
    random_percent = random.randint(1, 100)
    x = random.randint(10, columns-size)
    y = random.randint(10, rows-size)
    new_speed = random.randint(1, 5)*creature_speed
    if random_percent <= per:
        creatures.append(carn(x,y,new_speed,1))
    else:
        creatures.append(herb(x,y,new_speed,1))

## List of plants
plants = []
for _ in range(0, number_of_plants):
    x = random.randint(10, columns-size)
    y = random.randint(10, rows-size)
    plants.append(Plant(x,y))

##One round
def move():
    for creature in creatures:
        creature.move()
    for plant in plants:
        plant.breed()
    for creature1 in creatures:
        for creature2 in creatures:
            breed(creature1,creature2)
    for creature in creatures:
        creature.eat()
    for creature in creatures:
        if(creature.tick()):
            creatures.remove(creature)

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
        sim.after(int(game_speed*1000),update_clock)
def togglemovesquare(event):
    global but
    if but == 0:
        but = 1
        sim.after(int(game_speed*1000), update_clock)
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
