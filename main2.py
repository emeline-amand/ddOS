import pygame, os, math
from pygame.locals import *

#Pour l'appli terminal
files = {'C:':{'dossier1':{'réinitialiser.exe':"réinit", 'dossier2':{}},'dossier3':{'fichier2':2, 'dossier4':{'fichier3':3, 'fichier4':4}}}}
g_path = ""
g_log = []
g_log.append("Username : [insérer énigme]")
g_ligne = 290
g_text = ""

#Pour l'appli message
messages=[["de: Boss","Infos Hacker",["Voici le peu d'informations que nous avons trouvé sur le hacker,","Son mail: neo.mitrax@mymail.com, avec le mot de passe : ","a**0m*h*5* (les * sont les caractères que nous n'avons pas réussi à ","décrypter à l'heure actuelle, c'est à vous de les trouver) elles vous ","seront utiles tout le long de la partie. Nous savons  que le hacker est ","citoyen français. Il aurait fait l'École 42 fut deuxième de sa promo. ","Cependant ses études prirent un autre tour à la mort de son père ","le 28 octobre 1997. Il entreprit des études d'arquéologue à l'Université de ","Massachusetts. Il s'installa ensuite à Brest, cette profession lui aurait ","permis de mettre en place son activité de hacker. A ce jour, il a hacké ","plusieurs banques dans différents pays. ","Il représente un danger pour tous,d'où la rapidité dont vous devez ","disposer pour supprimer les codes nucléaires de son ordinateur."]],["de: Boss","Règles du jeu",["Bonjour Agent,","L'heure est grave, le célèbre hacker connu sous le nom de ddOS","s'est emparé d'importants fichiers nucléaires.","Votre mission, si toute fois vous l'acceptez, est de pénétrer dans le PC ","du hacker à distance, récupérer ses fichiers nucléaires et les ","supprimer de son PC. Pour se faire l'équipe s'est mobilisée pour ","maintenir le PC du hacker hors service depuis chez lui. Voici votre ","mail: christopher.wray@fbi.com et votre mot de passe: Ly46fZer ","pour vous connecter à votre messagerie lors de cette mission. ","Prenez soin de les noter sur une feuille: vous serez amené à vous ","déconnecter de votre compte plusieurs fois. Cette feuille vous servira ","également à noter toutes les informations et mots de passes que","vous trouvez: tout se réutilise! ","Bonne chance, la survie de l'humanité dépend de vous Agent Wray."]],["de: FBI","Vacances",["Vous n'avez pas pris de vacances depuis plusieurs mois Agent Wray, ","Songez-y."]],["de: FBI","année 2021",["Meilleurs voeux agent Wray! C'est un plaisir d'être à vos côtés ","une années de plus!"]],["de: Boss","Nouvelle équipe",["Agent Wray,","Vous voici affecté à une nouvelle équipe sous mon commandement. ","Je ne fais pas de doutes sur le fait que nous nous entendrons bien. ","Monsieur Decopmann m'a beaucoup parlé de vous en bien.","Bienvenue dans l'équipe 007"]]]

g_compte=1


def render(toBlit, firstPlan) :
	"""Fonction qui affiche les images spécfiée dans la liste de tuple en param2 dans l'ordre croissant des indices de la liste, sauf l'_imagese spécifiée dans le tuple en param1, qui sera affiché en premier plan"""
	#Si l'_imagese à mettre en 1er plan l'est déjà
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
	for _image in toBlit:
		screen.blit(_image[0], _image[1])
	return toBlit

#=========================================================================#
#================================= MESSAGE ===============================#
#=========================================================================#

