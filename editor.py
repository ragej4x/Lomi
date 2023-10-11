from MainClass import lomi
import csv
class editor_class():
    def __init__(self):
        import pygame as pg
        self.world_data = []
        self.max_col = 50
        self.rows = 32
        self.height = 620
        self.width = 900
        self.tile_size = self.height // self.rows
        self.tile = 0

        self.button_columns = 15
        self.button_rows = 14
        self.button_width = 16
        self.button_hight = 16
        self.buttons = []
        self.select = True

        #LOAD IMAGE
        self.item_list = []
        self.item_count = 215
    
        for i in range(self.item_count):
            self.small_items = pg.image.load(f"data/assets/street_tiles/tile ({i}).png")
            self.small_items = pg.transform.scale(self.small_items, (self.tile_size, self.tile_size))
            self.item_list.append(self.small_items)


        self.small_items_surface = pg.Surface((16, 16))

        for row in range(self.rows):
            r = [0] * self.max_col
            self.world_data.append(r)

        #print(self.world_data)



        for row in range(self.button_rows):
            for col in range(self.button_columns):
                x = col * (self.tile_size) + self.rows * self.tile_size
                y = row * (self.tile_size)
                text = f"Button {row * self.button_columns + col + 1}"

                #draw_button(x , y , self.tile_size, self.tile_size, text)
                self.buttons.append({"rect": pg.Rect(x, y, self.tile_size, self.tile_size), "text":text, "item":row * self.button_columns + col + 1, "posx":x, "posy":y} )


    def draw_tile(self, pg, display, keyinput, mx , my, mouseinput):
        #def draw_button(vx, vy, width, height, text):
            #button_rect = pg.draw.rect(display, (255,255,255), (vx, vy, width, height), 2)


        #draw tilesets
        #if keyinput[pg.K_RIGHT]:
        for button in self.buttons:
            if button["rect"].collidepoint(mx , my):
                self.select = True
                if mouseinput[0]:
                    self.tile = button['item']


        for button in self.buttons:

            #print(button["item"])
            display.blit(self.item_list[button["item"]], (button["posx"], button["posy"]))


        for y, row in enumerate(self.world_data):
            for x, tile in enumerate(row):
                if tile >= 1:
                    display.blit(self.item_list[tile], (x * self.tile_size, y * self.tile_size))
                    #display.blit(self.small_items_surface, (x * self.tile_size ,y * self.tile_size))

            

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

        for button in self.buttons:
            if mx < self.width and my < self.height:
                if mouseinput[0]:
                    if self.world_data[y][x] != self.tile:
                        self.world_data[y][x] = self.tile
                        #print(self.world_data[y][x])
                if mouseinput[2]:
                    self.world_data[y][x] = 0


        #SAVE DATA
        #print(x,y)

        if keyinput[pg.K_p]:
            #print("SAVED")
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