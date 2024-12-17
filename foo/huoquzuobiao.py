import os
import threading

import mss
import cv2
import numpy as np

from foo.modle import juese

wupin_zuobiao = [] #初始化物品坐标
guaiwu_zuobiao = [] #初始化怪物坐标
men_zuobiao = [] #初始化门坐标


#根据图片，获取所在坐标
def chazhao_tupian(datupian_huidu,xiaotupian_huidu):
    result = cv2.matchTemplate(datupian_huidu, xiaotupian_huidu, cv2.TM_CCOEFF_NORMED)

    locations = np.where(result >= 0.85)
    locations = list(zip(*locations[::-1]))
    if len(locations) > 0:
        return locations[0]


#根据怪物图片，判断怪物位置
def chazhao_guaiwu_tupian(datupian_huidu,xiaotupian_huidu,xiaotupian_mingcheng):
    global guaiwu_zuobiao
    result = cv2.matchTemplate(datupian_huidu, xiaotupian_huidu, cv2.TM_CCOEFF_NORMED)

    locations = np.where(result >= 0.85)
    locations = list(zip(*locations[::-1]))
    if len(locations) > 0:
        for location in locations:
            mingcheng_xinxi = xiaotupian_mingcheng.split("_")
            xiuzheng_x = mingcheng_xinxi[1]
            xiuzheng_y = mingcheng_xinxi[2]
            guaiwu_zuobiao.append((location[0] + int(xiuzheng_x),location[1]+130 + int(xiuzheng_y)))

#获取当前界面中所有怪物的位置
def huoqu_guaiwu_zuobiao(datupian_huidu):
    global guaiwu_zuobiao
    guaiwu_zuobiao = []
    guaiwutubiao_list = os.listdir('../img/guaiwu/')

    #datupian_huidu = datupian_huidu[130:535,0:799]

    threads = []

    for guaiwu_mingcheng in guaiwutubiao_list:
        xiaotupian = cv2.imread('img/guaiwu/' + guaiwu_mingcheng)
        xiaotupian_huidu = cv2.cvtColor(xiaotupian,cv2.COLOR_BGR2GRAY)

        thread = threading.Thread(target=chazhao_guaiwu_tupian,args=(datupian_huidu,xiaotupian_huidu,guaiwu_mingcheng))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()
    return guaiwu_zuobiao

#根据当前界面，获取boss位置
def huoqu_boss_zuobiao(datupian_huidu):
    #datupian_huidu = datupian_huidu[130:535,0:799]

    xiaotupian = cv2.imread('../img/guaiwu/boss.png')
    xiaotupian_huidu = cv2.cvtColor(xiaotupian,cv2.COLOR_BGR2GRAY)

    result = cv2.matchTemplate(datupian_huidu, xiaotupian_huidu, cv2.TM_CCOEFF_NORMED)

    locations = np.where(result >= 0.85)
    locations = list(zip(*locations[::-1]))

    if len(locations) > 0:
        return [(locations[0][0],locations[0][1] + 130+300)]

    return []


#根据物品图片，获取物品位置
def chazhao_wupin_tupian(datupian_huidu,xiaotupian_huidu,xiaotupian_mingcheng):
    global wupin_zuobiao
    result = cv2.matchTemplate(datupian_huidu, xiaotupian_huidu, cv2.TM_CCOEFF_NORMED)

    locations = np.where(result >= 0.85)
    locations = list(zip(*locations[::-1]))
    if len(locations) > 0:
        for location in locations:
            mingcheng_xinxi = xiaotupian_mingcheng.split("_")
            xiuzheng_x = mingcheng_xinxi[1]
            xiuzheng_y = mingcheng_xinxi[2]
            wupin_zuobiao.append((location[0] + int(xiuzheng_x),location[1]+130 + int(xiuzheng_y)))


#获取当前窗口中所有物品的坐标
def huoqu_wupin_zuobiao(datupian_huidu):
    global wupin_zuobiao
    wupin_zuobiao = []
    guaiwutubiao_list = os.listdir('../img/wupin/')

    #datupian_huidu = datupian_huidu[130:535,0:799]

    threads = []

    for wupin_mingcheng in guaiwutubiao_list:
        xiaotupian = cv2.imread('img/wupin/' + wupin_mingcheng)
        xiaotupian_huidu = cv2.cvtColor(xiaotupian,cv2.COLOR_BGR2GRAY)

        thread = threading.Thread(target=chazhao_wupin_tupian,args=(datupian_huidu,xiaotupian_huidu,wupin_mingcheng))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()
    return wupin_zuobiao


#根据门的图片，获取所在坐标
def chazhao_men_tupian_old(datupian_huidu,xiaotupian_huidu,xiaotupian_mingcheng):
    global men_zuobiao
    result = cv2.matchTemplate(datupian_huidu, xiaotupian_huidu, cv2.TM_CCOEFF_NORMED)

    locations = np.where(result >= 0.85)
    locations = list(zip(*locations[::-1]))
    if len(locations) > 0:
        for location in locations:
            mingcheng_xinxi = xiaotupian_mingcheng.split("_")
            xiuzheng_x = mingcheng_xinxi[1]
            xiuzheng_y = mingcheng_xinxi[2]
            men_zuobiao.append((location[0] + int(xiuzheng_x),location[1]+130 + int(xiuzheng_y)))

#根据门的图片，获取所在坐标
def chazhao_men_tupian(datupian_huidu,xiaotupian_huidu,xiaotupian_mingcheng,men_fangxiang):
    global men_zuobiao
    result = cv2.matchTemplate(datupian_huidu, xiaotupian_huidu, cv2.TM_CCOEFF_NORMED)

    locations = np.where(result >= 0.80)
    locations = list(zip(*locations[::-1]))
    if len(locations) > 0:
        for location in locations:
            #if men_fangxiang in xiaotupian_mingcheng:
            mingcheng_xinxi = xiaotupian_mingcheng.split("_")
            xiuzheng_x = mingcheng_xinxi[1]
            xiuzheng_y = mingcheng_xinxi[2]
            men_zuobiao.append((location[0] + int(xiuzheng_x),location[1]+130 + int(xiuzheng_y)))
            print('门坐标为',(location[0] + int(xiuzheng_x),location[1]+130 + int(xiuzheng_y)))


#获取当前窗口，所有门的位置
def huoqu_men_zuobiao(datupian_huidu,men_fangxiang):
    global men_zuobiao
    men_zuobiao = []
    men_list = os.listdir('../img/men/' + men_fangxiang + '/')

    #裁剪屏幕
    #datupian_huidu = datupian_huidu[130:535,0:799]

    threads = []

    for men_mingcheng in men_list:
        xiaotupian = cv2.imread('img/men/' + men_fangxiang + '/' + men_mingcheng)
        xiaotupian_huidu = cv2.cvtColor(xiaotupian,cv2.COLOR_BGR2GRAY)

        thread = threading.Thread(target=chazhao_men_tupian,args=(datupian_huidu,xiaotupian_huidu,men_mingcheng,men_fangxiang))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()
    return wupin_zuobiao

#根据dnf画面获取赛利亚传送阵位置
def huoqu_chuansongzhen_zuobiao(datupian_huidu):

    xiaotupian = cv2.imread('../img/xtp/chuansongzhen.png')#获取传送阵照片
    xiaotupian_huidu = cv2.cvtColor(xiaotupian,cv2.COLOR_BGR2GRAY)

    location = chazhao_tupian(datupian_huidu, xiaotupian_huidu)
    if location :
        return location[0], location[1] + 140


    #return juese_zuobiao