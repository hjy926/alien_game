import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """管理外星人的类"""
    # Sprite是Pygame中的一个基类，用于创建游戏对象，这些对象通常具有位置、大小、图像等属性。
    # 这是 Ship 类的构造函数（初始化方法）。它接受两个参数：self 和 screen。self 是类的实例的引用，
    # 而 screen 是传递给构造函数的一个参数，通常是一个 Pygame 的 Surface 对象，代表游戏的屏幕
    def __init__(self, ai_settings, screen):
        """初始化外星人并设置其起始位置"""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        # 加载外星人图像，并设置其rect属性
        self.image = pygame.image.load('image/alien.bmp')  # 加个异常
        self.rect = self.image.get_rect()  # 获取 self.image 对象的矩形（Rect）边界框，并将其赋值给 self.rect。这个矩形对象定义了图像的位置。
        # 每个外星人最初都在屏幕左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # 存储外星人准确的位置
        self.x = float(self.rect.x)

    def blitme(self):
        """在指定位置绘制外星人"""
        self.screen.blit(self.image, self.rect)  # 调用 self.screen 对象的 blit 方法，将 self.image 指定的图像绘制到屏幕上，位置由 self.rect 确定

    def update(self):
        """向右移动外星人"""
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)  # 向右还是向左
        self.rect.x = self.x

    def check_edges(self):
        """如果外星人位于屏幕边缘，就返回True"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
