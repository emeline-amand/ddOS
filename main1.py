import pygame, os, math
from pygame.locals import *

#Pour l'appli terminal
files = {'C:':{
	'Documents':{
		'Important':{
			'motsdepasses.txt':'txt',
			'motsdepasses.txt.':[
				'motsdepasses.txt',
				'Faire ESC pour quitter',
				'',
				'================================================================================',
				'shjkeuiOE',
				'a..0m..5.',
				'agfOsh48t',
				'adf0g5ec',
				'adf0mh456',
				'a8g0drd5o',
				'alrlsblus',
				'@5gOwzf5e',
				'af00my5z',
				'hZeOme15e',
				'af0mse5p',
				'zfs0m345e',
			],
			'adresses_IP_volés':'locked',
			'donnée_chiffrées.txt':'txt',
			'donnée_chiffrées.txt.':[
				'donnée_chiffrées.txt',
				'Faire ESC pour quitter',
				'',
				'================================================================================',
				'Code 4 : 1;19;3;9;9',
				'',
				'0111 0000',
				'0110 0010',
				'0110 0001',
				'0110 0100',
				'0100 0011',
				'0010 0011',
				'0110 0111',
				'0111 0101',
				'0110 1000',

			],
			'Émilie':'locked',
		},
		'Programmation':{
			'Blog_perso':'locked',
			'Projet_JARVIS':{
				'info_techniques.txt':'txt', #fichier qui sera affiché lors de 'dir'
				'info_techniques.txt.':[ #fichier fantôme qui sera caché mais contient le contenu du txt
					'info_techniques.txt',
					'Faire ESC pour quitter',
					'',
					'================================================================================',
					'PROJET JARVIS',
					'',
					'Date de création : 9 janvier 2020',
					'Jarvis est un assistant intelligent capable de prendre des initiatives.',
					'Il permet de déléguer des tâches simples et donc gagner du temps sur le',
					'travail.'
				],
				'Fichiers':'locked',
			},
			'Sudoku':'locked',
			'Project_Δ':'locked',
		},
		'Travail':'locked',
		'Cuisine':{
			'Recettes':{
				'COte DE porc aux 2 saisons.png':'png',
				'lAsagNe.png':'png',
				'Curry_et_poulEt.png':'png',
				'TaRte_aux_pommEs.png':'png',
				'tIramisu.png':'png',
				'kouigN_amann.png':'png',
				'hoTtEok.png':'png',
				'churRos.png':'png',
				'chili_coN_carne.png':'png',
				'ecrevissE_panée.png':'png',
				'tagliatelles_de_carotte_au_soja_et_haricoT.png':'png',
			},
			'Résultats':'locked',
		},
	}, 
	'Images':{
		'Jin.png':'png',
		'San.png':'png',
		'Hyunjin.png':'png',
		'RM.png':'png',
		'J-hope.png':'png',
		'Jungkook.png':'png',
		'Kai.png':'png',
		'Ni_Ki.png':'png',
		'Woo_Yung.png':'png',
	}, 
	'Téléchargements':'locked', 
	'Musique':{
		'Favoris':{
			'Black Catcher - Vickeblanka':'mp3',
			'Rapid as Wildfires - HOYO-MIX':'mp3',
			'Overwhelmed - Royal & the Serpent':'mp3',
			'Do Bad Well - KSHMR':'mp3',
			'Eternal Eleanor - Elvenking':'mp3',
			'Jazz Bar - Dreamcatcher':'mp3',
			'Kings - Tribe Society':'mp3',
			'The Time Is Now - Atreyu':'mp3',
			'Prey - Parkway Drive':'mp3',
			'Gasoline - I Prevail':'mp3',
			'Popular Monster - Falling in reverse':'mp3'
		},
		'Playlists':{
			'Fish_in_a_Bird_Cage':{
				'Rule #1 | Magic':'mp3',
				'Rule #2 | Moonlight':'mp3',
				'Rule #3 | Paperwork':'mp3',
				'Rule #4 | Fish in a Bridcage':'mp3',
				'Rule #5 | James Picard':'mp3',
				'Rule #7 | Angel Tango':'mp3',
				'Rule #8 | Otherside':'mp3',
				'Rule #9 | Child of the stars':'mp3',
				'Rule #10 | Roots':'mp3'
			},
			'Evlenking':{
				'Pagan Revolution':'mp3',
				'No Prayer for the Dying':'mp3',
				'The Divided Heart':'mp3',
				'Heaven Is a Place on Earth':'mp3',
				'Silverseal':'mp3',
				'Under the Sign of a Black Star':'mp3',
				'Elvenlegions':'mp3',
				'The One We Shall Follow':'mp3',
				'Heathen Divide':'mp3',
				'Seasonspeech':'mp3',
				'Black Roses for the Wicked One':'mp3'
			},
			'Slipknot':{
				'Duality':'mp3',
				'Before I Forget':'mp3',
				'Unsainted':'mp3',
				'The Devil in I':'mp3',
				'Psychosocial':'mp3',
				'Wait and Bleed':'mp3',
				'Snuff':'mp3',
				'Nero Forte':'mp3',
				'Vermilion, Pt. 2':'mp3',
				'All Out Life':'mp3',
				'Dead Memories':'mp3'
			},
			'Gloryhammer':{
				'Masters of the Galaxy':'mp3',
				'The Land of the Unicorns':'mp3',
				'Gloryhammer':'mp3',
				'Hootforce':'mp3',
				'Battel for Eternity':'mp3',
				'Universe on Fire':'mp3',
				'Apocalypse 1992':'mp3',
				'Magic Dragon':'mp3',
				'Angus Mcfife':'mp3'
			},
			'Dreamcatcher':{
				'Deja Vu':'mp3',
				'PIRI':'mp3',
				'You and I':'mp3',
				'And ther was no one left':'mp3',
				'Jazz Bar':'mp3',
				'Diamond':'mp3',
				'Chase Me':'mp3',
				'Black or White':'mp3',
				'SAHARA':'mp3',
				'I Miss You':'mp3',
				'Sleep-walking':'mp3'
			},
			'Twenty_One_Pilots':{
				'Stressed Out':'mp3',
				'Ride':'mp3',
				'Chlorine':'mp3',
				'Car Radio':'mp3',
				'Heavydirtysoul':'mp3',
				'The Judge':'mp3',
				'The Hype':'mp3',
				'Lane Boy':'mp3',
				'House of Gold':'mp3',
				'Nico and the Niners':'mp3',
				'Goner':'mp3',
				'Cut My Lip':'mp3',
				'Bandito':'mp3',
				'Neon Gravestones':'mp3'
			}
		},
		
	}, 
	'Videos':{
		'Twenty_One_Pilot_Vessel_concert.mp4':'mp4',
		'ATEEZ_meme_compilation.mp4':'mp4',
		'Make_A_Wish_dance_practice.mp4':'mp4',
		'Lucifer_Sinee_dance_practice.mp4':'mp4',
		'Interview_spéciale_Jeremy_Berthelemy.mp4':'mp4',
		'La_vérité_sur_le_drama_Vache_Qui_Rit.mp4':'mp4',
		'Comment_sont_élevés_les_émeux.mp4':'mp4',
		'Tuto_Programmer_en_C--.mp4':'mp4',
	}, 
	'Applications':{
		'Subnautico.exe':'lexe',
		'jarvis.exe':'exe', 
		'Gogole_Chrome.exe':'lexe',
		'Discard.exe':'lexe',
		'Paramètres':{
			'reinitialiser.exe':'exe',
			'utilisateur.exe':'lexe',
			'systeme.exe':'lexe',
		}
	}
}}
g_path = ""
g_log = []
g_ligne = 290
g_log.append("Username : 1 11 21 1211")
g_text = ""
g_appUsed = ""

