#!/usr/bin/python3
from tkinter import *
import random
import time
import sys
sim = Tk()
canvas = Canvas(sim, width=2000, height=2000)
canvas.pack()
class inputs():
    def inputa(self):
        while True:
            global h
            h = input()
            try:
                float(h)
                break
            except ValueError:
                print('Try again.')
print('Pixels per square(10-150):')
s = inputs()
s.inputa()
s = int(h)
print('Number of rows:')
rows = inputs()
rows.inputa()
rows = int(h)
print('Number of colomns:')
columns = inputs()
columns.inputa()
columns = int(h)
for a in range(0,rows):
    b = a*s+s
    c = b+s
    for x in range(0, columns):
        y = x*s+s
        z = y+s
        canvas.create_rectangle(y, b, z, c)
print('Number of creatures:')
e = inputs()
e.inputa()
e = int(h)
l=[]
m=[]
n=[]
for d in range(0, e):
    l.append('')
    l[d] = random.randint(1, 2)
    m.append('')
    m[d] = random.randint(1, x+1)
    n.append('')
    n[d] = random.randint(1, a+1)
    o = s/4
    p = m[d]*s+(s/2)
    q = n[d]*s+(s/2)
    dd = ('d'+str(d))
    if l[d] == 1:
        canvas.create_rectangle(p-o, q-o, p+o, q+o, fill='pink', tags=('carn', dd))
    if l[d] == 2:
        canvas.create_rectangle(p-o, q-o, p+o, q+o, fill='cyan', tags=('herb', dd))
print('Number of plants:')
f = inputs()
f.inputa()
f = int(h)
fm=[]
fn=[]
for d in range(0, f):
    fm.append('')
    fm[d] = random.randint(1, x+1)
    fn.append('')
    fn[d] = random.randint(1, a+1)
    o = s/4
    p = fm[d]*s+(s/2)
    q = fn[d]*s+(s/2)
    canvas.create_rectangle(p-o, q-o, p+o, q+o, fill='green', tags=('food', ('f'+str(d))))
v = 0
yy = []
xx = []
i = 0    
def move():
    for u in range(0, e):
        global i
        if i == 0:
            yy.append(n[u])
            xx.append(m[u])
            global v
        v = v +1
        while True:
            w = random.randint(1,9)
            if w == 9 or xx[u] == 0:
                r = 0
                t = 0
                break
            elif w == 1 or w == 2:
                if yy[u] <= a:
                    r = s
                    t = 0
                    yy[u] = yy[u]+1
                    break
            elif w == 3 or w == 4:
                if yy[u] > 1:
                    r = -s
                    t = 0
                    yy[u] = yy[u]-1
                    break
            elif w == 5 or w == 6:
                if xx[u] <= x:
                    r = 0
                    t = s
                    xx[u] = xx[u]+1
                    break
            elif w == 7 or w == 8:
                if xx[u] > 1:
                    r = 0
                    t = -s
                    xx[u] = xx[u]-1
                    break
        canvas.move(('d' + str(u)), t, r)
    i = 1
    v = 0
    for fo in range (0, f):
        for cr in range (0, e):
            if fm[fo] == xx[cr] and fn[fo] == yy[cr]:
                if l[cr] == 2:
                    canvas.itemconfig('d' + str(cr), fill='blue')
                    canvas.delete('f' + str(fo))
                    fm[fo] = (-1)
                    fn[fo] = (-1)
                    print('tasty')
    for nr in range (0, e):
        for nb in range (0, e):
            if xx[nr] == xx[nb] and yy[nr] == yy[nb] and nr != nb:
                if l[nr] == 1 and l[nb] == 2:
                    canvas.itemconfig('d' + str(nr), fill='red')
                    canvas.delete('d' + str(nb))
                    xx[nb] = 0
                    yy[nb] = 0
                    print('kill')
but = 0
speed = 0.5
print('Speed(s)(0.1-5):')
speed = inputs()
speed.inputa()
speed =float(h)
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

