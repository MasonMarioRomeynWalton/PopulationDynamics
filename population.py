#!/usr/bin/python3
from tkinter import *
import random
from math import *
import time
import sys
import traceback
import numpy

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
size = int(get_input(15))
print('Size vertically:')
rows = int(get_input(1000))
print('Size horizontally:')
columns = int(get_input(1000))
print('Number of creatures:')
number_of_creatures = int(get_input(200))
print('Percentage of carnivores:')
per = int(get_input(15))
print('Speed of creatures relative to size:')
creature_speed = get_input(0.01)
creature_speed = size*creature_speed
print('Lifespan:')
lifespan = int(get_input(500))
half_life = int(lifespan/2)
print('Randomness of movement:')
vertex = int(get_input(3))
print('Number of plants:')
number_of_plants = int(get_input(50))
print('Time between plant reproduction:')
planttime = int(get_input(15))
print('Speed(s)(0.1-5):')
game_speed = get_input(1)

##Board creation
sim = Tk()
canvas = Canvas(sim, width=2000, height=2000)
canvas.pack()
canvas.create_rectangle(10,10,columns,rows)
clock = 0

##Creature creation
class creature:
    def init(self,x,y,speed,angle,age):
        self.x = x
        self.y = y
        self.dest_x = self.x
        self.dest_y = self.y
        self.velocity = speed
        self.angle = angle
        self.age = age
        ## If something has been eaten signals that other creatures can't also eat it this tick
        self.ghost = False
    ##Creature movement
    def move(self):
        ## Update speed first
        velocity_change = random.randint(-1,1)*creature_speed
        if velocity_change >= 0:
            self.velocity = pow((self.velocity + velocity_change), 0.999999)

        while True:
            if self.velocity < 0:
                angle_attempt = random.randint(0, int(2000*pi))/1000
            else:
                angle_attempt = self.angle+random.randint(-1,1)/10
            x_attempt = self.x+self.velocity*cos(angle_attempt)*creature_speed
            y_attempt = self.y+self.velocity*sin(angle_attempt)*creature_speed

            if x_attempt >= 10 and x_attempt+size <= columns and y_attempt >= 10 and y_attempt+size <= rows:
                ## Update coordinates
                break
            else:
                self.velocity = self.velocity/2
                self.angle = self.angle+pi


        self.x = x_attempt
        self.y = y_attempt
        self.angle = angle_attempt

        #canvas.coords(self.n, int(self.x), int(self.y), int(self.x)+size, int(self.y)+size)

    def old_move(self):
        ## Update speed first
        velocity_change = random.randint(-1,1)*creature_speed
        if velocity_change >= 0:
            self.velocity = pow((self.velocity + velocity_change), 0.999999)
        while True:
            ## If we have reached the point of destination
            if dist([self.x,self.y],[self.dest_x,self.dest_y]) <= self.velocity or self.velocity < 0:

                ## New destination
                self.dest_x = random.randint(10, columns-size)
                self.dest_y = random.randint(10, rows-size)

                angle_to_dest = atan2(self.dest_y-self.y,self.dest_x-self.x)

                ## New intermediate destination
                while True:

                    distance_to_dest = dist([self.x,self.y],[self.dest_x,self.dest_y])
                    distance_along = random.randint(0,int(distance_to_dest))

                    point_along_x = self.x+distance_along*cos(angle_to_dest)
                    point_along_y = self.y+distance_along*sin(angle_to_dest)

                    distance_sideways = random.randint(-int(distance_to_dest/2),int(distance_to_dest/2))

                    self.inter_dest_x = point_along_x+distance_sideways*cos(angle_to_dest+pi/2)
                    self.inter_dest_y = point_along_y+distance_sideways*sin(angle_to_dest+pi/2)

                    if self.inter_dest_x >= 10 and self.inter_dest_x <= columns-size and self.inter_dest_y >= 10 and self.inter_dest_y < rows-size:
                        break

                #canvas.create_rectangle(self.dest_x, self.dest_y, self.dest_x+5, self.dest_y+5, fill='green')
                #canvas.create_rectangle(self.inter_dest_x, self.inter_dest_y, self.inter_dest_x+5, self.inter_dest_y+5, fill='blue')
                self.angle = atan2(self.inter_dest_y-self.y,self.inter_dest_x-self.x)

            ## If we have reached the intermediate point
            elif dist([self.x,self.y],[self.inter_dest_x,self.inter_dest_y]) <= self.velocity:
                self.angle = atan2(self.dest_y-self.y,self.dest_x-self.x)

            ## Update coordinates
            x_attempt = self.x+self.velocity*cos(self.angle)
            y_attempt = self.y+self.velocity*sin(self.angle)
            if x_attempt >= 10 and x_attempt+size <= columns and y_attempt >= 10 and y_attempt+size <= rows:
                break
            else:
                self.velocity = 0
        self.x = x_attempt
        self.y = y_attempt
        canvas.coords(self.n, int(self.x), int(self.y), int(self.x)+size, int(self.y)+size)
    def grow_older(self):
        self.age = self.age+1
        if self.age >= lifespan:
            canvas.delete(self.n)
            return True

    def tick(self):
        if self.type == 'carn':
            canvas.itemconfig(self.n, fill=carn_life_list[self.age])
        else:
            canvas.itemconfig(self.n, fill=herb_life_list[self.age])
        canvas.coords(self.n, int(self.x), int(self.y), int(self.x)+size, int(self.y)+size)
