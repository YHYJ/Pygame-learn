# -*- coding: utf-8 -*-

import sys      #使用sys模块退出游戏
import pygame   #游戏开发模块

def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()       #初始化
    screen = pygame.display.set_mode((750,1000))    #创建窗口，尺寸(750,1000)
    pygame.display.set_caption("三体入侵")      #标题

    # 设置背景色
    bg_color = (233,233,233)   #创建背景色存储到bg_color

    # 开始游戏的主循环
    while True:

        # 事件循环——监视键盘和鼠标事件
        for event in pygame.event.get():    #访问pygame检测到的事件
            if event.type == pygame.QUIT:
                sys.exit()

        # 每次循环都用背景色填充重绘屏幕
        screen.fill(bg_color)   #只接受颜色参数

        # 管理屏幕更新——只让最近绘制的屏幕可见
        pygame.display.flip()

run_game()  #初始化游戏并开始主循环
