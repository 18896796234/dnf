import cv2


# 公共方法类

# 根据怪物坐标画出框
def draw_guai(guaiwu_zuobiao,quyujieping):
    if len(guaiwu_zuobiao) > 0:
        for i in guaiwu_zuobiao:
            cv2.rectangle(quyujieping,(i[0] - 10,i[1] - 50 ),(i[0] + 10,i[1] + 0 ),(0,0,122),2)


# 根据boss坐标画出框
def draw_boss(boss_zuobiao,quyujieping):
    if len(boss_zuobiao) > 0:
        for i in boss_zuobiao:
            cv2.rectangle(quyujieping, (i[0] - 10, i[1] - 50), (i[0] + 10, i[1] + 0), (0, 0, 255), 5)

# 根据物品坐标画出框
def draw_wupin(wupin_zuobiao, quyujieping):
    if len(wupin_zuobiao) > 0:
        for i in wupin_zuobiao:
            cv2.rectangle(quyujieping, (i[0] - 10, i[1] - 10), (i[0] + 10, i[1] + 0), (0, 255, 0), 2)

# 根据物品坐标画出框
def draw_door(door_zuobiao, quyujieping):
    if len(door_zuobiao) > 0:
        for i in door_zuobiao:
            cv2.rectangle(quyujieping, (i[0] - 10, i[1] - 10), (i[0] + 10, i[1] + 0), (0, 122, 0), 2)