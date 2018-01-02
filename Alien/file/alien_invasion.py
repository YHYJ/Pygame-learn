# -*- coding: utf-8 -*-

import pygame
from pygame.sprite import Group     #引入编组——pygame.sprite.Group类类似于列表，但提供了有助于开发游戏的额外功能

from ship import Ship
from button import Button
from backdrop import Backdrop
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
import game_functions as game_func

def run_game():
    # 初始化pygame、设置、屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("三体")

    # 绘制背景
    backdrop = Backdrop(screen)

    # 创建‘开始’按钮
    play_button = Button(ai_settings, screen, "Start")

    # 创建一个用于存储游戏统计信息的实例创建记分牌
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # 绘制一艘飞船、一个用于存储子弹的编组和一个外星人编组
    ship = Ship(ai_settings,screen)    #创建Ship的实例，飞船
    bullets = Group()   #创建GROUP类实例，子弹编组
    aliens = Group()     #外星人编组

    # 创建外星人群
    game_func.create_fleet(ai_settings, screen, ship, aliens)

    # 开始游戏主循环
    while True:
        game_func.check_events(ai_settings,screen,stats,sb,play_button,
                 ship,aliens,bullets)  #对玩家的键鼠操作进行反应

        if stats.game_active:
            ship.update()   #更新飞船位置
            game_func.update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets)   #更新外星人和子弹
            game_func.update_aliens(ai_settings,screen,stats,sb,ship,aliens,bullets)

        game_func.update_screen(ai_settings,screen,backdrop,stats,sb,
                                ship,aliens,bullets,play_button)   #使用更新后的位置绘制新屏幕

run_game()