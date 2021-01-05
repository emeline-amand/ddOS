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
	screen.blit(text,coo)
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
		screen.blit(text, coo)
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


pygame.init()
pygame.font.init()


myfont = pygame.font.SysFont('Comic Sans MS', 30)
text = myfont.render("I'm moving", False, (0, 0, 0))
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
		images, continuer = appli1(images)
	elif images[len(images)-1][0] == fenIcon2:
		images, continuer = appli2(images)

pygame.quit()