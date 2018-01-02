# -*- coding: utf-8 -*-

import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):   #继承——Sprite类将游戏中相关的元素编组，进而同时操作编组中的所有元素
    """一个对飞船发射的子弹进行管理的类"""

    def __init__(self,ai_settings,screen,ship):
        """在飞船所处的位置创建一个子弹对象"""
        super().__init__()
        self.screen = screen

        # 创建一个表示子弹的矩形左上角的坐标是(0,0)，再设置正确的位置
        self.rect = pygame.Rect(0,0,ai_settings.bullet_width,    #创建子弹属性bullet_rect
                                ai_settings.bullet_height)  #因为子弹不是基于图像，要使用pygame.Rect()类从空白开始创建一个矩形
        self.rect.centerx = ship.rect.centerx #子弹中线对齐飞机
        self.rect.top = ship.rect.top     #子弹顶端对齐飞机顶端

        # 将子弹的y坐标设置为小数以微调子弹速度
        self.bullet_y = float(self.rect.y)

        # 子弹的颜色self.bullet_color和速度self.bullet_speed_factor
        self.bullet_color = ai_settings.bullet_color
        self.bullet_speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """向上移动子弹"""
        # 随着上移，子弹坐标不断减小。更新表示子弹 y 轴位置的小数值self.bullet_y
        self.bullet_y -= self.bullet_speed_factor
        # 更新表示子弹的二维位置的rect
        self.rect.y = self.bullet_y

    def draw_bullet(self):
        """在屏幕上绘制子弹"""
        # 在self.screen屏幕上使用颜色self.bullet_color在子弹位置self.bullet_rect绘制子弹
        pygame.draw.rect(self.screen,self.bullet_color,self.rect)