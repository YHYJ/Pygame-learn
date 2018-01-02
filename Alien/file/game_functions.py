# -*- coding: utf-8 -*-

import sys,pygame
from time import sleep

from bullet import Bullet
from alien import Alien


def fire_bullet(ai_settings, screen, ship, bullets):
    # 创建一颗子弹，并加入到编组bullets中
    if len(bullets) < ai_settings.bullet_num:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def check_keydown_events(event,ai_settings,screen,sb,stats,ship,aliens,bullets):    #传递编组bullets
    """响应按键"""
    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:  #按右箭头
        ship.moving_right = True
    elif event.key == pygame.K_LEFT or event.key == pygame.K_a: #按左箭头
        ship.moving_left = True
#    elif event.key == pygame.K_UP or event.key == pygame.K_w:   #按上箭头
#        ship.moving_up = True
#    elif event.key == pygame.K_DOWN or event.key == pygame.K_s: #按下箭头
#        ship.moving_down = True
    elif event.key == pygame.K_ESCAPE:  # ESC退出游戏
        pygame.quit()
        sys.exit()
    elif event.key == pygame.K_g and not stats.game_active: #按G并且游戏出于非活动状态
        start_game(ai_settings,screen,sb,stats,ship,aliens,bullets)  #开始游戏
    elif event.key == pygame.K_SPACE:  # 空格键发射子弹
        fire_bullet(ai_settings, screen, ship, bullets)

def check_keyup_events(event,ship):
    """响应松开按键"""
    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
        ship.moving_left = False
#    elif event.key == pygame.K_UP or event.key == pygame.K_w:
#        ship.moving_up = False
#    elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
#        ship.moving_down = False

def check_events(ai_settings,screen,stats,sb,play_button,
                 ship,aliens,bullets):   #包含形参ship以便移动飞船，bullets以便绘制子弹
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   #判断是点击关闭按钮
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:  # ↑ 或是进行按键操作
            check_keydown_events(event,ai_settings,screen,sb,stats,ship,aliens,bullets)
        elif event.type == pygame.KEYUP:    #停止按键
            check_keyup_events(event,ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:  #响应全部鼠标单击事件
            mouse_x,mouse_y = pygame.mouse.get_pos()  #返回鼠标单击的x,y坐标
            check_play_button(ai_settings,screen,stats,sb,play_button,
                              ship,aliens,bullets,mouse_x,mouse_y)

def check_play_button(ai_settings,screen,stats,sb,play_button,ship,
                      aliens,bullets,mouse_x,mouse_y):
    """检测到玩家单击Start按钮区域时开始游戏"""
    # 使用collidepoint()检查鼠标单击位置是否在按钮的rect内
    button_clicked = play_button.rect.collidepoint(mouse_x,mouse_y)
    if button_clicked and not stats.game_active:
        start_game(ai_settings,screen,sb,stats,ship,aliens,bullets)

def start_game(ai_settings,screen,sb,stats,ship,aliens,bullets):
    # 每次重新开始游戏重置游戏设置
    ai_settings.initialize_dynamic_settings()
    pygame.mouse.set_visible(False)     #游戏开始后隐藏光标
    stats.reset_stats()     #重置游戏统计信息
    stats.game_active = True

    # 重置记分牌图像
    sb.prep_images()

    # 清空外星人和子弹编组
    aliens.empty()
    bullets.empty()

    # 创建一群新的外星人，让飞船居中
    create_fleet(ai_settings,screen,ship,aliens)
    ship.center_ship()

def update_screen(ai_settings,screen,backdrop,
                  stats,sb,ship,aliens,bullets,play_button):
    # 更新屏幕上的图像，并切换到新屏幕
    screen.fill(ai_settings.bg_color)   #接受一个颜色参数绘制屏幕
    backdrop.blitme()    #绘制背景
    # 在飞船和外星人后面重绘所有子弹
    for bullet in bullets.sprites():    #方法bullets.sprites()返回一个列表，包含编组bullets的所有精灵
        bullet.draw_bullet()    #draw()绘制编组里每个子弹
    ship.blitme()        #绘制飞船
    aliens.draw(screen)      #aliens.draw(screen)在屏幕上绘制编组中的每个外星人

    # 显示得分
    sb.show_score()

    # 如果游戏处于非活动状态，就绘制‘开始’按钮
    if not stats.game_active:
        play_button.draw_button()

    # 只让最近绘制的屏幕可见
    pygame.display.flip()

def update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets):
    """更新子弹的位置，并删除已消失子弹"""
    # 更新子弹位置
    bullets.update()    #对编组调用update()，编组将自动对其中的每个sprite调用update()
    #因此代码行bullets.update()将为编组bullets中的每颗子弹调用bullet.update()

    # 删除已经消失的子弹
    for bullet in bullets.copy():  #在for循环中，不应从列表或编组中删除条目，因此必须遍历编组的副本
        if bullet.rect.bottom <= 0:  #子弹末端是否已经超出屏幕
            bullets.remove(bullet)

    check_bullet_alien_collisions(ai_settings,screen,stats,sb,ship,aliens,bullets)

