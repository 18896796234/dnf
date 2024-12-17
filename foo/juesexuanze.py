import cv2
import os
import numpy as np
from foo.common import ch9329
import huoquzuobiao

import jpsb

mykey = ch9329.kk

pilao0_juese_list = []

#获取当前角色名
def dangqian_juese(datupian_huidu):
    juese_list = os.listdir('../img/q2952485845/')
    for juese_pic in juese_list:
        xiaotupian = cv2.imread('img/zhanghao/q2952485845/' + juese_pic)
        xiaotupian_huidu = cv2.cvtColor(xiaotupian, cv2.COLOR_BGR2GRAY)
        result = cv2.matchTemplate(datupian_huidu, xiaotupian_huidu, cv2.TM_CCOEFF_NORMED)

        locations = np.where(result >= 0.85)
        locations = list(zip(*locations[::-1]))
        if len(locations) > 0:
            return juese_pic
    return "无角色"

#角色选择界面，查询有疲劳角色
def kexuan_juese(datupian_huidu,zhanghao):
    juese_list = os.listdir('../img/' + zhanghao + '/juesexuanze/')
    for juese_pic in juese_list:
        if juese_pic in pilao0_juese_list:
            print("角色无疲劳:" + juese_pic)
        else:
            xiaotupian = cv2.imread('../img/' + zhanghao + '/juesexuanze/' + juese_pic)
            xiaotupian_huidu = cv2.cvtColor(xiaotupian,cv2.COLOR_BGR2GRAY)
            result = cv2.matchTemplate(datupian_huidu, xiaotupian_huidu, cv2.TM_CCOEFF_NORMED)

            locations = np.where(result >= 0.85)
            locations = list(zip(*locations[::-1]))
            if len(locations) > 0:
                return locations[0]
    return "无角色"


#判断角色是否有疲劳
def panduan_pilao(datupian_huidu,juese_name):
    global pilao0_juese_list
    #0疲劳图片
    xiaotupian = cv2.imread('../img/xtp/pilao0.png')
    xiaotupian_huidu = cv2.cvtColor(xiaotupian,cv2.COLOR_BGR2GRAY)
    result = cv2.matchTemplate(datupian_huidu, xiaotupian_huidu, cv2.TM_CCOEFF_NORMED)
    locations = np.where(result >= 0.85)
    locations = list(zip(*locations[::-1]))
    if len(locations) > 0:
        pilao0_juese_list.append(juese_name)
        return 0
    return 1


#返回角色选择界面
def fanhui_juesexuanze(datupian_huidu):
    #按esc
    #jianpanshuibao.
    mykey.keyUp('esc')
    #查看选择角色按钮位置
    xiaotupian = cv2.imread('img/zhanghao/q2952485845/xuanzejuese_bnt.png')
    xiaotupian_huidu = cv2.cvtColor(xiaotupian,cv2.COLOR_BGR2GRAY)
    but = huoquzuobiao.chazhao_tupian(datupian_huidu, xiaotupian_huidu)
    #鼠标移动到按钮位置,单击左键
    jpsb.dianji(but)


