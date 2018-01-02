# bullet.py

> Bullet类继承了从模块pygame.sprite中导入的Sprite类
>
> 通过使用Sprite，可将游戏中相关的元素编组，进而同时操作编组中的所有元素
>
> 为创建子弹实例，需要向\__init__()传递ai_settings、 screen和ship实例，还调用了super()来继承Sprite

```python
#因为子弹不是基于图像，要使用pygame.Rect()类从空白开始创建一个矩形
#创建Bullet类的实例时，必须提供矩形左上角的x和y坐标，还有矩形的宽度和高度
#创建子弹属性bullet_rect
self.bullet_rect = pygame.Rect(0,0,ai_settings.bullet_width,    #在(0,0)处创建子弹
                            ai_settings.bullet_height) 	#从ai_settings中获取子弹的宽度和高度
#因为子弹的初始位置取决于飞船当前的位置：所以要将其移到正确的位置
self.bullet_rect.centerx = ship.ship_image_rect.centerx		#子弹和飞机的中线对齐
self.bullet_rect.top = ship.ship_image_rect.top				#子弹的顶端和飞机的顶端对齐
```

