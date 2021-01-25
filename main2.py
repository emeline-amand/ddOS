import pygame, os, math
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
					imag = render(imag, (fenIcon, fen_icon_coords))
					appli = False
				elif event.pos[0]>iconmessage_coords[0] and event.pos[0]<iconmessage_coords[0]+iconmessage_dim[0] and event.pos[1]>iconmessage_coords[1] and event.pos[1]<iconmessage_coords[1]+iconmessage_dim[1] and event.button == 1  : #Si clic sur icon2 (zone de clic définie par la position et taille de celui-ci)
					imag = render(imag, (fen_message, fen_message_coords))
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
				elif event.pos[0]>iconmessage_coords[0] and event.pos[0]<iconmessage_coords[0]+iconmessage_dim[0] and event.pos[1]>iconmessage_coords[1] and event.pos[1]<iconmessage_coords[1]+iconmessage_dim[1] and event.button == 1 : #Si clic sur iconmessage (zone de clic définie par la position et taille de celui-ci)
					imag = render(imag, (fen_message, fen_message_coords))
					appli = False

	return imag, conti


def message(_imag) :
	"""permet d'afficher les messages sur une fenetre en séparant l'émetteur du message et son objet"""
	appli = True
	conti = True
	coor = (700,700)
	increment = 0.2
	popup = myfont.render("pop up", True, (0, 0, 0))
	#screen.blit(popup,coor)

#definition variable avec objets et contenu des messages
	messages=[["de: Boss","objet1","message1"],["de: Boss","objet2","message2"],["de: Hacker","objet3","message3"]]

	y=300
	pygame.draw.line(screen,(0,0,0), (340, y), (750, y), 2)
	pygame.draw.line(screen,(0,0,0), (340, 270), (340, 910), 2)
	screen.blit(myfont.render("émetteur: ",True,(0,0,0)),(350,265))
	screen.blit(myfont.render("objet: ",True,(0,0,0)),(600,265))

	for i in range (len(messages)):
#on fait afficher l'émetteur des messages
		screen.blit(myfont.render(messages[i][0],True,(0,0,0)),(350,y))
		messages[i].append(y-30)


#on fait afficher l'objet des messages
		screen.blit(myfont.render(messages[i][1],True,(0,0,0)),(600,y))
		messages[i].append(y-30)

#on fait afficher ligne de séparation
		y+=40
		pygame.draw.line(screen,(0,0,0),(340, y),(750, y), 2)


	pygame.display.flip()
#on fait afficher séparation entre chaque lignes

#truc commun à toutes les applis
	while appli :
		for event in pygame.event.get(): #Attente des événements
			if event.type == QUIT:
				conti = False
				appli = False
			elif event.type == MOUSEBUTTONDOWN:
				y=300
				for i in range (len(messages)):
					#on regarde la position de la souris
					if 350<event.pos[0]<800 and y<event.pos[1]<y+40:
						#efface texte à l'écran
						render(_imag, None)

						#affiche texte à l'écran, precisez coordonnées
						screen.blit(myfont.render(messages[i][2],True,(0,0,0)),(350,310))
						screen.blit(myfont.render("return",True,(0,0,0)),(990,850))

						#refresh écran
						pygame.display.flip()
					y+=40
				#touche return qui permet de revenir à la liste des mails
				if 990<event.pos[0]<1070 and 820<event.pos[1]<900:
					render(_imag, None)
					y=300
					pygame.draw.line(screen,(0,0,0), (340, y), (750, y), 2)
					pygame.draw.line(screen,(0,0,0), (340, 270), (340, 910), 2)
					screen.blit(myfont.render("émetteur: ",True,(0,0,0)),(350,265))
					screen.blit(myfont.render("objet: ",True,(0,0,0)),(600,265))

					for i in range (len(messages)):
#on fait afficher l'émetteur des messages
						screen.blit(myfont.render(messages[i][0],True,(0,0,0)),(350,y))
						messages[i].append(y-30)
#on fait afficher l'objet des messages
						screen.blit(myfont.render(messages[i][1],True,(0,0,0)),(600,y))
						messages[i].append(y-30)
						y+=40
