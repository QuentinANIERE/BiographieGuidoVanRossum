"""
Programme conçu dans la cadre de l'enseignement de Spécialité NSI. 
Il permet d'afficher la biographie de Guido van Rossum dans une interface graphique
----------------------------------------------
Réalisé par Quentin ANIERE - 1G1 - 2019 / 2020
"""

from tkinter import *
import tkinter.font as tkFont


#Définition de la fenetre principale
fenPrin = Tk() #fenPrin ==> Fenetre principale
fenPrin.geometry("450x150")
fenPrin.resizable(width=False, height=False)
fenPrin.title("La vie de Guido van Rossum")
fenPrin.configure(bg="grey")
fenPrin.iconbitmap(bitmap="photos/icone.ico")

#Label de nom 
police_nom = tkFont.Font(family="Times",size=24,weight="bold")
nom = Label(fenPrin, text="Guido van Rossum", font=police_nom, bg="Grey")
nom.pack(pady=15)

#Création d'un cadre pour mettre les trois bouttons sur la même ligne
cadre = Frame(fenPrin, bg="Grey")
cadre.pack(side=BOTTOM, pady=25)         

#Création d'une police personalisée pour les bouttons
police_bt = tkFont.Font(family="Times New Roman",size=12)

#Premier boutton ==> Biographie

#Lecture du fichier "bio.txt" qui contient la biographie
biographie = open("textes/bio.txt", "r")
var_biographie = biographie.read()
biographie.close()

#Création de l'image de Guido et de l'easter egg
photo = PhotoImage(file="photos/photo.png")
hac = PhotoImage(file="photos/hac.png")

#Récupération des dates importantes
fichier_dates = open("textes/dates.txt","r")
dates_nt = fichier_dates.read() # "dates_nt" veut dire dates non traités
dates = dates_nt.split("\n")

#Fonction pour sauter des lignes
def saut_ligne(phrase_a_couper):
    phrase_separe = phrase_a_couper.split(" ") #On met tout les mots de la phrase à coupé dans une liste
    chaine = "" 
    #On coupe la phrase en deux et on écrit dans chaine tant que cette dernière ne dépasse pas 32 caractétres
    while len(chaine) < 32:
        if chaine == "":
            chaine = phrase_separe.pop(0)
        else:
            chaine = chaine + " " + phrase_separe.pop(0)

    #On enleve le dernier mot de chaine pour le remettre dans la liste "phrase_separe"
    chaine = chaine.split(" ")
    phrase_separe.insert(0, chaine.pop(-1))
    
    #On re-transforme met le contenu de chaine au format str dans la variable ligne1
    ligne1 = ""
    for longeurliste in range(len(chaine)):
        if ligne1 == "":
            ligne1 = chaine.pop(0)
        else:
            ligne1 = ligne1 + " " + chaine.pop(0)
    
    #On met les autres mots dans la str ligne2
    ligne2 = ""
    for longeurliste in range(len(phrase_separe)):
        if ligne2 == "":
            ligne2 = phrase_separe.pop(0)
        else:
            ligne2 = ligne2 + " " + phrase_separe.pop(0)

    #On met ligne 1 et 2 dans une liste pour retourner proprement
    resultat = []
    resultat.append(ligne1)
    resultat.append(ligne2)
    return resultat

#Fonction Biographie ("biogra")
def biogra():

    #Fonction de fermeture de la fenetre de biographie
    def quitter_biogra():
        fenBio.destroy()

    #Définition de la fenetre
    fenBio = Toplevel()
    fenBio.title("Biographie")
    fenBio.configure(bg="Grey")
    fenBio.geometry("450x350")
    fenBio.resizable(width=False, height=False)
    fenBio.iconbitmap(bitmap="photos/icone.ico")
    fenBio.focus_force() #On force le focus sur la fenetre qu'on vient d'ouvrir

    texte = Label(fenBio, bg="Grey", text=var_biographie, justify=LEFT)
    texte.pack(pady=10)

    bt_quitter_fen_biogra = Button(fenBio, text="Fermer",  font=police_bt, command=quitter_biogra)
    bt_quitter_fen_biogra.pack()

#Définiton du boutton "Biographie"
bt_biographie = Button(cadre, text="Biographie",font=police_bt, command=biogra)
bt_biographie.pack(side=LEFT)


#Deuxième boutton ==> Photo et Dates

