from assets.src import button, config
from assets.src.qr_gen import gen, filter
import pygame_textinput as pti
import pygame
import cv2
import sys, os
import numpy as np
import subprocess, sys

try:
	os.mkdir('qr_codes')
except:
	pass

# height-width	
SCREEN_HEIGHT = 450
SCREEN_WIDTH = 800
TEXTBOX_WIDTH = 272
TEXTBOX_HEIGHT = 35

WHITE = (255, 255, 255)

# create display window
pygame.display.set_caption('Lab-Eyes')
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# back button
backImg = pygame.image.load('assets/textures/back.png').convert_alpha()
backButton = button.Button(10,10, backImg, 0.07)

# load homepage images
genImg = pygame.image.load('assets/textures/QR_GEN.png').convert_alpha()
scanImg = pygame.image.load('assets/textures/QR_SCAN.png').convert_alpha()
font = pygame.font.Font('assets/fonts/Luckiestguy.ttf', 60*SCREEN_WIDTH//800)

titleText = font.render('LAB EYES', True, (255,255,255))

# text input
textInputManager = pti.TextInputManager(validator=lambda input: len(input)<=50)
textinputCustom = pti.TextInputVisualizer(manager=textInputManager,
										  font_color=WHITE,
										  cursor_color=WHITE)

# game loop
run = True
pygame.key.set_repeat(300, 25)
data = ''
camera = cv2.VideoCapture(0)

try:
	while run:
		screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
		events = pygame.event.get()
		screen.fill((37,38,39,1))

		if config.page in ['scan', 'gen']:
			if backButton.draw(screen):
				config.page = ''

		# Homepage buttons
		if config.page == '':
			screen.blit(titleText, (SCREEN_WIDTH/2-titleText.get_width()/2, SCREEN_HEIGHT/4))
			if button.Button(100,200, genImg, 0.25).draw(screen):
				config.page = 'gen'
			elif button.Button(500,200, scanImg, 0.25).draw(screen):
				config.page = 'scan'

		# QR generator
		elif config.page == 'gen':
			try:
				currQrImg = pygame.image.load(f'qr_codes/{staticData}.png').convert_alpha()
				if button.Button(SCREEN_WIDTH/2 - currQrImg.get_width()/2*0.4,
								   SCREEN_HEIGHT*0.65,
								   currQrImg, 0.4).draw(screen):
					pass
					# print(f'print qr code here')
			except:
				pass

			textinputCustom.update(events)
			screen.blit(textinputCustom.surface, (SCREEN_WIDTH/2 - 50,
												  SCREEN_HEIGHT/4,
												  TEXTBOX_WIDTH,
												  TEXTBOX_HEIGHT),)

		# QR scanner
		elif config.page == 'scan':

			while True:

				# read image
				ret, imgOG = camera.read()
				imgOG = cv2.cvtColor(imgOG, cv2.COLOR_BGR2RGB)

				# decode qr
				detector = cv2.QRCodeDetector()
				H_len = np.shape(imgOG)[1]
				config.Data, points, straight_qrcode = detector.detectAndDecode(imgOG)

				if points is not None and len(config.Data) > 0:
					imgOG = cv2.flip(imgOG, 1)

					# simpifies points array->list
					points = np.ndarray.tolist(points)
					points = points[0]
					n_lines = len(points)  

					# converts floats->ints
					for i in range(n_lines):  
						points[i] = [round(a) for a in points[i]]

					# flips lines horizontally
					for i in points:
						i[0] = H_len - i[0]

					# qr bounding
					for i in range(n_lines):
						point1 = tuple(points[i])
						point2 = tuple(points[(i+1) % n_lines])

						# makes box around qr
						cv2.line(imgOG, point1, point2, color=(255, 0, 0),
								thickness=3)  

						# prints text above box
						if i == 0:
							x, y = ((point1[0]//2 + point2[0]//2) - len(config.Data) //
									2*13, (point1[1]//2 + point2[1]//2) - 10)
							cv2.putText(imgOG, config.Data, (x, y),
										cv2.FONT_HERSHEY_DUPLEX, 0.7, (0, 255, 0), 2)
						
						# text to speech
						if len(config.Data) >= 1 and config.Data!= config.oldData:
							subprocess.Popen([sys.executable, 'assets/src/playCurrentAudio.py', config.Data],)
							config.oldData = config.Data = ''

				else:

					# flips image
					imgOG = cv2.flip(imgOG, 1)

				# image manipulation
				h, w = imgOG.shape[:2]
				ratio = SCREEN_WIDTH/SCREEN_HEIGHT
				if ratio > w/h:
					imgOG = imgOG[int(h-w/ratio)//2:(h - int(h-w/ratio)//2), :]
				elif ratio < w/h:
					imgOG = imgOG[:, :int(w-ratio*h)]
				imgOG = cv2.resize(imgOG, (800, 450), interpolation =cv2.INTER_LINEAR)
				imgOG = imgOG.swapaxes(0, 1)

				# print the image on screen
				pygame.surfarray.blit_array(screen, imgOG)

				# back button
				if button.Button(10,10, backImg, 0.07).draw(screen):
					config.page = ''
					screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT),)
					break

				# exit events
				pygame.display.update()
				events = pygame.event.get()
				flag = False

				for event in events:
					if event.type == pygame.QUIT: 
						sys.exit(0)
					if event.type == pygame.KEYDOWN:
						if event.key == pygame.K_ESCAPE:
							sys.exit(0)
						if pygame.key.get_mods() & pygame.KMOD_LCTRL:
							config.page = ''
							flag = True
						if event.key == pygame.K_UP:
							config.page = 'gen'
							flag = True
				# exit
				if flag:
					flag = False
					break
				
			pygame.display.quit()
			screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
			pygame.display.init()

		# event handler
		for event in events:

			# quit game
			if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
				run = False

			# enter data
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RETURN and config.page == 'gen':
					data = filter(textinputCustom.value)
					staticData = data
					gen(data)
					textinputCustom.value = ''

				if event.key == pygame.K_UP:
					config.page = 'gen'

				if event.key == pygame.K_DOWN:
					config.page = 'scan'

				if pygame.key.get_mods() & pygame.KMOD_LCTRL:
					config.page = ''

		pygame.display.update()

except (KeyboardInterrupt, SystemExit):
    pygame.quit()
    cv2.destroyAllWindows()

pygame.quit()