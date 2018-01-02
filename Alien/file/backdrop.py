# -*- coding: utf-8 -*-

import pygame

class Backdrop():
    """背景类"""

    def __init__(self,screen):
        """初始化背景并设置其位置"""
        self.screen = screen

        # 加载背景图并获取其外接矩形
        self.back_image = pygame.image.load('images/earth.bmp')
        self.back_image_rect = self.back_image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # 将背景图放到屏幕正中
        self.back_image_rect.center = self.screen_rect.center

    def blitme(self):
        """在指定位置绘制背景"""
        self.screen.blit(self.back_image,self.back_image_rect)