# -*- coding: utf-8 -*-

import pygame.font
from pygame.sprite import Group

from ship import Ship
#from  game_stats import GameStats

class Scoreboard():
    """显示得分信息的类"""

    def __init__(self,ai_settings,screen,stats):
        """初始化显示得分涉及的属性"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        # 显示得分信息的字体设置
        self.text_color = (30,30,30)    #设置文本颜色
        self.font = pygame.font.SysFont(None,32)    #实例化一个字体对象

        # 准备包含最高得分、当前得分、玩家等级和飞船剩余数量的图像
        self.prep_images()

    def prep_images(self):
        """准备包含最高得分、当前得分、玩家等级和飞船剩余数量的图像"""
        # 准备包含最高得分和当前得分的图像
        self.prep_score()  # 将要显示的文本转换为图像
        self.prep_heigh_score()

        # 准备玩家等级的图像和飞船剩余数量的图像
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        """将得分转换为一幅渲染的图像"""
        #函数round()通常让小数精确到小数点后多少位，其中小数位数是由第二个实参指定的
        rounded_score = round(self.stats.score, -1)  #如果第二个实参为负数,将圆整到最近的10、100、1000等整数倍,这里是10的整数倍
        score_str = "Sc:" + "{:,}".format(rounded_score)   #字符串格式设置，使Py将数值转换为字符串时在其中插入千位分隔符
        self.score_image = self.font.render(score_str,True,self.text_color)     #,self.ai_settings.bg_color)
        # 将得分显示在屏幕右上角
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 10    #得分牌左边缘与屏幕左边缘相距10像素
        self.score_rect.top = 5

    def prep_heigh_score(self):
        """将最高得分转换为渲染的图像"""
        high_score = round(self.stats.high_score, -1)
        high_score_str = "Top:" +  "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str,True,
                            self.text_color)    #,self.ai_settings.bg_color
        # 将最高得分放在屏幕顶部中央
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx + 110
        self.high_score_rect.top = self.score_rect.top

    def prep_level(self):
        """将等级转换为渲染的图像"""
        self.level_image = self.font.render("Lv:" + str(self.stats.level), True,
                                self.text_color)    #,self.ai_settings.bg_color
        # 将等级放在当前得分下方
        self.level_rect = self.level_image.get_rect()
        self.level_rect.left = self.screen_rect.centerx - 140
        self.level_rect.top = self.score_rect.top

    def prep_ships(self):
        """显示还剩下多少飞船"""
        for ship_number in range(self.stats.ships_left + 1):
            self.ship_image = self.font.render("Ship:" + str(ship_number),True,
                                           self.text_color)
            self.ship_rect = self.ship_image.get_rect()
            self.ship_rect.left = self.screen_rect.left + 10
            self.ship_rect.top = self.score_rect.top

        # 图形显示，因为飞机图片太大，弃用
        #self.ships = Group()
        #for ship_number in range(self.stats.ships_left):
        #   ship = Ship(self.ai_settings, self.screen)  #Ship实例
        #   ship.rect.x = 10 + ship_number * ship.rect.width
        #   ship.rect.y = 0
        #   self.ships.add(ship)

    def show_score(self):
        """在屏幕上显示当前得分、最高得分和玩家等级"""
        ship = Ship
        self.screen.blit(self.score_image,self.score_rect)
        self.screen.blit(self.high_score_image,self.high_score_rect)
        self.screen.blit(self.level_image,self.level_rect)
        self.screen.blit(self.ship_image, self.ship_rect)

        # 绘制图形飞船
        #self.ships.draw(self.screen)
