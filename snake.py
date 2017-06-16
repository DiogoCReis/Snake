import pygame,random

class snake_game:
	def __init__(self):
		self.disp_width = 800
		self.disp_height = 600

		pygame.init()
		pygame.display.set_caption('Snake')
		self.game_window = pygame.display.set_mode((self.disp_width,self.disp_height))
		self.clock = pygame.time.Clock()

		self.black = (0,0,0)
		self.white = (255,255,255)
		self.red = (255,0,0)
		self.green = (0,150,0)

		self.tamanho = 20
		self.food_image = pygame.Surface((self.tamanho, self.tamanho))
		self.food_image.fill(self.red)

		self.snake_block = pygame.Surface((self.tamanho, self.tamanho))
		self.snake_block.fill(self.green)

		self.dead = False
		self.score = 0
		self.snake_pos = [[280,280]]
		self.snake_next = (self.tamanho,0)

		self.food()

		self.game_loop()


	def snake(self):
		def update():
			for i in range(self.score):
				self.snake_pos[-i-1] = self.snake_pos[-i-2]
			self.snake_pos[0] = novo
		novo = [self.snake_pos[0][0] + self.snake_next[0]]
		novo += [self.snake_pos[0][1] + self.snake_next[1]]

		for i in range(self.score+1):
			if self.snake_pos[i] == novo:
				self.end()

		if 0 > novo[0]:
			novo[0] = self.disp_width - self.tamanho
			update()
		elif self.disp_width <= novo[0]:
			novo[0] = 0
			update()
		elif 0 > novo[1]:
			novo[1] = self.disp_height - self.tamanho
			update()
		elif self.disp_height <= novo[1]:
			novo[1] = 0
			update()
		elif novo == self.food_pos:
			self.score += 1
			self.snake_pos = [novo] + self.snake_pos
			self.food()
		else:
			update()

		for i in range(self.score + 1):
			self.game_window.blit(self.snake_block,self.snake_pos[i])


	def food(self):
		self.food_pos = [random.randint(0,(self.disp_width/self.tamanho)-1)*self.tamanho, \
			random.randint(0,(self.disp_height/self.tamanho)-1)*self.tamanho]


	def game_loop(self):
		while not self.dead:
			for event in pygame.event.get():
				if 	event.type == pygame.QUIT:
					self.end()
				elif event.type == pygame.KEYDOWN: #key pressed
					if event.key == pygame.K_UP and self.snake_next != (0,self.tamanho):
						self.snake_next = (0, -self.tamanho)
					elif event.key == pygame.K_DOWN and self.snake_next != (0,-self.tamanho):
						self.snake_next = (0, self.tamanho)
					elif event.key == pygame.K_LEFT and self.snake_next != (self.tamanho,0):
						self.snake_next = (-self.tamanho, 0)
					elif event.key == pygame.K_RIGHT and self.snake_next != (-self.tamanho,0):
						self.snake_next = (self.tamanho, 0)
			#refresh screen
			self.game_window.fill(self.black)
			self.game_window.blit(self.food_image, self.food_pos)
			self.snake()
			pygame.display.update()

			self.clock.tick(10)
		print ("NOT supposed to happen")


	def end(self):
		font=pygame.font.SysFont('Arial', 30)
		text=font.render('Your score is: '+str(self.score), True, self.white)
		self.game_window.blit(text, (10, 270))
		pygame.display.update()
		pygame.time.wait(2000)
		pygame.quit()
		quit()

snake_game()