#on fait afficher ligne de séparation
						pygame.draw.line(screen,(0,0,0),(340, y),(750, y), 2)

					pygame.display.flip()

				#quitter l'appli
				if event.pos[0]>iconCoords[0] and event.pos[0]<iconCoords[0]+iconDim[0] and event.pos[1]>iconCoords[1] and event.pos[1]<iconCoords[1]+iconDim[1] and event.button == 1 : #Si clic sur icon (zone de clic définie par la position et taille de celui-ci)
					_imag = render(_imag, (fenIcon, fen_icon_coords))
					appli = False
				elif event.pos[0]>iconmessage_coords[0] and event.pos[0]<iconmessage_coords[0]+iconmessage_dim[0] and event.pos[1]>iconmessage_coords[1] and event.pos[1]<iconmessage_coords[1]+iconmessage_dim[1] and event.button == 1 :
				#Si clic sur iconmessage (zone de clic définie par la position et taille de celui-ci)
					_imag = render(_imag, (fen_message, fen_message_coords))
					appli = False

		#pygame.display.flip()






	return _imag, conti



pygame.init()
pygame.font.init()


myfont = pygame.font.SysFont('Arial', 30)
text = myfont.render("I'm moving", True, (0, 0, 0))
text2 = myfont.render("Je suis généré dynamiquement quand cette fenêtre est ouverte", False, (0,0,0))

#Ouverture de la fenêtre Pygame
w = math.floor(pygame.display.Info().current_w/2-1280/2)
os.environ['SDL_VIDEO_WINDOW_POS'] = str(w)+",-10"
screenDim = (1280, 1024)
screen = pygame.display.set_mode(screenDim, pygame.NOFRAME)

#Chargement et collage du fond
fond = pygame.image.load("img/desktop.png").convert()
screen.blit(fond, (0,0))

#Icone de test 1
icon = pygame.image.load("img/icon.png").convert()
iconCoords = (100,989)
iconDim = icon.get_size()
screen.blit(icon, iconCoords)

#Icone des messages
iconmessage = pygame.image.load("img/iconmessage.png").convert()
iconmessage_coords = (150,989)
iconmessage_dim = iconmessage.get_size()
screen.blit(iconmessage, iconmessage_coords)

#Fenêtre qui apparaît lorsqu'icon est cliqué
fenIcon = pygame.image.load("img/fenetreICON.png").convert()
fenIconDim = fenIcon.get_size()
fen_icon_coords = ((screenDim[0]-fenIconDim[0])/2, (screenDim[1]-fenIconDim[1])/2)

#Fenêtre message qui apparaît lorsqu'icon est cliqué
fen_message = pygame.image.load("img/fen_message.png").convert()
fen_message_dim = fen_message.get_size()
fen_message_coords = ((screenDim[0]-fen_message_dim[0])/2, (screenDim[1]-fenIconDim[1])/2)

#POP UP
coor = (700,700)
increment = 0.2
popup = myfont.render("pop up", True, (0, 0, 0))
screen.blit(popup,coor)
for event in pygame.event.get(): #Attente des événements
	if event.type == MOUSEBUTTONDOWN:

		if event.button == 3 :

			increment*= -1
		render(_imag, None)
		coor = (coor[0]+increment,coor[1])
		screen.blit(popup, coor)
		pygame.display.flip()

#Rafraîchissement de l'écran
pygame.display.flip()

images = [(fond, (0,0)), (icon, iconCoords), (iconmessage, iconmessage_coords)]

continuer = True
#BOUCLE INFINIE
while continuer :
	#Attente des événements
	for event in pygame.event.get():
		if event.type == QUIT:
			continuer = False
		elif event.type == MOUSEBUTTONDOWN:
			if event.pos[0]>iconCoords[0] and event.pos[0]<iconCoords[0]+iconDim[0] and event.pos[1]>iconCoords[1] and event.pos[1]<iconCoords[1]+iconDim[1] and event.button == 1 : #Si clic sur icon (zone de clic définie par la position et taille de celui-ci)
				images = render(images, (fenIcon, fen_icon_coords))
			elif event.pos[0]>iconmessage_coords[0] and event.pos[0]<iconmessage_coords[0]+iconmessage_dim[0] and event.pos[1]>iconmessage_coords[1] and event.pos[1]<iconmessage_coords[1]+iconmessage_dim[1] and event.button == 1 : #Si clic sur icon2 (zone de clic définie par la position et taille de celui-ci)
				images = render(images, (fen_message, fen_message_coords))

	#Re-collage
	render(images, None)
	#Rafraichissement
	pygame.display.flip()
	if images[len(images)-1][0] == fenIcon:
		images, continuer = appli1(images)
	elif images[len(images)-1][0] == fen_message:
		images, continuer = message(images)

pygame.quit()
