
import time

import jpsb

#角色动作
x_left = 0
x_right = 0
y_up = 0
y_down = 0

putong_jineng = [
    {'anjian':'d','shifang_shijian':0,'cd':10,'shicang':0.5}
    ,{'anjian':'f','shifang_shijian':0,'cd':10,'shicang':0.5}
    ,{'anjian':'q','shifang_shijian':0,'cd':10,'shicang':0.5}
    ,{'anjian':'w','shifang_shijian':0,'cd':10,'shicang':0.5}
    ,{'anjian':'e','shifang_shijian':0,'cd':20,'shicang':0.5}
    ,{'anjian':'r','shifang_shijian':0,'cd':30,'shicang':0.5}
    ,{'anjian':'t','shifang_shijian':0,'cd':50,'shicang':0.5}
    ,{'anjian':'g','shifang_shijian':0,'cd':40,'shicang':0.5}
]


juexing_jineng = [
    {'anjian':'y','shifang_shijian':0,'cd':100,'shicang':4}
    ,{'anjian':'u','shifang_shijian':0,'cd':160,'shicang':5}
]




def yidong(juese_zuobiao,mubiao_zuobiao):
    global x_left,x_right,y_up,y_down
    if abs(juese_zuobiao[0] - mubiao_zuobiao[0]) >= 10:
        if juese_zuobiao[0] - mubiao_zuobiao[0] > 0:
            if x_right == 1:
                time.sleep(0.01)
                jpsb.keyUp('right')
                x_right = 0
            if x_left == 1:
                pass
            elif x_left == 0:
                if abs(juese_zuobiao[0] - mubiao_zuobiao[0]) > 80:
                    time.sleep(0.01)
                    jpsb.press('left')
                    time.sleep(0.05)
                time.sleep(0.01)
                jpsb.keyDown('left')
                x_left = 1
        elif juese_zuobiao[0] - mubiao_zuobiao[0] < 0:
            if x_left == 1:
                time.sleep(0.01)
                jpsb.keyUp('left')
                x_left = 0
            if x_right == 1:
                pass
            elif x_right == 0:
                if abs(juese_zuobiao[0] - mubiao_zuobiao[0]) > 80:
                    time.sleep(0.01)
                    jpsb.press("right")
                    time.sleep(0.05)
                time.sleep(0.01)
                jpsb.keyDown('right')
                x_right = 1
    else:
        if x_left == 1:
            time.sleep(0.01)
            jpsb.keyUp('left')
            x_left = 0
        if x_right == 1:
            time.sleep(0.01)
            jpsb.keyUp('right')
            x_right = 0

    #y轴
    if abs(juese_zuobiao[1] - mubiao_zuobiao[1]) > 5:
        if juese_zuobiao[1] - mubiao_zuobiao[1] > 0:
            if y_down == 1:
                time.sleep(0.01)
                jpsb.keyUp('down')
                y_down = 0
            if y_up == 1:
                pass
            elif y_up == 0:
                time.sleep(0.01)
                jpsb.keyDown('up')
                y_up = 1
        elif juese_zuobiao[1] - mubiao_zuobiao[1] < 0:
            if y_up == 1:
                time.sleep(0.01)
                jpsb.keyUp('up')
                y_up = 0
            if y_down == 1:
                pass
            elif y_down == 0:
                time.sleep(0.01)
                jpsb.keyDown('down')
                y_down = 1
    else:
        if y_down == 1:
            time.sleep(0.01)
            jpsb.keyUp('down')
            y_down = 0
        if y_up == 1:
            time.sleep(0.01)
            jpsb.keyUp('up')
            y_up = 0



def tingzhi():
    print("停止动作")
    time.sleep(0.01)
    jpsb.keyUp('left')
    time.sleep(0.01)
    jpsb.keyUp('right')
    time.sleep(0.01)
    jpsb.keyUp('up')
    time.sleep(0.01)
    jpsb.keyUp('down')

def yidong_fangxiang(fangxiang):
    #向门的方向移动2秒
    time.sleep(0.01)
    jpsb.keyDown(fangxiang)
    time.sleep(2)
    jpsb.keyUp(fangxiang)
    time.sleep(0.01)


def gongji_guaiwu(fangxiang):
    print("攻击" + fangxiang)
    shifang_jineng_geshu = 0 #记录是否释放了技能

    time.sleep(0.01)
    jpsb.press(fangxiang)
    time.sleep(0.01)

    for jineng in putong_jineng:
        if (time.time() - jineng['shifang_shijian']) > jineng['cd']:
            jpsb.press(jineng['anjian'])
            time.sleep(0.05)
            jineng['shifang_shijian'] = time.time()
            #shifang_jineng_geshu = shifang_jineng_geshu + 1
            shifang_jineng_geshu += 1
            time.sleep(jineng['shichang'])
        if shifang_jineng_geshu >= 1:
            break
    if shifang_jineng_geshu == 0:
        time.sleep(0.01)
        jpsb.press('x')
        time.sleep(0.1)
        jpsb.press('x')
        time.sleep(0.1)
        jpsb.press('x')

def gongji_boss(fangxiang):
    shifang_jineng_geshu = 0 #记录是否释放了技能

    time.sleep(0.01)
    jpsb.press(fangxiang)
    time.sleep(0.01)

    for juexing in juexing_jineng:
        if (time.time() - juexing['shifang_shijian']) > juexing['cd']:
            jpsb.press(juexing['anjian'])
            time.sleep(0.05)
            juexing['shifang_shijian'] = time.time()
            time.sleep(juexing['shijian'])


    for jineng in putong_jineng:
        if (time.time() - jineng['shifang_shijian']) > jineng['cd']:
            jpsb.press(jineng['anjian'])
            time.sleep(0.05)
            jineng['shifang_shijian'] = time.time()
            #shifang_jineng_geshu = shifang_jineng_geshu + 1
            shifang_jineng_geshu += 1
            time.sleep(jineng['shichang'])
        if shifang_jineng_geshu >= 1:
            break

    if shifang_jineng_geshu == 0:
        time.sleep(0.01)
        jpsb.press('x')
        time.sleep(0.1)
        jpsb.press('x')
        time.sleep(0.1)
        jpsb.press('x')
