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


class plot:

    def __init__(self):
        self.min = 0
        self.max = 100
        self.lst1 = list()
        self.lst2 = list()
        self.pointer1 = 0
        self.pointer2 = 0
        self.nlst1 = list()
        self.nlst2 = list()
        for i in range(0, 100):
            self.lst1.append(0.0)
            self.nlst1.append(0.0)
            self.lst2.append(0.0)
            self.nlst2.append(0.0)

    def normalize(self):
        ls = sorted(self.lst1)
        self.max = ls[99]
        self.min = ls[0]
        ls = sorted(self.lst2)
        if self.max < ls[99]:
            self.max = ls[99]
        if self.min > ls[0]:
            self.min = ls[0]

        for i in range(0, 100):
            self.nlst1[i] = self.lst1[i] - self.min
            self.nlst1[i] = self.nlst1[i] * 100.0 / (self.max - self.min)
            self.nlst2[i] = self.lst2[i] - self.min
            self.nlst2[i] = self.nlst2[i] * 100.0 / (self.max - self.min)

    def add1(self, a):
        if self.pointer1 < 100:
            self.lst1[self.pointer1] = a
            self.pointer1 = self.pointer1 + 1
        else:
            self.lst1.pop(0)
            self.lst1.append(a)

    def add2(self, a):
        if self.pointer2 < 100:
            self.lst2[self.pointer2] = a
            self.pointer2 = self.pointer2 + 1
        else:
            self.lst2.pop(0)
            self.lst2.append(a)
        self.normalize()
