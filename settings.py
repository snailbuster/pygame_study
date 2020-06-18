# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 16:09:14 2020

@author: Administrator
"""



WIDTH = 480
HEIGHT = 600
FPS = 60
FONT_NAME = 'arial'
TITLE= "JUMPY!"
HS_FILE = "heighscore.txt"

SPRITESHEET = "tiles_spritesheet.png"

#玩家属性
PLAYER_ACC = 0.5
PLAYER_FRICTION = -0.12  #摩擦力

#开始的platform
PLATFORM_LIST = [(0,HEIGHT - 40 ,WIDTH,40),
                (WIDTH/2 - 50 ,HEIGHT * 3/4, 100, 20),
                (125,HEIGHT-350,100,20),
                (350,200,100,20),
                (175,100,100,20)]
#定义颜色
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
