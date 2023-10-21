import math
import csv

class MainClass():
	def __init__(self, x , y,):
		self.x = x
		self.y = y

		self.left = True
		self.right = False
		self.down = False
		self.up = False

		self.speed = 1

		self.red = (255,0,0)
		self.green = (0,255,0)
		self.blue = (0,0,255)


		self.fix_speed = 0.8



		#CAMERA

		self.cameraSpeed = 0.8
		self.cameraX = self.x - 125
		self.cameraY = self.y - 110

	def player(self, display, pg):
		self.lomiRect = pg.Rect(self.x - self.cameraX , self.y - self.cameraY, 16,16)
		self.lomiObjRect = pg.Rect(self.x - self.cameraX + 3, self.y - self.cameraY + 14, 9,2)
		pg.draw.rect(display, self.red, self.lomiRect, 1)
		pg.draw.rect(display, self.blue, self.lomiObjRect, 1)
		#pg.draw.rect(display, (255,255,255), (30,30,30,30))
	
	def movement(self, keyinput, pg):
		self.xVel = 0
		self.yVel = 0


		if keyinput[pg.K_w]:
			self.yVel -= self.speed
			self.up = True
			self.down = False
			self.left = False
			self.right = False
		
		if keyinput[pg.K_s]:
			self.yVel += self.speed
			self.down = True
			self.up = False
			self.left = False
			self.right = False

		if keyinput[pg.K_d]:
			self.xVel += self.speed
			self.right = True
			self.left = False
			self.up = False
			self.down = False

		if keyinput[pg.K_a]:
			self.xVel -= self.speed
			self.left = True
			self.right = False
			self.up = False
			self.down = False

			#FIX


		if keyinput[pg.K_a] and keyinput[pg.K_d]:
			self.right = True
			self.xVel += self.speed

		elif keyinput[pg.K_w] and keyinput[pg.K_d]:
			self.speed = self.fix_speed

		elif keyinput[pg.K_a] and keyinput[pg.K_s]:
			self.speed = self.fix_speed

		elif keyinput[pg.K_w] and keyinput[pg.K_a]:
			self.speed = self.fix_speed

		elif keyinput[pg.K_s] and keyinput[pg.K_d]:
			self.speed = self.fix_speed

		else:
			self.speed = 1


		#print(self.yVel, self.xVel)
			
	def camera(self, display, pg, dynamicScale):
		center = pg.draw.rect(display, (255,255,255), (900 /6, 620/6, 1,1 ))
		distance = math.atan2(self.y - self.cameraY - 620 // 6, self.x - self.cameraX - 900 // 6)
		self.cdx = math.cos(distance)
		self.cdy = math.sin(distance)

		if not center.colliderect(self.lomiRect):
			self.cameraX += self.cdx * self.cameraSpeed
			self.cameraY += self.cdy * self.cameraSpeed


	def updateAnimation(self, display, keyinput, pg):


		if keyinput[pg.K_w] and self.up == True:
			anim.runUpAnim(display, pg)
		elif not keyinput[pg.K_w] and self.up == True:
			anim.idleUpAnim(display, pg)

		if keyinput[pg.K_s] and self.down == True:
			anim.runDownAnim(display, pg)
		
		elif not keyinput[pg.K_s] and self.down == True:
			anim.idleDownAnim(display, pg)

		if keyinput[pg.K_d] and self.right == True:
			anim.runRightAnim(display, pg)

		elif not keyinput[pg.K_d] and self.right == True:
			anim.idleRightAnim(display, pg)

		if keyinput[pg.K_a] and self.left == True:
			anim.runLeftAnim(display, pg)

		elif not keyinput[pg.K_a] and self.left == True:
			anim.idleLeftAnim(display, pg)



class MapClass():
	def __init__(self):
		import pygame as pg
		self.blockPos = []
		self.tileSurface = pg.Surface((16,16))


		self.world_data = []
		self.world_data_layer_2 = []
		self.world_coll_data = []
		self.max_col = 100
		self.rows = 40
		self.height = 900
		self.width = 620
		self.tile_size = self.height // self.rows
		self.tile = 1


		self.tile_list = []
		self.tile_count = 215

		#LOAD IMAGE


		for row in range(self.rows):
			r = [0] * self.max_col
			self.world_data.append(r)

		for row in range(self.rows):
			r = [0] * self.max_col
			self.world_data_layer_2.append(r)

		for row in range(self.rows):
			r = [0] * self.max_col
			self.world_coll_data.append(r)

		#LOAD DATA
		with open("map_layer_1.data", newline='') as data:
			reader = csv.reader(data, delimiter = ",")
			for x, row in enumerate(reader):
				for y, tile in enumerate(row):
					self.world_data[x][y] = int(tile)


		with open("map_layer_2.data", newline='') as data:
			reader = csv.reader(data, delimiter = ",")
			for x, row in enumerate(reader):
				for y, tile in enumerate(row):
					self.world_data_layer_2[x][y] = int(tile)
        

		with open("map_coll.data", newline='') as data:
			reader = csv.reader(data, delimiter = ",")
			for x, row in enumerate(reader):
				for y, tile in enumerate(row):
					self.world_coll_data[x][y] = int(tile)

		#load map
		self.layer_0 = pg.image.load("data/assets/map/layer_0.png")
		self.layer_1 = pg.image.load("data/assets/map/layer_1.png")


		for i in range(self.tile_count):
			self.tile = pg.image.load(f"data/assets/street_tiles/tile ({i}).png")
			#self.tile = pg.transform.scale(self.tile, (self.tile_size, self.tile_size))
			self.tile_list.append(self.tile)

	def update(self, display, pg, keyinput):




		self.show_rect = True


		#self.plat = pg.Surface(())

		for y, row in enumerate(self.world_coll_data):
			for x, tile in enumerate(row):

				if tile == -1:
					if self.show_rect == True:
						self.block = pg.Rect((x * 16 - lomi.cameraX -16 , y * 16 - lomi.cameraY, 16, 16))
						pg.draw.rect(display, (255,255,255), self.block,1)
					
					#COLLISION
					if self.block.colliderect(lomi.lomiObjRect.x + lomi.xVel , lomi.lomiObjRect.y, lomi.lomiObjRect.width, lomi.lomiObjRect.height):
						lomi.xVel = 0


					if self.block.colliderect(lomi.lomiObjRect.x + lomi.xVel , lomi.lomiObjRect.y, lomi.lomiObjRect.width , lomi.lomiObjRect.height):
						lomi.xVel = 0

					if self.block.colliderect(lomi.lomiObjRect.x, lomi.lomiObjRect.y + lomi.yVel, lomi.lomiObjRect.width , lomi.lomiObjRect.height):
						lomi.yVel = 0

	def update_layer_1(self, display, pg):
		#display.blit(self.layer_1, (0 - lomi.cameraX, 0 - lomi.cameraY))

		for y, row in enumerate(self.world_data):
			for x, tile in enumerate(row):
				if tile >= 1:
					display.blit(self.tile_list[tile], (x * 16 - lomi.cameraX , y * 16 - lomi.cameraY))
                #display.blit(self.small_items_surface, (x * self.tile_size ,y * self.tile_size))



	def update_layer_2(self, display, pg):
		#display.blit(self.layer_1, (0 - lomi.cameraX, 0 - lomi.cameraY))

		for y, row in enumerate(self.world_data_layer_2):
			for x, tile in enumerate(row):
				if tile >= 1:
					display.blit(self.tile_list[tile], (x * 16 - lomi.cameraX , y * 16 - lomi.cameraY))
                #display.blit(self.small_items_surface, (x * self.tile_size ,y * self.tile_size))


class AnimationClass():
	def __init__(self, x ,y):
		self.x = x
		self.y = y

		self.frameSpeed = 0.15

		self.idleDownFrame = 1
		self.idleUpFrame = 1
		self.idleLeftFrame = 1
		self.idleRightFrame = 1

		self.runDownFrame = 1
		self.runUpFrame = 1
		self.runLeftFrame = 1
		self.runRightFrame = 1



	def idleDownAnim(self, display, pg):
		idleImage = pg.image.load(f"data/assets/anim/totoy/idD{int(self.idleDownFrame)}.anim").convert()
		idleImage.set_colorkey((255,0,255))
		display.blit(idleImage, (lomi.x - lomi.cameraX , lomi.y - lomi.cameraY - 15))

		self.idleDownFrame += self.frameSpeed
		if self.idleDownFrame > 6:
			self.idleDownFrame = 1
	
	def idleUpAnim(self, display, pg):
		idleImage = pg.image.load(f"data/assets/anim/totoy/idU{int(self.idleUpFrame)}.anim").convert()
		idleImage.set_colorkey((255,0,255))
		display.blit(idleImage, (lomi.x - lomi.cameraX , lomi.y - lomi.cameraY - 15))

		self.idleUpFrame += self.frameSpeed
		if self.idleUpFrame > 6:
			self.idleUpFrame = 1

	def idleLeftAnim(self, display, pg):
		idleImage = pg.image.load(f"data/assets/anim/totoy/id{int(self.idleLeftFrame)}.anim").convert()
		leftImage = pg.transform.flip(idleImage, True, False)
		leftImage.set_colorkey((255,0,255))
		display.blit(leftImage, (lomi.x - lomi.cameraX , lomi.y - lomi.cameraY - 15))

		self.idleLeftFrame += self.frameSpeed
		if self.idleLeftFrame > 6:
			self.idleLeftFrame = 1

	def idleRightAnim(self, display, pg):

		idleImage = pg.image.load(f"data/assets/anim/totoy/id{int(self.idleRightFrame)}.anim").convert()
		idleImage.set_colorkey((255,0,255))
		display.blit(idleImage, (lomi.x - lomi.cameraX , lomi.y - lomi.cameraY - 15))

		self.idleRightFrame += self.frameSpeed
		if self.idleRightFrame > 6:
			self.idleRightFrame = 1

	#RUN

	def runDownAnim(self, display, pg):
		runImage = pg.image.load(f"data/assets/anim/totoy/rD{int(self.runDownFrame)}.anim").convert()
		runImage.set_colorkey((255,0,255))
		display.blit(runImage, (lomi.x - lomi.cameraX , lomi.y - lomi.cameraY - 15))

		self.runDownFrame += self.frameSpeed
		if self.runDownFrame > 6:
			self.runDownFrame = 1
	
	def runUpAnim(self, display, pg):
		runImage = pg.image.load(f"data/assets/anim/totoy/rU{int(self.runUpFrame)}.anim").convert()
		runImage.set_colorkey((255,0,255))
		display.blit(runImage, (lomi.x - lomi.cameraX , lomi.y - lomi.cameraY - 15))

		self.runUpFrame += self.frameSpeed
		if self.runUpFrame > 6:
			self.runUpFrame = 1

	def runLeftAnim(self, display, pg):
		runImage = pg.image.load(f"data/assets/anim/totoy/r{int(self.runLeftFrame)}.anim").convert()
		runImage = pg.transform.flip(runImage, True, False)
		runImage.set_colorkey((255,0,255))
		display.blit(runImage, (lomi.x - lomi.cameraX , lomi.y - lomi.cameraY - 15))

		self.runLeftFrame += self.frameSpeed
		if self.runLeftFrame > 6:
			self.runLeftFrame = 1

	def runRightAnim(self, display, pg):

		runImage = pg.image.load(f"data/assets/anim/totoy/r{int(self.runRightFrame)}.anim").convert()
		runImage.set_colorkey((255,0,255))
		display.blit(runImage, (lomi.x - lomi.cameraX , lomi.y - lomi.cameraY - 15))

		self.runRightFrame += self.frameSpeed
		if self.runRightFrame > 6:
			self.runRightFrame = 1


lomi = MainClass(80,80)
Map = MapClass()
anim = AnimationClass(lomi.x, lomi.y)


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


class homeClass():
	def __init__(self):
		self.tile_list = [] 


	def houseBase(self, pg, display, mx, my, mouseinput):

		if mouseinput[0]:
			self.tile_list.append([pg.Rect((mx , my , 16 , 16))])
			self.block = pg.draw.rect(display, (255,255,255), self.tile_list[0])


	def update(self, mx , my, mouseinput):
		pass
		

home = homeClass()


