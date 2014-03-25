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
    dS    = [row[4]/3.83e26 for row in data]
    y1p   = [row[5] for row in data]
    z1p   = [row[6] for row in data]
    y2p   = [row[7] for row in data]
    z2p   = [row[8] for row in data]
    ycmp  = [row[9] for row in data]
    zcmp  = [row[10] for row in data]
    return (t, v1r, v2r, Mbol, dS, y1p, z1p, y2p, z2p, ycmp, zcmp)

def Draw(var_h, var_v, title_name, var_h_str, var_v_str):
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
    lp.data = []
    for i in range(len(var_h)) :
        lp.data.append(zip(var_h[i], var_v[i]))

    drawing = Drawing(400, 200)
    drawing.add(lp)

    #曲线颜色和名字
    lp.lines[0].strokeColor = colors.blue
    lp.lines[1].strokeColor = colors.red
    lp.lines[2].strokeColor = colors.green
    lp.lines[3].strokeColor = colors.black
    #drawing.add(String(200, 180, 'Curve1', fontSize=14, fillColor=colors.red))

    #标题
    title = Label()
    title._text = title_name
    title.fontSize    = 14
    title.x           = 200
    title.y           = 180
    drawing.add(title)

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
    print '  * TwoStars.cpp.                                                      *'
    print '  * The diagram would be generated as pdf file                         *'
    print '  *                                                                    *'
    print '  **********************************************************************'
    print '  Now please: '
    var_h_str = 't'
    var_v_str = 'dS'
    var_h = []
    var_v = []
    while True :
        file_name = raw_input('  Input name of the file from TwoStars.cpp (Input "ok" if done): ')
        if file_name == 'ok' :
            break
        #打开文件
        var_list = OpenData(file_name)
        #读取两个变量
        var_h.append(var_list[var_list_str.index(var_h_str)])
        var_v.append(var_list[var_list_str.index(var_v_str)])
        #画图
        Draw(var_h, var_v, 'Light Curve', var_h_str, var_v_str)

if __name__ == '__main__':
    main()

