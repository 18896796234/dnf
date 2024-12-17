import os
import time

import cv2
import numpy as np

import huoquzuobiao
import jpsb

changjingliebiao = ['../img/changjing/dixiacheng.png','../img/changjing/juesexuanze.png','../img/changjing/sailiya.png'
    ,'../img/changjing/chuansongzhen.png','../img/changjing/chengzhen.png','../img/changjing/boss.png'
    ,'../img/changjing/dxc_choose.png']

# changjingliebiao = ['F:\py\dnfbz\dnfbz\changjing\dixiacheng.png']



#根据dnf窗口判断所在的场景
def panduanchangjing(datupian_huidu):

    for i in changjingliebiao:
        #获取场景唯一标识图片
        xiaotupian = cv2.imread(i)
        xiaotupian_huidu = cv2.cvtColor(xiaotupian,cv2.COLOR_BGR2GRAY)

        result = cv2.matchTemplate(datupian_huidu,xiaotupian_huidu,cv2.TM_CCOEFF_NORMED)

        locations = np.where(result >= 0.85)
        locations = list(zip(*locations[::-1]))

        if len(locations) > 0:
            if 'juesexuanze' in i:
                #print('当前画面角在角色选择画面',locations)
                return '角色选择'
            if 'chuansongzhen' in i:
                #print('当前画面角在地下城',locations)
                return '传送阵'
            if 'dxc_choose' in i:
                #print('当前画面角在地下城',locations)
                return '地下城选择'
            if 'sailiya' in i:
                #print('当前画面角在赛利亚画面',locations)
                return '赛利亚'
            if 'chengzhen' in i:
                #print('当前画面角在城镇画面',locations)
                return '城镇'
            if 'boss' in i:
                return 'boss'
            if 'dixiacheng' in i:
                #print('当前画面角在地下城',locations)
                return '地下城'
            break
    return '未知场景'


#根据dnf窗口判断所在的场景_分类
def mubiao_fangxiang(datupian_huidu):
    dxc_list = os.listdir('../img/dxc/')
    for dxc_name in dxc_list:
        #获取场景唯一标识图片
        xiaotupian = cv2.imread('img/dxc/' + dxc_name)
        xiaotupian_huidu = cv2.cvtColor(xiaotupian,cv2.COLOR_BGR2GRAY)
        result = cv2.matchTemplate(datupian_huidu,xiaotupian_huidu,cv2.TM_CCOEFF_NORMED)

        locations = np.where(result >= 0.85)
        locations = list(zip(*locations[::-1]))
        if len(locations) > 0:
            dxc_name_xinxi = dxc_name.split("_")
            fangxiang = dxc_name_xinxi[1]
            print('当前在房间',dxc_name)
            return fangxiang

    return '未知方向'


#通过传送阵进入风暴幽城城镇
def go_fengbao(datupian_huidu):
    #查找风暴幽城按钮位置
    xiaotupian = cv2.imread('../img/xtp/fengbao.png')
    xiaotupian_huidu = cv2.cvtColor(xiaotupian,cv2.COLOR_BGR2GRAY)
    but = huoquzuobiao.chazhao_tupian(datupian_huidu, xiaotupian_huidu)
    #点击风暴幽城按钮
    jpsb.dianji(but)
    time.sleep(2)#延迟2秒再操作



#进入风暴幽城地下城
def go_fengbao_dxc(datupian_huidu):
    #查找风暴幽城按钮位置
    xiaotupian = cv2.imread('img/xtp/fb_dxc.png')
    xiaotupian_huidu = cv2.cvtColor(xiaotupian,cv2.COLOR_BGR2GRAY)
    but = huoquzuobiao.chazhao_tupian(datupian_huidu, xiaotupian_huidu)
    #点击风暴又称按钮
    jpsb.dianji(but)
    time.sleep(2)#延迟2秒再操作
