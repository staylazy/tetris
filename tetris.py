import pygame, sys, time, random
from constants import *
from configuration import *
from pygame.locals import *
from colors import *
import copy

class Game:
	def __init__(self, width = WINDOWWIDTH, height = WINDOWHEIGHT, fps = FPS):
		pygame.init()
		self.width = width
		self.height = height
		self.win_size = (self.width, self.height)
		self.display = pygame.display.set_mode(self.win_size)
		pygame.display.set_caption('*')
		self.clock = pygame.time.Clock()
		self.running = False
		self.playtime = 0.0
		self.background = pygame.Surface(self.display.get_size())
		self.font = pygame.font.SysFont("comicsansms", int(20))
		self.font2 = pygame.font.SysFont("comicsansms", int(25))
		self.x = 3
		self.y = 0
		self.right = False
		self.left = False
		self.down = False
		self.cs = random.randint(0, len(SHAPES) - 1)
		self.rs = 0
		self.score = 0
						# 0              1             2    3         4              5         6 
		#SHAPES = [[L, L1, L2, L3], [J, J1, J2, J3], [O], [I, I1], [T, T1, T2, T3], [S, S1], [Z, Z1]]

	def check_win(self):
		pass

	def movedown(self):
		if (SHAPES[self.cs][self.rs] == L 
			or SHAPES[self.cs][self.rs] == J 
			or SHAPES[self.cs][self.rs] == O):
			if (GAME_FIELD[self.y + len(SHAPES[self.cs][self.rs])][self.x][0] == 'A'  
				or GAME_FIELD[self.y + len(SHAPES[self.cs][self.rs])][self.x + 1][0] == 'A'):
				return False
			else:
				return True

		if (SHAPES[self.cs][self.rs] == L3 
			or SHAPES[self.cs][self.rs] == J1 
			or SHAPES[self.cs][self.rs] == T):
			if (GAME_FIELD[self.y + len(SHAPES[self.cs][self.rs])][self.x][0] == 'A'  
				or GAME_FIELD[self.y + len(SHAPES[self.cs][self.rs])][self.x + 1][0] == 'A'
				or GAME_FIELD[self.y + len(SHAPES[self.cs][self.rs])][self.x + 2][0] == 'A'):
				return False
			else: 
				return True

		if (SHAPES[self.cs][self.rs] == Z1 
			or SHAPES[self.cs][self.rs] == T1):
			if (GAME_FIELD[self.y + 3][self.x][0] == 'A'  
				or GAME_FIELD[self.y + 2][self.x + 1][0] == 'A'):
				return False
			else: 
				return True
			
		if SHAPES[self.cs][self.rs] == I1:
			if (GAME_FIELD[self.y + 1][self.x][0] == 'A'
				or GAME_FIELD[self.y + 1][self.x + 1][0] == 'A'
				or GAME_FIELD[self.y + 1][self.x + 2][0] == 'A'
				or GAME_FIELD[self.y + 1][self.x + 3][0] == 'A'):
				return False
			else:
				return True 	

		if SHAPES[self.cs][self.rs] == I:
			if GAME_FIELD[self.y + len(SHAPES[self.cs][self.rs])][self.x][0] == 'A':
				return False
			else:
				return True

		if SHAPES[self.cs][self.rs] == L1:
			if (GAME_FIELD[self.y + len(SHAPES[self.cs][self.rs])][self.x][0] == 'A'
				or GAME_FIELD[self.y + 1][self.x + 1][0] == 'A'
				or GAME_FIELD[self.y + 1][self.x + 2][0] == 'A'):
				return False
			else:
				return True

		if SHAPES[self.cs][self.rs] == J2:
			if (GAME_FIELD[self.y + len(SHAPES[self.cs][self.rs])][self.x][0] == 'A'
				or GAME_FIELD[self.y + 1][self.x + 1][0] == 'A'):
				return False
			else:
				return True

		if SHAPES[self.cs][self.rs] == S:
			if (GAME_FIELD[self.y + len(SHAPES[self.cs][self.rs])][self.x][0] == 'A'
				or GAME_FIELD[self.y + len(SHAPES[self.cs][self.rs])][self.x + 1][0] == 'A'
				or GAME_FIELD[self.y + len(SHAPES[self.cs][self.rs]) - 1][self.x + 2][0] == 'A'):
				return False
			else:
				return True

		if SHAPES[self.cs][self.rs] == L2:
			if (GAME_FIELD[self.y + 1][self.x][0] == 'A'
				or GAME_FIELD[self.y + len(SHAPES[self.cs][self.rs])][self.x + 1][0] == 'A'):
				return False
			else:
				return True

		if (SHAPES[self.cs][self.rs] == T3
			or SHAPES[self.cs][self.rs] == S1):
			if (GAME_FIELD[self.y + len(SHAPES[self.cs][self.rs]) - 1][self.x][0] == 'A'
				or GAME_FIELD[self.y + len(SHAPES[self.cs][self.rs])][self.x + 1][0] == 'A'):
				return False
			else:
				return True

		if SHAPES[self.cs][self.rs] == J3:
			if (GAME_FIELD[self.y + len(SHAPES[self.cs][self.rs])][self.x + 2][0] == 'A'
				or GAME_FIELD[self.y + len(SHAPES[self.cs][self.rs]) - 1][self.x][0] == 'A'
				or GAME_FIELD[self.y + len(SHAPES[self.cs][self.rs]) - 1][self.x + 1][0] == 'A'):
				return False
			else:
				return True

		if SHAPES[self.cs][self.rs] == T2:
			if (GAME_FIELD[self.y + len(SHAPES[self.cs][self.rs])][self.x + 1][0] == 'A'
				or GAME_FIELD[self.y + len(SHAPES[self.cs][self.rs]) - 1][self.x][0] == 'A'
				or GAME_FIELD[self.y + len(SHAPES[self.cs][self.rs]) - 1][self.x + 2][0] == 'A'):
				return False
			else:
				return True

		if SHAPES[self.cs][self.rs] == Z:
			if (GAME_FIELD[self.y + len(SHAPES[self.cs][self.rs])][self.x + 1][0] == 'A'
				or GAME_FIELD[self.y + len(SHAPES[self.cs][self.rs]) - 1][self.x][0] == 'A'
				or GAME_FIELD[self.y + len(SHAPES[self.cs][self.rs])][self.x + 2][0] == 'A'):
				return False
			else:
				return True

	def render(self):
		self.background.fill(WHITE)
		self.display.blit(self.background, (0, 0))
		text = "W - поворот"
		text1 = "A - влево"
		text2 = "D - вправо"
		text3 = "S - вниз"
		text4 = str(self.score)
		text5 = "score:"
		text_surface = self.font.render(text, True, BLACK)
		text1_surface = self.font.render(text1, True, BLACK)
		text2_surface = self.font.render(text2, True, BLACK)
		text3_surface = self.font.render(text3, True, BLACK)
		text4_surface = self.font2.render(text4, True, BLACK)
		text5_surface = self.font2.render(text5, True, BLACK)
		self.display.blit(text_surface, (WINDOWWIDTH - len(text) * 11, 100))
		self.display.blit(text1_surface, (WINDOWWIDTH - len(text1) * 11, 120))
		self.display.blit(text2_surface, (WINDOWWIDTH - len(text2) * 11, 140))
		self.display.blit(text3_surface, (WINDOWWIDTH - len(text3) * 11, 160))
		self.display.blit(text5_surface, (WINDOWWIDTH - len(text5) * 16 - 50 - len(text4) * 16, 200))
		self.display.blit(text4_surface, (WINDOWWIDTH - len(text4) * 16 - 50, 200))
		self.load_field()
		self.draw_field()
		pygame.display.update()

	def draw_field(self):
		for i in range(FIELD_WIDTH + 1):
			pygame.draw.line(self.display, BLACK, (100 + i * BLOCK_SIZE, 100), (100 + i * BLOCK_SIZE, 100 + BLOCK_SIZE * FIELD_HEIGHT), 1)
		for i in range(FIELD_HEIGHT + 1):
			pygame.draw.line(self.display, BLACK, (100, 100 + i * BLOCK_SIZE), (100 + FIELD_WIDTH * BLOCK_SIZE, 100 + i * BLOCK_SIZE), 1)

	def events(self):
		for event in pygame.event.get():
			if event.type == QUIT:
				self.running = False
			if event.type == KEYUP:
				if event.key == K_ESCAPE:
					self.running = False
				if event.key == K_s:
					self.down = True
				if event.key == K_a and self.x > 0:
					self.left = True
				if event.key == K_d and self.x < (FIELD_WIDTH - len(SHAPES[self.cs][self.rs][0])):
					self.right = True
				if event.key == K_w:
					if len(SHAPES[self.cs][self.rs][0]) == 2 and self.x == 8 and SHAPES[self.cs][self.rs] != O:
						self.x -= 1
						self.rotate()
					elif len(SHAPES[self.cs][self.rs][0]) == 1 and self.x == 9:
						self.x -= 3
						self.rotate()
					else:
						self.rotate()

		if self.y < FIELD_HEIGHT - len(SHAPES[self.cs][self.rs]) and not self.right and not self.left:
			self.y += 1
		
		if self.right and self.y < FIELD_HEIGHT - len(SHAPES[self.cs][self.rs]):
			self.x += 1 
		if self.left and self.y < FIELD_HEIGHT - len(SHAPES[self.cs][self.rs]): 
			self.x -= 1
			
		if (self.down and self.y < FIELD_HEIGHT - len(SHAPES[self.cs][self.rs])                
			and not self.right and not self.left                                                                     
			and self.movedown()):
			self.y += 1

		self.right = False
		self.left = False
		self.down = False

		if (self.y == FIELD_HEIGHT - len(SHAPES[self.cs][self.rs]) 
			or self.movedown() == 0):  
			for i in range(len(SHAPES[self.cs][self.rs])):
				for j in range(len(SHAPES[self.cs][self.rs][i])):
					if SHAPES_DROPED[self.cs][self.rs][i][j][0] == 'A':
						GAME_FIELD[i + self.y][j + self.x] = SHAPES_DROPED[self.cs][self.rs][i][j]
			self.y = 0
			self.x = 3
			self.load_shape()
			self.choose()
			self.rotate()

	def actions(self):
		self.playtime += self.clock.tick(FPS) / 1000
		for i in range(len(GAME_FIELD)):
			for j in range(len(GAME_FIELD[i])):
				if GAME_FIELD[i][j][0] == 'X':
					GAME_FIELD[i][j] = '0'
		self.win_check()
		self.move_shape()
		self.load_field()
		self.check()
		
	def check(self):
		for i in range(len(GAME_FIELD)):
						if (GAME_FIELD[i][0][0] == GAME_FIELD[i][1][0]
						 == GAME_FIELD[i][2][0] == GAME_FIELD[i][3][0]
						  == GAME_FIELD[i][4][0] == GAME_FIELD[i][5][0]
						   == GAME_FIELD[i][6][0] == GAME_FIELD[i][7][0]
						   == GAME_FIELD[i][8][0] == GAME_FIELD[i][9][0] == 'A'): 
							GAME_FIELD[i] = ['0','0','0','0','0','0','0','0','0','0']
							self.shift(i)
							self.score += 100
					
	def shift(self, h):
		for i in range(h, 0, -1):
			for j in range(FIELD_WIDTH):
				GAME_FIELD[i][j] = GAME_FIELD[i - 1][j]

	def load_field(self):
		for i in range(len(GAME_FIELD)):
			for j in range(len(GAME_FIELD[i])):
				if GAME_FIELD[i][j][0] == 'X':
					pygame.draw.rect(self.display, GAME_FIELD[i][j][1], (j * BLOCK_SIZE + 100, i * BLOCK_SIZE + 100, BLOCK_SIZE, BLOCK_SIZE), 0)
				if GAME_FIELD[i][j][0] == 'A':
					pygame.draw.rect(self.display, GAME_FIELD[i][j][1], (j * BLOCK_SIZE + 100, i * BLOCK_SIZE + 100, BLOCK_SIZE, BLOCK_SIZE), 0)
					
	def move_shape(self):
		for i in range(len(SHAPES[self.cs][self.rs])):
			for j in range(len(SHAPES[self.cs][self.rs][i])):
				if SHAPES[self.cs][self.rs][i][j][0] == 'X':
					GAME_FIELD[i + self.y][j + self.x] = SHAPES[self.cs][self.rs][i][j]

	def load_shape(self):
		for i in range( len(SHAPES[self.cs][self.rs]) ): 
			for j in range(len(SHAPES[self.cs][self.rs][i])):
				GAME_FIELD[i][j] = SHAPES[self.cs][self.rs][i][j]

	def rotate(self):
		if len(SHAPES[self.cs]) - 1 > self.rs: 
			self.rs += 1
		else:
			self.rs = 0

	def choose(self):
		self.cs = random.randint(0, len(SHAPES) - 1)

	def win_check(self):
		if 'A' in GAME_FIELD[0] or 'A' in GAME_FIELD[len(SHAPES[self.cs][self.rs])][self.x]:
			self.running = False 

	def run(self):
		self.running = True
		while self.running:
			self.events()
			self.actions()
			self.render()
		
	def menu_update(self):
		self.clock.tick(FPS)
		# (!) выведите в заголовок окна текущий ФПС

	def menu_get_events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.menu_running = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					self.menu_running = False
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_p:
					# GAME_FIELD = copy.deepcopy(GAME_FIELD_NEW)
					for i in range(len(GAME_FIELD)):
						GAME_FIELD[i] = ['0','0','0','0','0','0','0','0','0','0']
					self.score = 0
					self.run()

	def menu_draw(self):
		self.background.fill(WHITE)
		self.display.blit(self.background, (0, 0))
		textmenu = "Press P to play"
		textmenu_surface = self.font2.render(textmenu, True, BLACK)
		self.display.blit(textmenu_surface, ((WINDOWWIDTH / 2) - len(textmenu) * 10, WINDOWHEIGHT / 2))
		text_score = "Score: " + str(self.score)
		text_score_surface = self.font2.render(text_score, True, BLACK)
		self.display.blit(text_score_surface, ((WINDOWWIDTH / 2) - len(text_score) * 10, WINDOWHEIGHT / 2 + 25 * 2))

		pygame.display.update()

	def menu(self):
		self.menu_running = True
		while self.menu_running:
			self.menu_get_events()
			self.menu_update()
			self.menu_draw()

if __name__ == '__main__':
	game = Game()
	game.menu()
	pygame.quit()