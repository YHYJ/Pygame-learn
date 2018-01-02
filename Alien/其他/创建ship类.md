# ship.py——控制飞船的属性

> 选择用于表示飞船的图像后，需要将其显示到屏幕上
>
> 我们将创建一个名为ship的模块，其中包含Ship类，它负责管理飞船的大部分行为

```python
# 加载飞船图像
self.image = pygame.image.load('images/ship.bmp')   #加载飞船图片
```

> pygame.image.load() 函数返回一个表示飞船的surface，将这个surface存储到 self.image 中

---

```python
# 获取飞船的外接矩形 —— pygame像处理矩形（rect对象）一样处理游戏元素
self.rect = self.image.get_rect()   #使用get_rect()获取相应surface的属性rect
self.screen_rect = screen.get_rect()
```

> 处理rect对象时，可通过设置矩形四角和中心的x和y坐标值来指定矩形的位置
>
> 要将游戏元素**居中**，可设置相应rect对象的属性：
>
> > center——中心对齐
> >
> > centerx——水平居中
> >
> > centery——上下居中
>
> 要让游戏元素与屏幕**边缘对齐**，可设置相应rect对象的属性：
>
> > top——顶部对齐
> >
> > bottom——底部对齐
> >
> > left——左对齐
> >
> > right——右对齐
>
> 要调整游戏元素的**水平或垂直位置**，可设置相应rect对象的属：
>
> > x——相应矩形_左上角的x坐标_
> >
> > y——相应矩形_左上角的y坐标_

---

```python
# 将每艘新飞船放在屏幕底部中央
self.image_rect.centerx = self.screen_rect.centerx  #将self.image.rect.centerx（表示飞船的矩形中心的x坐标）和self.screen_rect.centerx（表示屏幕的矩形中心的x坐标）水平对齐
self.image_rect.bottom = self.screen_rect.bottom    #将self.image.rect.bottom（表示飞船的矩形的下边缘）和self.screen_rect.bottom（表示屏幕的矩形的下边缘）对齐
```

---

### update()函数：根据飞船坐标限制其位置范围

#### 下表列出了pygame.Rect对象所提供的所有属性：

| 属性名称               | 说明                           |
| ------------------ | ---------------------------- |
| myRect.left        | 矩形的左边的*X* 坐标的int值            |
| myRect.right       | 矩形的右边的*X* 坐标的int值            |
| myRect.top         | 矩形的顶部的*Y* 坐标的int值            |
| myRect.bottom      | 矩形的底部的*Y* 坐标的int值            |
| myRect.center      | 两个整数的一个元组：(centerx, centery) |
| myRect.centerx     | 矩形的中央的*X* 坐标的int值            |
| myRect.centery     | 矩形的中央的*Y* 坐标的int值            |
| myRect.width       | 矩形的宽度的int值                   |
| myRect.height      | 矩形的高度的int值                   |
| myRect.size        | 两个整数的一个元组：(width, height)    |
| myRect.topleft     | 两个整数的一个元组：(left, top)        |
| myRect.topright    | 两个整数的一个元组：(right, top)       |
| myRect.bottomleft  | 两个整数的一个元组：(left, bottom)     |
| myRect.bottomright | 两个整数的一个元组：(right, bottom)    |
| myRect.midleft     | 两个整数的一个元组：(left, centery)    |
| myRect.midright    | 两个整数的一个元组：(right, centery)   |
| myRect.midtop      | 两个整数的一个元组：(centerx, top)     |
| myRect.midbottom   | 两个整数的一个元组：(centerx, bottom)  |

