class Settings:
    """Store all settings of game Alien Invasion"""
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 750
        self.bg_color = (230, 230, 230)

        # ship settings
        self.ship_speed = 1.5
        self.ship_limit = 3

        # bullet settings
        self.bullet_speed = 1.5
        self.bullet_width = 300
        self.bullet_height = 150
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # 外星人设置
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet_direction为1表示向右移， 为-1表示向左移
        self.fleet_direction = 1
