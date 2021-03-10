import pygame, os, math
from pygame.locals import *

#Pour l'appli terminal
files = {'C:':{'Documents':{}, 'Images':{}, 'Téléchargements':{}, 'Musique':{}, 'Videos':{}, 'Applications':{'jarvis.exe':'exe', 'Paramètres':{'reinitialiser.exe':'exe'}}}}
g_path = ""
g_log = []
g_ligne = 290
#<temporaire>
g_log.append("Ce message est temporaire, il sera plus tard supprimé")
g_log.append("Code du PC : 111221")
g_log.append("Réponse à la seule question de sécurité : Glad0s")
g_log.append("")
g_ligne+=80
#</temporaire>
g_log.append("Username : 1 11 21 1211")
g_text = ""
g_isJarvisUsed = False

#Pour l'appli message
messages=[["de: Boss","objet1","message1"],["de: Boss","objet2","message2"],["de: Hacker","objet3","message3"]]

def render(toBlit, firstPlan) :
	"""Fonction qui affiche les _imageses spécfiée dans la liste de tuple en param2 dans l'ordre croissant des indices de la liste, sauf l'_imagese spécifiée dans le tuple en param1, qui sera affiché en premier plan"""
	#Si l'_imagese à mettre en 1er plan l'est déjà
	if firstPlan==toBlit[len(toBlit)-1]:
		#ne plus l'afficher
		del toBlit[len(toBlit)-1]
	#Sinon s'il y un premier plan spécifié
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

#=========================================================================#
#================================= MESSAGE ===============================#
#=========================================================================#

def message(_images, _messages) :
	"""permet d'afficher les messages sur une fenetre en séparant l'émetteur du message et son objet"""
	appli = True
	_continuer = True
	coor = (700,700)
	increment = 0.2
	popup = messageFont.render("pop up", True, (0, 0, 0))
	#screen.blit(popup,coor)

	#definition variable avec objets et contenu des messages
	_messages=[["de: Boss","objet1","message1"],["de: Boss","objet2","message2"],["de: Hacker","objet3","message3"]]

	y=300
	pygame.draw.line(screen,(0,0,0), (340, y), (750, y), 2)
	pygame.draw.line(screen,(0,0,0), (340, 270), (340, 910), 2)
	screen.blit(messageFont.render("émetteur: ",True,(0,0,0)),(350,265))
	screen.blit(messageFont.render("objet: ",True,(0,0,0)),(600,265))

	for i in range (len(_messages)):
		#on fait afficher l'émetteur des messages
		screen.blit(messageFont.render(_messages[i][0],True,(0,0,0)),(350,y))
		_messages[i].append(y-30)

		#on fait afficher l'objet des messages
		screen.blit(messageFont.render(_messages[i][1],True,(0,0,0)),(600,y))
		_messages[i].append(y-30)

		#on fait afficher ligne de séparation
		y+=40
		pygame.draw.line(screen,(0,0,0),(340, y),(750, y), 2)


	pygame.display.flip()
	#on fait afficher séparation entre chaque lignes

	#truc commun à toutes les applis
	while appli :
		for event in pygame.event.get(): #Attente des événements
			if event.type == QUIT:
				_continuer = False
				appli = False
			elif event.type == MOUSEBUTTONDOWN:
				y=300
				for i in range (len(_messages)):
					#on regarde la position de la souris
					if 350<event.pos[0]<800 and y<event.pos[1]<y+40:
						#efface texte à l'écran
						render(_images, None)

						#affiche texte à l'écran, precisez coordonnées
						screen.blit(messageFont.render(_messages[i][2],True,(0,0,0)),(350,310))
						screen.blit(messageFont.render("return",True,(0,0,0)),(950,750))

						#refresh écran
						pygame.display.flip()
					y+=40
				#touche return qui permet de revenir à la liste des mails
				if 950<event.pos[0]<1020 and 750<event.pos[1]<790:
					render(_images, None)
					y=300
					pygame.draw.line(screen,(0,0,0), (340, y), (750, y), 2)
					pygame.draw.line(screen,(0,0,0), (340, 270), (340, 910), 2)
					screen.blit(messageFont.render("émetteur: ",True,(0,0,0)),(350,265))
					screen.blit(messageFont.render("objet: ",True,(0,0,0)),(600,265))

					for i in range (len(_messages)):
					#on fait afficher l'émetteur des messages
						screen.blit(messageFont.render(_messages[i][0],True,(0,0,0)),(350,y))
						_messages[i].append(y-30)
						#on fait afficher l'objet des messages
						screen.blit(messageFont.render(_messages[i][1],True,(0,0,0)),(600,y))
						_messages[i].append(y-30)
						y+=40
						#on fait afficher ligne de séparation
						pygame.draw.line(screen,(0,0,0),(340, y),(750, y), 2)
					pygame.display.flip()

				#quitter l'appli
				if event.pos[0]>iconterminal_coords[0] and event.pos[0]<iconterminal_coords[0]+iconterminal_dim[0] and event.pos[1]>iconterminal_coords[1] and event.pos[1]<iconterminal_coords[1]+iconterminal_dim[1] and event.button == 1 : #Si clic sur icon (zone de clic définie par la position et taille de celui-ci)
					#Clic sur gauche sur "icon"
					_images = render(_images, (fen_terminal, fen_terminal_coords))
					appli=False
				elif event.pos[0]>iconmessage_coords[0] and event.pos[0]<iconmessage_coords[0]+iconmessage_dim[0] and event.pos[1]>iconmessage_coords[1] and event.pos[1]<iconmessage_coords[1]+iconmessage_dim[1] and event.button == 1 : #Si clic sur icon2 (zone de clic définie par la position et taille de celui-ci)
					#Clic gauche sur icon2
					_images = render(_images, (fen_message, fen_message_coords))
					appli=False
				elif event.pos[0]>1205 and event.pos[0]<1225 and event.pos[1]>989 and event.pos[1]<1010 and event.button == 1 :
					#Clic gauche sur la croix en bas à droite
					_continuer = False
					appli = False

	return _images, _continuer, _messages

