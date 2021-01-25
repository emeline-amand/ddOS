import pygame, os, math
from pygame.locals import *

files = {'C:':{'dossier1':{'réinitialiser.exe':"réinit", 'dossier2':{}},'dossier3':{'fichier2':2, 'dossier4':{'fichier3':3, 'fichier4':4}}}}
path = ""
g_log = []
g_log.append("Username : [insérer énigme]")
g_ligne = 290
g_text = ""

def render(toBlit, firstPlan) :
	"""Fonction qui affiche les _imageses spécfiée dans la liste de tuple en param2 dans l'ordre croissant des indices de la liste, sauf l'_imagese spécifiée dans le tuple en param1, qui sera affiché en premier plan"""
	#Si l'_imagese à mettre en 1er plan l'est déjà
	if firstPlan==toBlit[len(toBlit)-1]:
		#ne plus l'afficher
		del toBlit[len(toBlit)-1]
	#Sinon si il y un premier plan spécifié
	elif firstPlan!=None:
		#Supprimer de la liste des _imageses le premier plan spécifié puis le réajouter tout à la fin
		for i in range(len(toBlit)) :
			if toBlit[i]==firstPlan:
				del toBlit[i]
				break
		toBlit.append(firstPlan)
	#afficher les _imageses dans l'ordre croissant
	for _imagese in toBlit:
		screen.blit(_imagese[0], _imagese[1])
	return toBlit

def appli1(_images) :
	appli = True
	_continuer = True
	coo = (512,300)
	increment = 0.2
	screen.blit(text1,coo)
	while appli :
		for event in pygame.event.get(): #Attente des événements
			if event.type == QUIT:
				_continuer = False
				appli = False
			elif event.type == MOUSEBUTTONDOWN:
				if event.pos[0]>iconterminal_coords[0] and event.pos[0]<iconterminal_coords[0]+iconterminal_dim[0] and event.pos[1]>iconterminal_coords[1] and event.pos[1]<iconterminal_coords[1]+iconterminal_dim[1] and event.button == 1 : #Si clic sur icon (zone de clic définie par la position et taille de celui-ci)
					#Clic sur gauche sur "icon"
					_images = render(_images, (fen_iconterminal, fen_iconterminal_coords))
					appli=False
				elif event.pos[0]>icon2Coords[0] and event.pos[0]<icon2Coords[0]+icon2Dim[0] and event.pos[1]>icon2Coords[1] and event.pos[1]<icon2Coords[1]+icon2Dim[1] and event.button == 1 : #Si clic sur icon2 (zone de clic définie par la position et taille de celui-ci)
					#Clic gauche sur icon2
					_images = render(_images, (fenIcon2, fenIcon2Coords))
					appli=False
				elif event.button == 3 :
					increment*= -1
		render(_images, None)
		coo = (coo[0]+increment,coo[1])
		screen.blit(text1, coo)
		pygame.display.flip()

	return _images, _continuer

#=========================================================================#
#=========================== PC HACKER/TERMINAL ==========================#
#=========================================================================#

#Toutes les fonctions ci-dessous servent pour l'application terminal (ou anciennement PChacker)
def printLog(_log, _images) :
	"""Affiche la liste 'log' qui contient toutes les anciennes lignes du terminal"""
	ligne=270
	render(_images, None)
	for line in _log:
		screen.blit(terminalFont.render(line, True, (0, 175, 0)), (125,ligne))
		ligne+=20
	pygame.display.flip()

def getDictKeys(dict) :
	'''fonction qui retourne les clés d'un dictionnaire. Prend en paramètre le dictionnaire'''
	k = []
	for key in dict.keys() :
		k.append(key)
	return k

def convertPath(_path) :
	'''fonction qui transforme le path string spécifié en path list utilisable par les autres fonctions. Prend en param le path string'''
	_path = _path.split('/')
	if _path[len(_path)-1] == '' : #Dans le cas où path = "C:/"
		#supprimer la dernière valeur de la liste p (car vide et gène pour le len(p) plus tard)
		del _path[len(_path)-1]
	return _path

