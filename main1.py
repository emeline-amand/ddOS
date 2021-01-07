import pygame
from pygame.locals import *

files = {'C:':{'dossier1':{'fichier1':1, 'dossier2':{}},'dossier3':{'fichier2':2, 'dossier4':{'fichier3':3, 'fichier4':4}}}}

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
	ligne=160
	render(imag, None)
	for line in l:
		screen.blit(terminal.render(line, False, (0, 175, 0)), (250,ligne))
		ligne+=20
	pygame.display.flip()

def getDictKeys(dict) :
	'''fonction qui retourne les clés d'un dictionnaire. Prend en paramètre le dictionnaire'''
	k = []
	for key in dict.keys() :
		k.append(key)
	return k

def convertPath(p) :
	'''fonction qui transforme le path string spécifié en path list utilisable par les autres fonctions. Prend en param le path string'''
	p = p.split('/')
	if p[len(p)-1] == '' : #Dans le cas où path = "C:/"
		#supprimer la dernière valeur de la liste p (car vide et gène pour le len(p) plus tard)
		del p[len(p)-1]
	return p

def goto(p) :
	'''fonction qui retourne le dictionnaire au bout du chemin spécifié. Prend en param le chemin qui mène au dictionnaire'''
	#prépare le path pour la navigation à travers le dictionnaire
	p = convertPath(p)
	#Va jusqu'au chemin spécifié en redéfinissant plusieurs fois current pour être le dictionnaire de fin demandé
	current = files[p[0]]
	for i in range(len(p)-1):
		current = current[p[i+1]]
	return current

def cd(p, target) :
	'''fonction qui simule la commande qui accède à un dossier en mettant à jour la variable chemin. Prend en param1 le chemin d'origine et en param2 le dossier à entrer'''
	if target == '..' : #Remonter d'un dossier
		p = p[:p.rfind('/')]
		if p  == 'C:' : #Si déjà au minimum alors
			p += '/' #Réajoute le '/' de fin uniquement présent au dossier racine de l'arbre
		return p
	else : #Avancer d'un dossier
		exist = False
		for key in goto(p).keys() : #Test si dossier cible existe
			if key == target :
				exist = True
		if not exist :
			return p
		if p  == 'C:/' : #Si au minimum alors
			p = p[:len(p)-1] #retire le '/' de fin uniquement présent au dossier racine de l'arbre
		p = p+'/'+target
		return p

def ls(p) :
	'''fonction qui simule la commande qui liste les fichiers et dossier présents dans le dossier où l'on se trouve. Prend en param le chemin actuel'''
	#prépare le path pour la navigation à travers le dictionnaire
	p = convertPath(p)
	#Va jusqu'au chemin spécifié en redéfinissant plusieurs fois current pour être le dictionnaire de fin demandé
	current = files[p[0]]
	for i in range(len(p)-1):
		current = current[p[i+1]]
	#Affiche les clés présentes dans le chemin demandé
	keys = getDictKeys(current)
	return keys

def scrolling(l, lign, imag, p) :
	if len(l) > 17 :
		while len(l) > 17 :
			del l[0]
			lign -=20
		printLog(l, imag)
		screen.blit(terminal.render(p+" > ", False, (0, 175, 0)), (250,lign))
		pygame.display.flip()
	return l, lign

def PChacker(imag) :
	path = 'C:/'
	appli = True
	conti = True
	text=""
	log=[]
	input=None
	output=None
	ligne=160
	screen.blit(terminal.render(path+" > ", False, (0, 175, 0)), (250,ligne))
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
			elif event.type == KEYDOWN :
				if event.key == K_RETURN:
					input = text
					log.append(path+" > "+text)
					log, ligne = scrolling(log, ligne, imag, path)
					printLog(log, imag)
					text = ''
					ligne+=20
				elif event.key == K_BACKSPACE:
					text = text[:-1]
					printLog(log, imag)
					screen.blit(terminal.render(path+" > "+text, False, (0, 175, 0)), (250,ligne))
					pygame.display.flip()
				else:
					if len(path+" > "+text)<60 :
						text += event.unicode
					printLog(log, imag)
					screen.blit(terminal.render(path+" > "+text, False, (0, 175, 0)), (250,ligne))
					pygame.display.flip()
		if input != None :
			input = input.split(" ")
			if input[0]=="test":
				output="1, 2, test !"
			elif input[0] == 'ls' :
				outp = ls(path)
				output=""
				ligne+=40
				log.append("Fichiers depuis : "+path)
				log.append("")
				for key in outp :
					log.append(key)
					ligne+=20
				output=""
			elif input[0] == 'cd' and len(input)>1 :
				path = cd(path, input[1])
			elif input[0] == 'clear' :
				log = []
				ligne = 160
				printLog(log, imag)
			screen.blit(terminal.render(path+" > ", False, (0, 175, 0)), (250,ligne))
			pygame.display.flip()
			input = None
		if output != None :
			log.append(output)
			log, ligne = scrolling(log, ligne, imag, path)
			printLog(log, imag)
			ligne+=20
			output=None
			screen.blit(terminal.render(path+" > ", False, (0, 175, 0)), (250,ligne))
			pygame.display.flip()
		log, ligne = scrolling(log, ligne, imag, path)

	return imag, conti


pygame.init()
pygame.font.init()


myfont = pygame.font.SysFont('Arial', 20)
terminal = pygame.font.Font('img/SLC_.ttf', 20)
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
iconCoords = (100,640)
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