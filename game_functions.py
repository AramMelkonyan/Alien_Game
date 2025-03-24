import sys # avartum e xax@ ,xaxacoxi trvac hramani mijocov 
from time import sleep
import pygame
from bullet import Bullet
from alien import Alien

def check_keydown_events(i,ai_settings,screen,ship,bullets):
    """asxatum e klaviaturayin sexmelu hamar"""
    if i.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif i.key == pygame.K_LEFT:
        ship.moving_left = True
    elif i.key == pygame.K_SPACE:
        fire_bullet(ai_settings,screen,ship,bullets)
    elif i.key == pygame.K_q:
        sys.exit()


def fire_bullet(ai_settings,screen,ship,bullets):
    """krakum ei pampusht ete maximum arden chenq hasel"""
    # stexcum enq nor pampusht ev gcum xumb(bullets)
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings,screen,ship)
        bullets.add(new_bullet)
    

def check_keyup_events(i,ship):
    """asxatum e klaviaturan bac toxnelu hamar"""
    if i.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif i.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets):
    """stugum e klaviaturayi ev mkniki gorcoxutyunner@"""
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()
        elif i.type == pygame.KEYDOWN:
            check_keydown_events(i,ai_settings,screen,ship,bullets)
        elif i.type == pygame.KEYUP:
            check_keyup_events(i,ship)
        elif i.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets,mouse_x,mouse_y)


def check_play_button(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets,mouse_x,mouse_y):
    """sksvum e nor xax@ erb sexmum enq "Play" """
    button_clicked = play_button.rect.collidepoint(mouse_x,mouse_y)
    if button_clicked and not stats.game_active:
        ai_settings.initialize_dynamic_settings()
        pygame.mouse.set_visible(False) # mknik@ korum e ekranic,erb xax@ sksvum e!
        stats.reset_stats() # xaxi statistikayi sbros
        stats.game_active = True
        # sbros score,high_score,level
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()
        # jnjum enq alien-er@ ev pampusht-er@
        aliens.empty()
        bullets.empty()
        # stexcum enq nor flot en ship-in texadrum kentronum
        create_fleet(ai_settings,screen,ship,aliens)
        ship.center_ship()


def update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button):
    """tarmacnum e ekran@ ev bacum nor ekran@ amen cikli jamanak"""
    screen.fill(ai_settings.screen_color) # nerkvum e ekran@
    # bolor pampushtner@ tpvum en ship ev aylmolorakayinneri nkarneri hetevum
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    sb.show_score()
    # Knopka "Play" cuyc e talis miayn ayn depqum erb xax@ aktiv che
    if not stats.game_active:
        play_button.draw_button()
    pygame.display.flip() # Pygame hramayum e verjin ekran@ cuyc talun


def update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets):
    """tarmacnum e dirq@ pampushtneri ev jnjum hin pampushtner@"""
    bullets.update() # tarmacnum e dirq@ pampushtneri
    # jnjum enq pampushtner@ erb durs en galis ekranic
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    #print(len(bullets)) cuyc e talis ardyoq irakanum pampushtner@ jnjvum en te voch
    check_bullet_alien_collisions(ai_settings,screen,stats,sb,ship,aliens,bullets)


def check_bullet_alien_collisions(ai_settings,screen,stats,sb,ship,aliens,bullets):
    """collisions "pampusht-alien" """
    # stugum enq alien xpel@ ,ev xpelu depqum jnjum te pampusht@ te alien-in
    collisions = pygame.sprite.groupcollide(bullets,aliens,True,True)
    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.points * len(aliens)
            sb.prep_score()
            check_high_score(stats,sb)
    if len(aliens) == 0:
        # jnjum enq goyutyun unecox pampushtner@ ev stexcum nor flot ev stexcum nor level
        bullets.empty()
        ai_settings.increase_speed()
        stats.level += 1
        sb.prep_level()
        create_fleet(ai_settings,screen,ship,aliens)
        #ai_settings.bullet_speed += 1 en depqum erb shaat dandax asxati !!!


