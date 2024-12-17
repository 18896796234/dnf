from foo import juesexuanze, huoquzuobiao, juese_dongzuo
from foo.common import view_util
from foo.modle import juese

wupin_zuobiao = [] #初始化物品坐标
guaiwu_zuobiao = [] #初始化怪物坐标
men_zuobiao = [] #初始化门坐标
boss_zuobiao = [] #初始化boss坐标

mubiao_leixing = ''
mubiao_zuobiao = ()

#根据dnf画面获取角色位置
def sailiya(datupian_huidu,juese_zuobiao,quyujieping,zhanghao,juese_name):
    if juese_name != '':
        # 查看当前角色是否有疲劳，1:有，0:没有
        pilao = juesexuanze.panduan_pilao(datupian_huidu, juese_name)
        print(juese_name,'的疲劳还有',pilao)
        if pilao == 0:
            # 回到角色选择界面
            juesexuanze.fanhui_juesexuanze(datupian_huidu)
        else:
            # 判断当前角色所在坐标
            juese_zuobiao = juese.huoqu_juese_zuobiao(datupian_huidu, zhanghao, juese_name, juese_zuobiao)
            print('角色坐标为', juese_zuobiao)
            if juese_zuobiao == (0, 0):
                print('暂时无法获取角色坐标，无动作')
            else:
                # 移动到传送阵
                # xiaotupian = cv2.imread('../img/xtp/chuansongzhen.png')  # 获取角色照片
                # xiaotupian_huidu = cv2.cvtColor(xiaotupian, cv2.COLOR_BGR2GRAY)
                # csz_weizhi = huoquzuobiao.chazhao_tupian(datupian_huidu,xiaotupian_huidu)
                csz_weizhi = huoquzuobiao.huoqu_chuansongzhen_zuobiao(datupian_huidu)
                print('传送阵位置=', csz_weizhi)
                #圈出传送阵位置
                view_util.draw_wupin(csz_weizhi,quyujieping)
                print('移动到传送阵',csz_weizhi)
                juese_dongzuo.yidong(juese_zuobiao, csz_weizhi)
                # mykey.press('right')#点击向右
                # mykey.keyDown('right')#按下向右
                # time.sleep(2)
                # mykey.keyUp('right')#松开向右


