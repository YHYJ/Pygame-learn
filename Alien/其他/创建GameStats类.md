# 跟踪游戏的统计信息

```python
class GameStats():
    """跟踪游戏的统计信息"""

    def __init__(self,ai_settings):
        """初始化统计信息"""
        self.ai_settings = ai_settings
        self.reset_stats()

    def reset_stats(self):
        """初始化在游戏运行期间可能变化的统计信息"""
        self.ships_left = self.ai_settings.ship_limit
```

>游戏运行期间只创建一个GameStats实例，但每当玩家开始新游戏时，需要重置一些统计信息
>
>为此，在方法reset_stats()中初始化大部分统计信息，而不是在\_\_init\__()中直接初始化它们
>
>但在\_\_init\__()中调用这个方法，这样创建GameStats实例时将妥善地设置这些统计信息，同时在玩家开始新游戏时也能调用reset_stats()
>当前只有一项统计信息——ships_left，其值在游戏运行期间将不断变化