#Pour l'appli message
messages=[["de: Boss","Infos Hacker part 2",["Agent Wray, ","De notre côté nous avons découverts plusieurs choses. ","Certains fichiers du PC du hacker sont signalé par la mention ","[CORROMPU]. D'après nos analyses, ces dossiers ne contiennent ","aucunes informations essentielles à votre missions. ","Il ne sert donc à rien de les parcourir."]],["de: Boss","Infos Hacker",["Voici le peu d'informations que nous avons trouvé sur le hacker,","Son mail: neo.mitrax@mymail.com, avec le mot de passe : ","a**0m*h*5* (les * sont les caractères que nous n'avons pas réussi à ","décrypter à l'heure actuelle, c'est à vous de les trouver dans le PC ","du hacker.) elles vous seront utiles tout le long de la partie. Nous ","savons  que le hacker est citoyen français. Il aurait fait l'École 42 ","fut deuxième de sa promo. Cependant ses études prirent un autre ","tour à la mort de son père le 28 octobre 1997. Il entreprit des études ","d'arquéologue à l'Université de Massachusetts. Il s'installa ensuite à ","Brest, cette profession lui aurait permis de mettre en place son activité ","de hacker. A ce jour, il a hacké plusieurs banques dans différents pays. ","Il représente un danger pour tous,d'où la rapidité dont vous devez ","disposer pour supprimer les codes nucléaires de son ordinateur."]],["de: Boss","Règles du jeu",["Bonjour Agent,","L'heure est grave, le célèbre hacker connu sous le nom de ddOS","s'est emparé d'importants fichiers nucléaires.","Votre mission, si toute fois vous l'acceptez, est de pénétrer dans le PC ","du hacker à distance, récupérer ses fichiers nucléaires et les ","supprimer de son PC. Pour se faire l'équipe s'est mobilisée pour ","maintenir le PC du hacker hors service depuis chez lui. Voici votre ","mail: christopher.wray@fbi.com et votre mot de passe: Ly46fZer ","pour vous connecter à votre messagerie lors de cette mission. ","Prenez soin de les noter sur une feuille: vous serez amené à vous ","déconnecter de votre compte plusieurs fois. Cette feuille vous servira ","également à noter toutes les informations et mots de passe que","vous trouvez: tout se réutilise! ","Bonne chance, la survie de l'humanité dépend de vous Agent Wray."]],["de: FBI","Vacances",["Vous n'avez pas pris de vacances depuis plusieurs mois Agent Wray, ","Songez-y."]],["de: FBI","année 2021",["Meilleurs voeux agent Wray! C'est un plaisir d'être à vos côtés ","une années de plus!"]],["de: Boss","Nouvelle équipe",["Agent Wray,","Vous voici affecté à une nouvelle équipe sous mon commandement. ","Je ne fais pas de doutes sur le fait que nous nous entendrons bien. ","Monsieur Decopmann m'a beaucoup parlé de vous en bien.","Bienvenue dans l'équipe 007"]],["de: Boss","Contenu rapport",["Bonjour Agent Wray, le rapport que tu m'as remis ce matin sur l'affaire"," Jonhson était peu fourni. Je me permets donc de te rappeler ","les éléments clefs afin de faire des rapports plus efficaces.","","Étape 1 – Bien faire préciser la demande: Le destinataire du rapport ","et la situtation","Étape 2 – Rassembler et traiter l’information nécessaire","Étape 3 – Faire son plan","Étape 4 – Rédiger le rapport"]],["de: James Scott","travail",["Salut Agent Wray, j'ai retrouvé cet article du FBI..."," à ressortir quand tes coéquipiers râlent pour les missions en groupe ;)"," ","Le FBI considère cela comme essentiel à son succès aujourd’hui. ","Les groupes de travail se sont avérés être un moyen très efficace ","pour le FBI et les forces de l’ordre fédérales, étatiques et locales ","de s’unir pour traiter des problèmes de criminalité spécifiques ","et des menaces à la sécurité nationale."]],["de: idee","idee",["idee"]],["de: idee","idee",["idee"]]]

g_compte=1
compte=1
g_champ=[]
text=""
utilisateur = "Agent"
g_countreturn=0

#Variable globale ... globale
g_gagne=False

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
	#afficher les _images dans l'ordre croissant
	for image in toBlit:
		screen.blit(image[0], image[1])
	return toBlit

#=========================================================================#
#================================= MESSAGE ===============================#
#=========================================================================#

