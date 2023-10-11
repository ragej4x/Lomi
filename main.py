import pygame as pg
import MainClass as main
import editor

pg.init()
dynamicScale = 3
width , height = 900,620
window = pg.display.set_mode((width, height))
display = pg.Surface((width//dynamicScale, height//dynamicScale))
clock = pg.time.Clock()
pg.display.set_caption("LOOOOOMIIIIIIIIIIIIKOOOOOO")

#MODES
home = False
freeRoam = False
editMode = True
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
	#//
	if editMode == False:
		window.blit(dynamicResolution, (0,0))

	#RENDER TXT INTO WINDOW
	showFps()

	renderIn_noDynamicScale()

def renderIn_noDynamicScale():

	#NO DYNAMIC RES BLIT IN MAIN
	if editMode == True:
		editor.main.draw_tile(pg, window, keyinput, mx , my, mouseinput)
		editor.main.update(pg, mx,my,mouseinput,keyinput,window)
		editor.main.draw_grid(pg, window)



def homeFunc():
	#CALLFUNC
	main.lomi.player(display, pg)
	main.lomi.movement(keyinput, pg)
	main.lomi.camera(display, pg, dynamicScale)


	#main.home.houseBase(pg, display, mx, my, mouseinput)
	#ANIMATION
	
	main.lomi.updateAnimation(display, keyinput, pg)

	#move
	main.lomi.x += main.lomi.xVelx
	main.lomi.y += main.lomi.yVel

def freeRoamFunc():
	#CALLFUNC
	
	main.lomi.player(display, pg)
	main.lomi.movement(keyinput, pg)
	main.lomi.camera(display, pg, dynamicScale)
	main.Map.update_layer_0(display)
	#ANIMATION
	
	main.lomi.updateAnimation(display, keyinput, pg)


	main.Map.update(display, pg,keyinput)

	main.Map.update_layer_1(display)
	#move
	main.lomi.x += main.lomi.xVel
	main.lomi.y += main.lomi.yVel

while True:
	window.fill(0)

	display.fill(0)

	#KEY EVENTS
	mx,my = pg.mouse.get_pos()
	mouseinput = pg.mouse.get_pressed()
	keyinput = pg.key.get_pressed()
	#
	if freeRoam == True:
		freeRoamFunc()
	
	if home == True:
		homeFunc()

	
	eventHandler()



	pg.display.flip()
	clock.tick(60)