#Fonction photo et dates ("phodates")
def phodates():
    #Fonction de fermeture de la fenetre de photo et dates
    def quitter_phodates():
        fenPhoDates.destroy()

    #Définition de la fenetre
    fenPhoDates = Toplevel()
    fenPhoDates.title("Photo et dates marquantes")
    fenPhoDates.configure(bg="Grey")
    fenPhoDates.geometry("450x500")
    fenPhoDates.resizable(width=False, height=False)
    fenPhoDates.iconbitmap(bitmap="photos/icone.ico")
    fenPhoDates.focus_force() #On force le focus sur la fenetre qu'on vient d'ouvrir

    
    #Création d'un Canvas qui contient l'image de Guido
    zone_photo = Canvas(fenPhoDates, bg="Grey", height=211)
    photo_guido = zone_photo.create_image(200, 105,image=photo) 
    zone_photo.pack(pady=10)

    #Petit easter egg :)
      #Fonction qui sera executée si on click gauche sur la zone de la photo 
    def egg(clic):
        zone_photo.delete(photo_guido)
        photo_hac = zone_photo.create_image(180, 105,image=hac)

    #On assigne la fonction "egg" au clic gauche de la souris sur la zone de la photo
    zone_photo.bind("<Button-1>", egg)

    #Créations des polices personalisée
    police_dates = tkFont.Font(family="Times New Roman",size=14,weight="bold")
    police_commentaires = tkFont.Font(family="Times New Roman",size=12)

    #Création d'un cadre 
    cadre = Frame(fenPhoDates, height=100, width=250)
    cadre.pack()
    #Dedans on met un canvas de la même taille et on configurer une barre défilement verticale
    canvas =Canvas(cadre,bg="Grey",width=250,height=200,scrollregion=(0,0,0,0))
    vbar=Scrollbar(cadre,orient=VERTICAL)
    vbar.pack(side=RIGHT,fill=Y)
    vbar.config(command=canvas.yview)
    canvas.config(yscrollcommand=vbar.set)       

    #Boucle for qui sépare les dates et leur commentaire
    dates_separes = []
    for nbr_dates in range(len(dates)):
        chaine = dates[nbr_dates]
        dates_traitement = chaine.split(" - ")
        for longeur_liste in range(len(dates_traitement)):
            dates_separes.append(dates_traitement[longeur_liste])
  
    
    padx = 25 #Combien de pixel de padding vertical
    nbr_ligne = 0 #Nbr de lignes à afficher, détermine la taille de l'ascenseur

    #Boucle for qui ajoute les objets crée un texte avec une font différente suivant si l'indice de l'index et pair ou non
    for nbr_dates in range(len(dates_separes)):

        if nbr_dates%2 == 0 or nbr_dates == 0: #Si l'indice est pair ou égal à 0, donc cela correspond toujours au dates
            a_ecrire =  dates_separes[nbr_dates]
            canvas.create_text(125, padx, text=a_ecrire, font=police_dates)
            nbr_ligne += 1
        else:
            a_ecrire =  dates_separes[nbr_dates]
            #On vérifie que le texte à écrire ne dépasse 32 caractéres, si c'est le cas on utilse la fonction "saut de ligne" afin de le couper en deux
            if len(a_ecrire) > 32:
              liste_lignes = saut_ligne(dates_separes[nbr_dates])
              canvas.create_text(125, padx, text=liste_lignes[0], font=police_commentaires)
              nbr_ligne += 1
              padx += 26
              canvas.create_text(125, padx, text=liste_lignes[1], font=police_commentaires)
              nbr_ligne += 1
            else:
                canvas.create_text(125, padx, text=a_ecrire, font=police_commentaires)
                nbr_ligne += 1
        padx += 25
    
    #On détermine la taille de la Scrollbar avec le nombre de ligne, sachan qu'une ligne à besoin de 26px
    taille_scrobar = nbr_ligne * 26
    canvas.configure(scrollregion=(0,0,0,taille_scrobar))
    #On pack et le tout, et voilà :)
    canvas.pack(side=LEFT,expand=True,fill=BOTH)
    
    bt_quitter_fen_PhoDates = Button(fenPhoDates, text="Fermer",font=police_bt, command=quitter_phodates)
    bt_quitter_fen_PhoDates.pack(pady=15)


#Définiton du boutton " Photo et dates"
bt_phodates = Button(cadre, text="Photo et dates", font=police_bt, command=phodates)
bt_phodates.pack(side=LEFT, padx=10)


#Troisième boutton ==> Quitter
#Fonction Quitter ("quitter")
def quitter():
    fenPrin.destroy()

#Définiton du boutton
bt_quitter = Button(cadre, text="Quitter", font=police_bt, command=quitter)
bt_quitter.pack(side=LEFT)

#On lance la fenetre principale
fenPrin.mainloop()