def message(_images, _messages, g_compte, compte, utilisateur, g_champ, g_countreturn, text) :
	"""permet d'afficher les messages sur une fenetre en séparant l'émetteur du message et son objet, ainsi que différents éléments propres à la messagerie"""
	# initialisations de variables au debut du jeu
	appli = True
	_continuer = True
	# variabes concernant des coordonnées sur l'espace de connexion
	lignex=529
	ligney=400
	lignereturny=400
	epaisseurchamp1=4  # pour le contour en gars lorsqu'on écrit dans l'espace de connexion
	epaisseurchamp2=2
	# variable spécifique au  message sur la boite mail du hacker contenant une photo
	photo=0
	# variable utilisée pour cliquer sur le bouton déconnexion de la messagerie
	deconnexion=0
	
	messagesHacker=[["de: Mamie","Dernières vacances",["Coucou mon chéri, ","Comment vas-tu? ","Je sais que ton métier de concierge te prends beaucoup de temps. ","Je t'envoie donc un petit mail pour te remercier d'être allé à Brest ","avec moi durant ses dernières vacances. Cela m'a beaucoup touché ","que tu prennes du temps avec ta vieille mamie. Ne t'inquiètes ","pas pour ton chat Glad0s, je prends soin de lui, il va très bien et se ","plaît beaucoup ici! J'ai pris soin de t'envoyer un colis avec une ","douzaine de durian que j'ai trouvé ce matin au marché du village, ","tu les aimes tant! C'est dans ce marché de Brest que se trouve les ","fruits les plus exotiques! De quoi te faire voyager depuis chez toi :)","Je t'embrasse, ","","Ta Mamie "]],["de: DUVAL Jacques","Ampoules grillées",["Bonjour Monsieur le concierge","Les ampoules du couloir au troisième étage sont cassées. ","Veuillez appeler un électricien.","","Bien Cordialement,","DUVAL Jacques, trosième étage du bâtiment 2"]],["de: CASTORAMA","Votre livraison est en route!",["Nous vous informons que votre commande est en route!","Vous devriez la recevoir dans les jours suivants, merci d'avoir choisi ","Castorama!","","Votre cagnotte fidélité bénéficie de 200 points supplémentaires.","","Détails de la commande:","Tuyau pvc Compact Ø100 mm L.2 m x5","Enduit de façade rénovation chaux ton pierre 25 kg x2","Elagueuse sur perche électrique FPPS710 710w 18cm"]],["de: moi","Binaire",[]],["de: MyMail","Votre compte",["Bonjour,",""," Afin de vous aider à définir vos paramètres de confidentialité ","encore plus facilement, nous avons ajouté des suggestions dans ","votre Check-up Confidentialité. Par exemple, nous vous aidons à ","activer ou désactiver le partage de votre position, définir la durée ","pendant laquelle vous souhaitez conserver votre historique sur le Web ","et les applications et bien plus encore, directement depuis ","votre Check-up Confidentialité.","","Bonne journée! "]],["de: DEF CON","Invitation",["Nous sommes heureux de vous accueillir à cette 28ème édition de ","la DEF CON! En raison des conditions sanitaires actuelles, ","les conférences seront effectuées en nombre limités. Pour cela que ","vous devez réserver dès maintenant vos tickets. Si vous ne pouvez ","participer à une conférence, vous aurez cependant accès à un lien de ","connexion, pour pouvoir y assister depuis un ordinateur."," ","DATE: 8-11 août.","LIEU: Rio All Suite Hotel & Casino ","","À bientôt","Comité de la DEFCON"]],["de: Spotify","Nouvelle chanson de votre groupe préféré",["Twenty One Pilots a sorti un nouveau single durant la période difficile","que nous avons traversé.","Découvrez Level Of Concern sur votre plateforme favorite !","","TOP shook the world with the release of their 2015 LP BLURRYFACE, ","an album that would go to on sell over 7 millions copies worldwide and ","earn the band their first ever GRAMMY Award... ","Discover more about them on Spotify.","","Essayez Spotify Premium gratuitement pendant un mois. ","Bénéficiez du mode écoute libre, zapping illimité ","et de l'écoute hors connexion."]],["de: PC","Réinitialisation",["Bonjour! ","Merci d'avoir changé l'un des mots de passe de votre PC grâce ","à notre logiciel!","","nouveau mot de passe: oJrVfMbOtJ"]]]
	
	# on regarde sur quelle messagerie on se trouve: 1=agent; 2= Neo Mitrax(hacker); 3=fenetre de connexion
	
	if g_compte == 1:
		# par défaut, quand on commence le jeu, on est sur la messagerie de l'agent
		utilisateur="Agent"
		compte=1
		# variable pour que les inputs soient seulement fonctionnels quand on est sur la page de connexion
		connexion = 0
		
		# mise en page de la messagerie
		y=250
		pygame.draw.line(screen,(0,0,0), (340, y), (1130, y), 2)
		pygame.draw.line(screen,(0,0,0), (340, 210), (340, 850), 2)
		screen.blit(messageFontpetit.render("Vous êtes connecté en  ",True,(0,0,0)),(160,222))
		screen.blit(messageFontpetit.render("tant que:"+ utilisateur,True,(0,0,0)),(160,240))
		screen.blit(messageFontpetit.render("déconnexion ",True,(0,0,0)),(160,800))
		screen.blit(messageFont.render("émetteur: ",True,(0,0,0)),(350,212))
		screen.blit(messageFont.render("objet: ",True,(0,0,0)),(600,212))
	
		# on fait apparaitre les messages à l'écran avec les émetteurs et les objets
		for i in range (len(_messages)):
			# on fait afficher l'émetteur des messages
			screen.blit(messageFont.render(_messages[i][0],True,(0,0,0)),(350,y))
			_messages[i].append(y-30)
	
			# on fait afficher l'objet des messages
			screen.blit(messageFont.render(_messages[i][1],True,(0,0,0)),(600,y))
			_messages[i].append(y-30)
	
			# on fait afficher ligne de séparation
			y+=40
			pygame.draw.line(screen,(0,0,0),(340, y),(1130, y), 2)
	
	
		pygame.display.flip()
		# on fait afficher séparation entre chaque lignes

	elif g_compte == 2:
		utilisateur= " Neo Mitrax"
		compte=2
		# variable pour que les inputs soient seulement fonctionnels quand on est sur la page de connexion
		connexion = 0

		# on affiche les mails et autres éléments de la messagerie.
		y=250
		pygame.draw.line(screen,(0,0,0), (340,250), (1130, 250), 2)
		pygame.draw.line(screen,(0,0,0), (340, 210), (340, 850), 2)
		screen.blit(messageFontpetit.render("Vous êtes connecté en  ",True,(0,0,0)),(160,222))
		screen.blit(messageFontpetit.render("tant que:"+ utilisateur,True,(0,0,0)),(160,240))
		screen.blit(messageFontpetit.render("déconnexion ",True,(0,0,0)),(160,800))
		screen.blit(messageFont.render("émetteur: ",True,(0,0,0)),(350,212))
		screen.blit(messageFont.render("objet: ",True,(0,0,0)),(600,212))
		
		# on fait apparaitre les messages à l'écran avec les émetteurs et les objets
		for i in range (len(messagesHacker)):
			#on fait afficher l'émetteur des messages
			screen.blit(messageFont.render(messagesHacker[i][0],True,(0,0,0)),(350,y))
			messagesHacker[i].append(y-30)
	
			# on fait afficher l'objet des messages
			screen.blit(messageFont.render(messagesHacker[i][1],True,(0,0,0)),(600,y))
			messagesHacker[i].append(y-30)
	
			# on fait afficher ligne de séparation
			y+=40
			pygame.draw.line(screen,(0,0,0),(340, y),(1130, y), 2)
	
	
		pygame.display.flip()
		
		
	elif g_compte == 3:
		connexion=2
		# si on a pas appuyé sur la touche "entrée", soit qu'on se trouve dans la case "insérer un mail"
		if g_countreturn == 0:
			render(_images, None)
			
			# affichage à l'écran
			screen.blit(messageFont.render(text, True, (0, 0, 0)), (lignex,lignereturny))
			screen.blit(messageFont.render("CONNECTER UN COMPTE",True,(0,0,0)),(430,300))
			screen.blit(messageFont.render("insérer votre mail: ",True,(0,0,0)),(325,400))
			pygame.draw.rect(screen,(0,0,0),(525,400,300,40),epaisseurchamp1)
			screen.blit(messageFont.render("insérer votre mot de passe: ",True,(0,0,0)),(220,500))
			pygame.draw.rect(screen,(0,0,0),(525,500,300,40),epaisseurchamp2)
			screen.blit(messageFont.render("retour",True,(0,0,0)),(822,620))
			
			retour=0
			connexion = 2
			pygame.display.flip()

		# dans les autres cas, c'est à dire lorsqu'on a appuyé sur la touche "entrée" 1 fois, soit qu'on se trouve dans la case "insérer votre mot de passe"
		else:
			input = text #Récupérer la valeur entrée
			epaisseurchamp1=2
			epaisseurchamp2=4
			
			# affichage à l'écran
			screen.blit(messageFont.render("CONNECTER UN COMPTE", True,(0,0,0)),(430,300))
			screen.blit(messageFont.render("insérer votre mail: ", True,(0,0,0)),(325,400))
			pygame.draw.rect(screen,(0,0,0),(525,400,300,40),epaisseurchamp1)
			screen.blit(messageFont.render("insérer votre mot de passe: ", True,(0,0,0)),(220,500))
			pygame.draw.rect(screen,(0,0,0),(525,500,300,40),epaisseurchamp2)
			screen.blit(messageFont.render("retour", True,(0,0,0)),(822,620))
			screen.blit(messageFont.render(g_champ[0], True, (0, 0, 0)), (lignex,lignereturny))
			screen.blit(messageFont.render(text, True, (0, 0, 0)), (lignex,500))
			retour=0
			lignex+=0
			lignereturny+=100
			pygame.display.flip()

			
	

	# pendant que l'appli=true, commun à toutes les applis
	while appli :
		for event in pygame.event.get(): #Attente des événements
			if event.type == QUIT:
				_continuer = False
				appli = False
			# si évènement est de type mousebuttondown
			elif event.type == MOUSEBUTTONDOWN:
				
				# faire afficher le message cliqué par le joueur, en fonction de la boite mail sur laquelle on se trouve
				if g_compte==1:
					y=250
					compte=1
					retour=1
					connexion=0
					for i in range (len(_messages)):
						# on regarde la position de la souris
						if 350<event.pos[0]<1132 and y<event.pos[1]<y+40 and connexion==0 and event.button == 1: 
							retour = 1
							# efface texte à l'écran
							render(_images, None)
	
							# affiche texte à l'écran, precisez coordonnées)
							y2 = 250
							for ligne in messages[i][2]:
								screen.blit(messageFont.render(ligne,True,(0,0,0)),(350,y2))
								y2+=40
							screen.blit(messageFontpetit.render("objet:  "+messages[i][1],True,(0,0,0)),(350,222))
							pygame.draw.line(screen,(0,0,0), (340, 210), (340, 850), 2)
							screen.blit(messageFontpetit.render("Vous êtes connecté en  ",True,(0,0,0)),(160,222))
							screen.blit(messageFontpetit.render("tant que:"+ utilisateur,True,(0,0,0)),(160,240))
							screen.blit(messageFontpetit.render("Boîte principale",True,(0,0,0)),(160,350))
							screen.blit(messageFontpetit.render("déconnexion ",True,(0,0,0)),(160,800))
							connexion=1
							deconnexion=0
							
							#refresh écran
							pygame.display.flip()
						y+=40
				
				
				if g_compte==2:
					y=250
					compte=2
					retour=1
					deconnexion=0
					connexion=0
					for i in range (len(messagesHacker)):
						if 350<event.pos[0]<1132 and y<event.pos[1]<y+40 and connexion==0 and event.button == 1:
							
							if 350<event.pos[0]<800 and 370<event.pos[1]<410 and event.button == 1: # message intitulé binaire qui comprend une photo
								# on met en premier plan l'image contenant la photo
								render(_images, (peinture, peinture_coords))
								# on fait afficher les éléments de la messagerie
								pygame.draw.line(screen,(0,0,0), (340, 210), (340, 850), 2)
								screen.blit(messageFontpetit.render("objet:  "+messagesHacker[i][1],True,(0,0,0)),(350,222))
								screen.blit(messageFontpetit.render("“Le visage est l'image de l'âme.”",True,(0,0,0)),(600,800))
								screen.blit(messageFontpetit.render("Vous êtes connecté en  ",True,(0,0,0)),(160,222))
								screen.blit(messageFontpetit.render("tant que:"+ utilisateur,True,(0,0,0)),(160,240))
								screen.blit(messageFontpetit.render("Boîte principale",True,(0,0,0)),(160,350))
								screen.blit(messageFontpetit.render("déconnexion ",True,(0,0,0)),(160,800))
								connexion=1
								photo=1
								# refresh écran
								pygame.display.flip()
								
							else:
								# efface texte à l'écran
								render(_images, None)
		
								# affiche texte à l'écran, precisez coordonnées
								y2 = 250
								for ligne in messagesHacker[i][2]:
									screen.blit(messageFont.render(ligne,True,(0,0,0)),(350,y2))
									y2+=40
								screen.blit(messageFontpetit.render("objet:  "+messagesHacker[i][1],True,(0,0,0)),(350,222))
								pygame.draw.line(screen,(0,0,0), (340, 210), (340, 850), 2)
								screen.blit(messageFontpetit.render("Vous êtes connecté en  ",True,(0,0,0)),(160,222))
								screen.blit(messageFontpetit.render("tant que:"+ utilisateur,True,(0,0,0)),(160,240))
								screen.blit(messageFontpetit.render("Boîte principale",True,(0,0,0)),(160,350))
								screen.blit(messageFontpetit.render("déconnexion ",True,(0,0,0)),(160,800))
								connexion=1
								photo=0
		
								# refresh écran
								pygame.display.flip()
						y+=40

					
					
				# CLIQUE SUR BOITE PRINCIPAL qui permet de revenir à la liste des mails en fonction du compte sur lequel on se trouve
				if 160<event.pos[0]<270 and 350<event.pos[1]<390 and event.button == 1:
					connexion=0
					if g_compte==1 :
						compte=1
						render(_images, None)
						y=250
						# on affiche les éléments de la messagerie
						pygame.draw.line(screen,(0,0,0), (340, y), (1130, y), 2)
						pygame.draw.line(screen,(0,0,0), (340, 210), (340, 850), 2)
						screen.blit(messageFontpetit.render("Vous êtes connecté en  ",True,(0,0,0)),(160,222))
						screen.blit(messageFontpetit.render("tant que:"+ utilisateur,True,(0,0,0)),(160,240))
						screen.blit(messageFontpetit.render("déconnexion ",True,(0,0,0)),(160,800))
						screen.blit(messageFont.render("émetteur: ",True,(0,0,0)),(350,212))
						screen.blit(messageFont.render("objet: ",True,(0,0,0)),(600,212))
	
						for i in range (len(_messages)):
						# on fait afficher l'émetteur des messages
							screen.blit(messageFont.render(_messages[i][0],True,(0,0,0)),(350,y))
							_messages[i].append(y-30)
							# on fait afficher l'objet des messages
							screen.blit(messageFont.render(_messages[i][1],True,(0,0,0)),(600,y))
							_messages[i].append(y-30)
							y+=40
							# on fait afficher ligne de séparation
							pygame.draw.line(screen,(0,0,0),(340, y),(1130, y), 2)
						pygame.display.flip()
						
					if g_compte==2 :
						compte=2
						
						# si on se trouve sur le message contenant la photo
						if photo==1:
							photo=0	
							del _images[-1]					
							render(_images, None)
							y=250
							pygame.draw.line(screen,(0,0,0), (340, y), (1130, y), 2)
							pygame.draw.line(screen,(0,0,0), (340, 210), (340, 850), 2)
							screen.blit(messageFontpetit.render("Vous êtes connecté en  ",True,(0,0,0)),(160,222))
							screen.blit(messageFontpetit.render("tant que:"+ utilisateur,True,(0,0,0)),(160,240))
							screen.blit(messageFontpetit.render("déconnexion ",True,(0,0,0)),(160,800))
							screen.blit(messageFont.render("émetteur: ",True,(0,0,0)),(350,212))
							screen.blit(messageFont.render("objet: ",True,(0,0,0)),(600,212))
		
							for i in range (len(messagesHacker)):
							# on fait afficher l'émetteur des messages
								screen.blit(messageFont.render(messagesHacker[i][0],True,(0,0,0)),(350,y))
								messagesHacker[i].append(y-30)
								# on fait afficher l'objet des messages
								screen.blit(messageFont.render(messagesHacker[i][1],True,(0,0,0)),(600,y))
								messagesHacker[i].append(y-30)
								y+=40
								# on fait afficher ligne de séparation
								pygame.draw.line(screen,(0,0,0),(340, y),(1130, y), 2)
								
						else:
							render(_images, None)
							y=250
							
							# on affiche les éléments de la messagerie
							pygame.draw.line(screen,(0,0,0), (340, y), (1130, y), 2)
							pygame.draw.line(screen,(0,0,0), (340, 210), (340, 850), 2)
							screen.blit(messageFontpetit.render("Vous êtes connecté en  ",True,(0,0,0)),(160,222))
							screen.blit(messageFontpetit.render("tant que:"+ utilisateur,True,(0,0,0)),(160,240))
							screen.blit(messageFontpetit.render("déconnexion ",True,(0,0,0)),(160,800))
							screen.blit(messageFont.render("émetteur: ",True,(0,0,0)),(350,212))
							screen.blit(messageFont.render("objet: ",True,(0,0,0)),(600,212))
		
							for i in range (len(messagesHacker)):
							# on fait afficher l'émetteur des messages
								screen.blit(messageFont.render(messagesHacker[i][0],True,(0,0,0)),(350,y))
								messagesHacker[i].append(y-30)
								# on fait afficher l'objet des messages
								screen.blit(messageFont.render(messagesHacker[i][1],True,(0,0,0)),(600,y))
								messagesHacker[i].append(y-30)
								y+=40
								# on fait afficher ligne de séparation
								pygame.draw.line(screen,(0,0,0),(340, y),(1130, y), 2)
						
						pygame.display.flip()
							
						
							
						

				# QUAND ON APPUIYE SUR TOUCHE DECONNEXION, pour se déconnecter du compte de la messagerie, avec confirmation
				if 160<event.pos[0]<270 and 700<event.pos[1]<850  and event.button == 1 and deconnexion==0:
					render(_images, None)
					screen.blit(messageFont.render("Confirmer la déconnexion: ",True,(0,0,0)),(425,400))
					screen.blit(messageFont.render("oui ",True,(0,0,0)),(400,500))
					screen.blit(messageFont.render("non ",True,(0,0,0)),(700,500))
					pygame.display.flip()
					connexion=1
					
					
				# SI TOUCHE CLIQUEE EST NON, alors on retourne a la boite principale de la messagerie 
				if 700<event.pos[0]<740 and 500<event.pos[1]<550 and connexion == 1 and event.button == 1:
					render(_images, None)
					connexion=0
					y=250
					retour = 1
					
					# on affiche les éléments de la messagerie
					pygame.draw.line(screen,(0,0,0), (340, y), (1130, y), 2)
					pygame.draw.line(screen,(0,0,0), (340, 210), (340, 850), 2)
					screen.blit(messageFontpetit.render("Vous êtes connecté en  ",True,(0,0,0)),(160,222))
					screen.blit(messageFontpetit.render("tant que:"+ utilisateur,True,(0,0,0)),(160,240))
					screen.blit(messageFontpetit.render("déconnexion ",True,(0,0,0)),(160,800))
					screen.blit(messageFont.render("émetteur: ",True,(0,0,0)),(350,212))
					screen.blit(messageFont.render("objet: ",True,(0,0,0)),(600,212))
					
					# on regarde sur quel compte on se trouvait, et on fait apparaitre les messages
					if compte == 1:
						for i in range (len(_messages)):
						# on fait afficher l'émetteur des messages
							screen.blit(messageFont.render(_messages[i][0],True,(0,0,0)),(350,y))
							_messages[i].append(y-30)
							# on fait afficher l'objet des messages
							screen.blit(messageFont.render(_messages[i][1],True,(0,0,0)),(600,y))
							_messages[i].append(y-30)
							y+=40
							# on fait afficher ligne de séparation
							pygame.draw.line(screen,(0,0,0),(340, y),(1130, y), 2)
							
					elif compte == 2:
						for i in range (len(messagesHacker)):
						# on fait afficher l'émetteur des messages
							screen.blit(messageFont.render(messagesHacker[i][0],True,(0,0,0)),(350,y))
							messagesHacker[i].append(y-30)
							# on fait afficher l'objet des messages
							screen.blit(messageFont.render(messagesHacker[i][1],True,(0,0,0)),(600,y))
							messagesHacker[i].append(y-30)
							y+=40
							# on fait afficher ligne de séparation
							pygame.draw.line(screen,(0,0,0),(340, y),(1130, y), 2)
					pygame.display.flip()
					

				# SI TOUCHE OUI CLIQUEE, alors on arrive sur l'espace de connexion de la messagerie 
				if 400<event.pos[0]<440 and 500<event.pos[1]<540 and connexion == 1 and event.button == 1:
					g_compte=3
					render(_images, None)
					screen.blit(messageFont.render("CONNECTER UN COMPTE",True,(0,0,0)),(430,300))
					screen.blit(messageFont.render("insérer votre mail: ",True,(0,0,0)),(325,400))
					pygame.draw.rect(screen,(0,0,0),(525,400,300,40),epaisseurchamp1)
					screen.blit(messageFont.render("insérer votre mot de passe: ",True,(0,0,0)),(220,500))
					pygame.draw.rect(screen,(0,0,0),(525,500,300,40),epaisseurchamp2)
					screen.blit(messageFont.render("retour",True,(0,0,0)),(822,620))
					retour=0
					connexion = 2
					pygame.display.flip()
					
				# SI TOUCHE RETOUR CLIQUEE, retour sur la messagerie pendant qu'on est sur l'espace de connexion, lorsqu'on a oublié un mot de passe par exemple
				if 822<event.pos[0]<900 and 620<event.pos[1]<660 and retour == 0 and event.button == 1:#retour == 0
					print("works")
					print(retour)
					retour=1
					g_countreturn=0
					epaisseurchamp1=4
					epaisseurchamp2=2
					lignereturny=400
					g_champ=[]
					text = ""
					connexion=0
					
					# on regarde la valeur de la variable compte pour voir sur quel compte on se trouvait précédemment
					if compte == 1 :
						render(_images, None)
						g_compte=1
						y=250
						
						# affichage éléments messagerie
						pygame.draw.line(screen,(0,0,0), (340, y), (1130, y), 2)
						pygame.draw.line(screen,(0,0,0), (340, 210), (340, 850), 2)
						screen.blit(messageFontpetit.render("Vous êtes connecté en  ",True,(0,0,0)),(160,222))
						screen.blit(messageFontpetit.render("tant que:"+ utilisateur,True,(0,0,0)),(160,240))
						screen.blit(messageFontpetit.render("déconnexion ",True,(0,0,0)),(160,800))
						screen.blit(messageFont.render("émetteur: ",True,(0,0,0)),(350,212))
						screen.blit(messageFont.render("objet: ",True,(0,0,0)),(600,212))
	
						for i in range (len(_messages)):
						# on fait afficher l'émetteur des messages
							screen.blit(messageFont.render(_messages[i][0],True,(0,0,0)),(350,y))
							_messages[i].append(y-30)
							# on fait afficher l'objet des messages
							screen.blit(messageFont.render(_messages[i][1],True,(0,0,0)),(600,y))
							_messages[i].append(y-30)
							y+=40
							# on fait afficher ligne de séparation
							pygame.draw.line(screen,(0,0,0),(340, y),(1130, y), 2)
						pygame.display.flip()
						
					if compte == 2 :
						g_compte=2
						y=250
						render(_images, None)
						connexion=0
						
						# affichage éléments messagerie
						pygame.draw.line(screen,(0,0,0), (340, y), (1130, y), 2)
						pygame.draw.line(screen,(0,0,0), (340, 210), (340, 850), 2)
						screen.blit(messageFontpetit.render("Vous êtes connecté en  ",True,(0,0,0)),(160,222))
						screen.blit(messageFontpetit.render("tant que:"+ utilisateur,True,(0,0,0)),(160,240))
						screen.blit(messageFontpetit.render("déconnexion ",True,(0,0,0)),(160,800))
						screen.blit(messageFont.render("émetteur: ",True,(0,0,0)),(350,212))
						screen.blit(messageFont.render("objet: ",True,(0,0,0)),(600,212))
	
						for i in range (len(messagesHacker)):
						# on fait afficher l'émetteur des messages
							screen.blit(messageFont.render(messagesHacker[i][0],True,(0,0,0)),(350,y))
							messagesHacker[i].append(y-30)
							# on fait afficher l'objet des messages
							screen.blit(messageFont.render(messagesHacker[i][1],True,(0,0,0)),(600,y))
							messagesHacker[i].append(y-30)
							y+=40
							# on fait afficher ligne de séparation
							pygame.draw.line(screen,(0,0,0),(340, y),(1130, y), 2)
								
								
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
					return _images, False, _messages, g_compte, compte, utilisateur, g_champ, g_countreturn, text
					
					#Clic gauche sur la croix en bas à droite  => quitte le jeu quitter l'appli (c'est à dire fermer la fonction)
			

			# Pour pouvoir écrire son id et son pwd sur l'espace de connexion
			if event.type == KEYDOWN and connexion == 2 :
				retour=0
				
				# lorsqu'on appuie sur la touche retour:
				if event.key == K_RETURN:
					g_countreturn+=1
					
					#si on a appuyé une fois sur la touche retour(on se trouve donc au niveau de "insérer votre mot de passe: "
					if g_countreturn==1:
						input = text #Récupérer la valeur entrée
						g_champ.append(text)
						lignechampy=400
						epaisseurchamp1=2
						epaisseurchamp2=4
	
						#---------------------------------------#
						#laisse le text écrit précédemment à l'écran:
						render(_images, None)
						for line in g_champ:
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
						screen.blit(messageFont.render("retour",True,(0,0,0)),(822,620))
						retour=0
	
						lignex+=0
						lignereturny+=100
						pygame.display.flip()
					# si on a appuyé plus de deux fois sur la touche retour, on efface tout les inputs rentrés à l'écran; le texte écrit sera ensuite placé au niveau de la case insérer votre mail.

					# si on a appuyé deux fois sur la touche retour, on fait donc valider le id et mdp qu'on a entré	
					if g_countreturn==2:
						g_countreturn=0
						g_champ.append(text)
						lignereturny=400
						epaisseurchamp1=4
						epaisseurchamp2=2
						
						#on procède alors à une verification des éléments entré par le joueur qui se trouvent dans g_champ
						
						#on regarde si le mail et pwd correspond à celui du hacker
						if g_champ[0]=="neo.mitrax@mymail.com" and g_champ[1]=="adf0mh456":
							#on efface texte écrit a l'écran
							render(_images, None)
							utilisateur= " Neo Mitrax"
							g_compte=2

							#on affiche les mails et autres éléments de la messagerie.
							pygame.draw.line(screen,(0,0,0), (340,250), (1130, 250), 2)
							pygame.draw.line(screen,(0,0,0), (340, 210), (340, 850), 2)
							screen.blit(messageFontpetit.render("Vous êtes connecté en  ",True,(0,0,0)),(160,222))
							screen.blit(messageFontpetit.render("tant que:"+ utilisateur,True,(0,0,0)),(160,240))
							screen.blit(messageFontpetit.render("déconnexion ",True,(0,0,0)),(160,800))
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
							g_champ=[]
							text = ""
							connexion=0

						#si id et pwd correspondent aux id et pwd de l'agent, on arrive sur la boite mail de l'agent
						elif g_champ[0]=="christopher.wray@fbi.com" and g_champ[1]=="Ly46fZer":
							#on efface texte écrit a l'écran
							render(_images, None)
							utilisateur="Agent"
							g_compte=1

							#on affiche les mails et autres éléments de la messagerie.
							pygame.draw.line(screen,(0,0,0), (340, y), (1130, y), 2)
							pygame.draw.line(screen,(0,0,0), (340, 210), (340, 850), 2)
							screen.blit(messageFontpetit.render("Vous êtes connecté en  ",True,(0,0,0)),(160,222))
							screen.blit(messageFontpetit.render("tant que:"+ utilisateur,True,(0,0,0)),(160,240))
							screen.blit(messageFontpetit.render("déconnexion ",True,(0,0,0)),(160,800))
							screen.blit(messageFont.render("émetteur: ",True,(0,0,0)),(350,212))
							screen.blit(messageFont.render("objet: ",True,(0,0,0)),(600,212))
							g_champ=[]
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
							connexion=0
							
						else:
							epaisseurchamp1=4
							epaisseurchamp2=2
							render(_images, None)
							screen.blit(messageFont.render("CONNECTER UN COMPTE",True,(0,0,0)),(430,300))
							screen.blit(messageFont.render("insérer votre mail: ",True,(0,0,0)),(325,400))
							pygame.draw.rect(screen,(0,0,0),(525,400,300,40),epaisseurchamp1)
							screen.blit(messageFont.render("insérer votre mot de passe: ",True,(0,0,0)),(220,500))
							pygame.draw.rect(screen,(0,0,0),(525,500,300,40),epaisseurchamp2)
							screen.blit(messageFont.render("retour",True,(0,0,0)),(822,620))
							screen.blit(messageFont.render("mail et mot de passe invalides",True,(0,0,0)),(355,600))
							retour=0
							connexion = 2
							pygame.display.flip()
							g_champ=[]
							text = ""
					
					pygame.display.flip()
					
				#pour supprimer un caractère	
				elif event.key == K_BACKSPACE:
					text = text[:-1]
					render(_images, None)
					
					if g_countreturn==1:
						screen.blit(messageFont.render(g_champ[0], True, (0, 0, 0)), (lignex,400))
						screen.blit(messageFont.render(text, True, (0, 0, 0)), (lignex,lignereturny))
						screen.blit(messageFont.render("CONNECTER UN COMPTE",True,(0,0,0)),(430,300))
						screen.blit(messageFont.render("insérer votre mail: ",True,(0,0,0)),(325,400))
						pygame.draw.rect(screen,(0,0,0),(525,400,300,40),epaisseurchamp1)
						screen.blit(messageFont.render("insérer votre mot de passe: ",True,(0,0,0)),(220,500))
						pygame.draw.rect(screen,(0,0,0),(525,500,300,40),epaisseurchamp2)
						screen.blit(messageFont.render("retour",True,(0,0,0)),(822,620))
						retour=0
						connexion = 2
						pygame.display.flip()
	
						
					else:
						
						screen.blit(messageFont.render(text, True, (0, 0, 0)), (lignex,lignereturny))
						screen.blit(messageFont.render("CONNECTER UN COMPTE",True,(0,0,0)),(430,300))
						screen.blit(messageFont.render("insérer votre mail: ",True,(0,0,0)),(325,400))
						pygame.draw.rect(screen,(0,0,0),(525,400,300,40),epaisseurchamp1)
						screen.blit(messageFont.render("insérer votre mot de passe: ",True,(0,0,0)),(220,500))
						pygame.draw.rect(screen,(0,0,0),(525,500,300,40),epaisseurchamp2)
						screen.blit(messageFont.render("retour",True,(0,0,0)),(822,620))
						retour=0
						connexion = 2
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
					for line in g_champ:
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
					screen.blit(messageFont.render("retour",True,(0,0,0)),(822,620))
					retour=0
					connexion = 2
					pygame.display.flip()




	return _images, _continuer, _messages, g_compte, compte, utilisateur, g_champ, g_countreturn, text