def goto(_path) :
	'''fonction qui retourne le dictionnaire au bout du chemin spécifié. Prend en param le chemin qui mène au dictionnaire'''
	#prépare le path pour la navigation à travers le dictionnaire
	_path = convertPath(_path)
	#Va jusqu'au chemin spécifié en redéfinissant plusieurs fois current pour être le dictionnaire de fin demandé
	current = files[_path[0]]
	for i in range(len(_path)-1):
		current = current[_path[i+1]]
	return current

def cd(_path, target) :
	'''Simule la commande 'cd'. Prend en param1 le chemin d'origine et en param2 le dossier à entrer'''
	if target == '..' : #Remonter d'un dossier
		_path = _path[:_path.rfind('/')]
		if _path  == 'C:' : #Si déjà au minimum alors
			_path += '/' #Réajoute le '/' de fin uniquement présent au dossier racine de l'arbre
		return _path
	else : #Avancer d'un dossier
		exist = False
		for key in goto(_path).keys() : #Test si dossier cible existe
			if key == target :
				exist = True
		if not exist :
			return _path
		if _path  == 'C:/' : #Si au minimum alors
			_path = _path[:len(_path)-1] #retire le '/' de fin uniquement présent au dossier racine de l'arbre
		_path = _path+'/'+target
		return _path

def ls(_path) :
	'''Simule la commande 'dir' (sous windows) ou 'ls' (sous mac). Prend en param le chemin actuel'''
	#prépare le path pour la navigation à travers le dictionnaire
	_path = convertPath(_path)
	#Va jusqu'au chemin spécifié en redéfinissant plusieurs fois current pour être le dictionnaire de fin demandé
	current = files[_path[0]]
	for i in range(len(_path)-1):
		current = current[_path[i+1]]
	#Affiche les clés présentes dans le chemin demandé
	keys = getDictKeys(current)
	return keys

def scrolling(_log, _ligne, _images, _path) :
	"""Renvoie la variable 'log' modifiée pour simuler un scrolling de l'écran (retire l'élément le plus ancien lorsque que celle-ci dépasse une longueur de 17)"""
	if len(_log) > 24 :
		while len(_log) > 24 :
			del _log[0]
			_ligne -=20
		printLog(_log, _images)
		screen.blit(terminalFont.render(_path+" > ", True, (0, 175, 0)), (250,_ligne))
		pygame.display.flip()
	return _log, _ligne

