import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    # 这是 Ship 类的构造函数（初始化方法）。它接受两个参数：self 和 screen。self 是类的实例的引用，
    # 而 screen 是传递给构造函数的一个参数，通常是一个 Pygame 的 Surface 对象，代表游戏的屏幕
    def __init__(self, ai_settings, screen):
        """初始化飞船并设置其起始位置"""
        super(Ship, self).__init__()  # python2.7语法，也适用于python3 也可简写：super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load('image/ship.bmp')  # 加个异常
        self.rect = self.image.get_rect()  # 获取 self.image 对象的矩形（Rect）边界框，并将其赋值给 self.rect。这个矩形对象定义了图像的位置。
        self.screen_rect = screen.get_rect()  # 获取 self.screen 对象的矩形边界框，并将其赋值给 self.screen_rect。这通常用于获取屏幕的大小和位置
        # 将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx  # 将飞船的 rect 对象的水平中心（centerx）设置为与屏幕的中心（self.screen_rect.centerx）相同，从而使飞船在水平方向上居中显示。
        self.rect.bottom = self.screen_rect.bottom  # 将飞船的 rect 对象的底部（bottom）设置为与屏幕的底部（self.screen_rect.bottom）相同，从而使飞船位于屏幕底部。
        # 在飞船的属性center中存储小数值
        self.center = float(self.rect.centerx)
        # 移动标志
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """根据移动标志调整飞船的位置"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.rect.centerx -= self.ai_settings.ship_speed_factor
        # 根据self.center更新rect对象
        self.rect.centerx = self.center

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)  # 调用 self.screen 对象的 blit 方法，将 self.image 指定的图像绘制到屏幕上，位置由 self.rect 确定

    def center_ship(self):
        """让飞船在屏幕上居中"""
        self.center = self.screen_rect.centerx
