from assets.src import button
from assets.src.qr_gen import gen, filter
from assets.src.videoScanner import scan
import pygame_textinput as pti
import pygame
import cv2
import sys, os

try:
	os.mkdir('qr_codes')
except:
	pass

# height-width	
SCREEN_HEIGHT = 450
SCREEN_WIDTH = 800
TEXTBOX_WIDTH = 272
TEXTBOX_HEIGHT = 35

# create display window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption('Lab-Eyes')

# back button
backImg = pygame.image.load('assets/textures/back.png').convert_alpha()
backButton = button.Button(10,10, backImg, 0.07)

# load homepage images
# titleImg = pygame.image.load('assets/textures/title.png')
genImg = pygame.image.load('assets/textures/QR_GEN.png').convert_alpha()
scanImg = pygame.image.load('assets/textures/QR_SCAN.png').convert_alpha()
font = pygame.font.Font('assets/fonts/Luckiestguy.ttf', 60*SCREEN_WIDTH//800)

titleText = font.render('LAB EYES', True, (255,255,255))

# text input
textInputManager = pti.TextInputManager(validator=lambda input: len(input)<=50)
textinputCustom = pti.TextInputVisualizer(manager=textInputManager,
										  font_color=(255, 255, 255),
										  cursor_color=(255, 255, 255))

# game loop
run = True
pygame.key.set_repeat(300, 25)
data = ''
page = ''

try:
	while run:
		events = pygame.event.get()
		screen.fill((37,38,39,1))

		if page in ['scan', 'gen']:
			if backButton.draw(screen):
				page = ''

		# Homepage buttons
		if page == '':
			# button.Button(SCREEN_WIDTH/2-titleImg.get_width()/2*0.6, SCREEN_HEIGHT/4, titleImg, 0.6).draw(screen)
			screen.blit(titleText, (SCREEN_WIDTH/2-titleText.get_width()/2, SCREEN_HEIGHT/4))
			if button.Button(100,200, genImg, 0.25).draw(screen):
				print('Generate QR')
				page = 'gen'
			elif button.Button(500,200, scanImg, 0.25).draw(screen):
				print('Scan QR')
				page = 'scan'

		# QR generator
		elif page == 'gen':
			try:
				currQrImg = pygame.image.load(f'pics/{staticData}.png').convert_alpha()
				if button.Button(SCREEN_WIDTH/2 - currQrImg.get_width()/2*0.4,
								 SCREEN_HEIGHT*0.65,
								 currQrImg, 0.4).draw(screen):
					print(f'print qr code here')
			except:
				pass

			textinputCustom.update(events)
			screen.blit(textinputCustom.surface, (SCREEN_WIDTH/2 - 50,
												  SCREEN_HEIGHT/4,
												  TEXTBOX_WIDTH,
												  TEXTBOX_HEIGHT))

		# QR scanner
		elif page == 'scan':
			camera = cv2.VideoCapture(0)
			while True:
				ret, frame = camera.read()
				frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
				frame = scan(frame)
				frame = frame.swapaxes(0, 1)
				screen = pygame.display.set_mode((640, 480), pygame.RESIZABLE)
				pygame.surfarray.blit_array(screen, frame)

				if button.Button(10,10, backImg, 0.07).draw(screen):
					page = ''
					screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT),
													  pygame.RESIZABLE)
					break

				pygame.display.update()
				events = pygame.event.get()
				for event in events:
					if event.type == pygame.QUIT:
						sys.exit(0)

		# event handler
		for event in events:
			# quit game
			if event.type == pygame.QUIT:
				run = False

			# enter data
			if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
				if page == 'gen':
					data = filter(textinputCustom.value)
					staticData = data
					print(f"Data = {data}")
					gen(data)
					textinputCustom.value = ''

			if event.type == pygame.VIDEORESIZE:
				screen = pygame.display.set_mode((event.w, event.h),
												  pygame.RESIZABLE)

		pygame.display.update()

except (KeyboardInterrupt, SystemExit):
    pygame.quit()
    cv2.destroyAllWindows()

pygame.quit()