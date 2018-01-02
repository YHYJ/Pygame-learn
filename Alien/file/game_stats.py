# -*- coding: utf-8 -*-

class GameStats():
    """跟踪游戏的统计信息"""

    def __init__(self,ai_settings):
        """初始化统计信息"""
        self.ai_settings = ai_settings
        self.reset_stats()
        # 使游戏刚启动时处于非活动状态
        self.game_active = False

        # 任何情况下都不应重置最高纪录
        self.high_score = 0

    def reset_stats(self):
        """游戏重新开始时初始化随游戏进行变化的统计信息"""
        self.ships_left = self.ai_settings.ship_limit   #ship_limit是玩家的飞船数
        self.score = 0  #玩家初始得分
        self.level = 1  #玩家初始等级