#=========================================================================#
#=========================== PC HACKER/TERMINAL ==========================#
#=========================================================================#

#Toutes les fonctions ci-dessous servent pour l'application terminal (ou anciennement PChacker)
def printLog(_log, _images) :
	"""Affiche la liste 'log' qui contient toutes les anciennes lignes du terminal"""
	#coordonée y à partir desquelles les log vont s'afficher
	ligne=270
	#Refresh l'écran
	render(_images, None)
	#Affiche ligne par ligne en prenant pour une ligne un élément de la list '_log'
	for line in _log:
		screen.blit(terminalFont.render(line, True, (0, 175, 0)), (125,ligne))
		ligne+=20
	pygame.display.flip()

def getDictKeys(dict) :
	'''fonction qui retourne les clés d'un dictionnaire sous forme de liste. Prend en paramètre le dictionnaire'''
	#utile car en ne modifie pas de variable mais renvoie une valeur sur place (il est possible de s'en passer mais ça aide à la lisibilité)
	return list(dict.keys())

def getDictContent(dict) :
	'''fonction qui retourne le contenu d'un dictionnaire sous forme de liste. Prend en paramètre le dictionnaire'''
	#utile car en ne modifie pas de variable mais renvoie une valeur sur place (il est possible de s'en passer mais ça aide à la lisibilité)
	return list(dict.values())

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
	if target == '..' : #si commande 'remonter d'un dossier'
		_path = _path[:_path.rfind('/')]
		if _path  == 'C:' : #Si déjà au minimum alors
			_path += '/' #Réajoute le '/' de fin uniquement présent au dossier racine de l'arbre
			return _path, False
		return _path, True
	else : #sinon avancer d'un dossier
		exist = False
		for key in goto(_path).keys() : #Regarde si dossier cible existe
			if key == target :
				exist = True
		if not exist : # s'il n'existe pas
			return _path, False # fin, rien ne se passe
		if _path  == 'C:/' : #Si à la racine alors
			_path = _path[:len(_path)-1] #retire le '/' de fin uniquement présent au dossier racine de l'arbre
		_path = _path+'/'+target #Enfin, ajoute le dossier cible au chemin
		return _path, True