def popup(_popup, _info,_images):
	"""Fais apparaître un popup à l'écran"""
	_images = render(_images,(iconpopup,iconpopup_coords))
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
				if event.pos[0] > 1000 and event.pos[0] < 1250 and event.pos[1] > 750 and event.pos[1] < 933 and event.button == 1:
					_images = render(_images,(iconpopup,iconpopup_coords) )
					appli=False
					pygame.display.flip()

	return _images, _popup

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
			return _path, True
		return _path, True
	else : #sinon avancer d'un dossier
		target = target.split('/')
		for t in target :
			exist = False
			for key in goto(_path).keys() : #Regarde si dossier cible existe
				if key == t and type(goto(_path)[key]) == dict :
					exist = True
			if not exist : # s'il n'existe pas
				return _path, False # fin, rien ne se passe
			if _path  == 'C:/' : #Si à la racine alors
				_path = _path[:len(_path)-1] #retire le '/' de fin uniquement présent au dossier racine de l'arbre
			_path = _path+'/'+t #Enfin, ajoute le dossier cible au chemin
		return _path, True

def openTXT(open, _images) :
	'''Permet d'ouvrir et lire des txt dans la console'''
	printLog(open, images)
	while True :
		#Attente des événements
		for event in pygame.event.get():
			if event.type == QUIT:
				return False, False, ""
			elif event.type == MOUSEBUTTONDOWN:
				if event.pos[0]>iconterminal_coords[0] and event.pos[0]<iconterminal_coords[0]+iconterminal_dim[0] and event.pos[1]>iconterminal_coords[1] and event.pos[1]<iconterminal_coords[1]+iconterminal_dim[1] and event.button == 1 : #Si clic sur icon (zone de clic définie par la position et taille de celui-ci)
					#Clic sur gauche sur "terminal" => quitte l'appli
					_images = render(_images, (fen_terminal, fen_terminal_coords))
					return False, True, "txt;"+open[0]
				elif event.pos[0]>iconmessage_coords[0] and event.pos[0]<iconmessage_coords[0]+iconmessage_dim[0] and event.pos[1]>iconmessage_coords[1] and event.pos[1]<iconmessage_coords[1]+iconmessage_dim[1] and event.button == 1 : #Si clic sur icon2 (zone de clic définie par la position et taille de celui-ci)
					#Clic gauche sur "message" => quitte l'appli vers message
					_images = render(_images, (fen_message, fen_message_coords))
					return False, True, "txt;"+open[0]
				elif event.pos[0]>1205 and event.pos[0]<1225 and event.pos[1]>989 and event.pos[1]<1010 and event.button == 1 :
					#Clic gauche sur la croix en bas à droite  => quitte le jeu
					return False, False, ""
					
			#Pour écrire dans le terminal
			elif event.type == KEYDOWN:
				if event.key == K_ESCAPE : 
					return True, True, ""

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
	screen.blit(terminalFont.render(_path+" > _", True, (0, 175, 0)), (125,_ligne))
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