##Carnivore creation
class carn(creature):
    def __init__(self,x,y,speed,angle,age):
        self.init(x,y,speed,angle,age)
        self.type = 'carn'
        ## Tag of some sort
        self.n = canvas.create_oval(self.x, self.y, self.x+size, self.y+size, fill='red',tags='carn')
    ## carnivore eating
    def eat(self, collision_grid, collision_grid_plant):
        for creature in collision_grid[int(self.x/size)][int(self.y/size)]:
            if creature == None:
                break
            if dist([self.x,self.y],[creature.x,creature.y]) < size and creature.type == 'herb' and creature.ghost == False:
                canvas.itemconfig(self.n, fill='red')
                self.age = 1
                canvas.delete(creature.n)
                creature.ghost = True
                creatures.remove(creature)

##Herbivore creation
class herb(creature):
    def __init__(self,x,y,speed,angle,age):
        self.init(x,y,speed,angle,age)
        self.type = 'herb'
        ## Tag of some sort
        self.n = canvas.create_oval(self.x, self.y, self.x+size, self.y+size, fill='blue', outline='#008080',tags='herb')
    ## Herbivore eating
    def eat(self, collision_grid, collision_grid_plant):
        for plant in collision_grid_plant[int(self.x/size)][int(self.y/size)]:
            if plant == None:
                break
            if dist([self.x,self.y],[plant.x,plant.y]) < size and plant.ghost == False:
                canvas.itemconfig(self.n, fill='blue')
                self.age = 1
                canvas.delete(plant.n)
                plant.ghost = True
                plants.remove(plant)