def check_bullet_alien_collisions(ai_settings,screen,stats,sb,ship,aliens,bullets):
    """响应子弹和外星人的碰撞"""
    # 删除发生碰撞的子弹和外星人
    collisions = pygame.sprite.groupcollide(bullets,aliens,True,True)

    if collisions:  #如果外星人和子弹发生碰撞
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
            sb.prep_score()
        check_high_score(stats,sb)

    # 检查外星人是否全部消灭
    if len(aliens) == 0:    #检查外星人编组aliens是否为空
        # 删除现有的子弹并新建一群外星人
        bullets.empty() #aliens编组为空的话，使用方法empty()删除编组中余下的所有子弹
        ai_settings.increase_speed()    #加快游戏节奏

        lift_level(stats, sb)

        create_fleet(ai_settings,screen,ship,aliens)  #调用create_fleet()，再次在屏幕上显示一群外星人

def lift_level(stats,sb):
    """在外星人群被消灭干净时提升等级"""
    # 如果整群外星人都被消灭，就提高一个等级
    stats.level += 1
    sb.prep_level()

def get_number_aliens_x(ai_settings,alien_width):
    """计算一行可容纳多少外星人"""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def get_number_rows(ai_settings,ship_height,alien_height):
    """计算屏幕可容纳多少行外星人"""
    available_space_y = (ai_settings.screen_height -
                         (4 * alien_height) - ship_height)

    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def create_alien(ai_settings, screen, aliens, alien_number,row_number):
    """创建一个外星人并放在当前行"""
    alien = Alien(ai_settings, screen)  #第一个外星人
    alien_width = alien.rect.width      #获取外星人宽度
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def create_fleet(ai_settings, screen, ship, aliens):
    """创建外星人舰队"""
    # 创建一个外星人，并计算一行可容纳多少外星人
    alien = Alien(ai_settings,screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings,
                                  ship.rect.height,alien.rect.height)
    # 创建外星人群
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen,aliens, alien_number,row_number)

def check_fleet_edges(ai_settings, aliens):
    """有外星人到达边缘时采取相应的措施"""
    for alien in aliens.sprites():
        if alien.check_edges():     #如果有外星人到达边缘
            change_fleet_direction(ai_settings,aliens)
            break

def change_fleet_direction(ai_settings,aliens):
    """将整群外星人下移，并改变它们的水平运动方向"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def ship_hit(ai_settings,screen,stats,sb,ship,aliens,bullets):
    """响应被外星人撞到的飞船"""
    if stats.ships_left > 0:
        # 将ships_left减1
        stats.ships_left -= 1   #飞船数

        # 更新记分牌
        sb.prep_ships()

        # 清空外星人和子弹列表
        aliens.empty()
        bullets.empty()

        # 创建一群新的外星人，并将飞船放到屏幕底端中央
        create_fleet(ai_settings,screen,ship,aliens)    #新外星人
        ship.center_ship()

        # 暂停
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)  # 游戏结束后显示光标

def check_aliens_bottom(ai_settings,screen,stats,sb,ship,aliens,bullets):
    """检查是否有外星人到达了屏幕底端"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # 像飞船被撞到一样进行处理
            ship_hit(ai_settings,screen,stats,sb,ship,aliens,bullets)
            break

def update_aliens(ai_settings,screen,stats,sb,ship,aliens,bullets):
    """检查是否有外星人位于屏幕边缘后更新外星人的位置"""
    check_fleet_edges(ai_settings, aliens)
    aliens.update() #对编组aliens调用方法update()将自动对每个外星人调用方法update()。

    # 检测外星人和飞船之间的碰撞
    if pygame.sprite.spritecollideany(ship,aliens):
        ship_hit(ai_settings,screen,stats,sb,ship,aliens,bullets)

    # 检测外星人和屏幕底端之间的碰撞
    check_aliens_bottom(ai_settings,screen,stats,sb,ship,aliens,bullets)

def check_high_score(stats,sb):
    """检查是否诞生了新的最高分"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_heigh_score()