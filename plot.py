#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

def OpenData(file_name):
    '''
    读取数据
    '''
    log = open(file_name, 'r')
    data = []
    #log.readline()
    for line in log:
        data.append( [float(str) for str in list(line.split())] )
    log.close()
    x     = [row[0] for row in data]
    y     = [row[1] for row in data]
    return (x, y)

def Draw(x, y):
    '''
    画图
    '''
    font = {'family' : 'serif',
        'color'  : 'darkred',
        'weight' : 'normal',
        'size'   : 16,
        }

    plt.plot(x, y, 'k.', label=r'$ 70^{\degree} $')
    plt.title('FFT', fontdict=font)
    plt.xlabel('x', fontdict=font)
    plt.ylabel('y', fontdict=font)
    plt.subplots_adjust(left=0.15)
    #plt.axis([0.28, 0.45, -2.6, -1.4])
    #plt.legend(loc='lower left')
    #plt.gca().invert_yaxis()
    plt.show()


def main():
    file_name = 'log.txt'
    (x, y) = OpenData(file_name)
    Draw(x, y)

if __name__ == '__main__':
    main()


