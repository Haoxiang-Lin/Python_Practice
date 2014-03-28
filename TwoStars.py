#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

def OpenData(file_name):
    '''
    读取数据
    '''
    log = open(file_name, 'r')
    data = []
    #去文件头
    log.readline()
    #读取数据并转换为数字
    for line in log:
        data.append( [float(str) for str in list(line.split())] )
    log.close()
    #读取数据到变量
    t     = [row[0] for row in data]
    v1r   = [row[1] for row in data]
    v2r   = [row[2] for row in data]
    Mbol  = [row[3] for row in data]
    dS    = [row[4]/3.83e26 for row in data]
    y1p   = [row[5] for row in data]
    z1p   = [row[6] for row in data]
    y2p   = [row[7] for row in data]
    z2p   = [row[8] for row in data]
    ycmp  = [row[9] for row in data]
    zcmp  = [row[10] for row in data]
    return (t, v1r, v2r, Mbol, dS, y1p, z1p, y2p, z2p, ycmp, zcmp)

def Draw(var_h, var_v):
    '''
    画图
    '''
    font = {'family' : 'serif',
        'color'  : 'darkred',
        'weight' : 'normal',
        'size'   : 16,
        }

    plt.plot(var_h[70], var_v[70], 'r', label=r'$ 70^{\degree} $')
    plt.plot(var_h[75], var_v[75], 'c', label=r'$ 75^{\degree} $')
    plt.plot(var_h[80], var_v[80], 'm', label=r'$ 80^{\degree} $')
    plt.plot(var_h[85], var_v[85], 'y', label=r'$ 85^{\degree} $')
    plt.plot(var_h[90], var_v[90], 'b', label=r'$ 90^{\degree} $')
    plt.title('Light Curve', fontdict=font)
    plt.xlabel('Period', fontdict=font)
    plt.ylabel(r'Magnitude', fontdict=font)
    #plt.ylabel(r'Luminosity\ $ (L_{\bigodot}) $', fontdict=font)
    plt.subplots_adjust(left=0.15)
    #plt.axis([0.85, 1, -2.6, -1.4])
    #plt.axis([0.28, 0.45, -2.6, -1.4])
    plt.axis([0, 1, -2.6, -1.4])
    plt.legend(loc='center left')
    plt.gca().invert_yaxis()
    plt.show()


def main():
    var_list_str = ('t', 'v1r', 'v2r', 'Mbol','dS', 'y1p', 'z1p', 'y2p', 'z2p', 'ycmp', 'zcmp')
    print '  **********************************************************************'
    print '  *                   TwoStars Line Plot Program                       *'
    print '  *                                                                    *'
    print '  * Hi! This program is designed to plot Curve diagram with data from  *'
    print '  * TwoStars.cpp.                                                      *'
    print '  *                                                                    *'
    print '  **********************************************************************'
    var_h_str = 't'
    var_v_str = 'Mbol'
    var_h = []
    var_v = []
    i = 0
    while True :
        file_name = str(i)#raw_input('  Input name of the file from TwoStars.cpp (Input "ok" if done): ')
        if file_name == '91' :
            break
        #打开文件
        var_list = OpenData(file_name)
        #读取两个变量
        var_h.append(var_list[var_list_str.index(var_h_str)])
        var_v.append(var_list[var_list_str.index(var_v_str)])
        i += 1
    #画图
    Draw(var_h, var_v)

if __name__ == '__main__':
    main()

