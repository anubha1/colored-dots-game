import pygame
import sys
import time
import random

WIDTH = 400
HEIGHT = 400
REALHEIGHT = 500
PSIZE = 20
COLS = int(WIDTH/PSIZE)
ROWS = int(HEIGHT/PSIZE)
RED = (176,16,25)
ORANGE = (229,125,0)
GREEN = (0,205,0)
YELLOW = (254,253,65)
PURPLE = (89,18,70)
PINK = (255,116,140)
TEAL = (52,235,229)
LIGHTBLUE = (142,177,194)
BLUE = 	(95,121,144)
BCKGD = (25,48,79)
RANDCOLORS = [RED, ORANGE, GREEN, YELLOW, PINK, TEAL]
GAMEOVER = False
GOAL = RANDCOLORS[random.randint(0,5)]
class Player:
	score = 0
	def __init__(self):
		self.x = 0
		self.y = 0
	def moveRight(self):
		if self.x + PSIZE <= WIDTH-PSIZE:
			self.x += PSIZE
	def moveLeft(self):
		if self.x-PSIZE >= 0:
			self.x -= PSIZE
	def moveUp(self):
		if self.y-PSIZE >= 0:
			self.y -= PSIZE
	def moveDown(self):
		if self.y+PSIZE <= HEIGHT-PSIZE:
			self.y += PSIZE
class Food:
	def __init__(self, p):
		self.x = PSIZE*random.randint(1,COLS-1)
		while self.x == p.x:
			self.x = PSIZE*random.randint(1,COLS-1)
		self.y = PSIZE*random.randint(1,ROWS-1)
		while self.y == p.y:
			self.y = PSIZE*random.randint(1,ROWS-1)
		self.color = RANDCOLORS[random.randint(0,5)]

def drawBoard(screen, p, foods):
	global GOAL
	screen.fill(BCKGD)
	pygame.draw.rect(screen, BLUE, (0,HEIGHT, WIDTH, REALHEIGHT-HEIGHT))
	myfont = pygame.font.SysFont("Arial", 20)
	score_label = myfont.render("SCORE: " + str(p.score), 1, (0,0,0))
	find_label = myfont.render("FIND:", 1, (0,0,0))
	screen.blit(score_label, (10, HEIGHT+10))
	screen.blit(find_label, (10, HEIGHT+40))
	pygame.draw.circle(screen, GOAL, (20*4+int(PSIZE/2),HEIGHT+40+int(PSIZE/2)) ,int(PSIZE/2)) 
	
	for f in foods:
		if p.x == f.x and p.y == f.y:
			if f.color == GOAL:
				foods.remove(f)
				p.score += 1
				GOAL = RANDCOLORS[random.randint(0,5)]
			else:
				foods.remove(f)
				game_over = True
				global GAMEOVER
				GAMEOVER = True
		else:
			pygame.draw.circle(screen, f.color, (f.x+int(PSIZE/2),f.y+int(PSIZE/2)), int(PSIZE/2))

def main():
	pygame.init()
	screen = pygame.display.set_mode((WIDTH,REALHEIGHT))
	screen.fill(BCKGD)
	p = Player()
	foods = []
	while not GAMEOVER:
		if random.randint(0,600) == 0:
			f = Food(p)
			foods.append(f)

		for event in pygame.event.get():
			print(event)
			if event.type == pygame.QUIT:
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RIGHT:
					p.moveRight()
				elif event.key == pygame.K_LEFT:
					p.moveLeft()
				elif event.key == pygame.K_UP:
					p.moveUp()
				elif event.key == pygame.K_DOWN:
					p.moveDown()
		drawBoard(screen, p, foods)
		pygame.draw.rect(screen, LIGHTBLUE, (p.x,p.y, PSIZE, PSIZE))
		pygame.display.update()
	while True:
		screen.fill(BCKGD)
		pygame.draw.rect(screen, BLUE, (0,HEIGHT, WIDTH, REALHEIGHT-HEIGHT))
		pygame.draw.rect(screen, LIGHTBLUE, (p.x,p.y, PSIZE, PSIZE))
		myfont = pygame.font.SysFont("Arial", 50)
		end_label = myfont.render("GAME OVER :(" , 1, (0,0,0))
		screen.blit(end_label, (10, 10))
		pygame.display.update()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
		time.sleep(5)
		break

main()