def ls(_path) :
	'''Renvoie des listes contenants les clefs et valeurs d'un dictionnaire'''
	#mieux que dict.items car renvoie deux listes plutot qu'une liste de tuple (en plus dict.item ne revoie pas un objet de type list mais qq chose de différent qu'il faut convertir)
	return list(getDictKeys(goto(_path))), list(getDictContent(goto(_path)))

def scrolling(_log, _ligne, _images, _path) :
	"""Renvoie la variable 'log' modifiée pour simuler un scrolling de l'écran (retire l'élément le plus ancien lorsque que celle-ci dépasse une longueur de 17)"""
	while len(_log) > 24 : #longueur de log = nombre de lignes affichées, et comme la capacité du terminal est de 24 lignes, la fonction scrolling s'exécute vraiment quand len(log) > 24
		#Donc tant qu'il y a des lignes en trop : retirer la première ligne (la plus ancienne)
		del _log[0]
		_ligne -=20
	#Afficher les logs corrigées
	printLog(_log, _images)
	screen.blit(terminalFont.render(_path+" > ", True, (0, 175, 0)), (125,_ligne))
	pygame.display.flip()
	return _log, _ligne

def printDialogue(_log, _ligne, dialogue) :
	"""Modifie log pour lui ajouter ce qu'il faut pour afficher un nouveau dialogue"""
	_log.append(dialogue[0]) #Afficher ce que dit l'IA
	#saut de ligne \/
	_ligne+=20
	if len(dialogue[1]) > 0 : #Si choix de réponses disponible
		for reponse in dialogue[1] : 
			#Afficher chacune des réponses possibles
			_log.append(reponse)
			_ligne+=20
		_log.append("")
		_ligne+=20
	return _log, _ligne

