#!/bin/python3
from tkinter import *
import random
import time
tk = Tk()
canvas = Canvas(tk, width=2000, height=2000)
canvas.pack()
print('Pixels per square(10-150):')
s = int(input())
print('Number of rows(1-8):')
rows = int(input())
print('Number of colomns(1-8):')
columns = int(input())
for a in range(0,rows):
    b = a*s+s
    c = b+s
    for x in range(0, columns):
        y = x*s+s
        z = y+s
        canvas.create_rectangle(y, b, z, c)
print('Number of creatures:')
e = int(input())
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
    if l[d] == 1:
        canvas.create_rectangle(p-o, q-o, p+o, q+o, fill='pink')
    if l[d] == 2:
        canvas.create_rectangle(p-o, q-o, p+o, q+o, fill='cyan')
print('Number of plants:')
f = int(input())
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
    canvas.create_rectangle(p-o, q-o, p+o, q+o, fill='green')
v = 0
yy = []
xx = []
i = 0    
class creature():
    def move(self):
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
            canvas.move((a+1)*(x+1)+v, t, r)
        i = 1
        v = 0
        for fo in range (0, f):
            for cr in range (0, e):
                if fm[fo] == xx[cr] and fn[fo] == yy[cr]:
                    if l[cr] == 2:
                        canvas.itemconfig((a+1)*(x+1)+cr+1, fill='blue')
                        canvas.delete((a+1)*(x+1)+e+1+fo)
                        fm[fo] = (-1)
                        fn[fo] = (-1)
                        print('tasty')
        for nr in range (0, e):
            for nb in range (0, e):
                if xx[nr] == xx[nb] and yy[nr] == yy[nb] and nr != nb:
                    if l[nr] == 1 and l[nb] == 2:
                        canvas.itemconfig((a+1)*(x+1)+nr+1, fill='red')
                        canvas.delete((a+1)*(x+1)+nb+1)
                        xx[nb] = 0
                        yy[nb] = 0
                        print('kill')
less=creature()
def movesquare(event):
    if event.keysym == 'space':
        less.move()
canvas.bind_all('<KeyPress-space>', movesquare)
done = input()

