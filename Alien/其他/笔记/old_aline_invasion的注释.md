# aline_invasion.py

#### 创建 Pygame 窗口以及响应用户输入

```python
# 初始化游戏并创建一个屏幕对象
pygame.init()    # 初始化景设置，让Pygame能够正确工作
screen = pygame.display.set_mode((750,1000))    # 窗口尺寸(750,1000)
pygame.display.set_caption("三体入侵")      #标题
```

>1.调用 pygame.display.set_mode() 创建名为screen的显示窗口，游戏的所有图形元素都在其中绘制
>
>2.对象screen是一个surface ——
>
>>Pygame中，surface是屏幕的一部分，用于显示游戏元素
>>
>>在这个游戏中，每个元素（如外星人或飞船）都是一个surface
>>
>>display.set_mode()返回的surface表示整个游戏窗口
>>
>>激活游戏的动画循环后，每经过一次循环都将自动重绘这个surface

---

```python
# 事件循环——监视键盘和鼠标事件
for event in pygame.event.get():   # 写事件循环以响应用户操作。所有键盘和鼠标事件都将使for循环运行
	if event.type == pygame.QUIT:  # 单击关闭按钮，将检测到pygame.QUIT事件
    	sys.exit()				   # 然后调用sys.exit()来退出游戏
```

---

```python
# 管理屏幕更新——只让最近绘制的屏幕可见
pygame.display.flip()
```

> pygame.display.flip() 代码在每次执行while循环时绘制一个空屏幕并擦去旧屏幕，使得只有新屏幕可见
>
> > 移动游戏元素时， pygame.display.flip()不断更新屏幕，以显示元素的新位置，并在原来位置隐藏元素，从而营造平滑移动的效果



