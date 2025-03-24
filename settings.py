class Settings():
    def __init__(self):
        self.screen_layn = 800
        self.screen_barzr = 900
        self.screen_color = (80,200,100) # I -karmir, II -kanach, III -kapuyt. [0,255]
        self.ship_limit = 3 #xaxi kyanqeri qanak
        # pampushti parametrer@
        self.bullet_layn = 3
        self.bullet_barzr = 15
        self.bullet_color = (0,0,60) # I -karmir, II -kanach, III -kapuyt. [0,255]
        self.bullets_allowed = 3 # ekrani vra tuylatrvum e 3 pampushtic voch avel !!
        # alien parametrer@
        self.fleet_drop_speed = 10
        # xaxi aragacman temp@
        self.speedup_scale = 1.2
        # "alien" miavorneri avelacman temp@
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed = 3.5
        self.bullet_speed = 3
        self.alien_speed = 1
        self.fleet_direction = 1 # 1 <=> aj, -1 <=> dzax
        self.points = 50

    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.points = int(self.points * self.score_scale)
