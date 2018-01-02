# game_functions.py——存放功能函数

#### 对代码进行重构，将功能函数从aline_invasion.py装移到game_functions.py，以使逻辑清晰

> 将函数放到单独的模块让while循环更简单，并让后续开发更容易：
>
> > 在模块game_functions而不是run_game()函数中完成大部分工作

---

### check_events()函数：

> 把管理事件的代码移到game_functions.py的check_events()函数中，简化run_game()并隔离事件管理循环
>
> **响应单次按键——按一次按键移动一下**
>
> > 每当用户按键时，都将在Pygame中注册一个事件，事件都是通过方法pygame.event.get()获取的
> >
> > 因此在函数check_events()中，需要指定要检查哪些类型的事件
> >
> > 按键被注册为一个KEYDOWN类型事件，检测到KEYDOWN事件时，需要检查按下的是否是特定的键：
> >
> > > 例如如果按下的是右箭头键，就增大飞船的rect.centerx值，将飞船向右移动
>
> **响应持续按键——按下移动，松开停止**
>
> >每当用户松开按键时，也在Pygame中注册一个事件，事件都是通过方法pygame.event.get()获取的
> >
> >因此在函数check_events()中，需要指定要检查哪些类型的事件
> >
> >松开按键被注册为一个KEYUP类型事件
> >
> >结合使用KEYDOWN和KEYUP事件，以及一个名为moving_right的标志来实现持续移动
> >
> >> 玩家按下右箭头键时，设置标志为True，则飞船移动；
> >>
> >> 玩家松开右箭头键时，设置标志为False，则飞船不动；

---

### update_screen()函数：

> 进一步简化run_game()
>
> 将更新屏幕的代码移到game_functions.py的update_screen()函数中
>
> 函数 update_screen() 包含三个形参：
>
> > ai_settings		##Settings类的实例化对象，像素颜色等的设置
> >
> > screen			##程序框大小
> >
> > ship			##Ship类的实例化对象，绘制飞船
>
> 将alien_invasion.py的while循环中更新屏幕的代码替换为对函数update_screen()的调用
>
> > ```python
> > game_functions.update_screen(ai_settings,screen,ship)	#将形参传入
> > ```

### update_bullets()函数

```python
bullets.update()    #对编组调用update()，编组将自动对其中的每个sprite调用update()
#因此代码行bullets.update()将为编组bullets中的每颗子弹调用bullet.update()

# 删除已经消失的子弹
for bullet in bullets.copy():  #在for循环中，不应从列表或编组中删除条目，因此必须遍历编组的副本
    if bullet.bullet_rect.bottom <= 0:  #子弹末端是否已经超出屏幕
        bullets.remove(bullet)
# 检查是否有子弹击中外星人
# 如果击中，就删除相应的子弹和外星人
collisions = pygame.sprite.groupcollide(bullets,aliens,True,True)
#遍历编组bullets中的每颗子弹和编组aliens中的每个外星人
#当有子弹和外星人的rect重叠时，groupcollide()就在它返回的字典中添加一个键-值对
#两个实参True告诉Pygame删除发生碰撞的子弹和外星人
#（要模拟能够穿行到屏幕顶端的高能子弹——消灭它击中的每个外星人，可将第一个布尔实参设置为False，并让第二个布尔实参为True，这样被击中的外星人将消失，但所有的子弹都始终有效，直到抵达屏幕顶端后消失。）

```

### update_aliens()函数

```python
check_fleet_edges(ai_settings, aliens)
aliens.update() #对编组aliens调用方法update()将自动对每个外星人调用方法update()。

# 检测外星人和飞船之间的碰撞
if pygame.sprite.spritecollideany(ship,aliens):
	pass
```

>方法spritecollideany()接受两个实参：一个精灵和一个编组
>
>它检查编组是否有成员与精灵发生了碰撞，并在找到与精灵发生了碰撞的成员后就停止遍历编组
>
>在这里，它遍历编组aliens，并返回它找到的第一个与飞船发生了碰撞的外星人
>
>如果没有发生碰撞， spritecollideany()将返回None，因此Ø处的if代码块不会执行
>
>如果找到了与飞船发生碰撞的外星人，它就返回这个外星人，因此if代码块将执行 pass

