import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """stexcum enq 1 hat alien"""
    def __init__(self,ai_settings,screen):
        """alien enq stexcum ev nra naxnakan dirq@"""
        super(Alien,self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings        
        self.image = pygame.image.load('images/alien.png')
        self.rect = self.image.get_rect()
        #amen nor alien haytvum e ekrani dzax verevi ankyunum
        self.rect.x = self.rect.width 
        self.rect.y = self.rect.height
        #pahpanvum e alien konkret dirq@
        self.x = float(self.rect.x)
    def check_edges(self):
        """Veradarzum enq True ete alien gtnvum e ekrani verjum"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
        
    def update(self):
        """texapoxum e alien-erin depi aj kam dzax"""
        self.x += self.ai_settings.alien_speed * self.ai_settings.fleet_direction
        self.rect.x = self.x

    def blitme(self):
        self.screen.blit(self.image,self.rect)

