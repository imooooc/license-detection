# -*- coding:utf-8 -*-
# Author: Zhu Chen
# Organization: 07 LP detection group
# Create Time: 2020/04  All rights reserved
from hyperlpr import *
import cv2
import random


class PlateRecogTool:
    '''
    车牌识别工具
    '''
    def __init__(self, path):
        self.path = path

    def getColor(self):
        ls = ['black', 'white', 'red', 'blue', 'green', 'gray', 'yellow', 'brown']
        color = random.choice(ls)
        return color

    def getBrand(self):
        seq = ['劳斯莱斯', '本田', '丰田', '北京现代', '一汽大众', '宝马', '奔驰', '兰博基尼']
        brand = random.choice(seq)
        return brand

    def getPlate(self):
        plate_info = {}
        image = cv2.imread(self.path)
        plate_list = HyperLPR_plate_recognition(image)
        plate_info['plate'] = plate_list[0][0]
        plate_info['confidence'] = plate_list[0][1]
        plate_info['p1'] = plate_list[0][2][0]
        plate_info['p2'] = plate_list[0][2][1]
        plate_info['p3'] = plate_list[0][2][2]
        plate_info['p4'] = plate_list[0][2][3]
        return plate_info

    def run(self):
        info = {}
        info.update(self.getPlate())
        info['brand'] = self.getBrand()
        info['color'] = self.getColor()
        return info


if __name__ == '__main__':
    path = '/Users/charles./Projects/deep_learning/Car/2.jpg'
    info = PlateRecogTool(path).run()
    print(info)
