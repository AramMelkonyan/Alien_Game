import pygame.font

class Button():
    def __init__(self,ai_settings,screen,msg):
        """stexcum enq knopkayi parametrer@"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.layn, self.barzr = 200, 50
        self.button_color = (255,0,70)
        self.text_color = (255,255,255)
        self.font = pygame.font.SysFont(None,48)
        self.rect = pygame.Rect(0,0,self.layn,self.barzr)
        self.rect.center = self.screen_rect.center
        self.message(msg) # knopki message-@ stexcvum e miayn mek angam

    def message(self,msg):
        """msg dzevavorum enq uxxankyun ev havasarecnum text-@ kentroni uxxutyamb"""
        self.msg_image = self.font.render(msg,True,self.text_color,self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """cuyc e talis datark knopkan ev tpum text-@"""
        self.screen.fill(self.button_color,self.rect)
        self.screen.blit(self.msg_image,self.msg_image_rect)
