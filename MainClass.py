import csv
import math

class MainClass():
	def __init__(self, x , y):
		self.x = x
		self.y = y

		self.speed = 2

		self.red = (255,0,0)
		self.green = (0,255,0)
		self.blue = (0,0,255)


		#CAMERA

		self.cameraSpeed = 1.5
		self.cameraX = self.x - 900/3
		self.cameraY = self.y - 620/3

	def player(self, display, pg):
		self.lomiRect = pg.Rect(self.x - self.cameraX , self.y - self.cameraY, 16,16)
		pg.draw.rect(display, self.red, self.lomiRect, 1)
		#pg.draw.rect(display, (255,255,255), (30,30,30,30))
	
	def movement(self, keyinput, pg):
		self.xVel = 0
		self.yVel = 0


		if keyinput[pg.K_w]:
			self.yVel -= self.speed
		
		if keyinput[pg.K_s]:
			self.yVel += self.speed

		if keyinput[pg.K_d]:
			self.xVel += self.speed

		if keyinput[pg.K_a]:
			self.xVel -= self.speed


		print(self.yVel, self.xVel)
			


	def camera(self, display, pg):
		center = pg.draw.rect(display, (255,255,255), (900 /4 , 620/4, 4,4 ))
		distance = math.atan2(self.y - self.cameraY - 620/4 , self.x - self.cameraX - 900/4)
		self.cdx = math.cos(distance)
		self.cdy = math.sin(distance)

		if not center.colliderect(self.lomiRect):
			self.cameraX += self.cdx * self.cameraSpeed
			self.cameraY += self.cdy * self.cameraSpeed


class MapClass():
	def __init__(self):
		pass

	def update(self, display, pg):
		with open ("data/map_1.data") as file:
			data = csv.reader(file, delimiter=',')

			y = 0

			for row in data:
				x = -1

				for column in range(len(row)):
					x += 1

					if row[column] == "1":
						self.block = pg.draw.rect(display, (255,255,255), (x * 16 - lomi.cameraX , y * 16 - lomi.cameraY, 16, 16),1)

						#COLLISION
						if self.block.colliderect(lomi.lomiRect.x + lomi.xVel , lomi.lomiRect.y, lomi.lomiRect.width, lomi.lomiRect.height):
							lomi.xVel = 0


						if self.block.colliderect(lomi.lomiRect.x + lomi.xVel , lomi.lomiRect.y, lomi.lomiRect.width , lomi.lomiRect.height):
							lomi.xVel = 0

						if self.block.colliderect(lomi.lomiRect.x, lomi.lomiRect.y + lomi.yVel, lomi.lomiRect.width , lomi.lomiRect.height):
							lomi.yVel = 0

				y += 1

class AnimationClass():
	def __init__(self):
		pass



lomi = MainClass(0,0)
Map = MapClass()
anim = AnimationClass()

