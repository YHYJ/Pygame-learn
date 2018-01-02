# button.py

```python
# -*- coding: utf-8 -*-

import pygame.font  #导入了模块pygame.font使Pygame能够将文本渲染到屏幕上

class Button():

    def __init__(self,ai_settings,screen,msg):	#接受参数self，对象ai_settings、screen、msg
        """初始化按钮的属性"""					   #其中msg是要在按钮中显示的文本
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # 设置按钮的尺寸和其他属性
        self.width,self.height = 200, 50	#设置按钮的尺寸
        self.button_color = (0,255,0)		#设置button_color让按钮的rect对象为亮绿色
        self.text_color = (255,255,255)		#设置text_color让文本为白色
        self.font = pygame.font.SysFont(None,48)	#实参：None——默认字体，48——文本的字号

        # 创建按钮的rect对象，并使其居中
        self.rect = pygame.Rect(0,0,self.width,self.height)		#让按钮在屏幕上居中
        self.rect.center = self.screen_rect.center	#将按钮center属性设置为屏幕的center属性

        # 按钮的标签只需创建一次
        self.prep_msg(msg)	#Pygame通过将字符串渲染为图像来处理文本，调用prep_msg()来处理渲染
  
	def perp_msg(self,msg): #msg存储要渲染为图像的文本，通过font.render方法转换
        """将msg渲染为图像，并使其在按钮上居中"""
        #msg_image存储转换过的图像。font.render接受一个布尔参数决定是否开启反锯齿功能
        #self.text_color,self.button_color分别为文本和背景颜色，不指定背景颜色则为透明
        self.msg_image = self.font.render(msg,True,self.text_color,self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center	#文本图像在按钮上居中显示
```

