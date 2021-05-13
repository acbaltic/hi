# 基本模式
'''
x = 5
while x < 10:
    print('x小於10喔!')
    print('我還困在框框裡')
    x += 1
    print(x)
print('我逃出迴圈了')
'''

# 無限迴圈： while true 要用 break 逃出圖圈
'''
while True:
    print('x小於10喔!')
    print('我還困在框框裡')
    break
print('我逃出迴圈了')
'''

# while true 處理遊戲模式
'''
while True:
    mode = input('請輸入遊戲模式： ')
    if mode == 'q':
        break
    elif mode == '1':
        print('啟動模式一')
    elif mode == '2':
        print('啟動模式二')
    elif mode == '3':
        print('啟動模式三')
    else:
        print('請輸入1、2、3或 q 離開')'''

# While True - Minecraft遊戲外掛使用
'''
from mine import *
import time

mc = Minecraft()

while True:
    pos = mc.player.getPos()
    mc.setBlock(pos.x, pos.y, pos.z, 46, 1)
    time.sleep(1)
'''
