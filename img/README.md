# ddOS
Le projet de NSI

### Présentation
ddOS sera un jeu type escape-game programmé en python et HTML où l'on incarne un white hacker (hacker au service de la police) et où l'on doit s'introduire dans le PC d'un hacker pour effacer des informations top secrètes de l'État que celui-ci a volé.

### Informations techniques
L'interface du jeu sera un ordinateur très sommaire entièrement simulé via du code HTML et Python, l'une des applications de cet ordinateur sera un terminal (codé en python) qui permettra d'accéder au PC du hacker a distance en utilisant des commandes ("dir", "cd", etc...). Une appliaction de l'ordinateur du white hacker donnera toute l'aide nécessaire pour naviguer via ce terminal.
L'intégration dy python dans le HTML se fait via un server python et CGI

### Répartition des tâches
Émeline s'occupe de faire une version fonctionnelle du bureau du héro dans le serveur python et Anatole s'occupe d'y intégrer le PC du hacker (faux terminal)
