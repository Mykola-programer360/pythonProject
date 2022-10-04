import pygame
import time
import random
from ship import Ship
from button import Button
from button import Game_Over
import game_functions as gf
from settings import Settings
from pygame.sprite import Group
from game_stats import GameStats
from scoreboard import Scoreboard
from scoreboard import Quit_Sta

def run_game():

	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")


	FPS = 60
	clock = pygame.time.Clock()


	ship = Ship(ai_settings, screen)
	bullets = Group()
	enemy_bullets = Group()
	aliens = Group()


	stats = GameStats(ai_settings)
	sb = Scoreboard(ai_settings, screen, stats)
	qs = Quit_State(ai_settings, screen)

	gf.create_fleet(ai_settings, screen, ship, aliens)


	play_button = Button(ai_settings, screen, "PRESS ENTER")
	game_over = Game_Over(ai_settings, screen, "GAME OVER")


	gf.load_score(stats)
	sb.prep_high_score()
	sb.show_score()


	while True:
		clock.tick(FPS)
		gf.check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets, sb, enemy_bullets )
		if stats.game_active:
			ship.update()
			gf.update_bullets(ai_settings, screen, stats, sb,
			 ship, aliens, bullets)
			gf.update_enemy_bullets(ai_settings, screen, stats, sb, ship, aliens, enemy_bullets)
			gf.update_aliens(ai_settings, stats, sb, screen, ship, aliens, bullets, enemy_bullets, game_over)
		if not stats.game_active:
			game_over.draw_button()
		gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button, qs, enemy_bullets, game_over)

run_game()