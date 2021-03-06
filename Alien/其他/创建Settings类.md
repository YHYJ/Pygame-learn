# settings.py——存储游戏的所有设置

> 每次给游戏添加新功能时，通常也将引入一些新设置
>
> 编写一个名为settings的模块，其中包含一个名为Settings的类：
>
> > 用于将所有设置存储在一个地方以免在代码中到处添加设置
>
> 这样，就能传递一个设置对象，而不是众多不同的设置
>
> 另外，这让函数调用更简单，且在项目增大时修改游戏的外观更容易：
>
> > 要修改游戏，只需修改settings.py中的一些值，而无需查找散布在文件中的不同设置

---

#### 设置背景色

```python
# 设置背景色
self.bg_color = (233,233,233)   #创建背景色存储到self.bg_color
```

> 在Pygame中，颜色是以RGB值指定的
>
> 这种颜色由红色、绿色和蓝色值组成，其中每个值的可能取值范围都为0~255:
>
> > (255, 0, 0)表示红色
> >
> > (0, 255, 0)表示绿色
> >
> > (0, 0, 255)表示蓝色
>
> 通过组合不同的RGB值，可创建1600万种颜色
>
> 颜色值(230, 230, 230)中，红色、蓝色和绿色量相同，它将背景设置为一种浅灰色