def message(_images, _messages, g_compte) :
	"""permet d'afficher les messages sur une fenetre en séparant l'émetteur du message et son objet"""
	appli = True
	_continuer = True
	text=""
	champ=[]
	lignex=529
	ligney=400
	x=529
	y=400
	lignereturny=400
	countreturn=0
	epaisseurchamp1=4
	epaisseurchamp2=2
	photo=0
	
	messagesHacker=[["de: Mamie","Dernières vacances",["Coucou mon chéri, ","Comment vas-tu? ","Je sais que ton métier de concierge te prends beaucoup de temps. ","Je t'envoie donc un petit mail pour te remercier d'être allé à Brest ","avec moi durant ses dernières vacances. Cela m'a beaucoup touché ","que tu prennes du temps avec ta vieille mamie. Ne t'inquiètes ","pas pour ton chat Glad0s, je prends soin de lui, il va très bien et se ","plaît beaucoup ici! J'ai pris soin de t'envoyer un colis avec une ","douzaine de durian que j'ai trouvé ce matin au marché du village, ","tu les aimes tant! C'est dans ce marché de Brest que se trouve les ","fruits les plus exotiques! De quoi te faire voyager depuis chez toi :)","Je t'embrasse, ","","Ta Mamie "]],["de: DUVAL Jacques","Ampoules grillées",["Bonjour Monsieur le concierge","Les ampoules du couloir au troisième étage sont cassées. ","Veuillez appeler un électricien.","","Bien Cordialement,","DUVAL Jacques, trosième étage du bâtiment 2"]],["de: CASTORAMA","Votre livraison est en route!",["Nous vous informons que votre commande est en route!","Vous devriez la recevoir dans les jours suivants, merci d'avoir choisi ","Castorama!","","Votre cagnotte fidélité bénéficie de 200 points supplémentaires.","","Détails de la commande:","Tuyau pvc Compact Ø100 mm L.2 m x5","Enduit de façade rénovation chaux ton pierre 25 kg x2","Elagueuse sur perche électrique FPPS710 710w 18cm"]],["de: moi","ASCII",[]]]
	
	#on regarde sur quelle messagerie on se trouve: 1=agent; 2=hacker; 3=fenetre de connection
	if g_compte == 1:
		
		#par défaut on est sur la messagerie de l'agent
		utilisateur="Agent"
		
		
		#variable pour que les inputs soient seulement fonctionnels quand on est sur la page de connection
		deconnection = 0
	
		#mise en page de la messagerie
		y=250
		pygame.draw.line(screen,(0,0,0), (340, y), (1130, y), 2)
		pygame.draw.line(screen,(0,0,0), (340, 210), (340, 850), 2)
		screen.blit(messageFontpetit.render("Vous êtes connecté en  ",True,(0,0,0)),(160,222))
		screen.blit(messageFontpetit.render("tant que:"+ utilisateur,True,(0,0,0)),(160,240))
		screen.blit(messageFontpetit.render("déconnection ",True,(0,0,0)),(160,800))
		screen.blit(messageFont.render("émetteur: ",True,(0,0,0)),(350,212))
		screen.blit(messageFont.render("objet: ",True,(0,0,0)),(600,212))
	
	
		for i in range (len(_messages)):
			#on fait afficher l'émetteur des messages
			screen.blit(messageFont.render(_messages[i][0],True,(0,0,0)),(350,y))
			_messages[i].append(y-30)
	
			#on fait afficher l'objet des messages
			screen.blit(messageFont.render(_messages[i][1],True,(0,0,0)),(600,y))
			_messages[i].append(y-30)
	
			#on fait afficher ligne de séparation
			y+=40
			pygame.draw.line(screen,(0,0,0),(340, y),(1130, y), 2)
	
	
		pygame.display.flip()
		#on fait afficher séparation entre chaque lignes

	elif g_compte == 2:
		
		utilisateur= "Hacker"
		
		#variable pour que les inputs soient seulement fonctionnels quand on est sur la page de connection
		deconnection = 0

		#on affiche les mails et autres éléments de la messagerie.
		y=250
		pygame.draw.line(screen,(0,0,0), (340,250), (1130, 250), 2)
		pygame.draw.line(screen,(0,0,0), (340, 210), (340, 850), 2)
		screen.blit(messageFontpetit.render("Vous êtes connecté en  ",True,(0,0,0)),(160,222))
		screen.blit(messageFontpetit.render("tant que:"+ utilisateur,True,(0,0,0)),(160,240))
		screen.blit(messageFontpetit.render("déconnection ",True,(0,0,0)),(160,800))
		screen.blit(messageFont.render("émetteur: ",True,(0,0,0)),(350,212))
		screen.blit(messageFont.render("objet: ",True,(0,0,0)),(600,212))
		
		for i in range (len(messagesHacker)):
			#on fait afficher l'émetteur des messages
			screen.blit(messageFont.render(messagesHacker[i][0],True,(0,0,0)),(350,y))
			messagesHacker[i].append(y-30)
	
			#on fait afficher l'objet des messages
			screen.blit(messageFont.render(messagesHacker[i][1],True,(0,0,0)),(600,y))
			messagesHacker[i].append(y-30)
	
			#on fait afficher ligne de séparation
			y+=40
			pygame.draw.line(screen,(0,0,0),(340, y),(1130, y), 2)
	
	
		pygame.display.flip()
		
	elif g_compte == 3:
		
		screen.blit(messageFont.render("CONNECTER UN COMPTE",True,(0,0,0)),(430,300))
		screen.blit(messageFont.render("insérer votre mail: ",True,(0,0,0)),(325,400))
		pygame.draw.rect(screen,(0,0,0),(525,400,300,40),epaisseurchamp1)
		screen.blit(messageFont.render("insérer votre mot de passe: ",True,(0,0,0)),(220,500))
		pygame.draw.rect(screen,(0,0,0),(525,500,300,40),epaisseurchamp2)
		pygame.display.flip()
		deconnection = 2
		


	#truc commun à toutes les applis
	while appli :
		for event in pygame.event.get(): #Attente des événements
			if event.type == QUIT:
				_continuer = False
				appli = False
			elif event.type == MOUSEBUTTONDOWN:
				y=250
				for i in range (len(_messages)):
					#on regarde la position de la souris
					if 350<event.pos[0]<800 and y<event.pos[1]<y+40 and deconnection==0 :
						
						if g_compte==1:
						
							#efface texte à l'écran
							render(_images, None)
	
							#affiche texte à l'écran, precisez coordonnées
							#screen.blit(messageFont.render(_messages[i][2],True,(0,0,0)),(350,310))
							y2 = 250
							for ligne in messages[i][2]:
								screen.blit(messageFont.render(ligne,True,(0,0,0)),(350,y2))
								y2+=40
							pygame.draw.line(screen,(0,0,0), (340, 210), (340, 850), 2)
							screen.blit(messageFontpetit.render("Vous êtes connecté en  ",True,(0,0,0)),(160,222))
							screen.blit(messageFontpetit.render("tant que:"+ utilisateur,True,(0,0,0)),(160,240))
							screen.blit(messageFontpetit.render("Boîte principale",True,(0,0,0)),(160,350))
							screen.blit(messageFontpetit.render("déconnection ",True,(0,0,0)),(160,800))
							deconnection=1
	
							#refresh écran
							pygame.display.flip()
						
					
						if g_compte==2:
							if 350<event.pos[0]<800 and 370<event.pos[1]<410:#message intitulé binaire qui comprend une photo
								#on met en premier plan l'image contenant la photo
								render(_images, (peinture, peinture_coords))
								
								pygame.draw.line(screen,(0,0,0), (340, 210), (340, 850), 2)
								screen.blit(messageFontpetit.render("Vous êtes connecté en  ",True,(0,0,0)),(160,222))
								screen.blit(messageFontpetit.render("tant que:"+ utilisateur,True,(0,0,0)),(160,240))
								screen.blit(messageFontpetit.render("Boîte principale",True,(0,0,0)),(160,350))
								screen.blit(messageFontpetit.render("déconnection ",True,(0,0,0)),(160,800))
								deconnection=1
								photo=1
		
								#refresh écran
								pygame.display.flip()
								
							else:
									
								#efface texte à l'écran
								render(_images, None)
		
								#affiche texte à l'écran, precisez coordonnées
								y2 = 250
								for ligne in messagesHacker[i][2]:
									screen.blit(messageFont.render(ligne,True,(0,0,0)),(350,y2))
									y2+=40
								pygame.draw.line(screen,(0,0,0), (340, 210), (340, 850), 2)
								screen.blit(messageFontpetit.render("Vous êtes connecté en  ",True,(0,0,0)),(160,222))
								screen.blit(messageFontpetit.render("tant que:"+ utilisateur,True,(0,0,0)),(160,240))
								screen.blit(messageFontpetit.render("Boîte principale",True,(0,0,0)),(160,350))
								screen.blit(messageFontpetit.render("déconnection ",True,(0,0,0)),(160,800))
								deconnection=1
								photo=0
		
								#refresh écran
								pygame.display.flip()
						
					y+=40
					
					
				#touche boite principale qui permet de revenir à la liste des mails
				if 160<event.pos[0]<270 and 350<event.pos[1]<390:
					deconnection=0
					if g_compte==1 :
						render(_images, None)
						y=250
						pygame.draw.line(screen,(0,0,0), (340, y), (1130, y), 2)
						pygame.draw.line(screen,(0,0,0), (340, 210), (340, 850), 2)
						screen.blit(messageFontpetit.render("Vous êtes connecté en  ",True,(0,0,0)),(160,222))
						screen.blit(messageFontpetit.render("tant que:"+ utilisateur,True,(0,0,0)),(160,240))
						screen.blit(messageFontpetit.render("déconnection ",True,(0,0,0)),(160,800))
						screen.blit(messageFont.render("émetteur: ",True,(0,0,0)),(350,212))
						screen.blit(messageFont.render("objet: ",True,(0,0,0)),(600,212))
	
						for i in range (len(_messages)):
						#on fait afficher l'émetteur des messages
							screen.blit(messageFont.render(_messages[i][0],True,(0,0,0)),(350,y))
							_messages[i].append(y-30)
							#on fait afficher l'objet des messages
							screen.blit(messageFont.render(_messages[i][1],True,(0,0,0)),(600,y))
							_messages[i].append(y-30)
							y+=40
							#on fait afficher ligne de séparation
							pygame.draw.line(screen,(0,0,0),(340, y),(1130, y), 2)
						pygame.display.flip()
						
					if g_compte==2 :
						if photo==1:
							del _images[4]						
							render(_images, None)
							y=250
							pygame.draw.line(screen,(0,0,0), (340, y), (1130, y), 2)
							pygame.draw.line(screen,(0,0,0), (340, 210), (340, 850), 2)
							screen.blit(messageFontpetit.render("Vous êtes connecté en  ",True,(0,0,0)),(160,222))
							screen.blit(messageFontpetit.render("tant que:"+ utilisateur,True,(0,0,0)),(160,240))
							screen.blit(messageFontpetit.render("déconnection ",True,(0,0,0)),(160,800))
							screen.blit(messageFont.render("émetteur: ",True,(0,0,0)),(350,212))
							screen.blit(messageFont.render("objet: ",True,(0,0,0)),(600,212))
		
							for i in range (len(messagesHacker)):
							#on fait afficher l'émetteur des messages
								screen.blit(messageFont.render(messagesHacker[i][0],True,(0,0,0)),(350,y))
								messagesHacker[i].append(y-30)
								#on fait afficher l'objet des messages
								screen.blit(messageFont.render(messagesHacker[i][1],True,(0,0,0)),(600,y))
								messagesHacker[i].append(y-30)
								y+=40
								#on fait afficher ligne de séparation
								pygame.draw.line(screen,(0,0,0),(340, y),(1130, y), 2)
								
						else:
							render(_images, None)
							y=250
							pygame.draw.line(screen,(0,0,0), (340, y), (1130, y), 2)
							pygame.draw.line(screen,(0,0,0), (340, 210), (340, 850), 2)
							screen.blit(messageFontpetit.render("Vous êtes connecté en  ",True,(0,0,0)),(160,222))
							screen.blit(messageFontpetit.render("tant que:"+ utilisateur,True,(0,0,0)),(160,240))
							screen.blit(messageFontpetit.render("déconnection ",True,(0,0,0)),(160,800))
							screen.blit(messageFont.render("émetteur: ",True,(0,0,0)),(350,212))
							screen.blit(messageFont.render("objet: ",True,(0,0,0)),(600,212))
		
							for i in range (len(messagesHacker)):
							#on fait afficher l'émetteur des messages
								screen.blit(messageFont.render(messagesHacker[i][0],True,(0,0,0)),(350,y))
								messagesHacker[i].append(y-30)
								#on fait afficher l'objet des messages
								screen.blit(messageFont.render(messagesHacker[i][1],True,(0,0,0)),(600,y))
								messagesHacker[i].append(y-30)
								y+=40
								#on fait afficher ligne de séparation
								pygame.draw.line(screen,(0,0,0),(340, y),(1130, y), 2)
						
						pygame.display.flip()
							
						
							
						

				#pour se déconnecter du compte de la messagerie, avec confirmation
				if 160<event.pos[0]<270 and 700<event.pos[1]<850 and deconnection == 0:
					render(_images, None)
					screen.blit(messageFont.render("Confirmer la déconnection: ",True,(0,0,0)),(425,400))
					screen.blit(messageFont.render("oui ",True,(0,0,0)),(400,500))
					screen.blit(messageFont.render("non ",True,(0,0,0)),(700,500))
					pygame.display.flip()
					deconnection=1
					
				#Si touche cliquée est non, alors retour a la boite principale de la messagerie PAS SURE
				if 700<event.pos[0]<740 and 500<event.pos[1]<550 and deconnection == 1 :
					render(_images, None)
					deconnection=0
					y=250
					pygame.draw.line(screen,(0,0,0), (340, y), (1130, y), 2)
					pygame.draw.line(screen,(0,0,0), (340, 210), (340, 850), 2)
					screen.blit(messageFontpetit.render("Vous êtes connecté en  ",True,(0,0,0)),(160,222))
					screen.blit(messageFontpetit.render("tant que:"+ utilisateur,True,(0,0,0)),(160,240))
					screen.blit(messageFontpetit.render("déconnection ",True,(0,0,0)),(160,800))
					screen.blit(messageFont.render("émetteur: ",True,(0,0,0)),(350,212))
					screen.blit(messageFont.render("objet: ",True,(0,0,0)),(600,212))
					deconnection = 0

					for i in range (len(_messages)):
					#on fait afficher l'émetteur des messages
						screen.blit(messageFont.render(_messages[i][0],True,(0,0,0)),(350,y))
						_messages[i].append(y-30)
						#on fait afficher l'objet des messages
						screen.blit(messageFont.render(_messages[i][1],True,(0,0,0)),(600,y))
						_messages[i].append(y-30)
						y+=40
						#on fait afficher ligne de séparation
						pygame.draw.line(screen,(0,0,0),(340, y),(1130, y), 2)
					pygame.display.flip()
					

				#login de la messagerie (par défaut ON EST SUR MESSAGERIE AGENT)
				if 400<event.pos[0]<440 and 500<event.pos[1]<540 and deconnection == 1:
					g_compte=3
					render(_images, None)
					screen.blit(messageFont.render("CONNECTER UN COMPTE",True,(0,0,0)),(430,300))
					screen.blit(messageFont.render("insérer votre mail: ",True,(0,0,0)),(325,400))
					pygame.draw.rect(screen,(0,0,0),(525,400,300,40),epaisseurchamp1)
					screen.blit(messageFont.render("insérer votre mot de passe: ",True,(0,0,0)),(220,500))
					pygame.draw.rect(screen,(0,0,0),(525,500,300,40),epaisseurchamp2)
					pygame.display.flip()
					deconnection = 2




				#quitter l'appli
				if event.pos[0]>iconterminal_coords[0] and event.pos[0]<iconterminal_coords[0]+iconterminal_dim[0] and event.pos[1]>iconterminal_coords[1] and event.pos[1]<iconterminal_coords[1]+iconterminal_dim[1] and event.button == 1 : #Si clic sur icon (zone de clic définie par la position et taille de celui-ci)
					#Clic sur gauche sur "icon"
					_images = render(_images, (fen_terminal, fen_terminal_coords))
					appli=False
				elif event.pos[0]>iconmessage_coords[0] and event.pos[0]<iconmessage_coords[0]+iconmessage_dim[0] and event.pos[1]>iconmessage_coords[1] and event.pos[1]<iconmessage_coords[1]+iconmessage_dim[1] and event.button == 1 : #Si clic sur icon2 (zone de clic définie par la position et taille de celui-ci)
					#Clic gauche sur icon2
					_images = render(_images, (fen_message, fen_message_coords))
					appli=False


			#Pour pouvoir écrire son id et son pwd

			if event.type == KEYDOWN and deconnection == 2 :
				

				#lorsqu'on appuie sur la touche retour:
				if event.key == K_RETURN:#Si entrée appuyée
					countreturn+=1
					
					
						
					if countreturn==1:
						input = text #Récupérer la valeur entrée
						champ.append(text)
						lignechampy=400
						epaisseurchamp1=2
						epaisseurchamp2=4
	
	
						#---------------------------------------#
						#laisse le text écrit précédemment à l'écran:
						render(_images, None)
						for line in champ:
							screen.blit(messageFont.render(line, True, (0, 0, 0)), (lignex,lignechampy))
							lignechampy+=100
	
						#---------------------------------------#
	
						text = '' #reinitialiser le champ d'entrée
						#affichage a l'écran
						screen.blit(messageFont.render("", True, (0, 0, 0)), (lignex,lignereturny))
						screen.blit(messageFont.render("CONNECTER UN COMPTE",True,(0,0,0)),(430,300))
						screen.blit(messageFont.render("insérer votre mail: ",True,(0,0,0)),(325,400))
						pygame.draw.rect(screen,(0,0,0),(525,400,300,40),epaisseurchamp1)
						screen.blit(messageFont.render("insérer votre mot de passe: ",True,(0,0,0)),(220,500))
						pygame.draw.rect(screen,(0,0,0),(525,500,300,40),epaisseurchamp2)
	
						lignex+=0
						lignereturny+=100
						pygame.display.flip()
					#si on a appuyé plus de deux fois sur la touche retour, on efface tout les inputs rentrés à l'écran; le texte écrit sera ensuite placé au niveau de la case insérer votre mail.

						
					if countreturn==2:
						countreturn=0
						champ.append(text)
						lignereturny=400
						epaisseurchamp1=4
						epaisseurchamp2=2
						
						#on regarde si le mail et pwd correspond à celui du hacker
						if champ[0]=="neo.mitrax@mymail.com" and champ[1]=="adf0mh456":
							#on efface texte écrit a l'écran
							render(_images, None)
							utilisateur= "Hacker"
							g_compte=2

							#on affiche les mails(pour l'instant pas de mails) et autres éléments de la messagerie.
							pygame.draw.line(screen,(0,0,0), (340,250), (1130, 250), 2)
							pygame.draw.line(screen,(0,0,0), (340, 210), (340, 850), 2)
							screen.blit(messageFontpetit.render("Vous êtes connecté en  ",True,(0,0,0)),(160,222))
							screen.blit(messageFontpetit.render("tant que:"+ utilisateur,True,(0,0,0)),(160,240))
							screen.blit(messageFontpetit.render("déconnection ",True,(0,0,0)),(160,800))
							screen.blit(messageFont.render("émetteur: ",True,(0,0,0)),(350,212))
							screen.blit(messageFont.render("objet: ",True,(0,0,0)),(600,212))
							y=250
							for i in range (len(messagesHacker)):
							#on fait afficher l'émetteur des messages
								screen.blit(messageFont.render(messagesHacker[i][0],True,(0,0,0)),(350,y))
								messagesHacker[i].append(y-30)
								#on fait afficher l'objet des messages
								screen.blit(messageFont.render(messagesHacker[i][1],True,(0,0,0)),(600,y))
								messagesHacker[i].append(y-30)
								y+=40
								#on fait afficher ligne de séparation
								pygame.draw.line(screen,(0,0,0),(340, y),(1130, y), 2)
							pygame.display.flip()
							champ=[]
							text = ""
							deconnection=0

						#si id et pwd correspondent aux id et pwd de l'agent, on arrive sur la boite mail de l'agent
						elif champ[0]=="christopher.wray@fbi.com" and champ[1]=="Ly46fZer":
							#on efface texte écrit a l'écran
							render(_images, None)
							utilisateur="Agent"
							g_compte=1

							#on affiche les mails et autres éléments de la messagerie.
							pygame.draw.line(screen,(0,0,0), (340, y), (1130, y), 2)
							pygame.draw.line(screen,(0,0,0), (340, 210), (340, 850), 2)
							screen.blit(messageFontpetit.render("Vous êtes connecté en  ",True,(0,0,0)),(160,222))
							screen.blit(messageFontpetit.render("tant que:"+ utilisateur,True,(0,0,0)),(160,240))
							screen.blit(messageFontpetit.render("déconnection ",True,(0,0,0)),(160,800))
							screen.blit(messageFont.render("émetteur: ",True,(0,0,0)),(350,212))
							screen.blit(messageFont.render("objet: ",True,(0,0,0)),(600,212))
							champ=[]
							text = ""
							y=250
							for i in range (len(_messages)):
							#on fait afficher l'émetteur des messages
								screen.blit(messageFont.render(_messages[i][0],True,(0,0,0)),(350,y))
								_messages[i].append(y-30)
								#on fait afficher l'objet des messages
								screen.blit(messageFont.render(_messages[i][1],True,(0,0,0)),(600,y))
								_messages[i].append(y-30)
								y+=40
								#on fait afficher ligne de séparation
								pygame.draw.line(screen,(0,0,0),(340, y),(1130, y), 2)
							pygame.display.flip()
							deconnection=0
							
						else:
							epaisseurchamp1=4
							epaisseurchamp2=2
							render(_images, None)
							screen.blit(messageFont.render("CONNECTER UN COMPTE",True,(0,0,0)),(430,300))
							screen.blit(messageFont.render("insérer votre mail: ",True,(0,0,0)),(325,400))
							pygame.draw.rect(screen,(0,0,0),(525,400,300,40),epaisseurchamp1)
							screen.blit(messageFont.render("insérer votre mot de passe: ",True,(0,0,0)),(220,500))
							pygame.draw.rect(screen,(0,0,0),(525,500,300,40),epaisseurchamp2)
							pygame.display.flip()
							champ=[]
							text = ""
							
							screen.blit(messageFont.render("mail et mot de passe invalides",True,(0,0,0)),(355,600))

					pygame.display.flip()
					
				#pour supprimer un caractère	
				elif event.key == K_BACKSPACE:
					text = text[:-1]
					render(_images, None)
					if countreturn==1:
						screen.blit(messageFont.render(champ[0], True, (0, 0, 0)), (lignex,400))
						screen.blit(messageFont.render(text, True, (0, 0, 0)), (lignex,lignereturny))
						screen.blit(messageFont.render("CONNECTER UN COMPTE",True,(0,0,0)),(430,300))
						screen.blit(messageFont.render("insérer votre mail: ",True,(0,0,0)),(325,400))
						pygame.draw.rect(screen,(0,0,0),(525,400,300,40),epaisseurchamp1)
						screen.blit(messageFont.render("insérer votre mot de passe: ",True,(0,0,0)),(220,500))
						pygame.draw.rect(screen,(0,0,0),(525,500,300,40),epaisseurchamp2)
	
						pygame.display.flip()
						
					else:
						
						screen.blit(messageFont.render(text, True, (0, 0, 0)), (lignex,lignereturny))
						screen.blit(messageFont.render("CONNECTER UN COMPTE",True,(0,0,0)),(430,300))
						screen.blit(messageFont.render("insérer votre mail: ",True,(0,0,0)),(325,400))
						pygame.draw.rect(screen,(0,0,0),(525,400,300,40),epaisseurchamp1)
						screen.blit(messageFont.render("insérer votre mot de passe: ",True,(0,0,0)),(220,500))
						pygame.draw.rect(screen,(0,0,0),(525,500,300,40),epaisseurchamp2)
	
						pygame.display.flip()
					
				#sinon dans les autres cas:
				else: #sinon
					if len(text)<25 : #si la ligne ne dépasse pas la longueur maximale 
						text += event.unicode #ajouter le caractère associé à la touche appuyée au champ d'entrée
					#Affichage /

					render(_images, None)

					#---------------------------------------#
					#laisse le text écrit précédemment à l'écran:
					render(_images, None)
					for line in champ:
						screen.blit(messageFont.render(line, True, (0, 0, 0)), (lignex,ligney))

					pygame.display.flip()
					#---------------------------------------#
					#affichage à l'écran
					screen.blit(messageFont.render(text, True, (0, 0, 0)), (lignex,lignereturny))
					screen.blit(messageFont.render("CONNECTER UN COMPTE",True,(0,0,0)),(430,300))
					screen.blit(messageFont.render("insérer votre mail: ",True,(0,0,0)),(325,400))
					pygame.draw.rect(screen,(0,0,0),(525,400,300,40),epaisseurchamp1)
					screen.blit(messageFont.render("insérer votre mot de passe: ",True,(0,0,0)),(220,500))
					pygame.draw.rect(screen,(0,0,0),(525,500,300,40),epaisseurchamp2)

					pygame.display.flip()




	return _images, _continuer, _messages, g_compte

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
					_images = render(_images, (fen_terminal, fen_terminal_coords))
					appli=False
				elif event.pos[0]>iconmessage_coords[0] and event.pos[0]<iconmessage_coords[0]+iconmessage_dim[0] and event.pos[1]>iconmessage_coords[1] and event.pos[1]<iconmessage_coords[1]+iconmessage_dim[1] and event.button == 1 : #Si clic sur icon2 (zone de clic définie par la position et taille de celui-ci)
					#Clic gauche sur icon2
					_images = render(_images, (fen_message, fen_message_coords))
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
							_images = render(_images, (fen_terminal, fen_terminal_coords))
							appli=False
							firstBoucle = False
							break
						elif event.pos[0]>iconmessage_coords[0] and event.pos[0]<iconmessage_coords[0]+iconmessage_dim[0] and event.pos[1]>iconmessage_coords[1] and event.pos[1]<iconmessage_coords[1]+iconmessage_dim[1] and event.button == 1 : #Si clic sur icon2 (zone de clic définie par la position et taille de celui-ci)
							#Clic gauche sur icon2
							_images = render(_images, (fen_message, fen_message_coords))
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



