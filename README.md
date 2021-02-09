# ddOS
Le projet de NSI

### Présentation
ddOS sera un jeu type escape-game programmé en python où l'on incarne un white hacker (hacker au service de la police) et où l'on doit s'introduire dans le PC d'un hacker pour effacer des informations top secrètes de l'État que celui-ci a volé.

### Informations techniques
L'interface du jeu sera un ordinateur très sommaire entièrement simulé via du code Python, l'une des applications de cet ordinateur sera un terminal qui permettra d'accéder au PC du hacker a distance en utilisant des commandes ("dir", "cd", etc...). Une appliaction de l'ordinateur du white hacker donnera toute l'aide nécessaire pour naviguer via ce terminal.

### Répartition des tâches
Maintenant que la base du jeu est faite (PC du héro), il faut faire les applications qui s'y attachent, Émeline s'occupe de faire une application de message, l'application d'indices (donc un moyen pour le programme de voir la progression du joueur), et le l'explorateur de fichier du PC du héro (très sommaire), et Anatole s'occupe de faire le PC du hacker, ce qui signifie : faire un terminal, faire une application annexe pour afficher les commandes pour naviguer dedans, faire la nivgation dans les fichiers, faire l'endroit où il faut rentrer les 5 codes pour gagner, faire l'assistant personnel qui permettra de récupérer un des codes, et empêcher cette application se reset lorsqu'elle est basculée en second plan

### Fichiers
Comme vous pouvez le constater, il y a trois main (main.py, main1.py, et main2.py). 'main.py' est la base des deux suivants, c'est juste le PC du héro, fonctionnel, mais vide. 'main1.py' est le fichier sur lequel travaille Anatole.  Et enfin, 'main2.py' est comme 'main.py' mais avec le travail d'Émeline, il est aussi  fonctionnel on peut également le tester en lançant python et pygame.

Il faut ignorer les dossiers .vs, et \_\_pycache\_\_, ils viennent des applications utilisées pour pour le projet

### Utilisation
Pour utiliser les dossiers main1.py et main2.py , il faut télécharger le dossier img et le mettre dans le même répertoire que main1 ou main2.

### main1.py par Anatole
Il s'agit de 'main.py' avec en plus ce qui est listé à son nom dans la partie 'répartition des tâches' (ce n'est pas fini donc il n'y a pas tout), le fichier est cependant fonctionnel et il est possible de le lancer avec python et pygame pour le tester. Le mot de passe du PC du hacker est "111221" et actuellement, tous les dossiers sont vides sauf "Applications", dans lequel seulement "jarvis.exe" fait quelque chose (mais aucune intéraction n'est possible et pour quitter jarvis il faut fermer et réouvrir le terminal). Les commandes disponibles sont : ls, pour lister les fichiers présents dans le chemin actuel; cd, pour entrer dans un dossier (syntaxe : cd nonDuDossier); exit, pour retourner à l'écran de login; et clear, pour effacer tous les précédents messages du terminal

### main2.py par Emeline
Il s'agit de 'main.py' avec en plus la fonction message. Cette fonction permet de faire appaître à l'écran les émeteurs suivis des objets des messages. En cliquant sur l'objet ou l'émetteur d'un message, l'écran affiche le contenu du message (pour l'instant il sera seulement écrit "message1" ou "message2"...) ainsi que la touche return qui, une fois cliquée, renvoie à la liste des émetteurs et objets des messages. 

### Difficultées passées
Parmit les difficultées rencontrées, nous avons dû choisir le langage à utiliser, en effet, nous étions indécit quant à utiliser le html et python mélangé ou uniquement du pyhton, après quelques recherches et tests, nous avons décidés de partir pleinement sur du python. Un deuxième problème auquels nous avons faits face est la planification de l'histoire et des énigmes, car nous n'étions pas encore certains des moyens dont nous allions disposer et donc des énigmes possibles. Ensuite, un autre problème qui nous a causé pas mal de reflexion et la taille de la fenêtre pygame, nous étions partis pour faire une taille qui s'adapte à l'écran actuel, mais cela posait un trop gros défi, ce qui nous a mené vers le choix d'une résolution fixe qui correspond à la taille de la plupart des écrans du CIV. A part cela, nous avons subit une montagne de bugs, que nous avons résolus plus ou moins bien.

### Difficultées actuelles
Nous sommes toujours en train de planifier certaines énigmes et paufiner l'histoire mais nous ne rencontrons pas de difficulté majeures actuellement car nous venons tous les deux de finir une grosse partie du code de notre jeu, ce qui signifie que les problèmes ne sont plus que passés ou futurs

### Difficultées futures
Nous hésitons à créer un explorateur de fichier utilisable sur le PC du héro, pour pouvoir faire des énigmes liées à des images que l'on 'téléchargerait' depuis le PC du hacker, cela s'avèrerait compliqué à faire et nous feront notre choix en fonction de comment les choses avancent et du temps restant. Les autres applications planifiées pour le PC du héro ne requièrent pas beaucoup d'intéractivité, ce que ne les positionnent pas comme défis.

### Aspects techniques
**Structure de donnée :** Pour stocker nos données, nous utilisons principalements des listes, des dictionnaires, et des tuples, en les emboîtants les un dans les autres. Par exemple pour stocker les messages reçus, nous utilisons une liste contenants des listes dont les items sont les objets, contenus, et emmetteurs des messages. Ou pour l'affichage du jeu, nous utilisons des tuples compris dans une liste avec pour items les images et coordonnées de celles-ci
**Modules de bibliothèques :** Nous utilisons les librairies `pygame, os, et math`
**Interfacage entre fonctions :** Notre programme se base beaucoup sur l'utilisation de fonctions, donc pour que celles-ci intéragissent entre elles, à la fin de l'exécution de ces dernières retournent beaucoup de leurs variables pour les assigner à des variables globales qui serviront pour la prochaine exécution de la fontion. Par exemple lorsque l'on quitte une application (dans l'exemple on imaginera que l'on quitte l'application terminal), la fonction associée à l'application retournera les variables `ligne, path, log, text, images, et continuer` et s'en servira comme paramètre de la fontion `Terminal()` lors de son prochain appel.