def Terminal(_images, _path, log, ligne, text) :
	appli = True
	_continuer = True
	input=None
	output=None
	printLog(log, _images)
	screen.blit(terminalFont.render(_path+" > "+text, True, (0, 175, 0)), (125,ligne))
	pygame.display.flip()
	#Boucle de qui fait tourner l'appli
	while appli :
		for event in pygame.event.get(): #Attente des événements
			if event.type == QUIT:
				_continuer = False
				appli = False
			elif event.type == MOUSEBUTTONDOWN:
				if event.pos[0]>iconterminal_coords[0] and event.pos[0]<iconterminal_coords[0]+iconterminal_dim[0] and event.pos[1]>iconterminal_coords[1] and event.pos[1]<iconterminal_coords[1]+iconterminal_dim[1] and event.button == 1 : #Si clic sur icon (zone de clic définie par la position et taille de celui-ci)
					#Clic sur gauche sur "icon"
					_images = render(_images, (fen_iconterminal, fen_iconterminal_coords))
					appli=False
				elif event.pos[0]>icon2Coords[0] and event.pos[0]<icon2Coords[0]+icon2Dim[0] and event.pos[1]>icon2Coords[1] and event.pos[1]<icon2Coords[1]+icon2Dim[1] and event.button == 1 : #Si clic sur icon2 (zone de clic définie par la position et taille de celui-ci)
					#Clic gauche sur icon2
					_images = render(_images, (fenIcon2, fenIcon2Coords))
					appli=False
					
			#Pour écrire dans la console
			elif event.type == KEYDOWN and _path != "" :
				if event.key == K_RETURN:
					input = text
					log.append(_path+" > "+text)
					log, ligne = scrolling(log, ligne, _images, _path)
					printLog(log, _images)
					text = ''
					ligne+=20
				elif event.key == K_BACKSPACE:
					text = text[:-1]
					printLog(log, _images)
					screen.blit(terminalFont.render(_path+" > "+text, True, (0, 175, 0)), (125,ligne))
					pygame.display.flip()
				else:
					if len(_path+" > "+text)<80 :
						text += event.unicode
					printLog(log, _images)
					screen.blit(terminalFont.render(_path+" > "+text, True, (0, 175, 0)), (125,ligne))
					pygame.display.flip()
		
		#Premier lancer de l'application ou quand "exit" est utilisé			
		if _path == "" :
			firstBoucle = True
			printLog(log, _images)
			screen.blit(terminalFont.render("Password : "+text, True, (0, 175, 0)), (125,ligne))
			pygame.display.flip()
			while firstBoucle :
				for event in pygame.event.get(): #Attente des événements
					if event.type == QUIT:
						_continuer = False
						appli = False
						firstBoucle = False
						break
					elif event.type == MOUSEBUTTONDOWN:
						if event.pos[0]>iconterminal_coords[0] and event.pos[0]<iconterminal_coords[0]+iconterminal_dim[0] and event.pos[1]>iconterminal_coords[1] and event.pos[1]<iconterminal_coords[1]+iconterminal_dim[1] and event.button == 1 : #Si clic sur icon (zone de clic définie par la position et taille de celui-ci)
							#Clic sur gauche sur "icon"
							_images = render(_images, (fen_iconterminal, fen_iconterminal_coords))
							appli=False
							firstBoucle = False
							break
						elif event.pos[0]>icon2Coords[0] and event.pos[0]<icon2Coords[0]+icon2Dim[0] and event.pos[1]>icon2Coords[1] and event.pos[1]<icon2Coords[1]+icon2Dim[1] and event.button == 1 : #Si clic sur icon2 (zone de clic définie par la position et taille de celui-ci)
							#Clic gauche sur icon2
							_images = render(_images, (fenIcon2, fenIcon2Coords))
							appli=False
							firstBoucle = False
							break
							
					#Pour écrire dans la console
					elif event.type == KEYDOWN :
						if event.key == K_RETURN:
							input = text
							log.append("Password : "+text)
							log, ligne = scrolling(log, ligne, _images, _path)
							printLog(log, _images)
							text = ''
							ligne+=20
						elif event.key == K_BACKSPACE:
							text = text[:-1]
							printLog(log, _images)
							screen.blit(terminalFont.render("Password : "+text, True, (0, 175, 0)), (125,ligne))
							pygame.display.flip()
						else:
							if len("Password : "+text)<80 :
								text += event.unicode
							printLog(log, _images)
							screen.blit(terminalFont.render("Password : "+text, True, (0, 175, 0)), (125,ligne))
							pygame.display.flip()
				if input == "password" :
					log.append("Accès autorisé, bienvenue [insérer username]")
					log.append("")
					_path = "C:/"
					ligne+=40
					input = None
					log, ligne = scrolling(log, ligne, _images, _path)
					printLog(log, _images)
					screen.blit(terminalFont.render(_path+" > ", True, (0, 175, 0)), (125,ligne))
					pygame.display.flip()
					break
				if input != None:
					screen.blit(terminalFont.render("Password : "+text, True, (0, 175, 0)), (125,ligne))
					pygame.display.flip()
					input = None
					
		#S'exécute uniquement quand la touche "enter" est appuyée (voir plus haut pourquoi)
		elif input != None :
			input = input.split(" ")
			if input[0]=="test":
				output="1, 2, test !"
			elif input[0] == 'ls' :
				outp = ls(_path)
				output=""
				ligne+=40
				log.append("Fichiers depuis : "+_path)
				log.append("")
				for key in outp :
					log.append(key)
					ligne+=20
				output=""
			elif input[0] == 'cd' and len(input)>1 :
				_path = cd(_path, input[1])
			elif input[0] == 'clear' :
				log = []
				ligne = 160
				printLog(log, _images)
			elif input[0] == 'exit' :
				log.append("")
				log.append("Username : [insérer énigme]")
				ligne+=40
				_path=""
				printLog(log, _images)
			screen.blit(terminalFont.render(_path+" > ", True, (0, 175, 0)), (125,ligne))
			pygame.display.flip()
			input = None
		if output != None :
			log.append(output)
			log, ligne = scrolling(log, ligne, _images, _path)
			printLog(log, _images)
			ligne+=20
			output=None
			screen.blit(terminalFont.render(_path+" > ", True, (0, 175, 0)), (125,ligne))
			pygame.display.flip()
		log, ligne = scrolling(log, ligne, _images, _path)

	return _images, _continuer, _path, log, ligne, text