def Terminal(_images, path, log, ligne, text, isJarvisUsed) :
	appli = True #Condition pour la boucle principale
	_continuer = True #Valeur qui sera retournée lors de la sortie de l'application pour stopper ou non le jeu
	input=None #Utile plus tard pour regarder ce qui a été entré au clavier
	if isJarvisUsed : input = "appli jarvis"
	printLog(log, _images) #Affiche les logs (valeur de log récupérée depuis les paramètres de la fonction
	screen.blit(terminalFont.render(path+" > "+text, True, (0, 175, 0)), (125,ligne))
	pygame.display.flip()
	#Boucle de qui fait tourner l'appli
	while appli :
		#Attente des événements
		for event in pygame.event.get():
			if event.type == QUIT:
				_continuer = False
				appli = False
			elif event.type == MOUSEBUTTONDOWN:
				if event.pos[0]>iconterminal_coords[0] and event.pos[0]<iconterminal_coords[0]+iconterminal_dim[0] and event.pos[1]>iconterminal_coords[1] and event.pos[1]<iconterminal_coords[1]+iconterminal_dim[1] and event.button == 1 : #Si clic sur icon (zone de clic définie par la position et taille de celui-ci)
					#Clic sur gauche sur "terminal" => quitte l'appli
					_images = render(_images, (fen_terminal, fen_terminal_coords))
					appli=False
				elif event.pos[0]>iconmessage_coords[0] and event.pos[0]<iconmessage_coords[0]+iconmessage_dim[0] and event.pos[1]>iconmessage_coords[1] and event.pos[1]<iconmessage_coords[1]+iconmessage_dim[1] and event.button == 1 : #Si clic sur icon2 (zone de clic définie par la position et taille de celui-ci)
					#Clic gauche sur "message" => quitte l'appli
					_images = render(_images, (fen_message, fen_message_coords))
					appli=False
				elif event.pos[0]>1205 and event.pos[0]<1225 and event.pos[1]>989 and event.pos[1]<1010 and event.button == 1 :
					#Clic gauche sur la croix en bas à droite  => quitte le jeu
					_continuer = False
					appli = False
					
			#Pour écrire dans le terminal
			elif event.type == KEYDOWN and path != "" :
				if event.key == K_RETURN: #Si entrée appuyée
					input = text #Récupérer la valeur entrée
					log.append(path+" > "+text) #ajout de la ligne dans log
					log, ligne = scrolling(log, ligne, _images, path) #scroll si nécessaire
					printLog(log, _images)
					text = '' #reset le champ d'entrée
					ligne+=20
				elif event.key == K_BACKSPACE: #Si retour appuyé
					text = text[:-1] #supprime dernier charactère
					#Affichage \/
					printLog(log, _images)
					screen.blit(terminalFont.render(path+" > "+text, True, (0, 175, 0)), (125,ligne))
					pygame.display.flip()
				else: #sinon
					if len(path+" > "+text)<80 : #si la ligne ne dépasse pas la longueur maximale du terminal
						text += event.unicode #ajouter le charactère associé à la touche appuyée au champ d'entrée
					#Affichage \/
					printLog(log, _images)
					screen.blit(terminalFont.render(path+" > "+text, True, (0, 175, 0)), (125,ligne))
					pygame.display.flip()
		
		#interface de login (premier lancer de terminal ou "exit")		
		if path == "" :
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
							#Clic sur gauche sur "terminal" => quitte l'appli
							_images = render(_images, (fen_terminal, fen_terminal_coords))
							appli=False
							firstBoucle = False
							break
						elif event.pos[0]>iconmessage_coords[0] and event.pos[0]<iconmessage_coords[0]+iconmessage_dim[0] and event.pos[1]>iconmessage_coords[1] and event.pos[1]<iconmessage_coords[1]+iconmessage_dim[1] and event.button == 1 : #Si clic sur icon2 (zone de clic définie par la position et taille de celui-ci)
							#Clic gauche sur "message" => quitte l'appli
							_images = render(_images, (fen_message, fen_message_coords))
							appli=False
							firstBoucle = False
							break
						elif event.pos[0]>1205 and event.pos[0]<1225 and event.pos[1]>989 and event.pos[1]<1010 and event.button == 1 :
							#Clic gauche sur la croix en bas à droite  => quitte le jeu
							_continuer = False
							appli = False
							firstBoucle = False
							
					#Pour écrire dans le terminal
					elif event.type == KEYDOWN :
						if event.key == K_RETURN: #Si entrée appuyée
							input = text #Récupérer la valeur entrée
							log.append("Password : "+text) #ajout de la ligne dans log
							log, ligne = scrolling(log, ligne, _images, path) #scroll si nécessaire
							printLog(log, _images)
							text = '' #reset le champ d'entrée
							ligne+=20
						elif event.key == K_BACKSPACE: #Si retour appuyé
							text = text[:-1] #supprime dernier charactère
							#Affichage \/
							printLog(log, _images)
							screen.blit(terminalFont.render("Password : "+text, True, (0, 175, 0)), (125,ligne))
							pygame.display.flip()
						else: #sinon
							if len("Password : "+text)<80 : #si la ligne ne dépasse pas la longueur maximale du terminal
								text += event.unicode #ajouter le charactère associé à la touche appuyée au champ d'entrée
							#Affichage \/
							printLog(log, _images)
							screen.blit(terminalFont.render("Password : "+text, True, (0, 175, 0)), (125,ligne))
							pygame.display.flip()
				if input == "111221" : #Si le bon mot de passe est entré
					#Accès au PC \/
					log.append("Accès autorisé, bienvenue ddOS")
					log.append("")
					path = "C:/"
					ligne+=40
					input = None
					log, ligne = scrolling(log, ligne, _images, path)
					printLog(log, _images)
					screen.blit(terminalFont.render(path+" > ", True, (0, 175, 0)), (125,ligne))
					pygame.display.flip()
					break
				elif input != None: #Sinon rien faire
					log.append("Mot de passe incorrect")
					ligne+=20
					printLog(log, _images)
					screen.blit(terminalFont.render("Password : "+text, True, (0, 175, 0)), (125,ligne))
					pygame.display.flip()
					input = None
					
		#S'exécute quand la touche "entrée" est appuyée
		if input != None :
			input = input.split(" ") #Sépare input à chaque espace pour utiliser des commandes et ses arguements
			#dir \/
			if input[0] == 'dir' :
				keys, contents = ls(path)
				ligne+=40
				log.append("Fichiers depuis : "+path)
				log.append("")
				for i in range(len(keys)) :
					if type(contents[i]) == dict : log.append("dossier --- "+str(keys[i]))
					elif type(contents[i]) == str and contents[i] == "exe": log.append("executable --- "+str(keys[i]))
					elif type(contents[i]) == str and contents[i] == "mp3": log.append("musique --- "+str(keys[i]))
					elif type(contents[i]) == str and contents[i] == "mp4": log.append("video --- "+str(keys[i]))
					elif type(contents[i]) == str and contents[i] == "txt": log.append("texte --- "+str(keys[i]))
					ligne+=20
				printLog(log, _images)
				log, ligne = scrolling(log, ligne, _images, path)
			#cd \/
			elif input[0] == 'cd' and len(input)>1 :
				path, success = cd(path, input[1])
				if not success :
					log.append("Chemin inexistant")
					ligne+=20
					printLog(log, _images)
			#clear \/
			elif input[0] == 'clear' :
				log = []
				ligne = 270
				printLog(log, _images)
			#exit \/
			elif input[0] == 'exit' :
				log.append("")
				log.append("Username : 1 11 21 1211")
				ligne+=40
				path=""
				printLog(log, _images)
			#appli \/
			elif input[0] == "appli" :
				if input[1] == "jarvis":
					log = []
					ligne = 270
					appli, _continuer, isJarvisUsed = jarvis(_images)
					printLog(log, _images)
				else :
					log.append("Executable non trouvé")
					ligne+=20
					printLog(log, _images)
			#ouvrir des fichiers ou programmes depuis le path actuel \/
			else :
				items = goto(path).items()
				#pour rendre la recherche d'executable plus rapide (un peu useless à cette échelle) \/
				if input[0].find('.') != -1 :
					extension_de_l_input = input[0].split('.')
				else :
					extension_de_l_input = [None, None]
				for item in items :
					if extension_de_l_input[1] == "exe" and item[1] == "exe" : #si executable détecté
						if item[0] == "jarvis.exe" and input[0] == "jarvis.exe" : #lance jarvis
							log = []
							ligne = 270
							appli, _continuer, isJarvisUsed = jarvis(_images)
						elif item[0] == "reinitialiser.exe" and input[0] == "reinitialiser.exe" : #lance réinitialiser
							reinitialiser()
						else : #message d'erreur
							log.append("Executable non trouvé") 
							ligne+=20
							printLog(log, _images)
							break
					else : #message d'erreur
						if extension_de_l_input[1] == "exe" :
							log.append("Executable non trouvé")
						else :
							log.append("Commande inexistante")
							log.append("Une application sera bientôt disponible pour vous fournir de l'aide")
						ligne+=40
						printLog(log, _images)
						break
						
			screen.blit(terminalFont.render(path+" > ", True, (0, 175, 0)), (125,ligne))
			pygame.display.flip()
			input = None
			log, ligne = scrolling(log, ligne, _images, path)

	return _images, _continuer, path, log, ligne, text, isJarvisUsed