#Chargement popup
def popup(_popup, _info,_images):
	render(_images,None)
	appli=True
	y=780

	#on affiche le message du popup a l'écran
	for i in range (5):
		screen.blit(messageFontpetit.render(_info[i][0],True,(0,0,0)),(1000,y))
		y=y+20
	pygame.display.flip()


	while appli:
		for event in pygame.event.get(): #Attente des événements
			if event.type == QUIT:
				_continuer = False
				appli = False

			#pour fermer le popup
			elif event.type == MOUSEBUTTONDOWN:
				if 1000<event.pos[0]<1090 and 860<event.pos[1]<880:
					_images = render(_images,(iconpopup,iconpopup_coords) )
					appli=False
					pygame.display.flip()

	return _images, _popup

#=========================================================================#
#======================= VARIABLES ET INITALISATIONS =====================#
#=========================================================================#
pygame.init()
pygame.font.init()

#Polices
messageFont = pygame.font.SysFont('Arial', 30)
messageFontpetit = pygame.font.SysFont('Arial', 20)
terminalFont = pygame.font.Font('img/SLC_.ttf', 23)


#Ouverture de la fenêtre Pygame
#w = math.floor(pygame.display.Info().current_w/2-1280/2) #Calcule les coordonnées de la fenetre pygame en fonction de la taille de l'écran
#os.environ['SDL_VIDEO_WINDOW_POS'] = str(w)+",-10" #Applique les calculs précédent
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

