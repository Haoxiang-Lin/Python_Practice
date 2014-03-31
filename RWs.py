#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from random import choice

class RandomWalk:
    def __init__(self):
        """
        构造函数
        """
        self.x = 0                         #坐标x
        self.y = 0                         #坐标y
        self.k = 0                         #步数
        self.v = choice([0, 1, 2, 3])      #方向记忆
        self.pre = []                      #坐标记忆

    def Walk(self):
        if self.v == 0 :
            self.x += 1
        elif self.v == 1 :
            self.y += 1
        elif self.v == 2 :
            self.x += -1
        elif self.v == 3 :
             self.y += -1
        self.k += 1

    def Draw(self):
        for i in range(len(self.pre) - 1):
                plt.plot([self.pre[i][0], self.pre[i+1][0]], [self.pre[i][1], self.pre[i+1][1]])
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Free Random Walk')
        plt.show()

    def FRW(self, N):
        """
        自由无规行走
        """
        if N != int(N) :
            print "N must be an integer"
        else :
            self.pre = []
            while self.k != N:
                self.pre.append([self.x, self.y])

                self.v = choice([0, 1, 2, 3])
                self.Walk()

            self.Draw()
        self.__init__()

    def NRRW(self, N):
        """
        非即回无规步行
        """
        if N != int(N) :
            print "N must be an integer"
        else :
            self.pre = []
            while self.k != N :
                self.pre.append([self.x, self.y])

                self.v = choice([self.v - 1, self.v, self.v + 1])
                self.v %= 4
                self.Walk()

            self.Draw()
        self.__init__()

    def SAW(self, N):
        """
        自避随机行走
        """
        if N != int(N) :
            print "N must be an integer"
        else :
            self.pre = []
            while self.k != N :
                self.pre.append([self.x, self.y])

                self.v = choice([self.v - 1, self.v, self.v + 1])
                self.v %= 4
                self.Walk()

                if [self.x, self.y] in self.pre :
                    self.__init__()
                    self.SAW(N)
                    exit(0)

            self.Draw()
        self.__init__()


# if __name__ == '__main__' :
#     rw = RandomWalk()
#     rw.FRW(1000)
#     rw.NRRW(1000)
#     rw.SAW(50)
