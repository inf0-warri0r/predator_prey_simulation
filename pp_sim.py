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

import random


class rabbit:
    def __init__(self, mx, x, y, cw, ch, r):
        self.mx_speed = mx
        self.x = x
        self.y = y
        self.cos = random.uniform(-1.0, 1.0)
        self.sin = random.uniform(-1.0, 1.0)
        self.width = cw
        self.height = ch
        self.r = r

    def find_near(self, lst):
        n_point = list()
        for l in lst:
            x = l.x
            y = l.y

            if self.x > x:
                if self.x - x < self.r:
                    if self.y > y:
                        if self.y - y < self.r:
                            n_point.append((x, y))
                    else:
                        if y - self.y < self.r:
                            n_point.append((x, y))
            else:
                if x - self.x < r:
                    if self.y > y:
                        if self.y - y < self.r:
                            n_point.append((x, y))
                    else:
                        if y - self.y < self.r:
                            n_point.append((x, y))

        return n_point

    def move(self, lst):
        x = 0.0
        y = 0.0
        ls = self.find_near(lst)
        for l in ls:
            x = x - (l[0] - self.x)
            y = y - (l[1] - self.y)

        d = (x * x + y * y) ** 0.5
        if d != 0:
            self.cos = x / d
            self.sin = y / d
        else:
            self.cos = random.uniform(-1.0, 1.0)
            self.sin = random.uniform(-1.0, 1.0)

        self.x = self.x + self.mx_speed * self.cos
        self.y = self.y + self.mx_speed * self.sin

        if self.x > self.width:
            self.x = self.width
        elif self.x < 0.0:
            self.x = 0.0

        if self.y > self.height:
            self.y = self.height
        elif self.y < 0.0:
            self.y = 0.0


class fox:
    def __init__(self, mx, mxs, x, y, cw, ch):
        self.mx_speed = mx
        self.speed = mx / 2
        self.steps = 0
        self.mx_steps = mxs
        self.x = x
        self.y = y
        self.cos = random.uniform(-1.0, 1.0)
        self.sin = random.uniform(-1.0, 1.0)
        self.width = cw
        self.height = ch

    def find_near(self, lst):
        mn = 1000
        mni = 0
        mn_point = (self.x, self.y)
        for i in range(0, len(lst)):
            l = lst[i]
            x = l.x
            y = l.y

            d = (self.x - x) ** 2.0
            d = d + (self.y - y) ** 2.0
            d = d ** 0.5

            if d < mn:
                mn = d
                mni = i
                mn_point = (x, y)

        return mn, mn_point, mni

    def move(self, lst):
        self.steps = self.steps + 1
        d, (x, y), min_i = self.find_near(lst)
        if d < 10:
            return min_i

        x = x - self.x
        y = y - self.y

        d = (x * x + y * y) ** 0.5
        if d != 0:
            self.cos = x / d
            self.sin = y / d
        else:
            self.cos = random.uniform(-1.0, 1.0)
            self.sin = random.uniform(-1.0, 1.0)

        self.x = self.x + self.mx_speed * self.cos
        self.y = self.y + self.mx_speed * self.sin

        if self.x > self.width:
            self.x = self.width
        elif self.x < 0.0:
            self.x = 0.0

        if self.y > self.height:
            self.y = self.height
        elif self.y < 0.0:
            self.y = 0.0

        return -1