def Terminal(_images, path, log, ligne, text, appUsed) :
	appli = True #Condition pour la boucle principale
	_continuer = True #Valeur qui sera retournée lors de la sortie de l'application pour stopper ou non le jeu
	input=None #Utile plus tard pour regarder ce qui a été entré au clavier
	if appUsed != "" : 
		appUsed = appUsed.split(';')
		if appUsed[0] == "jarvis" : input = "appli jarvis"
		elif appUsed[0] == "reinit" : input = "appli reinit"
		elif appUsed[0] == "txt" : input = appUsed[1]
	printLog(log, _images) #Affiche les logs (valeur de log récupérée depuis les paramètres de la fonction
	screen.blit(terminalFont.render(path+" > "+text+"_", True, (0, 175, 0)), (125,ligne))
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
				elif event.pos[0]>iconhelp_coords[0] and event.pos[0]<iconhelp_coords[0]+iconhelp_dim[0] and event.pos[1]>iconhelp_coords[1] and event.pos[1]<iconhelp_coords[1]+iconhelp_dim[1] and event.button == 1 : #Si clic sur icon2 (zone de clic définie par la position et taille de celui-ci)
					#Clic gauche sur "iconhelp" => quitte l'appli
					_images = render(_images, (fen_help, fen_help_coords))
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
					screen.blit(terminalFont.render(path+" > "+text+"_", True, (0, 175, 0)), (125,ligne))
					pygame.display.flip()
				else: #sinon
					if len(path+" > "+text)<93 : #si la ligne ne dépasse pas la longueur maximale du terminal
						text += event.unicode #ajouter le charactère associé à la touche appuyée au champ d'entrée
					#Affichage \/
					printLog(log, _images)
					screen.blit(terminalFont.render(path+" > "+text+"_", True, (0, 175, 0)), (125,ligne))
					pygame.display.flip()
		
		#interface de login (premier lancer de terminal ou "exit")		
		if path == "" :
			firstBoucle = True
			printLog(log, _images)
			screen.blit(terminalFont.render("Password : "+text+"_", True, (0, 175, 0)), (125,ligne))
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
						elif event.pos[0]>iconhelp_coords[0] and event.pos[0]<iconhelp_coords[0]+iconhelp_dim[0] and event.pos[1]>iconhelp_coords[1] and event.pos[1]<iconhelp_coords[1]+iconhelp_dim[1] and event.button == 1 : #Si clic sur icon2 (zone de clic définie par la position et taille de celui-ci)
							#Clic gauche sur "iconhelp" => quitte l'appli
							_images = render(_images, (fen_help, fen_help_coords))
							appli=False
							firstBoucle=False
							break
						elif event.pos[0]>1205 and event.pos[0]<1225 and event.pos[1]>989 and event.pos[1]<1010 and event.button == 1 :
							#Clic gauche sur la croix en bas à droite  => quitte le jeu
							_continuer = False
							appli = False
							firstBoucle = False
							break
							
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
							screen.blit(terminalFont.render("Password : "+text+"_", True, (0, 175, 0)), (125,ligne))
							pygame.display.flip()
						else: #sinon
							if len("Password : "+text)<93 : #si la ligne ne dépasse pas la longueur maximale du terminal
								text += event.unicode #ajouter le charactère associé à la touche appuyée au champ d'entrée
							#Affichage \/
							printLog(log, _images)
							screen.blit(terminalFont.render("Password : "+text+"_", True, (0, 175, 0)), (125,ligne))
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
					screen.blit(terminalFont.render(path+" > "+text+"_", True, (0, 175, 0)), (125,ligne))
					pygame.display.flip()
					break
				elif input != None: #Sinon rien faire
					log.append("Mot de passe incorrect")
					ligne+=20
					printLog(log, _images)
					screen.blit(terminalFont.render("Password : "+text+"_", True, (0, 175, 0)), (125,ligne))
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
					elif type(contents[i]) == list : ligne -= 20
					elif type(contents[i]) == str and contents[i] == "locked": log.append("dossier --- [CORROMPU]"+str(keys[i]))
					elif type(contents[i]) == str and contents[i] == "lexe": log.append("executable --- [CORROMPU]"+str(keys[i]))
					elif type(contents[i]) == str and contents[i] == "exe": log.append("executable --- "+str(keys[i]))
					elif type(contents[i]) == str and contents[i] == "png": log.append("image --- "+str(keys[i]))
					elif type(contents[i]) == str and contents[i] == "mp3": log.append("musique --- "+str(keys[i]))
					elif type(contents[i]) == str and contents[i] == "mp4": log.append("video --- "+str(keys[i]))
					elif type(contents[i]) == str and contents[i] == "txt": log.append("texte --- "+str(keys[i]))
					ligne+=20
				log, ligne = scrolling(log, ligne, _images, path)
				printLog(log, _images)
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
				log = []
				ligne = 270
				log.append("Username : 1 11 21 1211")
				ligne+=20
				path=""
				printLog(log, _images)
			#appli \/
			elif input[0] == "appli" :
				if input[1] == "jarvis":
					if type(appUsed) == list : 
						s=appUsed[-1];
					else : 
						s=0
					appli, _continuer, appUsed = jarvis(_images, int(s))
					printLog(log, _images)
				elif input[1] == "reinit":
					if type(appUsed) == list : 
						appli, _continuer, appUsed = reinitialiser(_images, appUsed[1])
					else : 
						appli, _continuer, appUsed = reinitialiser(_images, ",,,,")
					printLog(log, _images)
				else :
					log.append("Application inexistante")
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
							appli, _continuer, appUsed = jarvis(_images, 0)
						elif item[0] == "reinitialiser.exe" and input[0] == "reinitialiser.exe" : #lance réinitialiser
							appli, _continuer, appUsed = reinitialiser(_images, ",,,,")
						else : #message d'erreur
							log.append("Executable inexistant") 
							ligne+=20
							printLog(log, _images)
							break
					elif extension_de_l_input[1] == "txt" and item[1] == "txt" : #si txt détecté
						if item[0] == input[0] :
							appli, _continuer, appUsed = openTXT(goto(path+"/"+item[0]+"."), _images)
							break
					else : #message d'erreur
						if extension_de_l_input[1] == "exe" :
							log.append("Executable inexistant")
							ligne+=20
						elif extension_de_l_input[1] == "txt" :
							log.append("Fichier texte inexistant")
							ligne+=20
						else :
							log.append("Commande inexistante")
							ligne+=20
						printLog(log, _images)
						break
						
			screen.blit(terminalFont.render(path+" > "+text+"_", True, (0, 175, 0)), (125,ligne))
			pygame.display.flip()
			input = None
			log, ligne = scrolling(log, ligne, _images, path)

	return _images, _continuer, path, log, ligne, text, appUsed

