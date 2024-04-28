class Settings():
    """存储外星人入侵的所有类"""

    def __init__(self):
        """屏幕设置"""
        # 控制游戏的外观
        self.screen_width = 1200
        self.screen_height = 800
        # self.bg_color = (255, 240, 245)
        self.bg_color = (230, 230, 230)

        # 子弹的设置
        self.bullet_width = 3
        self.bullet_height = 15
        # self.bullet_color = (128, 128, 128)
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3  # 子弹数量

        # 外星人设置
        self.fleet_drop_speed = 10

        # 以什么样的速度游戏节奏
        self.speedup_scale = 1.1
        # 外星人点数的提高速度
        self.score_scale = 1.5

        self.initialize_dynamic_settings()   # 飞船，子弹，外星人的初始速度

        # 飞船设置
        self.ship_limit = 3

        # 飞船，子弹，外星人的初始速度
    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        # fleet_direction为1表示向右移动，为-1表示向左移动
        self.fleet_direction = 1

        #记分
        self.alien_points = 50

    def increase_speed(self):
        """提高速度设置"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)
