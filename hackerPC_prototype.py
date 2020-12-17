#Prototype du PC du hacker

#Arbre de dossier créé avec des dictionnaires imbriqués (nom du dossier = clé et contenu du dossier = dictionnaire)
files = {'C:':{'dossier1':{'fichier1':1, 'dossier2':{}},'dossier3':{'fichier2':2, 'dossier4':{'fichier3':3, 'fichier4':4}}}}


def printDictKeys(dict) :
    '''fonction qui affiche les clés d'un dictionnaire mais joliment. Prend en paramètre le dictionnaire dont l'on veut imprimer les clés'''
    for key in dict.keys() :
        print(key)

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
            print("Chemin cible inexistant")
            return p
        if p  == 'C:/' : #Si au minimum alors
            p = p[:len(p)-1] #retire le '/' de fin uniquement présent au dossier racine de l'arbre
        p = p+'/'+target
        return p

def ls(p) :
    '''fonction qui simule la commande qui liste les fichiers et dossier présents dans le dossier où l'on se trouve. Prend en param le chemin actuel'''
    #Affiche le path actuel
    print("Affichage des fichers depuis : '"+p+"'")
    print("")
    #prépare le path pour la navigation à travers le dictionnaire
    p = convertPath(p)
    #Va jusqu'au chemin spécifié en redéfinissant plusieurs fois current pour être le dictionnaire de fin demandé
    current = files[p[0]]
    for i in range(len(p)-1):
        current = current[p[i+1]]
    #Affiche les clés présentes dans le chemin demandé
    printDictKeys(current)
    print("")

#Initalise la variable path a la racine de l'arbre de dossier
path = 'C:/'

#répéter indéfiniment
while 1>0 :
    do = input("{}> ".format(path))
    do = do.split(' ')
    if do[0] == 'ls' :
        ls(path)
    elif do[0] == 'cd' :
        path = cd(path, do[1])
        print("")
    elif do[0] == 'exit' :
        break