def breed(creature1,creature2):
    possible_to_breed = [creature1.n < creature2.n,
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
        direction = random.randint(0,int(2000*pi))/1000
        if which_parent == 1:
            new_x = creature1.x+size*cos(direction)
            new_y = creature1.y+size*sin(direction)
        if which_parent == 2:
            new_x = creature2.x+size*cos(direction)
            new_y = creature2.y+size*sin(direction)
        new_speed = 1
        new_angle = random.randint(0, int(2000*pi))/1000
        if new_x > 10 and new_x+size < columns and new_y > 10 and new_y+size < rows:
            if creature1.type == 'herb':
                creatures.append(herb(new_x,new_y,new_speed,new_angle,half_life))
            elif creature1.type == 'carn':
                creatures.append(carn(new_x,new_y,new_speed,new_angle,half_life))
            break



##Plant creation
class Plant():
    def __init__(self,x,y,age):
        self.x = x
        self.y = y
        self.age = age
        self.n = canvas.create_oval(self.x, self.y, self.x+size ,self.y+size, fill='lime',tags='plant')
        ## If something has been eaten signals that other creatures can't also eat it this tick
        self.ghost = False

    ## Plant spread
    def breed(self,collision_grid_plant,collision_grid_plant_num,direction_to_breed):
        if self.age == 0:

            self.age = int(planttime/2)
            new_x = self.x+size*cos(direction_to_breed)
            new_y = self.y+size*sin(direction_to_breed)

            if new_x > 10 and new_x+size < columns and new_y > 10 and new_y+size < rows:
                ## Create a view of plants in the area
                for plant in collision_grid_plant[int(new_x/size),int(new_y/size)]:
                    if plant == None:
                        break
                    if self.n != plant.n and dist([new_x,new_y],[plant.x,plant.y]) < size:
                        return
                plants.append(Plant(new_x,new_y,planttime))

    def eat(self):
        self.age = self.age-1
    def tick(self):
        canvas.itemconfig(self.n, fill=plant_life_list[self.age])

## List of creatures
creatures= []
for _ in range(number_of_creatures):
    random_percent = random.randint(0, 100)
    x = random.randint(10, columns-size)
    y = random.randint(10, rows-size)
    new_speed = 1
    angle = random.randint(0, int(2000*pi))/1000
    age = random.randint(1,int(lifespan))
    if random_percent <= per:
        creatures.append(carn(x,y,new_speed,angle,age))
    else:
        creatures.append(herb(x,y,new_speed,angle,age))

## List of plants
plants = []
for _ in range(number_of_plants):
    x = random.randint(10, columns-size)
    y = random.randint(10, rows-size)
    plants.append(Plant(x,y,random.randint(0,int(planttime))))

##One round
def move():
    global clock
    ## Create a collision grid
    collision_grid = numpy.empty([int(rows/size)+1,int(columns/size)+1,30], dtype=object)
    collision_grid_num = numpy.zeros([int(rows/size)+1,int(columns/size)+1], dtype=int)

    for creature in creatures:
        for i in range(-1,2):
            for j in range(-1,2):
                index = (int(creature.x/size)+i,int(creature.y/size)+j)
                num = collision_grid_num[index]
                collision_grid[index][num] = creature
                collision_grid_num[index] = num+1

    collision_grid_plant = numpy.empty([int(rows/size)+1,int(columns/size)+1,300], dtype=object)
    collision_grid_plant_num = numpy.zeros([int(rows/size)+1,int(columns/size)+1], dtype=int)

    for plant in plants:
        x = int(plant.x/size)
        y = int(plant.y/size)
        for index in ((x-1,y-1),(x-1,y),(x-1,y+1),(x,y-1),(x,y),(x,y+1),(x+1,y-1),(x+1,y),(x+1,y+1)):
            
                collision_grid_plant[index][collision_grid_plant_num[index]] = plant

        collision_grid_plant_num[x-1:x+2,y-1:y+2] += 1



    for creature in creatures:
        creature.move()

    direction_to_breed = numpy.random.rand(len(plants))*(2*pi)
    for u in range(len(plants)):
        plants[u].breed(collision_grid_plant, collision_grid_plant_num, direction_to_breed[u])

    for creature1 in creatures:
        for creature2 in collision_grid[int(creature1.x/size),int(creature1.y/size)]:
            if creature2 == None:
                break
            if dist([creature1.x,creature1.y],[creature2.x,creature2.y]) < size:
                breed(creature1,creature2)

    for creature in creatures:
        creature.eat(collision_grid, collision_grid_plant)

    for creature in creatures:
        if(creature.grow_older()):
            creatures.remove(creature)

    for plant in plants:
        plant.eat()

    if clock == 1:
        clock = 0

        for creature in creatures:
            creature.tick()

        for plant in plants:
            plant.tick()
    else:
        clock = clock+1

    canvas.tag_raise('herb')
    canvas.tag_raise('carn')

##Lifespan
herb_life_list=[]
carn_life_list=[]
difference = 255/lifespan
for i in range(int(lifespan)+1):
    amount = difference*i
    amount_hex = (hex(int(amount))[2:])
    if len(amount_hex) == 1:
        amount_hex = '0' + amount_hex

    herb_life_list.append('#'+amount_hex+amount_hex+'ff')
    carn_life_list.append('#'+'ff'+amount_hex+amount_hex)

plant_life_list=[]
difference = 255/planttime
for i in range(int(planttime)+1):
    amount = difference*i
    amount_hex = (hex(int(amount))[2:])
    if len(amount_hex) == 1:
        amount_hex = '0' + amount_hex

    plant_life_list.append('#'+amount_hex+'ff'+amount_hex)

##Controls
pause = 1
def update_clock():
    if pause == 0:
        move()
        sim.after(int(game_speed),update_clock)
def togglemovesquare(event):
    global pause
    if pause == 1:
        pause = 0
        sim.after(int(game_speed), update_clock)
    elif pause == 0:
        pause = 1
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
