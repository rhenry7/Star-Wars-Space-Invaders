class Settings():
    # a class to store all the settings for Alien Invasion

    def __init__(self):
        # initialize the game's settings.
        # screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)
        self.bullets_allowed = 10
        self.ship_speed = 1.5
        self.ship_limit = 3
        # Bullet settings
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (250, 0, 0)
        # ALIEN SETTINGS
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # HOW QUICKLY THE GAME SPEEDS UP
        self.speedup_scale = 1.5
        # HOW QUICKLY THE ALIEN POINT VALUES INCREASE
        self.score_scale = 1.5
        self.initialize_dynamic_settings()
        # FLEET_DIRECTION OF 1 REPRESENTS RIGHT; -1 REPRESENTS LEFT.
        self.fleet_direction = 1
    def initialize_dynamic_settings(self):
        # INITIALIZE SETTINGS THAT CHANGE THROUGHOUT THE GAME.
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0
        # FLEET_DIRECTION OF 1 REPRESENTS RIGHT; -1 REPRESENTS LEFT.
        self.fleet_direction = 1
        # SCORING
        self.alien_points = 100
    def increase_speed(self):
        # INCREASE SPEED SETTINGS AND ALIEN POINT VALUES
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        # AND ALIEN POINT VALUES
        self.alien_points = int(self.alien_points * self.score_scale)
