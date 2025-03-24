import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """ship-ic krakox pampushtneri hamar"""
    def __init__(self,ai_settings,screen,ship):
        """stexcum enq pampushti obyekt@ ship-i dirqi motic"""
        super(Bullet,self).__init__() # kam super().__init__()
        self.screen = screen
        # pampushti stexcum@ (0,0) dirqic
        self.rect = pygame.Rect(0,0,ai_settings.bullet_layn,
                                ai_settings.bullet_barzr)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.y = float(self.rect.y)
        self.color = ai_settings.bullet_color
        self.speed = ai_settings.bullet_speed
    def update(self):
        """texapoxum enq pampusht@ verev ekrani vrayov"""
        self.y -= self.speed
        self.rect.y = self.y
    def draw_bullet(self):
        """tpum enq pampusht@ ekrani vra"""
        pygame.draw.rect(self.screen,self.color,self.rect)
