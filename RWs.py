#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from random import *

class RandomWalk:
    def __init__(self):
        """
        构造函数
        """
        self.x = 0                         #坐标x
        self.y = 0                         #坐标y
        self.k = 0                         #步数
        self.v = choice([0, 1, 2, 3])      #前一步记忆

    def FRW(self, N):
        """
        自由无规行走
        """
        if N != int(N) :
            print "N must be an integer"
        else :
            while self.k != N:
                prex = self.x
                prey = self.y

                self.v = choice([0, 1, 2, 3])
                if self.v == 0 :
                    self.x += 1
                elif self.v == 1 :
                    self.y += 1
                elif self.v == 2 :
                    self.x += -1
                elif self.v == 3 :
                    self.y += -1
                self.k += 1

                plt.plot([prex, self.x], [prey, self.y])
            plt.xlabel('x')
            plt.ylabel('y')
            plt.title('Free Random Walk')
            plt.show()
        self.k = 0     #重置步数

    def NRRW(self, N):
        """
        非即回无规步行
        """
        if N != int(N) :
            print "N must be an integer"
        else :
            while self.k != N :
                prex = self.x
                prey = self.y

                self.v = choice([self.v - 1, self.v, self.v + 1])
                self.v %= 4

                if self.v == 0 :
                    self.x += 1
                elif self.v == 1 :
                    self.y += 1
                elif self.v == 2 :
                    self.x += -1
                elif self.v == 3 :
                    self.y += -1
                self.k += 1

                plt.plot([prex, self.x], [prey, self.y])
            plt.xlabel('x')
            plt.ylabel('y')
            plt.title('Non Reversal Random Walk')
            plt.show()
        self.k = 0     #重置步数

if __name__ == '__main__' :
    rw = RandomWalk()
    rw.FRW(1000)
    rw.NRRW(1000)
    print rw.x, rw.y