def jarvis(_images) :
	"""Progamme qui tourne dans le terminal, assistant IA du hacker"""
	#Se référer aux déclarations de variables de Terminal pour comprendre celles-ci
	log = []
	ligne = 270
	dialogues = [ #pour chaque tuple 't' de la liste : 
				  #t[0] => Messages de l'IA  |  t[1] => tuple contenants les réponses disponibles si t[2] = "qcm"  |  t[2] => type de réponse attendue
		("Bonjour ddOS, que puis-je faire pour vous ?", ("  1 - Je veux les codes", "  2 - Rien du tout, au revoir"), "qcm"),
		("Pour récupérer les codes, veuillez répondre aux questions de sécurité", ("  1 - Oui", "  2 - Non"), "qcm"),
		("Première question : Quel est le nom de votre premier animal de compagnie ?", (), "text"),
		("Deuxième question : Quelle a été l'école dans laquelle vous avez étudié ?", (), "text"),
		("Troisième question : Quelle est la date de création de Jarvis ?", (), "text"),
		("Quatrième question : Quelle est votre musique préférée", (), "text"),
		("Cinquième question : Quel votre fruit préféré ?", (), "text"),
		("Sixième question : Où étiez-vous durant les dernières vacances ?", (), "text"),
		("Septième question : Quelle était votre dernière profession ?", (), "text"),
		("Questions de sécurités répondues, voici le code n°1 : 489a6282A", ("  1 - Merci !", "  2 - Au revoir"), "qcm")
	]
	answer = "Réponse n°"
	text = ""
	input = None
	output = False
	appli = True
	_continuer = True

	#Affiche le premier dialogue \/
	current_dialogue = 0
	log, ligne = printDialogue(log, ligne, dialogues[current_dialogue])
	printLog(log, _images)
	screen.blit(terminalFont.render(answer+" > "+text, True, (0, 175, 0)), (125,ligne))
	pygame.display.flip()

	while appli :
		#Attente des événements
		for event in pygame.event.get():
			if event.type == QUIT:
				_continuer = False
				appli = False
			elif event.type == MOUSEBUTTONDOWN:
				if event.pos[0]>iconterminal_coords[0] and event.pos[0]<iconterminal_coords[0]+iconterminal_dim[0] and event.pos[1]>iconterminal_coords[1] and event.pos[1]<iconterminal_coords[1]+iconterminal_dim[1] and event.button == 1 : #Si clic sur icon (zone de clic définie par la position et taille de celui-ci)
					#Clic sur gauche sur "terminal" => quitte l'appli
					_images = render(_images, (fen_terminal, fen_terminal_coords))
					appli=False
					return False, _continuer, True
				elif event.pos[0]>iconmessage_coords[0] and event.pos[0]<iconmessage_coords[0]+iconmessage_dim[0] and event.pos[1]>iconmessage_coords[1] and event.pos[1]<iconmessage_coords[1]+iconmessage_dim[1] and event.button == 1 : #Si clic sur icon2 (zone de clic définie par la position et taille de celui-ci)
					#Clic gauche sur "message" => quitte l'appli vers message
					_images = render(_images, (fen_message, fen_message_coords))
					appli=False
					return False, _continuer, True
				elif event.pos[0]>1205 and event.pos[0]<1225 and event.pos[1]>989 and event.pos[1]<1010 and event.button == 1 :
					#Clic gauche sur la croix en bas à droite  => quitte le jeu
					_continuer = False
					return False, _continuer, True
					
			#Pour écrire dans le terminal
			elif event.type == KEYDOWN:
				if event.key == K_RETURN: #Si entrée appuyée
					input = text #Récupérer la valeur entrée
					log.append(answer+" > "+text) #ajout de la ligne dans log
					log, ligne = scrolling(log, ligne, _images, answer) #scroll si nécessaire
					printLog(log, _images)
					text = '' #reset le champ d'entrée
					ligne+=20
				elif event.key == K_BACKSPACE: #Si retour appuyé
					text = text[:-1] #supprime dernier charactère
					#Affichage \/
					printLog(log, _images)
					screen.blit(terminalFont.render(answer+" > "+text, True, (0, 175, 0)), (125,ligne))
					pygame.display.flip()
				else: #sinon
					if len(answer+" > "+text)<80 : #si la ligne ne dépasse pas la longueur maximale du terminal
						text += event.unicode #ajouter le charactère associé à la touche appuyée au champ d'entrée
					#Affichage \/
					printLog(log, _images)
					screen.blit(terminalFont.render(answer+" > "+text, True, (0, 175, 0)), (125,ligne))
					pygame.display.flip()
			
		#Tests des réponses
		if input != None :
			if current_dialogue == 0 : #Si dialogue 1 "Que puis-je faire pour vous ?"
				if input == "1" :
					current_dialogue += 1
					output = True
				elif input == "2" :
					return True, True, False
				else : 
					output = False
			elif current_dialogue == 1 : #Si dialogue 2 "Veuillez répoondre aux question de sécurité"
				if input == "1" :
					current_dialogue += 1
					output = True
				elif input == "2" :
					current_dialogue -= 1
					output = True
				else :
					output = False
			elif current_dialogue == 2 : #Si dialogue 3 "Premier animal de compagnie"
				if input == "Glad0s" :
					current_dialogue += 1
					output = True
				elif input == "back" :
					current_dialogue = 1
					output = True
				else : 
					output = False
			elif current_dialogue == 3 : #Si dialogue 4 "École"
				if input == "École 42" or input == "école 42" or input == "42" :
					current_dialogue += 1
					output = True
				elif input == "back" :
					current_dialogue = 1
					output = True
				else : 
					output = False
			elif current_dialogue == 4 : #Si dialogue 5 "Création de Jarvis"
				if input == "9 janvier 2020" or input == "9/01/2020" or input == "09/01/2020" :
					current_dialogue += 1
					output = True
				elif input == "back" :
					current_dialogue = 1
					output = True
				else : 
					output = False
			elif current_dialogue == 5 : #Si dialogue 6 "Musique préférée"
				if input == "Black Catcher" or input == "black catcher" or input == "Black catcher" :
					current_dialogue += 1
					output = True
				elif input == "back" :
					current_dialogue = 1
					output = True
				else : 
					output = False
			elif current_dialogue == 6 : #Si dialogue 7 "Fruit préféré"
				if input == "Durian" or input == "durian" or input == "DURIAN" :
					current_dialogue += 1
					output = True
				elif input == "back" :
					current_dialogue = 1
					output = True
				else : 
					output = False
			elif current_dialogue == 7 : #Si dialogue 8 "Dernières vacances"
				if input == "Brest" or input == "brest" or input == "BREST" :
					current_dialogue += 1
					output = True
				elif input == "back" :
					current_dialogue = 1
					output = True
				else : 
					output = False
			elif current_dialogue == 8 : #Si dialogue 9 "Ancienne profession"
				if input == "Concierge" or input == "concierge" :
					current_dialogue += 1
					output = True
				elif input == "back" :
					current_dialogue = 1
					output = True
				else : 
					output = False
			elif current_dialogue == 9 : #Si dialogue 10 "Voilà le code"
				if input == "1" :
					current_dialogue = 0
					output = True
				elif input == "2" :
					return True, True, False
				else :
					output = False

			#Pour avoir le bon texte de demande de réponse
			if dialogues[current_dialogue][2] == "qcm" :
				answer = "Réponse n°"
			elif dialogues[current_dialogue][2] == "text" :
				answer = "Réponse libre"

			#Si output = True alors afficher la question entière
			if output == True :
				log.append("")
				ligne+=20
				log, ligne = printDialogue(log, ligne, dialogues[current_dialogue])
				log, ligne = scrolling(log, ligne, _images, answer)
				printLog(log, _images)
				screen.blit(terminalFont.render(answer+" > "+text, True, (0, 175, 0)), (125,ligne))
				pygame.display.flip()
				output = False
			else : #Sinon afficher juste la ligne
				if dialogues[current_dialogue][2] == "qcm" :
					log.append("Réponse invalide, veuillez entrer un des chiffres proposés")
					ligne+=20
				elif dialogues[current_dialogue][2] == "text" :
					log.append("Réponse invalide")
					ligne+=20
				printLog(log, _images)
				screen.blit(terminalFont.render(answer+" > "+text, True, (0, 175, 0)), (125,ligne))
				pygame.display.flip()

			input = None
					
	return True, _continuer, False

