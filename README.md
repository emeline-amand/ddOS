# ddOS
Le projet de NSI

### Présentation
ddOS sera un jeu type escape-game programmé en python et HTML où l'on incarne un white hacker (hacker au service de la police) et où l'on doit s'introduire dans le PC d'un hacker pour effacer des informations top secrètes de l'État que celui-ci a volé.

### Informations techniques
L'interface du jeu sera un ordinateur très sommaire entièrement simulé via du code HTML et Python, l'une des applications de cet ordinateur sera un terminal (codé en python) qui permettra d'accéder au PC du hacker a distance en utilisant des commandes ("dir", "cd", etc...). Une appliaction de l'ordinateur du white hacker donnera toute l'aide nécessaire pour naviguer via ce terminal.
L'intégration dy python dans le HTML se fait via un server python et CGI

### Répartition des tâches
Maintenant que la base du jeu est faite (PC du héro), il faut faire les applications qui s'y attachent, Émeline s'occupe de faire une application de message, l'application d'indices (donc un moyen pour le programme de voir la progression du joueur), et le l'explorateur de fichier du PC du héro (très sommaire), et Anatole s'occupe de faire le PC du hacker, ce qui signifie : faire un terminal, faire une application annexe pour afficher les commandes pour naviguer dedans, faire la nivgation dans les fichiers, faire l'endroit où il faut rentrer les 5 codes pour gagner, faire l'assistant personnel qui permettra de récupérer un des codes, et empêcher cette application se reset lorsqu'elle est basculée en second plan

### Fichiers
Comme vous pouvez le constater, il y a trois main (main.py, main1.py, et main2.py). 'main.py' est la base des deux suivants, c'est juste le PC du héro, fonctionnel, mais vide. 'main1.py' est le fichier sur lequel travaille Anatole, il s'agit de 'main.py' avec en plus ce qui est listé à son nom dans la partie 'répartition des tâches' (ce n'est pas fini donc il n'y a pas tout), le fichier est cependant fonctionnel et il est possible de le lancer avec python et pygame pour le tester. Et enfin, 'main2.py' est comme 'main.py' mais avec le travil d'Émeline, il est fonctionnel aussi (du moins à l'heure à laquelle j'écrit ces lignes) donc il également possible de le tester

Il faut ignorer les dossiers .git, .vs, et __pycache__, ils viennent des applications utilisées pour pour le projet