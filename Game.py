# Libraries
import os
import pygame
from pygame.locals import *
import random
pygame.init()
# Sets Window Position
x = 740
y = 80
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)

# Creates the Pygame window
lent = 600
bret = 800
win = pygame.display.set_mode((lent, bret))
pygame.display.set_caption("Second Game!")
neko = False
	
# Colors
white = [255, 255, 255]
red = [255, 0, 0]
blue = [0, 0, 255]
green = [0, 255, 0]
black = [0, 0, 0]
yellow = [255, 255, 0]
green1 = [100, 255,200]

c = pygame.time.Clock()
fps = 70
# Objects
r2_size = 60
r1_size = 60
r1_x = lent//2
r1_y = bret - (r1_size)
r2_x = random.randint(0, (lent - lent//6))
r2_y = 0
font = pygame.font.Font(None, 30)
font1 = pygame.font.Font(None, 30)
score = 0

# Loading Image(background)
pic = pygame.image.load("background.jpg").convert()
pygame.time.wait(500)
# Game Loop
while not neko:
	scoref=score/15
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			neko = True
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				neko = True
	
	keys = pygame.key.get_pressed()
	if keys[K_RIGHT] and (r1_x < (lent-r1_size)):
			r1_x += 7
	elif keys[K_LEFT] and (r1_x>0):
			r1_x -= 7
	win.blit(pic, (0, -1000))
	
	
	if r2_y >= 0 and r2_y <= bret:
		r2_y += 10
	else:
		r2_y = 0
		r2_x = random.randint(0, lent-(lent//6))
	
	o = (r1_x >= r2_x) and (r1_x <= r2_x + r2_size) and (r2_y+ r2_size >= r1_y)
	p = (r1_x <= r2_x) and (r2_x <= r1_x + r1_size) and (r2_y+ r2_size >= r1_y)
	
	if  (r2_y+r2_size//2 == r1_y+r1_size//2)and ((((r2_x > (r1_x)) and ((r2_x > (r1_x + (r1_size+5))))) or (((r2_x+(r2_size)) < r1_x)))):
		font1 = pygame.font.Font(None, 35)
		win.blit(pic, (0,-1400))
		S = font1.render("Game Over!", 1, white)
		win.blit(S, (lent//3, bret//3))
		Q = font1.render(str(" "+"{:.2f}".format(scoref)), 1, green1)
		win.blit(Q, ((lent - lent//4), bret//2))
		R = font1.render("Score --> ", 1, green1)
		win.blit(R, ((lent//3), bret//2))
		pygame.display.update()
		neko = True
		pygame.time.wait(1000)
	else:
		if o or p:
			score += 1		
		
	# In-game Score
	NUMBER= font.render(str(" "+"{:.2f}".format(scoref)), 1, white)
	SCORE = font.render("Score: ", 1, black)
	win.blit(SCORE, (lent - (3*r1_size), r1_size))
	win.blit(NUMBER, ((lent - r1_size-10), r1_size))

	
	# Draw Retangle 
	pygame.draw.rect(win, green, (r1_x, r1_y, r1_size, r1_size))
	pygame.draw.rect(win, red, (r2_x, r2_y, r2_size, r2_size))

	pygame.display.update()
	c.tick(fps)


