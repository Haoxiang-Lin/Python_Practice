#!/usr/bin/env python2
# -*- coding: utf-8 -*-

class QueenChess:
    def __init__(self):
        """
        构造函数
        """
        self.solves = 0                              #解的数目
        self.chessState = ['-' * 8] * 8              #生成一个棋盘

    def Solves(self):
        """
        求解函数
        """
        self.PlaceQueen(0)                           #启用迭代器
        print 'Total solutions of QueenChess problem are:', self.solves/4, '\n'
        raw_input('Press <Enter> to continue')

    def PlaceQueen(self, row):
        """
        放置皇后的函数
        """
        for col in range(8):
            if self.SafeJudge(row, col) :            #如果没有冲突
                self.chessState[row] = self.chessState[row][:col] + 'Q' + self.chessState[row][(col + 1):]
                if row < 7 :
                    self.PlaceQueen(row + 1)         #进入下一行迭代
                    self.chessState[row] = '-' * 8   #回溯并重置
                else :
                    self.solves += 1                 #成功
                    self.DrawChess()
                    self.chessState[row] = '-' * 8   #重置最后一行

    def SafeJudge(self, row, col):
        """
        位置安全性判断函数
        """
        for qRow in range(row):
            rowState = self.chessState[qRow]
            qCol = rowState.find('Q')                #qRow, qCol是已放置的皇后的位置
            if (qRow == row) or (qCol == col) or ((qCol - qRow) == (col - row)) or ((qCol + qRow) == (col + row)) :
                return False
        return True

    def DrawChess(self):
        """
        画棋盘的函数
        """
        print 'The ' + str(self.solves) + 'th solution of the QueenChess problem is: '
        print '    0   1   2   3   4   5   6   7'
        for i in range(8):
            print i, ' ',
            for j in range(8):
                print self.chessState[i][j], ' ',
            print '\n'
        raw_input('Press <Enter> to continue')

# 具体实现
# chess = QueenChess()
# chess.Solves()
