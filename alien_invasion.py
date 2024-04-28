import pygame

import game_functions as gf
from settings import Settings
from ship import Ship
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    # 设置
    ai_settings = Settings()
    # 主显示
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    # pygame.key.stop_text_input()
    pygame.display.set_caption("Alien Invasion")

    # 创建play按钮
    play_button = Button(ai_settings, screen, "Play")

    # 创建一个用于存储游戏统计信息的实例
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # 创建一艘飞船
    ship = Ship(ai_settings, screen)
    # 创建一个用于存储子弹的编组
    bullets = pygame.sprite.Group()
    # 创建一个外星人
    aliens = pygame.sprite.Group()

    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)
    # 开始游戏的主循环
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)  # 检测到键盘事件后
        if stats.game_active:
            ship.update()  # 更新飞船的位置
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)  # 更新子弹位置，删除已消失的子弹
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)  # 更新外星人
            gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)  # 在屏幕上显示相应的


run_game()
