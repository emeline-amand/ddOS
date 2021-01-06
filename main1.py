import pygame
from pygame.locals import *

def render(toBlit, firstPlan) :
	"""Fonction qui affiche les images spécfiée dans la liste de tuple en param2 dans l'ordre croissant des indices de la liste, sauf l'image spécifiée dans le tuple en param1, qui sera affiché en premier plan"""
	#Si l'image à mettre en 1er plan l'est déjà
	if firstPlan==toBlit[len(toBlit)-1]:
		#ne plus l'afficher
		del toBlit[len(toBlit)-1]
	#Sinon si il y un premier plan spécifié
	elif firstPlan!=None:
		#Supprimer de la liste des images le premier plan spécifié puis le réajouter tout à la fin
		for i in range(len(toBlit)) :
			if toBlit[i]==firstPlan:
				del toBlit[i]
				break
		toBlit.append(firstPlan)
	#afficher les images dans l'ordre croissant
	for image in toBlit:
		screen.blit(image[0], image[1])
	return toBlit

def appli1(imag) :
	appli = True
	conti = True
	coo = (300,200)
	increment = 0.2
	screen.blit(text1,coo)
	while appli :
		for event in pygame.event.get(): #Attente des événements
			if event.type == QUIT:
				conti = False
				appli = False
			elif event.type == MOUSEBUTTONDOWN:
				if event.pos[0]>iconCoords[0] and event.pos[0]<iconCoords[0]+iconDim[0] and event.pos[1]>iconCoords[1] and event.pos[1]<iconCoords[1]+iconDim[1] and event.button == 1 : #Si clic sur icon (zone de clic définie par la position et taille de celui-ci)
					imag = render(imag, (fenIcon, fenIconCoords))
					appli = False
				elif event.pos[0]>icon2Coords[0] and event.pos[0]<icon2Coords[0]+icon2Dim[0] and event.pos[1]>icon2Coords[1] and event.pos[1]<icon2Coords[1]+icon2Dim[1] and event.button == 1  : #Si clic sur icon2 (zone de clic définie par la position et taille de celui-ci)
					imag = render(imag, (fenIcon2, fenIcon2Coords))
					appli = False
				elif event.button == 3 :
					increment*= -1
		render(imag, None)
		coo = (coo[0]+increment,coo[1])
		screen.blit(text1, coo)
		pygame.display.flip()

	return imag, conti


def appli2(imag) :
	appli = True
	conti = True
	screen.blit(text2, (350,400))
	pygame.display.flip()
	while appli :
		for event in pygame.event.get(): #Attente des événements
			if event.type == QUIT:
				conti = False
				appli = False
			elif event.type == MOUSEBUTTONDOWN:
				if event.pos[0]>iconCoords[0] and event.pos[0]<iconCoords[0]+iconDim[0] and event.pos[1]>iconCoords[1] and event.pos[1]<iconCoords[1]+iconDim[1] and event.button == 1 : #Si clic sur icon (zone de clic définie par la position et taille de celui-ci)
					imag = render(imag, (fenIcon, fenIconCoords))
					appli = False
				elif event.pos[0]>icon2Coords[0] and event.pos[0]<icon2Coords[0]+icon2Dim[0] and event.pos[1]>icon2Coords[1] and event.pos[1]<icon2Coords[1]+icon2Dim[1] and event.button == 1 : #Si clic sur icon2 (zone de clic définie par la position et taille de celui-ci)
					imag = render(imag, (fenIcon2, fenIcon2Coords))
					appli = False

	return imag, conti
	
def printLog(l, imag) :
	l=l.split("\n")
	ligne=150
	render(imag, None)
	for line in l:
		screen.blit(terminal.render(line, False, (0, 0, 0)), (300,ligne))
		ligne+=30
	pygame.display.flip()
	
