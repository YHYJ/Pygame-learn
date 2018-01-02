# 程序主体

```python
# -*- coding: utf-8 -*-

import pygame
from pygame.sprite import Group     #引入编组——pygame.sprite.Group类类似于列表，但提供了有助于开发游戏的额外功能

from settings import Settings
from game_stats import GameStats
from ship import Ship
from backdrop import Backdrop
import game_functions as game_func

def run_game():
    # 初始化pygame、设置、屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("三体")

    # 创建一个用于存储游戏统计信息的实例
    stats = GameStats(ai_settings)

    # 绘制背景
    backdrop = Backdrop(screen)

    # 绘制一艘飞船、一个用于存储子弹的编组和一个外星人编组
    ship = Ship(ai_settings,screen)    #创建Ship的实例，飞船
    bullets = Group()   #创建GROUP类实例，子弹编组
    aliens = Group()     #外星人编组

    # 创建外星人群
    game_func.create_fleet(ai_settings, screen, ship, aliens)

    # 开始游戏主循环
    while True:
        game_func.check_events(ai_settings,screen,ship,bullets)  #对玩家的键鼠操作进行反应
        ship.update()   #更新飞船位置
        game_func.update_bullets(ai_settings,screen,ship,aliens,bullets)   #更新外星人和子弹
        
        #有外星人撞到飞船时使用这些实参来跟踪玩家还有多少艘飞船，以及创建一群新的外星人
        #有外星人撞到飞船时将余下的飞船数减1，创建一群新的外星人，并将飞船重新放置到屏幕底端中央
        #并让游戏暂停一段时间，让玩家在新外星人群出现前注意到发生了碰撞，并将重新创建外星人群
        game_func.update_aliens(ai_settings,stats,screen,ship,aliens,bullets)
        
        #使用更新后的位置绘制新屏幕
        game_func.update_screen(ai_settings,screen,backdrop,ship,aliens,bullets)

run_game()
```

