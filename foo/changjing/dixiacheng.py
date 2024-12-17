import huoquzuobiao

import cv2

import juese_dongzuo
import panduanchangjing
from foo.common import view_util

wupin_zuobiao = [] #初始化物品坐标
guaiwu_zuobiao = [] #初始化怪物坐标
men_zuobiao = [] #初始化门坐标
boss_zuobiao = [] #初始化boss坐标

mubiao_leixing = ''
mubiao_zuobiao = ()

#根据dnf画面获取角色位置
def dixiacheng(datupian_huidu,juese_zuobiao,quyujieping):

    global guaiwu_zuobiao,boss_zuobiao,wupin_zuobiao,men_zuobiao
    global mubiao_leixing,mubiao_zuobiao

    wupin_zuobiao = []  # 初始化物品坐标
    guaiwu_zuobiao = []  # 初始化怪物坐标
    men_zuobiao = []  # 初始化门坐标
    boss_zuobiao = []  # 初始化boss坐标

    mubiao_leixing = ''
    mubiao_zuobiao = ()

    #获取怪物坐标
    guaiwu_zuobiao = huoquzuobiao.huoqu_guaiwu_zuobiao(datupian_huidu)
    #print('怪物坐标为',guaiwu_zuobiao)
    #圈出怪物位置
    view_util.draw_guai(guaiwu_zuobiao,quyujieping)

    #获取boss坐标
    boss_zuobiao = huoquzuobiao.huoqu_boss_zuobiao(datupian_huidu)
    #print('boss坐标为',boss_zuobiao)
    #圈出boss位置
    view_util.draw_guai(boss_zuobiao,quyujieping)

    #获取物品坐标
    wupin_zuobiao = huoquzuobiao.huoqu_wupin_zuobiao(datupian_huidu)
    #print('物品坐标为',wupin_zuobiao)
    #圈出物品位置
    view_util.draw_wupin(wupin_zuobiao,quyujieping)


    #获取门方向
    men_fangxiang = panduanchangjing.mubiao_fangxiang(datupian_huidu)
    #获取门坐标
    men_zuobiao = huoquzuobiao.huoqu_men_zuobiao(datupian_huidu, men_fangxiang)
    #print('门坐标为',men_zuobiao)
    #圈出门所在位置
    view_util.draw_door(men_zuobiao,quyujieping)


    # 圈出boss位置
    # if len(boss_zuobiao) > 0:
    #     mubiao_leixing = 'boss'
    #     mubiao_zuobiao = boss_zuobiao

    # 圈出怪物位置
    if len(guaiwu_zuobiao) > 0:
        mubiao_leixing = 'guaiwu'
        mubiao_zuobiao = zuijin_zuobiao(guaiwu_zuobiao,juese_zuobiao)

    # 获取物品位置
    elif len(guaiwu_zuobiao) == 0 and len(wupin_zuobiao) > 0:
        mubiao_leixing = 'wupin'
        mubiao_zuobiao = wupin_zuobiao[0]

    elif len(men_zuobiao) > 0:
        mubiao_leixing = 'door'
        mubiao_zuobiao = men_zuobiao[0]

    else :
        mubiao_leixing = ''
        mubiao_zuobiao = []
        juese_dongzuo.yidong_fangxiang(men_fangxiang)
    print('当前目标为：' + mubiao_leixing)

    if mubiao_leixing == 'boss':
        juese_dongzuo.gongji_boss('right')
        # if abs(juese_zuobiao[1] - mubiao_zuobiao[1]) <= 20 and abs(juese_zuobiao[0]- mubiao_zuobiao[0]) <= 200:
        #     dongzuo = 'gongji boss'
        #     print(dongzuo)
        #     juese_dongzuo.tingzhi()
        #     if juese_zuobiao[0] - mubiao_zuobiao[0] > 0:
        #         juese_dongzuo.gongji_boss('a')
        #         pass
        #     else:
        #         juese_dongzuo.gongji_boss('d')
        #         pass
        # else:
        #     dongzuo = '移动到boss附近'
        #     print(dongzuo)
        #     juese_dongzuo.yidong(juese_zuobiao,mubiao_zuobiao)
    elif mubiao_leixing == 'guaiwu':
        if abs(juese_zuobiao[1] - mubiao_zuobiao[1]) <= 20 and abs(juese_zuobiao[0]- mubiao_zuobiao[0]) <= 200:
            dongzuo = '攻击 怪物'
            print(dongzuo)
            juese_dongzuo.tingzhi()
            if juese_zuobiao[0] - mubiao_zuobiao[0] > 0:
                juese_dongzuo.gongji_guaiwu('left')
                pass
            else:
                juese_dongzuo.gongji_guaiwu('right')
                pass
        else:
            dongzuo = '移动到 怪物 附近'
            print(dongzuo)
            juese_dongzuo.yidong(juese_zuobiao, mubiao_zuobiao)
    elif mubiao_leixing == 'wupin':
        if abs(juese_zuobiao[1] - mubiao_zuobiao[1]) <= 5 and abs(juese_zuobiao[0]- mubiao_zuobiao[0]) <= 10:
            dongzuo = '捡 物品'
            print(dongzuo)
            juese_dongzuo.tingzhi()
        else:
            dongzuo = '移动到 物品 上'
            print(dongzuo)
            juese_dongzuo.yidong(juese_zuobiao, mubiao_zuobiao)
    elif mubiao_leixing == 'door':
        if abs(juese_zuobiao[1] - mubiao_zuobiao[1]) <= 10 and abs(juese_zuobiao[0]- mubiao_zuobiao[0]) <= 10:
            dongzuo = '进 门'
            print(dongzuo)
            juese_dongzuo.tingzhi()
        else:
            dongzuo = '移动到 门 '
            print(dongzuo)
            juese_dongzuo.yidong(juese_zuobiao, mubiao_zuobiao)





def zuijin_zuobiao(coordinates_list,given_coordinate):

    min_distance = None
    zuijin_zuobiao = None

    for coord in coordinates_list:
        x1,y1 = given_coordinate
        x2,y2 = coord
        distance = abs(x1 - x2) + abs(y1 - y2)

        #下面是自己写的
        if min_distance == None or min_distance >= distance:
            min_distance = distance
            zuijin_zuobiao = coord

    return zuijin_zuobiao