def PChacker(imag) :
	appli = True
	conti = True
	text=""
	log=""
	input=None
	output=None
	ligne=150
	while appli :
		for event in pygame.event.get(): #Attente des événements
			if event.type == QUIT:
				conti = False
				appli = False
			elif event.type == MOUSEBUTTONDOWN:
				if event.pos[0]>iconCoords[0] and event.pos[0]<iconCoords[0]+iconDim[0] and event.pos[1]>iconCoords[1] and event.pos[1]<iconCoords[1]+iconDim[1] and event.button == 1 : #Si clic sur icon (zone de clic définie par la position et taille de celui-ci)
					imag = render(imag, (fenIcon, fenIconCoords))
					appli = False
				elif event.pos[0]>icon2Coords[0] and event.pos[0]<icon2Coords[0]+icon2Dim[0] and event.pos[1]>icon2Coords[1] and event.pos[1]<icon2Coords[1]+icon2Dim[1] and event.button == 1 : #Si clic sur icon2 (zone de clic définie par la position et taille de celui-ci)
					imag = render(imag, (fenIcon2, fenIcon2Coords))
					appli = False
			elif event.type == KEYDOWN :
				if event.key == K_RETURN:
					input = text
					log+="> "+text+"\n"
					printLog(log, imag)
					text = ''
					ligne+=30
				elif event.key == K_BACKSPACE:
					text = text[:-1]
					printLog(log, imag)
					screen.blit(terminal.render("> ", False, (0, 0, 0)), (300,ligne))
					screen.blit(terminal.render(text, False, (0, 0, 0)), (320,ligne))
					pygame.display.flip()
				else:
					text += event.unicode
					screen.blit(terminal.render("> ", False, (0, 0, 0)), (300,ligne))
					screen.blit(terminal.render(text, False, (0, 0, 0)), (320,ligne))
					pygame.display.flip()
		if input != None :
			if input=="test":
				output="1, 2, test !"
				input = None
		if output != None :
			log+=output+"\n"
			printLog(log, imag)
			ligne+=30
			output=None

	return imag, conti


pygame.init()
pygame.font.init()


myfont = pygame.font.SysFont('Arial', 30)
terminal = pygame.font.Font('img/SLC_.ttf', 30)
text1 = myfont.render("I'm moving", False, (0, 0, 0))
text2 = myfont.render("Je suis généré dynamiquement quand cette fenêtre est ouverte", False, (0,0,0))

#Ouverture de la fenêtre Pygame
screenDim = (1200, 675)
screen = pygame.display.set_mode(screenDim)

#Chargement et collage du fond
fond = pygame.image.load("img/desktop.png").convert()
screen.blit(fond, (0,0))

#Icone de test 1
icon = pygame.image.load("img/icon.png").convert()
iconCoords = (100,639)
iconDim = icon.get_size()
screen.blit(icon, iconCoords)

#Icone de test 2
icon2 = pygame.image.load("img/icon2.png").convert()
icon2Coords = (150,639)
icon2Dim = icon2.get_size()
screen.blit(icon2, icon2Coords)

#Fenêtre qui apparaît lorsqu'icon est cliqué
fenIcon = pygame.image.load("img/fenetreICON.png").convert()
fenIconDim = fenIcon.get_size()
fenIconCoords = ((screenDim[0]-fenIconDim[0])/2, (screenDim[1]-fenIconDim[1])/2)

#Fenêtre qui apparaît lorsqu'icon est cliqué
fenIcon2 = pygame.image.load("img/fenetreICON2.png").convert()
fenIcon2Dim = fenIcon2.get_size()
fenIcon2Coords = ((screenDim[0]-fenIcon2Dim[0])/2, (screenDim[1]-fenIcon2Dim[1])/2)

#Rafraîchissement de l'écran
pygame.display.flip()

images = [(fond, (0,0)), (icon, iconCoords), (icon2, icon2Coords)]

pygame.key.set_repeat(400, 30)

continuer = True
#BOUCLE INFINIE
while continuer :
	#Attente des événements
	for event in pygame.event.get():
		if event.type == QUIT:
			continuer = False
		elif event.type == MOUSEBUTTONDOWN:
			if event.pos[0]>iconCoords[0] and event.pos[0]<iconCoords[0]+iconDim[0] and event.pos[1]>iconCoords[1] and event.pos[1]<iconCoords[1]+iconDim[1] and event.button == 1 : #Si clic sur icon (zone de clic définie par la position et taille de celui-ci)
				images = render(images, (fenIcon, fenIconCoords))
			elif event.pos[0]>icon2Coords[0] and event.pos[0]<icon2Coords[0]+icon2Dim[0] and event.pos[1]>icon2Coords[1] and event.pos[1]<icon2Coords[1]+icon2Dim[1] and event.button == 1 : #Si clic sur icon2 (zone de clic définie par la position et taille de celui-ci)
				images = render(images, (fenIcon2, fenIcon2Coords))

	#Re-collage
	render(images, None)
	#Rafraichissement
	pygame.display.flip()
	if images[len(images)-1][0] == fenIcon:
		images, continuer = PChacker(images)
	elif images[len(images)-1][0] == fenIcon2:
		images, continuer = appli1(images)

pygame.quit()