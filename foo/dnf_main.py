import time

import mss
import cv2
import numpy as np


from foo import juesexuanze, huoquzuobiao, panduanchangjing, juese_dongzuo, jpsb
from foo.changjing.sailiya import sailiya
from foo.common import ch9329, view_util
from foo.changjing.dixiacheng import dixiacheng
from foo.modle import juese

mykey = ch9329.kk

#dnf窗口大小
quyu = {"left":0,"top":0,"width":1000,"height":750}
wupin_zuobiao =[]
global changjing
global zhanghao
global juese_name
global juese_zuobiao
changjing = ''
zhanghao = ''
juese_name = ''
juese_zuobiao = (0, 0)

with mss.mss() as sct:
    # sct.shot(output='jieping.png')
    while True:
        #窗口截屏
        quyujieping = sct.grab(quyu)
        quyujieping = np.array(quyujieping)
        datupian_huidu = cv2.cvtColor(quyujieping,cv2.COLOR_BGR2GRAY)

        #判断当前场景
        changjing = panduanchangjing.panduanchangjing(datupian_huidu)
        print('当前画面在',changjing)
        #判断当前账号
        zhanghao = juese.get_zhanghao(datupian_huidu,zhanghao)
        print('zhanghao=',zhanghao)

        if changjing == '角色选择':
            #选择有疲劳的角色
            print('选择有疲劳的角色')
            juese_name_weizhi = juesexuanze.kexuan_juese(datupian_huidu,zhanghao)
            jpsb.doubleClick(juese_name_weizhi)
            time.sleep(4)

        if changjing == '传送阵':
            #选择次元风暴
            panduanchangjing.go_fengbao(datupian_huidu)

        if changjing == '地下城选择':
            # 选择风暴幽城
            panduanchangjing.go_fengbao_dxc(datupian_huidu)

        if changjing == '城镇':
            # 一直向右走
            juese_dongzuo.yidong_fangxiang('right')

        if changjing == '赛利亚':
            # 判断当前角色名字
            juese_name = juese.get_juese(datupian_huidu, zhanghao, juese_name)
            print('juese=', juese_name)
            sailiya(datupian_huidu,juese_zuobiao,quyujieping,zhanghao,juese_name)

        if changjing == 'boss':
            # 攻击bosss
            juese_dongzuo.gongji_boss('right')

        if changjing == '地下城':
            dixiacheng(datupian_huidu,juese_zuobiao,quyujieping)

        #复制dnf画面并展示
        cv2.imshow("dnf",quyujieping)
        #cv2.waitKey(0)
        #cv2.destroyAllWindows()

        #每50ms刷新一次画面
        if cv2.waitKey(50) & 0xFF == ord("q"):
            cv2.destroyAllWindows()
            break


#mss.tools.to_png(quyujieping.rgb,quyujieping.size,output='quyujieping_50_110.png')