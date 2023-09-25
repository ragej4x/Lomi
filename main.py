import pygame as pg
import MainClass as main


dynamicScale = 2
width , height = 900,620
window = pg.display.set_mode((width, height))
display = pg.Surface((width//dynamicScale, height//dynamicScale))
clock = pg.time.Clock()
pg.init()


def showFps():
	font = pg.font.SysFont("Arial", 18)
	getFps = str(int(clock.get_fps()))
	fpsTxt = font.render(getFps, True, (255,255,255))
	window.blit(fpsTxt,(5,5))


def eventHandler():
	for event in pg.event.get():
		if event.type == pg.QUIT:
			exit()
			
	dynamicResolution = pg.transform.scale(display, (width, height))
	window.blit(dynamicResolution, (0,0))

	#RENDER TXT INTO WINDOW
	showFps()

while True:
	window.fill(0)

	display.fill(0)

	#KEY EVENTS
	mx,my = pg.mouse.get_pos()
	mouseinput = pg.mouse.get_pressed()
	keyinput = pg.key.get_pressed()
	#

	#CALLFUNC
	main.lomi.player(display, pg)
	main.lomi.movement(keyinput, pg)
	main.lomi.camera(display, pg)

	#ANIMATION
	main.lomi.updateAnimation(display, keyinput, pg)

	main.Map.update(display, pg)



	#move
	main.lomi.x += main.lomi.xVel
	main.lomi.y += main.lomi.yVel

	eventHandler()
	pg.display.flip()
	clock.tick(60)


