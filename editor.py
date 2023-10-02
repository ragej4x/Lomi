from MainClass import lomi
import csv
class editor_class():
	def __init__(self):
		self.world_data = []
		self.max_col = 150
		self.rows = 22
		self.height = 900
		self.width = 620
		self.tile_size = self.height // self.rows
		self.tile = 1

		for row in range(self.rows):
			r = [0] * self.max_col
			self.world_data.append(r)

		print(self.world_data)

	def draw_tile(self, pg, display):
		for y, row in enumerate(self.world_data):
			for x, tile in enumerate(row):
				if tile >= 1:	
					pg.draw.rect(display, (255,2,2), (x * self.tile_size, y * self.tile_size, self.tile_size,  self.tile_size))



	def draw_grid(self, pg, display):
		#vertical lines
		for c in range(self.max_col + 1):
			pg.draw.line(display, (255,255,255), (c * self.tile_size, 0 ), (c * self.tile_size , self.height ))
		#horizontal lines
		for c in range(self.rows + 1):
			pg.draw.line(display, (255,255,255), (0, c * self.tile_size ), (self.width , c * self.tile_size ))


	def update(self, pg, mx, my, mouseinput, keyinput, display):
		#CHECK COORD	
		x = int(mx )// self.tile_size 
		y = int(my )// self.tile_size

		if mx < self.width and my < self.height:
			if mouseinput[0]:
				if self.world_data[y][x] != self.tile:
					self.world_data[y][x] = self.tile
					print(self.world_data[y][x])
			if mouseinput[2]:
				self.world_data[y][x] = 0


		#SAVE DATA
		print(x,y)

		if keyinput[pg.K_p]:
			print("SAVED")
			print(self.world_data)
			with open("data/assets/map_1.data", "w", newline="") as file:
				writer = csv.writer(file, delimiter = ",")
				for row in self.world_data:
					writer.writerow(row)


		#LOAD DATA
		if keyinput[pg.K_o]:
			with open("data/assets/map_1.data", newline='') as data:
				reader = csv.reader(data, delimiter = ",")
				for x, row in enumerate(reader):
					for y, tile in enumerate(row):
						self.world_data[x][y] = int(tile)

main = editor_class()