def reinitialiser() :
	"""Progamme qui tourne dans le terminal, permet de reinitialiser le PC du hacker (nécessite les 5 codes)"""
	#WIP
	return

#=========================================================================#
#======================= VARIABLES ET INITALISATIONS =====================#
#=========================================================================#
pygame.init()
pygame.font.init()

#Polices
messageFont = pygame.font.SysFont('Arial', 30)
terminalFont = pygame.font.Font('img/SLC_.ttf', 23)

#Ouverture de la fenêtre Pygame
w = math.floor(pygame.display.Info().current_w/2-1280/2) #Calcule les coordonnées de la fenetre pygame en fonction de la taille de l'écran
os.environ['SDL_VIDEO_WINDOW_POS'] = str(w)+",0" #Applique les calculs précédent
screen_dim = (1280, 1024) #Taille de la fenetre
screen = pygame.display.set_mode(screen_dim, pygame.NOFRAME) #Ouvre la fenetre en borderless window

#Chargement du fond
background = pygame.image.load("img/desktop.png").convert()

#Chargement de l'icone du terminal
iconterminal = pygame.image.load("img/iconterminal.png").convert()
iconterminal_coords = (100,989)
iconterminal_dim = iconterminal.get_size()

#Chargement de l'icone des messages
iconmessage = pygame.image.load("img/iconmessage.png").convert()
iconmessage_coords = (150,989)
iconmessage_dim = iconmessage.get_size()
screen.blit(iconmessage, iconmessage_coords)