#Chargement de la case popup
iconpopup = pygame.image.load("img/blanc.jfif").convert()
iconpopup_dim = iconpopup.get_size()
iconpopup_coords=(1000,750)

#Chargement de l'image peinture
peinture = pygame.image.load("img/peinture.png").convert()
peinture_dim = peinture.get_size()
peinture_coords = (490,240)


images = [(peinture,peinture_coords),(background, (0,0)), (iconterminal, iconterminal_coords), (iconmessage, iconmessage_coords),(iconpopup,iconpopup_coords)] #Prépare la liste pour l'affichage des éléments
pygame.key.set_repeat(400, 30) #Active la possibilité de rester appuyer sur une touche







#=========================================================================#
#=================================== JEU =================================#
#=========================================================================#
g_info = [["Vous avez reçu un nouveau message"], ["en provenance du Boss"], ["Cliquez sur la boîte mail"], ["pour le consulter"], ["Cliquez ICI pour le fermer"]]
images, iconpopup = popup(iconpopup, g_info, images)

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

	#Affichage du jeu (affichage des _imageses dans l'ordre + rafraichissement de l'écran)
	render(images, None)
	pygame.display.flip()
	#Appel des fonctions associés à l'application en premier plan
	if images[len(images)-1][0] == fen_terminal:
		images, continuer, g_path, g_log, g_ligne, g_text = Terminal(images, g_path, g_log, g_ligne, g_text)
	elif images[len(images)-1][0] == fen_message:
		images, continuer, messages, g_compte = message(images, messages, g_compte)

pygame.quit()