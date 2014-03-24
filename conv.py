#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import Image

class Converter:
    def __init__(self):
        self.width = 0                      #字符画宽度
        self.height = 0                     #字符画高度
        self.compress = 200.0               #字符密度
        self.pic_str = ''                   #储存字符画的数组
        self.character = 'MNHQOC?7>!:-;.'   #使用的字符集

    def ConvImage(self, img_name, file_name):
        """
        字符画生成函数
        """
        img = self.OpenImage(img_name)
        self.WriteASCii(img)
        self.WriteHTML(file_name)

    def OpenImage(self, img_name):
        """
        打开图片并压缩
        """
        img = Image.open(img_name)
        self.width, self.height = img.size

        delta = max(img.size) / self.compress
        self.width, self.height = int(self.width / delta), int(self.height / delta)
        img = img.resize((self.width, self.height))
        img = img.convert('L')
        return img

    def WriteASCii(self, img):
        """
        写入字符到数组
        """
        pixel = img.load()
        for h in xrange(self.height):
            for w in xrange(self.width):
                self.pic_str += self.character[int(pixel[w, h]) * (len(self.character) - 1) / 255]
                self.pic_str += ' '
            self.pic_str += '\n'

    def WriteHTML(self, file_name):
        """
        写入字符到html
        """
        html_head = '''
            <html>
              <head>
                <style type="text/css">
                  body {font-family:Monospace; font-size:5px;}
                </style>
              </head>
            <body> '''
        html_foot = '</body></html>'
        self.pic_str = html_head + ''.join(l + ' <br/>' for l in self.pic_str.splitlines()) + html_foot
        outfile = open(file_name, 'w')
        outfile.write(self.pic_str)
        outfile.close()


# conv = Converter()
# conv.ConvImage('*.jpg', '*.htm')