#Chargement de la fenêtre de terminal
fen_terminal = pygame.image.load("img/fen_terminal.png").convert()
fen_terminal_dim = fen_terminal.get_size()
fen_terminal_coords = ((screen_dim[0]-fen_terminal_dim[0])/2, (screen_dim[1]-fen_terminal_dim[1])/2)

#Chargement de la fenêtre de message
fen_message = pygame.image.load("img/fen_message.png").convert()
fen_message_dim = fen_message.get_size()
fen_message_coords = ((screen_dim[0]-fen_message_dim[0])/2, (screen_dim[1]-fen_message_dim[1])/2)


images = [(background, (0,0)), (iconterminal, iconterminal_coords), (iconmessage, iconmessage_coords)] #Prépare la liste pour l'affichage des éléments
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
				images = render(images, (fen_terminal, fen_terminal_coords))
			elif event.pos[0]>iconmessage_coords[0] and event.pos[0]<iconmessage_coords[0]+iconmessage_dim[0] and event.pos[1]>iconmessage_coords[1] and event.pos[1]<iconmessage_coords[1]+iconmessage_dim[1] and event.button == 1 : #Si clic sur icon2 (zone de clic définie par la position et taille de celui-ci)
				#Clic gauche sur icon2
				images = render(images, (fen_message, fen_message_coords))
			elif event.pos[0]>1205 and event.pos[0]<1225 and event.pos[1]>989 and event.pos[1]<1010 and event.button == 1 : #Si clic sur icon2 (zone de clic définie par la position et taille de celui-ci)
				#Clic gauche sur la croix en bas à droite
				continuer = False

	#Affichage du jeu (affichage des _imageses dans l'ordre + rafraichissement de l'écran)
	render(images, None)
	pygame.display.flip()
	#Appel des fonctions associés à l'application en premier plan
	if images[len(images)-1][0] == fen_terminal:
		images, continuer, g_path, g_log, g_ligne, g_text, g_isJarvisUsed = Terminal(images, g_path, g_log, g_ligne, g_text, g_isJarvisUsed)
	elif images[len(images)-1][0] == fen_message:
		images, continuer, messages = message(images, messages)

pygame.quit()