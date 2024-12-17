import time

from foo.common import ch9329

#键盘鼠标

mykey = ch9329.kk
#ser = serial.Serial('COM3',baudrate=9600,timeout=0.2)

time.sleep(2)

anjianma = {
    'up':'52',
    'down':'51',
    'left':'50',
    'right':'4F',
    'w':'1A',
    'a':'04',
    's':'16',
    'd':'07',
}

# def fasong(data):
#     data_str = ''.join(data)
#     hex_data = bytes.fromhex(data_str)
#     ser.write(hex_data)
#     time.sleep(0.05)

def jisuan_sum(datalist):
    total_sum = 0
    for data in datalist:
        total_sum += int(data,16)

    sum = hex(total_sum)[-2:]
    return sum

# def anxia(anjian):
#     datalist = ["57","AB","00","02","08","00","00"]
#
#     datalist.append(anjianma[anjian])#第一个键
#     datalist.append("00")#其他5个键默认不按
#     datalist.append("00")
#     datalist.append("00")
#     datalist.append("00")
#     datalist.append("00")
#     #加上最后的校验码
#     datalist.append(jisuan_sum(datalist))
#
#     fasong(datalist)

# def tanqi(annjian):
#     datalist = ["57","AB","00","02","08","00","00","00","00","00","00","00","00","0C"]
#
#     fasong(datalist)



def dianji(but):
    #鼠标移动到按钮位置
    mykey.move_to(but[0], but[1], 1920, 1080)
    #单击左键
    mykey.click('left')

def doubleClick(but):
    # 鼠标移动到按钮位置
    mykey.move_to(but[0], but[1], 1920, 1080)
    # 单击左键
    mykey.doubleClick()



def press(jian):
    #按一下键盘
    mykey.press(jian)

def anxia(jian):
    # 按一下2秒键盘
    mykey.keyDown(jian)  # 按下向右
    time.sleep(2)
    mykey.keyUp(jian)  # 松开向右


def keyUp(jian):
    print('抬起:' + jian)
    mykey.keyUp(jian)

def keyDown(jian):
    print('按下:' + jian)
    mykey.keyDown(jian)



#hex_data = bytes.fromhex('57AB000208000004000000000010')
#ser.write(hex_data)
#time.sleep(0.05)


#hex_data = bytes.fromhex('57AB00020800000400000000000C')
#ser.write(hex_data)
#time.sleep(0.05)

