#Prototype du PC du hacker

#Arbre de dossier créé avec des dictionnaires imbriqués
files = {'C:':{'dossier1':{'fichier1':1, 'dossier2':{}},'dossier3':{'fichier2':2, 'dossier4':{'fichier3':3, 'fichier4':4}}}}


#fonction qui affiche les clés d'un dictionnaire mais joliment
def printDictKeys(dict) :
    for key in dict.keys() :
        print(key)

 #commande qui accède à un dossier en mettant à jour la variable chemin
def cd(p, target) :
    if target == '..' :
        p = p.split('/')
        del p[len(p)-1]
        for element in p :
            newP = element+'/'
        newP = newP[:len(newP)-1]
        return newP
    else :
        p = p+'/'+target
        return p

#commande qui liste les fichiers et dossier présents dans le dossier où l'on se trouve
def ls(p) :
    print("")
    print("Showing files from : '"+p+"'")
    print("")
    p = p.split('/')
    current = files[p[0]]
    for i in range(len(p)-1):
        current = current[p[i+1]]
    printDictKeys(current)
    print("")


path = 'C:'
#répéter indéfiniment
while 1>0 :
    do = input("{}> ".format(path))
    do = do.split(' ')
    if do[0] == 'ls' :
        ls(path)
    elif do[0] == 'cd' :
        path = cd(path, do[1])
        ls(path)
    elif do[0] == 'exit' :
        break


#Bug à résoudre : reconstruction de la variable path lors de "cd .."