# -*- coding: utf-8 -*-

#from random import randint

class Settings():
    """Settings类：用来存储《外星人入侵》的所有设置"""

    def __init__(self):
        """初始化游戏的静态设置"""
        # 屏幕设置
        self.screen_width = 740         #宽像素
        self.screen_height = 1000       #高像素
        self.bg_color = (255,255,255)   #颜色

        # 飞船设置
        self.ship_limit = 3     #玩家拥有的飞船数

        # 子弹设置
        self.bullet_width = 6       #默认6
        self.bullet_height = 22     #默认22
        self.bullet_color = (255,0,0)   #红色子弹
        self.bullet_num = 12    #设置屏幕上子弹数的最大值

        # 外星人设置
        self.fleet_drop_speed = 8      #外星人上下移动幅度，默认8

        # 控制游戏节奏的加快速度
        self.speedup_scale = 1.2

        # 外星人点数的提升速度
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置"""
        self.ship_speed_factor = 2.5    #飞船每次移动的幅度，默认2.5
        self.bullet_speed_factor = 3  # 子弹每次移动的幅度，默认3。randint(4,100)
        self.alien_speed_factor = 1  # 外星人左右移动幅度，默认1。randint(1,5)

        self.fleet_direction = 1    #1表示向右移，-1表示向左移

        # 每个外星人10分
        self.alien_points = 10

    def increase_speed(self):
        """提高游戏速度，提升外星人点数"""
        self.ship_speed_factor *= self.speedup_scale    #飞船速度
        self.bullet_speed_factor *= self.speedup_scale  #子弹移速
        self.alien_speed_factor *= self.speedup_scale   #外星人左右移速

        self.alien_points = int(self.alien_points * self.score_scale)