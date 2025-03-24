import pygame.font
from pygame.sprite import Group
from ship import Ship

class Scoreboard():
    def __init__(self,ai_settings,screen,stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats
        self.text_color = (30,30,30) # miavori guyn
        self.font = pygame.font.SysFont(None, 40) # miavori font
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        rounded_score = int(round(self.stats.score, -1)) # kloracum 10-akanov
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str,True,
                                            self.text_color,
                                            self.ai_settings.screen_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20 # miavori dirq (aj-dzax)
        self.score_rect.top = 5 # miavori dirq (verev-nerqev)

    def prep_high_score(self):
        rounded_score = int(round(self.stats.high_score, -1)) # kloracum 10-akanov
        high_score_str = "{:,}".format(rounded_score)
        self.high_score_image = self.font.render(high_score_str,True,
                                                 self.text_color,
                                                 self.ai_settings.screen_color)
        # record cuyc ei talis mejtexi verevum
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.right = self.screen_rect.centerx 
        self.high_score_rect.top = self.score_rect.top

    def prep_level(self):
        self.level_image = self.font.render(str(self.stats.level),True,
                                            self.text_color,
                                            self.ai_settings.screen_color)
        # level cuyc ei talis nerka score-i tak
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        """tesnum enq qani kyanq(ship) mnac"""
        self.ships = Group()
        for i in range(self.stats.ships_left):
            ship = Ship(self.ai_settings,self.screen)
            ship.rect.x = 10 + i * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)
        
    def show_score(self):
        self.screen.blit(self.score_image,self.score_rect)
        self.screen.blit(self.high_score_image,self.high_score_rect)
        self.screen.blit(self.level_image,self.level_rect)
        self.ships.draw(self.screen)