def get_number_aliens_x(ai_settings,alien_layn):
    """hashvarkum enq alien-i qanak sharqum"""
    available_space_x = ai_settings.screen_layn - 2*alien_layn
    number_aliens_x = int(available_space_x / (2*alien_layn))
    return number_aliens_x


def get_number_rows(ai_settings,ship_barzr,alien_barzr):
    """hashvarkum enq sharqeri qanak@ texavorvox ekrani vra"""
    available_space_y = ai_settings.screen_barzr - (3*alien_barzr) - 3*ship_barzr
    number_rows = int(available_space_y / (2*alien_barzr))
    return number_rows


def create_alien(ai_settings,screen,aliens,alien_N,row_N):
    """stexcum enq alien ev texadrum sharqum"""
    alien = Alien(ai_settings,screen)
    alien_layn = alien.rect.width
    alien.x = alien_layn + 2*alien_layn*alien_N
    alien.rect.x = alien.x # + floti dirq@ depi aj tanel, -` dzax
    alien.rect.y = alien.rect.height + 2*alien.rect.height*row_N + 60 # +60 nshanakum ei floti dirq@ depi nerqev ijacnel,-` verev
    aliens.add(alien)


def create_fleet(ai_settings,screen,ship,aliens):
    """stecum enq alien flot"""
    alien = Alien(ai_settings,screen)
    number_aliens_x = get_number_aliens_x(ai_settings,alien.rect.width)
    number_rows = get_number_rows(ai_settings,ship.rect.height,alien.rect.height)
    #  stexcum enq flot !
    for row_N in range(number_rows-1): # qanakn enq apahovum alien floti toxerov 
        # stexcum enq arajin alien sharq@
        for alien_N in range(number_aliens_x):
            create_alien(ai_settings,screen,aliens,alien_N,row_N)


def check_fleet_edges(ai_settings,aliens):
    """alien erb hasnum e ekrani verjin"""
    for i in aliens.sprites():
        if i.check_edges():
            change_fleet_direction(ai_settings,aliens)
            break


def change_fleet_direction(ai_settings,aliens):
    """ijacnum e amboxj flot@ ev poxum uxxutyun@"""
    for i in aliens.sprites():
        i.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def ship_hit(ai_settings,stats,screen,sb,ship,aliens,bullets):
    """ ship-alien xpel@"""
    if stats.ships_left > 0:
        stats.ships_left -= 1 # kyanq@ 1-ov pakasum e
        sb.prep_ships()
        # jnjum enq alien-er@ ev pampusht-er@
        aliens.empty()
        bullets.empty()
        # stexcum enq nor flot en ship-in texadrum kentronum
        create_fleet(ai_settings,screen,ship,aliens)
        ship.center_ship()
        sleep(0.5) # Pauza
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True) # mknik@ haytvum e erb xax@ avartvum e!


def check_aliens_bottom(ai_settings,stats,screen,sb,ship,aliens,bullets):
    """stugum e aliens hasan ekrani nerqevin"""
    screen_rect = screen.get_rect()
    for i in aliens.sprites():
        if i.rect.bottom >= screen_rect.bottom:
            # nuynn bann e linum inch vor xpeum er ship-in
            ship_hit(ai_settings,stats,screen,sb,ship,aliens,bullets)
            break
            

def update_aliens(ai_settings,stats,screen,sb,ship,aliens,bullets):
    """stugum e flot@ hasel e ekrani verjin,ev heto tarmacnum e bolor alien-erin flotum"""
    check_fleet_edges(ai_settings,aliens)
    aliens.update()
    # stugum e collisions "alien-ship"
    if pygame.sprite.spritecollideany(ship,aliens):
        ship_hit(ai_settings,stats,screen,sb,ship,aliens,bullets)
    check_aliens_bottom(ai_settings,stats,screen,sb,ship,aliens,bullets)


def check_high_score(stats,sb):
    """stugum e haytnvum e nor record"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()



































