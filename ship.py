import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self,ai_settings,screen):
        super(Ship,self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        #amen nor nav@ haytvum e ekrani nerqevi ankyunum
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        #pahpanvum e ship mejtexi koordinatner@
        self.center = float(self.rect.centerx)
        self.moving_right = False #texapoxum depi aj ->
        self.moving_left = False #texapoxum depi dzax <-
    def update(self):    
        """tarmacnum e navi dirq@ moving_right mijocov"""
        #tarmacvum e center !
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed #ship gnum e depi right(->)
        if self.moving_left and self.rect.left > 0: 
            self.center -= self.ai_settings.ship_speed #ship gnum e depi left(<-)
        self.rect.centerx = self.center
    def center_ship(self):
        """texadrum e ship nerqevi kentronum"""
        self.center = self.screen_rect.centerx
    def blitme(self):
        self.screen.blit(self.image,self.rect)
