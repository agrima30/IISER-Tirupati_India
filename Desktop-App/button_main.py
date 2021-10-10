import pygame
import button
from qr_gen import gen, filter
import pygame_textinput as pti
import cv2
import sys
from videoScanner import scan

# create display window
SCREEN_HEIGHT = 450
SCREEN_WIDTH = 800
TEXTBOX_WIDTH = 272
TEXTBOX_HEIGHT = 35

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption('Button Demo')

backImg = pygame.image.load('back.png').convert_alpha()
backButton = button.Button(10,10, backImg, 0.07)

# load button images
start_img = pygame.image.load('createroom.png').convert_alpha()
exit_img = pygame.image.load('joinroom.png').convert_alpha()

# create button instances
createButton = button.Button(100, 200, start_img, 0.4)
joinButton = button.Button(450, 200, exit_img, 0.4)

# text input
textInputManager = pti.TextInputManager(validator=lambda input: len(input)<=24)
textinputCustom = pti.TextInputVisualizer(manager=textInputManager)
data = ''
page = ''

#--------------------
# Scanner
#--------------------

# game loop
run = True
pygame.key.set_repeat(300, 25)

try:
	while run:
		events = pygame.event.get()
		# screen.fill((202, 228, 241))
		screen.fill((37,38,39,1))

		if page in ['scan', 'gen']:
			if backButton.draw(screen):
				page = ''

		if page == '':
			if createButton.draw(screen):
				print('CREATE SCRIPT')
				page = 'gen'

			elif joinButton.draw(screen):
				print('JOIN SCRIPT HERE')
				page = 'scan'

		elif page == 'gen':
			try:
				currQrImg = pygame.image.load(f'pics/{staticData}.png').convert_alpha()
				if button.Button(SCREEN_WIDTH/2 - currQrImg.get_width()/2*0.4, SCREEN_HEIGHT*0.65, currQrImg, 0.4).draw(screen):
					print(f'print qr code here')
			except:
				pass

			textinputCustom.update(events)
			screen.blit(textinputCustom.surface, (SCREEN_WIDTH/2 - 50,
												SCREEN_HEIGHT/2 + 7,
												TEXTBOX_WIDTH,
												TEXTBOX_HEIGHT))

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
					screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
					break
				pygame.display.update()
				events = pygame.event.get()
				for event in events:
					if event.type == pygame.QUIT:
						sys.exit(0)


		# event handler
		for event in events:
			#quit game
			if event.type == pygame.QUIT:
				run = False

			if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
				if page == 'gen':
					data = filter(textinputCustom.value)
					staticData = data
					print(f"Name = {data}")
					gen(data)
					textinputCustom.value = ''

			if event.type == pygame.VIDEORESIZE:
				old_surface_saved = screen
				screen = pygame.display.set_mode((event.w, event.h),
												pygame.RESIZABLE)
				screen.blit(old_surface_saved, (0,0))
				del old_surface_saved

		pygame.display.update()
		
except (KeyboardInterrupt, SystemExit):
    pygame.quit()
    cv2.destroyAllWindows()

pygame.quit()