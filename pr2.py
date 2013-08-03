"""
Author : tharindra galahena (inf0_warri0r)
Project: predator-prey simulation
Blog   : http://www.inf0warri0r.blogspot.com
Date   : 03/08/2013
License:

     Copyright 2013 Tharindra Galahena

This is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version. This is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
details.

* You should have received a copy of the GNU General Public License along with
this. If not, see http://www.gnu.org/licenses/.

"""

from Tkinter import *
import plot
import random
import pp_sim


number_of_rabbits = 50
rabbit_multiply_rate = 0.5
rabbit_max_speed = 5
rabbit_range_of_vision = 50

number_of_foxs = 20
fox_multiply_rate = 0.5
fox_max_speed = 7
fox_max_steps = 25


cw = 800
ch = 600

r = list()
f = list()

for i in range(0, number_of_rabbits):
    x = random.uniform(0, cw)
    y = random.uniform(0, ch - 180)
    r.append(pp_sim.rabbit(rabbit_max_speed, x, y, cw,
                            ch - 180, rabbit_range_of_vision))

for i in range(0, number_of_foxs):
    x = random.uniform(0, cw)
    y = random.uniform(0, ch - 180)
    f.append(pp_sim.fox(fox_max_speed, fox_max_steps, x, y, cw, ch - 180))

root = Tk()
root.title("predetor pray simulation")

chart_1 = Canvas(root, width=cw, height=ch, background="black")
chart_1.grid(row=0, column=0)

pl = plot.plot()

gn = 0

while 1:
    gn = gn + 1

    chart_1.create_line(0, ch - 173, cw, ch - 173, fill='white')

    for i in range(0, len(r)):
        chart_1.create_oval(r[i].x - 5, r[i].y - 5,
                            r[i].x + 5, r[i].y + 5,
                            fill='green')
        r[i].move(f)

    t = list()
    tmp_f = list()
    for i in range(0, len(f)):
        chart_1.create_oval(f[i].x - 5, f[i].y - 5,
                            f[i].x + 5, f[i].y + 5,
                            fill='yellow')

        min_i = f[i].move(r)
        if min_i != -1:
            t.append(min_i)
            f[i].steps = 0

        if f[i].steps <= f[i].mx_steps:
            tmp_f.append(f[i])

    p = list()
    t = list(set(t))
    tmp = list()
    for i in range(0, len(r)):
        if i not in t:
            tmp.append(r[i])

    r = tmp[:]
    f = tmp_f[:]
    if gn > 25:
        print len(r), " - ", len(f)
        pl.add1(len(r))
        pl.add2(len(f))
        for i in range(0, int(len(r) * rabbit_multiply_rate) + 1):
            x = random.uniform(0, cw)
            y = random.uniform(0, ch - 190)
            r.append(pp_sim.rabbit(rabbit_max_speed, x, y,
                                cw, ch - 180, rabbit_range_of_vision))

        for i in range(0, int(len(f) * fox_multiply_rate) + 1):
            x = random.uniform(0, cw)
            y = random.uniform(0, ch - 190)
            f.append(pp_sim.fox(fox_max_speed, fox_max_steps,
                                x, y, cw, ch - 180))

        gn = 0

    for x in range(0, pl.pointer2 - 2):
        y1 = 150 - pl.nlst1[x] + ch - 170
        y2 = 150 - pl.nlst1[x + 1] + ch - 170
        chart_1.create_line(x * 6, y1,
                            (x + 1) * 6, y2,
                            fill='red')

        y1 = 150 - pl.nlst2[x] + ch - 170
        y2 = 150 - pl.nlst2[x + 1] + ch - 170
        chart_1.create_line(x * 6, y1,
                            (x + 1) * 6, y2,
                            fill='blue')

    chart_1.update()
    chart_1.after(20)

    chart_1.delete(ALL)
root.mainloop()
