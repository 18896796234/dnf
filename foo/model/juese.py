import os

import cv2
import numpy as np

from foo import huoquzuobiao


# 角色相关方法

#查找当前账号
def get_zhanghao(datupian_huidu,zhanghao):
    if zhanghao == '':
        zhanghao_list = os.listdir('../img/zhanghao/')
        for zhanghao_name in zhanghao_list:
            xiaotupian = cv2.imread('../img/zhanghao/' + zhanghao_name)
            xiaotupian_huidu = cv2.cvtColor(xiaotupian,cv2.COLOR_BGR2GRAY)
            result = cv2.matchTemplate(datupian_huidu, xiaotupian_huidu, cv2.TM_CCOEFF_NORMED)

            locations = np.where(result >= 0.85)
            locations = list(zip(*locations[::-1]))
            if len(locations) > 0:
                zhanghao_xinxi = zhanghao_name.split("_")
                return zhanghao_xinxi[0]
        return ''
    return zhanghao

#确认当前角色
def get_juese(datupian_huidu,zhanghao,juese):

    if zhanghao == '':
        return
    juese_list = os.listdir('../img/' + zhanghao + '/juese/')
    for juese_name in juese_list:
        print('../img/' + zhanghao + '/juese/' + juese_name)
        xiaotupian = cv2.imread('../img/' + zhanghao + '/juese/' + juese_name)
        xiaotupian_huidu = cv2.cvtColor(xiaotupian,cv2.COLOR_BGR2GRAY)
        result = cv2.matchTemplate(datupian_huidu, xiaotupian_huidu, cv2.TM_CCOEFF_NORMED)

        locations = np.where(result >= 0.85)
        locations = list(zip(*locations[::-1]))
        if len(locations) > 0:
            juese_xinxi = juese_name.split("_")
            return juese_xinxi[0]
    return juese


#获取当前角色的照片，用于确定角色位置
def get_photo(zhanghao,juese_name,sort):
    path1 = '../img/' + zhanghao + '/' + juese_name + '/juese' + sort + '.png'
    print(path1)
    return path1

#获取角色坐标角色位置

#根据dnf画面获取角色位置
def huoqu_juese_zuobiao(datupian_huidu,zhanghao,juese_name,juese_zuobiao):
    if zhanghao == '':
        return
    if juese_name == '':
        return
    xiaotupian = cv2.imread(get_photo(zhanghao,juese_name,'1'))#获取角色照片
    xiaotupian_huidu = cv2.cvtColor(xiaotupian,cv2.COLOR_BGR2GRAY)

    location = huoquzuobiao.chazhao_tupian(datupian_huidu, xiaotupian_huidu)
    if location :
        return location[0], location[1] + 140

    xiaotupian = cv2.imread(get_photo(zhanghao,juese_name,'2'))#获取角色照片
    xiaotupian_huidu = cv2.cvtColor(xiaotupian, cv2.COLOR_BGR2GRAY)
    location = huoquzuobiao.chazhao_tupian(datupian_huidu, xiaotupian_huidu)
    if location:
        return location[0], location[1] + 140
    return juese_zuobiao

