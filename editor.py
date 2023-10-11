import csv
import pygame as pg

class Editor:
    def __init__(self):
        self.world_data = [[0] * 53 for _ in range(23)]
        self.max_col = 53
        self.rows = 23
        self.height = 900
        self.width = 620
        self.tile_size = self.height // self.rows - 8
        self.tile = 0

        self.button_columns = 9
        self.button_rows = 7
        self.buttons = []

        self.item_list = [pg.transform.scale(pg.image.load(f"data/assets/items/item ({i}).png"), (self.tile_size, self.tile_size)) for i in range(1, 65)]

        for row in range(self.button_rows):
            for col in range(self.button_columns):
                x = col * self.tile_size + 20 * self.tile_size
                y = row * self.tile_size
                text = f"Button {row * self.button_columns + col + 1}"
                self.buttons.append({"rect": pg.Rect(x, y, self.tile_size, self.tile_size), "text": text, "item": row * self.button_columns + col + 1, "posx": x, "posy": y})

    def draw_tile(self, display, keyinput, mx, my, mouseinput):
        if mouseinput[0]:
            for button in self.buttons:
                if button["rect"].collidepoint(mx, my):
                    self.tile = button['item']

        for button in self.buttons:
            display.blit(self.item_list[button["item"]], (button["posx"], button["posy"]))

        for y, row in enumerate(self.world_data):
            for x, tile in enumerate(row):
                if tile >= 1:
                    display.blit(self.item_list[tile], (x * self.tile_size, y * self.tile_size))

    def draw_grid(self, display):
        for c in range(self.max_col + 1):
            pg.draw.line(display, (255, 255, 255), (c * self.tile_size, 0), (c * self.tile_size, self.height))

        for c in range(self.rows + 1):
            pg.draw.line(display, (255, 255, 255), (0, c * self.tile_size), (self.width, c * self.tile_size))

    def update(self, mx, my, mouseinput, keyinput, display):
        x = int(mx) // self.tile_size
        y = int(my) // self.tile_size

        if mx < self.width and my < self.height:
            if mouseinput[0]:
                if self.world_data[y][x] != self.tile:
                    self.world_data[y][x] = self.tile
            if mouseinput[2]:
                self.world_data[y][x] = 0

        if keyinput[pg.K_p]:
            with open("data/assets/map_1.data", "w", newline="") as file:
                writer = csv.writer(file, delimiter=",")
                for row in self.world_data:
                    writer.writerow(row)

        if keyinput[pg.K_o]:
            with open("data/assets/map_1.data", newline='') as data:
                reader = csv.reader(data, delimiter=",")
                for x, row in enumerate(reader):
                    for y, tile in enumerate(row):
                        self.world_data[x][y] = int(tile)

main = Editor()
