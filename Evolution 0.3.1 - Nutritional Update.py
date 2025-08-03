#!/usr/bin/python3
from tkinter import *
import random
import time
import sys
sim = Tk()
canvas = Canvas(sim, width=2000, height=2000)
canvas.pack()
class inputs():
    def inputa(self, nums):
        while True:
            global h
            h = input()
            if h=='':
                h = nums
                break
            try:
                float(h)
                break
            except ValueError:
                print('Try again.')
print('Pixels per square(10-150):')
s = inputs()
s.inputa(50)
s = int(h)
print('Number of rows:')
rows = inputs()
rows.inputa(6)
rows = int(h)
print('Number of columns:')
columns = inputs()
columns.inputa(6)
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
e.inputa(3)
e = int(h)

print('Percentage of carnivores(0-100):')
per = inputs()
per.inputa(50)
per = int(h)

l=[]
m=[]
n=[]
dm=[]
for d in range(0, e):
    l.append('')
    ll = random.randint(1, 100)
    if ll <= per:
        l[d] = 1
    if ll >= per + 1:
        l[d] = 2
    m.append('')
    m[d] = random.randint(1, x+1)
    n.append('')
    n[d] = random.randint(1, a+1)
    o = s/4
    p = m[d]*s+(s/2)
    q = n[d]*s+(s/2)
    dd = ('d'+str(d))
    if l[d] == 1:
        canvas.create_rectangle(p-o, q-o, p+o, q+o, fill='red', tags=('carn', dd))
    if l[d] == 2:
        canvas.create_rectangle(p-o, q-o, p+o, q+o, fill='blue', outline='#008080', tags=('herb', dd))
    dm.append(1)
print('Number of plants:')
f = inputs()
f.inputa(2)
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
    global e
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
    ge = e
    for br in range (0, ge):
        for bb in range (0,ge):
            if xx[br] == xx[bb] and yy[br] == yy[bb] and br != bb and br < bb and xx[br] > 0:
                if l[br] == 2 and l[bb] == 2 and dm[br] < hl and dm[bb] < hl:
                    l.append('')
                    print(l)
                    ll = random.randint(1, 100)
                    l[e] = 2
                    m.append('')
                    m[e] = xx[br]
                    n.append('')
                    n[e] = yy[br]
                    o = s/4
                    p = m[e]*s+(s/2)
                    q = n[e]*s+(s/2)
                    dd = ('d'+str(e))
                    canvas.create_rectangle(p-o, q-o, p+o, q+o, fill='blue', outline='#008080', tags=('herb', dd))
                    dm.append(hl)                
                    yy.append(n[e])
                    xx.append(m[e])
                    e = e+1
    for fo in range (0, f):
        for cr in range (0, e):
            if fm[fo] == xx[cr] and fn[fo] == yy[cr]:
                if l[cr] == 2:
                    canvas.itemconfig('d' + str(cr), fill='blue')
                    dm[cr]=1
                    canvas.delete('f' + str(fo))
                    fm[fo] = (-1)
                    fn[fo] = (-1)
                    print('tasty')
    for nr in range (0, e):
        for nb in range (0, e):
            if xx[nr] == xx[nb] and yy[nr] == yy[nb] and nr != nb and xx[nr] > 0:
                if l[nr] == 1 and l[nb] == 2:
                    canvas.itemconfig('d' + str(nr), fill='red')
                    dm[nr]=1
                    canvas.delete('d' + str(nb))
                    xx[nb] = 0
                    yy[nb] = 0
                    print('kill')
    for de in range (0, e):
        if dm[de] == life:
            canvas.delete('d' + str(de))
            xx[de] = de * -2
            yy[de] = de * -2
            dm[de] = life + 1
            print('death')
        if dm[de] < life:
            if l[de]==1:
                canvas.itemconfig('d' + str(de), fill=llh[dm[de]])
                dm[de]=dm[de]+1
            if l[de]==2:
                canvas.itemconfig('d' + str(de), fill=llc[dm[de]])
                dm[de]=dm[de]+1
    canvas.create_rectangle(0, 0, 1300 , 700, fill='', outline='black')
print('Lifespan:')
life = inputs()
life.inputa(20)
life = int(h)
hl = int(life/2)
llc=[]
llh=[]
llv = 255/life
for llz in range(0, int(life)+1):
    lly = llv*llz
    llw = (hex(int(lly))[2:])
    if len(llw) == 1:
        llw = '0' + llw
    llc.append('#'+llw + llw + 'ff')
    llh.append('#'+'ff'+llw+llw)
but = 0
speed = 0.5
print('Speed(s)(0.1-5):')
speed = inputs()
speed.inputa(1)
speed = float(h)
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