def jarvis(_images, step) :
	"""Progamme qui tourne dans le terminal, assistant IA du hacker"""
	#Se référer aux déclarations de variables de Terminal pour comprendre celles-ci
	log = []
	ligne = 270
	dialogues = [ #pour chaque tuple 't' de la liste : 
				  #t[0] => Messages de l'IA  |  t[1] => tuple contenants les réponses disponibles si t[2] = "qcm"  |  t[2] => type de réponse attendue
		("Bonjour ddOS, que puis-je faire pour vous ? ('escape' à tout moment pour quitter)", ("  1 - Je veux les codes", "  2 - Rien du tout, au revoir"), "qcm"),
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
	current_dialogue = step
	log, ligne = printDialogue(log, ligne, dialogues[current_dialogue])
	printLog(log, _images)
	screen.blit(terminalFont.render(answer+" > "+text+"_", True, (0, 175, 0)), (125,ligne))
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
					return False, _continuer, "jarvis;"+str(current_dialogue)
				elif event.pos[0]>iconmessage_coords[0] and event.pos[0]<iconmessage_coords[0]+iconmessage_dim[0] and event.pos[1]>iconmessage_coords[1] and event.pos[1]<iconmessage_coords[1]+iconmessage_dim[1] and event.button == 1 : #Si clic sur icon2 (zone de clic définie par la position et taille de celui-ci)
					#Clic gauche sur "message" => quitte l'appli vers message
					_images = render(_images, (fen_message, fen_message_coords))
					appli=False
					return False, _continuer, "jarvis;"+str(current_dialogue)
				elif event.pos[0]>iconhelp_coords[0] and event.pos[0]<iconhelp_coords[0]+iconhelp_dim[0] and event.pos[1]>iconhelp_coords[1] and event.pos[1]<iconhelp_coords[1]+iconhelp_dim[1] and event.button == 1 : #Si clic sur icon2 (zone de clic définie par la position et taille de celui-ci)
					#Clic gauche sur "iconhelp" => quitte l'appli
					_images = render(_images, (fen_help, fen_help_coords))
					appli=False
					return False, _continuer, "jarvis;"+str(current_dialogue)
				elif event.pos[0]>1205 and event.pos[0]<1225 and event.pos[1]>989 and event.pos[1]<1010 and event.button == 1 :
					#Clic gauche sur la croix en bas à droite  => quitte le jeu
					_continuer = False
					return False, _continuer, "jarvis;"+str(current_dialogue)
					
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
					screen.blit(terminalFont.render(answer+" > "+text+"_", True, (0, 175, 0)), (125,ligne))
					pygame.display.flip()
				elif event.key == K_ESCAPE : 
					return True, True, ""
				else: #sinon
					if len(answer+" > "+text)<93 : #si la ligne ne dépasse pas la longueur maximale du terminal
						text += event.unicode #ajouter le charactère associé à la touche appuyée au champ d'entrée
					#Affichage \/
					printLog(log, _images)
					screen.blit(terminalFont.render(answer+" > "+text+"_", True, (0, 175, 0)), (125,ligne))
					pygame.display.flip()
			
		#Tests des réponses
		if input != None :
			if current_dialogue == 0 : #Si dialogue 1 "Que puis-je faire pour vous ?"
				if input == "1" :
					current_dialogue += 1
					output = True
				elif input == "2" :
					return True, True, ""
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
					return True, True, ""
				else :
					output = False

			#Pour avoir le bon texte de demande de réponse
			if dialogues[current_dialogue][2] == "qcm" :
				answer = "Réponse n°"
			elif dialogues[current_dialogue][2] == "text" :
				answer = "Réponse libre"

			#Si output = True alors afficher la question entière
			if output == True :
				log = []
				ligne = 270
				log, ligne = printDialogue(log, ligne, dialogues[current_dialogue])
				log, ligne = scrolling(log, ligne, _images, answer)
				printLog(log, _images)
				screen.blit(terminalFont.render(answer+" > "+text+"_", True, (0, 175, 0)), (125,ligne))
				pygame.display.flip()
				output = False
			else : #Sinon afficher juste la ligne
				if dialogues[current_dialogue][2] == "qcm" :
					log.append("Réponse invalide, veuillez entrer un des chiffres proposés")
					ligne+=20
				elif dialogues[current_dialogue][2] == "text" :
					log.append("Mauvaise réponse")
					ligne+=20
				printLog(log, _images)
				screen.blit(terminalFont.render(answer+" > "+text+"_", True, (0, 175, 0)), (125,ligne))
				pygame.display.flip()

			input = None
					
	return True, _continuer, ""

def reinitialiser(_images, m) :
	"""Progamme qui tourne dans le terminal, permet de reinitialiser le PC du hacker (nécessite les 5 codes)"""
	#Se référer aux déclarations de variables de Terminal pour comprendre celles non expliquées
	log = []
	log.append("Pour réinitialiser l'ordinateur, veuillez rentrer les mots de passe de sécurité")
	log.append("'escape' pour quitter l'application")
	log.append("")
	log.append("Mot de passe 1 : ")
	log.append("Mot de passe 2 : ")
	log.append("Mot de passe 3 : ")
	log.append("Mot de passe 4 : ")
	log.append("Mot de passe 5 : ")
	log.append("")
	log.append("")
	
	ligne = 330

	printLog(log, _images)

	#mdp => champs de texte de chaque mot de passe à rentrer
	mdp = m.split(',')
	for i in range(len(mdp)) :
		if i != 0 :
			log[3+i] = "Mot de passe "+str(i+1)+" : "+mdp[i]
	printLog(log, _images)
	correctmdp = ["489a6282A", "arpanet", "0000 1001", "pbadC#gud", "oJrVfMbOtJ"] #liste des mdp attendus
	text = mdp[0]
	screen.blit(terminalFont.render(text+"_", True, (0, 175, 0)), (313,ligne))
	pygame.display.flip()
	currentInput = 0 #Current mot de passe modifié
	input = None
	output = False
	appli = True
	_continuer = True

	while appli :
		ligne = 330 + currentInput*20
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
					return False, _continuer, "reinit;"+str(mdp[0])+","+str(mdp[1])+","+str(mdp[2])+","+str(mdp[3])+","+str(mdp[4])
				elif event.pos[0]>iconmessage_coords[0] and event.pos[0]<iconmessage_coords[0]+iconmessage_dim[0] and event.pos[1]>iconmessage_coords[1] and event.pos[1]<iconmessage_coords[1]+iconmessage_dim[1] and event.button == 1 : #Si clic sur icon2 (zone de clic définie par la position et taille de celui-ci)
					#Clic gauche sur "message" => quitte l'appli vers message
					_images = render(_images, (fen_message, fen_message_coords))
					appli=False
					return False, _continuer, "reinit;"+str(mdp[0])+","+str(mdp[1])+","+str(mdp[2])+","+str(mdp[3])+","+str(mdp[4])
				elif event.pos[0]>iconhelp_coords[0] and event.pos[0]<iconhelp_coords[0]+iconhelp_dim[0] and event.pos[1]>iconhelp_coords[1] and event.pos[1]<iconhelp_coords[1]+iconhelp_dim[1] and event.button == 1 : #Si clic sur icon2 (zone de clic définie par la position et taille de celui-ci)
					#Clic gauche sur "iconhelp" => quitte l'appli
					_images = render(_images, (fen_help, fen_help_coords))
					appli=False
					return False, _continuer, "reinit;"+str(mdp[0])+","+str(mdp[1])+","+str(mdp[2])+","+str(mdp[3])+","+str(mdp[4])
				elif event.pos[0]>1205 and event.pos[0]<1225 and event.pos[1]>989 and event.pos[1]<1010 and event.button == 1 :
					#Clic gauche sur la croix en bas à droite  => quitte le jeu
					_continuer = False
					return False, _continuer, "reinit;"+str(mdp[0])+","+str(mdp[1])+","+str(mdp[2])+","+str(mdp[3])+","+str(mdp[4])
					
			#Pour écrire
			elif event.type == KEYDOWN:
				log[9] = ""
				if event.key == K_RETURN or event.key == K_DOWN : #Si entrée ou flèche bas appuyée
					if currentInput < 4 :
						input = text #Récupérer la valeur entrée
						mdp[currentInput] = input
						log[3+currentInput] = "Mot de passe "+str(1+currentInput)+" : "+mdp[currentInput]
						currentInput += 1
						text = mdp[currentInput]
						ligne = 330 + currentInput*20
						log[3+currentInput] = "Mot de passe "+str(1+currentInput)+" : "
						printLog(log, _images)
						screen.blit(terminalFont.render(text+"_", True, (0, 175, 0)), (313,ligne))
						pygame.display.flip()
					else :
						log[3+currentInput] = "Mot de passe "+str(1+currentInput)+" : "+mdp[currentInput]
						currentInput += 1
				elif event.key == K_UP: #Si flèche haut appuyée
					if currentInput > 0 :
						input = text #Récupérer la valeur entrée
						mdp[currentInput] = input
						log[3+currentInput] = "Mot de passe "+str(1+currentInput)+" : "+mdp[currentInput]
						currentInput -= 1
						text = mdp[currentInput]
						ligne = 330 + currentInput*20
						log[3+currentInput] = "Mot de passe "+str(1+currentInput)+" : "
						printLog(log, _images)
						screen.blit(terminalFont.render(text+"_", True, (0, 175, 0)), (313,ligne))
						pygame.display.flip()
				elif event.key == K_BACKSPACE: #Si retour appuyé
					text = text[:-1] #supprime dernier charactère
					#Affichage \/
					printLog(log, _images)
					screen.blit(terminalFont.render(text+"_", True, (0, 175, 0)), (313,ligne))
					pygame.display.flip()
				elif event.key == K_ESCAPE : 
					return True, True, ""
				else: #sinon
					if len("Mot de passe ? : > "+text)<93 : #si la ligne ne dépasse pas la longueur maximale du terminal
						text += event.unicode #ajouter le charactère associé à la touche appuyée au champ d'entrée
					#Affichage \/
					mdp[currentInput] = text
					printLog(log, _images)
					screen.blit(terminalFont.render(text+"_", True, (0, 175, 0)), (313,ligne))
					pygame.display.flip()

		if currentInput > 4 :
			#test si mdp sont bons
			for i in range(len(mdp)) :
				if mdp[i] != correctmdp[i] :
					break
				return False, False, "win" #victoire
			currentInput = 0
			text = mdp[currentInput]
			ligne = 330 + currentInput*20
			log[3+currentInput] = "Mot de passe "+str(1+currentInput)+" : "
			log[9] = "Un ou plusieurs mot de passe sont incorrects, vérifez l'ordre et l'orthographe"
			printLog(log, _images)
			screen.blit(terminalFont.render(text+"_", True, (0, 175, 0)), (313,ligne))
			pygame.display.flip()

	return True, True, ""

#=========================================================================#
#======================= VARIABLES ET INITALISATIONS =====================#
#=========================================================================#
pygame.init()
pygame.font.init()

#Polices
messageFont = pygame.font.SysFont('Arial', 30)
messageFontpetit = pygame.font.SysFont('Arial', 20)
terminalFont = pygame.font.Font('img/callCode.ttf', 20)

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

#Chargement de l'icone d'aide au terminal
iconhelp = pygame.image.load("img/iconhelp.png").convert()
iconhelp_coords = (200,989)
iconhelp_dim = iconhelp.get_size()

#Chargement de la fenêtre de terminal
fen_terminal = pygame.image.load("img/fen_terminal.png").convert()
fen_terminal_dim = fen_terminal.get_size()
fen_terminal_coords = ((screen_dim[0]-fen_terminal_dim[0])/2, (screen_dim[1]-fen_terminal_dim[1])/2)

#Chargement de la fenêtre de message
fen_message = pygame.image.load("img/fen_message.png").convert()
fen_message_dim = fen_message.get_size()
fen_message_coords = ((screen_dim[0]-fen_message_dim[0])/2, (screen_dim[1]-fen_message_dim[1])/2)

#Chargement de la fenêtre d'aide au terminal
fen_help = pygame.image.load("img/fen_help.png").convert()
fen_help_dim = fen_help.get_size()
fen_help_coords = ((screen_dim[0]-fen_help_dim[0])/2, (screen_dim[1]-fen_help_dim[1])/2)

#Chargement de la case popup
iconpopup = pygame.image.load("img/blanc.jfif").convert()
iconpopup_dim = iconpopup.get_size()
print(iconpopup_dim)
iconpopup_coords=(1000,750) 

#Chargement de l'image peinture
peinture = pygame.image.load("img/peinture.png").convert()
peinture_dim = peinture.get_size()
peinture_coords = (490,240)

images = [(peinture, peinture_coords), (background, (0,0)), (iconterminal, iconterminal_coords), (iconmessage, iconmessage_coords), (iconhelp, iconhelp_coords)] #Prépare la liste pour l'affichage des éléments
pygame.key.set_repeat(400, 30) #Active la possibilité de rester appuyer sur une touche


#=========================================================================#
#=================================== JEU =================================#
#=========================================================================#
g_info = [["Vous avez reçu un nouveau message"], ["en provenance du Boss"], [""], ["Cliquez sur la boîte mail"], ["pour le consulter"], ["Cliquez ici pour fermer"]]
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
				#Clic sur gauche sur "iconterminal"
				images = render(images, (fen_terminal, fen_terminal_coords))
			elif event.pos[0]>iconmessage_coords[0] and event.pos[0]<iconmessage_coords[0]+iconmessage_dim[0] and event.pos[1]>iconmessage_coords[1] and event.pos[1]<iconmessage_coords[1]+iconmessage_dim[1] and event.button == 1 : #Si clic sur icon2 (zone de clic définie par la position et taille de celui-ci)
				#Clic sur gauche sur "iconmessage"
				images = render(images, (fen_message, fen_message_coords))
			elif event.pos[0]>iconhelp_coords[0] and event.pos[0]<iconhelp_coords[0]+iconhelp_dim[0] and event.pos[1]>iconhelp_coords[1] and event.pos[1]<iconhelp_coords[1]+iconhelp_dim[1] and event.button == 1 : #Si clic sur icon2 (zone de clic définie par la position et taille de celui-ci)
				#Clic sur gauche sur "iconhelp"
				images = render(images, (fen_help, fen_help_coords))
			elif event.pos[0]>1205 and event.pos[0]<1225 and event.pos[1]>989 and event.pos[1]<1010 and event.button == 1 : #Si clic sur icon2 (zone de clic définie par la position et taille de celui-ci)
				#Clic gauche sur la croix en bas à droite
				continuer = False

	#Affichage du jeu (affichage des _imageses dans l'ordre + rafraichissement de l'écran)
	render(images, None)
	pygame.display.flip()
	#Appel des fonctions associés à l'application en premier plan
	if images[len(images)-1][0] == fen_terminal:
		images, continuer, g_path, g_log, g_ligne, g_text, g_appUsed = Terminal(images, g_path, g_log, g_ligne, g_text, g_appUsed)
	elif images[len(images)-1][0] == fen_message:
		images, continuer, messages, g_compte, compte, utilisateur, g_champ, g_countreturn, text = message(images, messages, g_compte, compte, utilisateur, g_champ, g_countreturn, text)

if g_appUsed == "win" :
	print("Victoire")
pygame.quit()