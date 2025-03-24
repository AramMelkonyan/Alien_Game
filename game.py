import pygame #bolor xaxeri hamar petq e
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from button import Button
from ship import Ship
from scoreboard import Scoreboard
import game_functions as gf

def run_game():
    pygame.init() #partadir! skizb
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_layn,ai_settings.screen_barzr)) #ekrani chap
    pygame.display.set_caption("Alien Invasion")
    play_button = Button(ai_settings,screen,"Play")
    stats = GameStats(ai_settings) # xaxi statitikayi stexcum
    sb = Scoreboard(ai_settings,screen,stats) # xaxi miavorneri stexcum
    ship = Ship(ai_settings,screen) # ship-i stexcum
    bullets = Group() # stexcum enq xumb,pampushtner@ pahelu hamar
    aliens = Group() # alien-i xmbi stexcum    
    gf.create_fleet(ai_settings,screen,ship,aliens) # alien floti stexcum
    # glxavor xaxi cikl !!
    while True:
        gf.check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets)
            gf.update_aliens(ai_settings,stats,screen,sb,ship,aliens,bullets)
        gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button) 



run_game()
