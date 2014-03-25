#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from reportlab.graphics.shapes import *
from reportlab.graphics.charts.lineplots import LinePlot
from reportlab.graphics.charts.textlabels import Label
from reportlab.graphics import renderPDF

def OpenData(file_name):
    '''
    读取数据
    '''
    log = open(file_name, 'r')
    data = []
    #去掉第一行
    log.readline()
    #读取数据并转换为
    for line in log:
        data.append( [float(str) for str in list(line.split())] )
    log.close()
    #读取数据到变量
    t     = [row[0] for row in data]
    v1r   = [row[1] for row in data]
    v2r   = [row[2] for row in data]
    Mbol  = [row[3] for row in data]
    dS    = [row[4] for row in data]
    y1p   = [row[5] for row in data]
    z1p   = [row[6] for row in data]
    y2p   = [row[7] for row in data]
    z2p   = [row[8] for row in data]
    ycmp  = [row[9] for row in data]
    zcmp  = [row[10] for row in data]
    return (t, v1r, v2r, Mbol, dS, y1p, z1p, y2p, z2p, ycmp, zcmp)

def Scientific(data):
    '''
    科学计数法, 返回最大值对应的指数
    '''
    temp = data[:]
    temp.sort()
    #index用于记录最大数(绝对值)对应10的次幂
    index = 0
    #全为0
    if temp[-1] == 0 :
        return temp[-1]
    #最大数大于1e3
    if abs(temp[-1]) > 1000.0 :
        while True :
            if abs(temp[-1]) < 10.0 :
                break
            temp[-1] =  temp[-1] / 10.0
            index += 1
    #最大数小于1e-3
    if abs(temp[-1]) < 0.001 :
        while True :
            if abs(temp[-1]) > 0.1 :
                break
            temp[-1] = temp[-1] * 10.0
            index -= 1
    #用最大数的对应10的次幂去除所有数
    for i in xrange(len(data)):
        data[i] = data[i]/pow(10.0, index)
    return index

def Draw(data1, data2, title_name, var_h_str, var_v_str):
    '''
    画图
    '''
    lp = LinePlot()
    #原点位置
    lp.x = 50
    lp.y = 50
    #坐标轴长宽
    lp.height = 125
    lp.width  = 300
    #使用数据
    lp.data   = [zip(data1, data2)]

    drawing = Drawing(400, 200)
    drawing.add(lp)

    #曲线颜色和名字
    lp.lines[0].strokeColor = colors.blue
    #drawing.add(String(200, 180, 'Curve1', fontSize=14, fillColor=colors.red))

    #标题
    title = Label()
    title._text = title_name
    title.fontSize    = 14
    title.x           = 200
    title.y           = 180

    #x轴标签
    Xlabel = Label()
    Xlabel._text = var_h_str
    Xlabel.fontSize   = 10
    Xlabel.x          = 380
    Xlabel.y          = 40
    Xlabel.textAnchor ='middle'
    drawing.add(Xlabel)

    #y轴标签
    Ylabel = Label()
    Ylabel._text = var_v_str
    Ylabel.fontSize   = 10
    Ylabel.x          = 30
    Ylabel.y          = 180
    Ylabel.textAnchor ='middle'
    drawing.add(Ylabel)

    renderPDF.drawToFile(drawing, 'LinePlot.pdf')

def main():
    var_list_str = ('t', 'v1r', 'v2r', 'Mbol','dS', 'y1p', 'z1p', 'y2p', 'z2p', 'ycmp', 'zcmp')
    print '  **********************************************************************'
    print '  *                   TwoStars Line Plot Program                       *'
    print '  *                                                                    *'
    print '  * Hi! This program is designed to plot Curve diagram with data from  *'
    print '  * TwoStars.cpp. Variables available are listed below:                *'
    print '  *                                                                    *'
    print '  * t    v1r    v2r    Mbol    dS    y1p    z1p    z2p    ycmp    zcmp *'
    print '  *                                                                    *'
    print '  * The diagram would be generated as pdf file                         *'
    print '  **********************************************************************'
    print '  Now please: '
    var_h_str = raw_input('  Input the variable as the horizontal axis: ')
    var_v_str = raw_input('  Input the variable as the vertical axis: ')

    if (var_h_str not in var_list_str) or (var_v_str not in var_list_str) :
        print 'Wrong variable name'

    else :
        #读取数据
        file_name = raw_input('  Input file name in which you saved data from TwoStars.cpp: ')
        var_list = OpenData(file_name)
        var_h = var_list[var_list_str.index(var_h_str)]
        var_v = var_list[var_list_str.index(var_v_str)]
        #科学计数法
        index_h = Scientific(var_h)
        if index_h != 0 :
            var_h_str = var_h_str + '\n (1e' + str(index_h) + ')'
        index_v = Scientific(var_v)
        if index_v != 0 :
            var_v_str = var_v_str + '\n (1e' + str(index_v) + ')'
        #标题名
        title_name = raw_input('  Input the title of the diagram: ')
        #画图
        Draw(var_h, var_v, title_name, var_h_str, var_v_str)

if __name__ == '__main__':
    main()