#=========================================================================#
#======================= VARIABLES ET INITALISATIONS =====================#
#=========================================================================#
pygame.init()
pygame.font.init()

#Polices
defaultFont = pygame.font.SysFont('Arial', 23)
terminalFont = pygame.font.Font('img/SLC_.ttf', 23)

#Textes placeholders pour les test
text1 = defaultFont.render("I'm moving", True, (0, 0, 0))
text2 = defaultFont.render("Je suis généré dynamiquement quand cette fenêtre est ouverte", True, (0,0,0))

#Ouverture de la fenêtre Pygame
w = math.floor(pygame.display.Info().current_w/2-1280/2)
os.environ['SDL_VIDEO_WINDOW_POS'] = str(w)+",-10"
screen_dim = (1280, 1024)
screen = pygame.display.set_mode(screen_dim, pygame.NOFRAME)

#Chargement du fond
background = pygame.image.load("img/desktop.png").convert()

#Chargement de l'icone du terminal
iconterminal = pygame.image.load("img/icon.png").convert()
iconterminal_coords = (100,989)
iconterminal_dim = iconterminal.get_size()

#Chargement de l'icone de [WIP]
icon2 = pygame.image.load("img/icon2.png").convert()
icon2Coords = (150,989)
icon2Dim = icon2.get_size()

#Chargement de la fenêtre d'application de terminal
fen_iconterminal = pygame.image.load("img/fenetreICON.png").convert()
fen_iconterminal_dim = fen_iconterminal.get_size()
fen_iconterminal_coords = ((screen_dim[0]-fen_iconterminal_dim[0])/2, (screen_dim[1]-fen_iconterminal_dim[1])/2)

#Chargement de la fenêtre d'application de [WIP]
fenIcon2 = pygame.image.load("img/fenetreICON2.png").convert()
fenIcon2Dim = fenIcon2.get_size()
fenIcon2Coords = ((screen_dim[0]-fenIcon2Dim[0])/2, (screen_dim[1]-fenIcon2Dim[1])/2)

images = [(background, (0,0)), (iconterminal, iconterminal_coords), (icon2, icon2Coords)] #Prépare la liste pour l'affichage des éléments
pygame.key.set_repeat(400, 30) #Active la possibilité de rester appuyer sur une touche


#=========================================================================#
#=================================== JEU =================================#
#=========================================================================#
continuer = True
while continuer :
	#Gestion des événements
	for event in pygame.event.get():
		if event.type == QUIT: 
			#Clic sur la croix pour fermer la fenêtre
			continuer = False
		elif event.type == MOUSEBUTTONDOWN: 
			#Clic de souris
			if event.pos[0]>iconterminal_coords[0] and event.pos[0]<iconterminal_coords[0]+iconterminal_dim[0] and event.pos[1]>iconterminal_coords[1] and event.pos[1]<iconterminal_coords[1]+iconterminal_dim[1] and event.button == 1 : #Si clic sur icon (zone de clic définie par la position et taille de celui-ci)
				#Clic sur gauche sur "icon"
				images = render(images, (fen_iconterminal, fen_iconterminal_coords))
			elif event.pos[0]>icon2Coords[0] and event.pos[0]<icon2Coords[0]+icon2Dim[0] and event.pos[1]>icon2Coords[1] and event.pos[1]<icon2Coords[1]+icon2Dim[1] and event.button == 1 : #Si clic sur icon2 (zone de clic définie par la position et taille de celui-ci)
				#Clic gauche sur icon2
				images = render(images, (fenIcon2, fenIcon2Coords))

	#Affichage du jeu (affichage des _imageses dans l'ordre + rafraichissement de l'écran)
	render(images, None)
	pygame.display.flip()
	#Appel des fonctions associés à l'application en premier plan
	if images[len(images)-1][0] == fen_iconterminal:
		images, continuer, path, g_log, g_ligne, g_text = Terminal(images, path, g_log, g_ligne, g_text)
	elif images[len(images)-1][0] == fenIcon2:
		images, continuer = appli1(images)

pygame.quit()