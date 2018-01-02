# -*- coding: utf-8 -*-

import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """飞船类"""

    def __init__(self,ai_settings,screen):  #screen参数指定飞船的位置
        """初始化飞船并设置其初始位置"""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')   #加载飞船图片
        self.rect = self.image.get_rect()     #将表示飞船的矩形存储在self.image_rect
        self.screen_rect = self.screen.get_rect()   #将表示屏幕的矩形存储在self.screen_rect中

        # 将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx  #水平居中
        self.rect.bottom = self.screen_rect.bottom    #底部对齐

        # 将飞船的初始位置转化为浮点数，self.center存储飞船的位置变化幅度
        self.center = float(self.rect.centerx)
        self.tb = float(self.rect.bottom)

        # 是否移动的标志
        self.moving_right  = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """根据移动标志调整飞船的位置"""
        # 上下调整
        #if self.moving_up and self.rect.top > self.screen_rect.top:
        #    self.tb -= self.ai_settings.ship_speed_factor
        #if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
        #    self.tb += self.ai_settings.ship_speed_factor
        #self.rect.bottom = self.tb
        # 左右调整
        if self.moving_right and self.rect.centerx < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.centerx > 0:
            self.center -= self.ai_settings.ship_speed_factor
        self.rect.centerx = self.center  #根据self.center更新飞船位置

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image,self.rect)  #根据self.image_rect指定的位置将图像self.image绘制到屏幕上

    def center_ship(self):
        """让飞船在屏幕上居中"""
        self.center = self.screen_rect.centerx  # 水平居中
        self.rect.bottom = self.screen_rect.bottom  # 底部对齐
        #为了让飞船居中，将飞船的属性center设置为屏幕中心的x坐标，而该坐标是通过属性screen_rect获得的

