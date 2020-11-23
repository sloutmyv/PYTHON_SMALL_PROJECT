#!/usr/bin/env python
# -*- coding: utf-8 -*-

#################################################################################################
# Projet : 			Cadeaux Noel
# Participant(s): 	Sylvain C.
# Lieu / Date : 	15/10/2015 - Paris
# Update :          22/11/2020 - New Caledonia
# Explication(s):
#################################################################################################

from random import randint
import smtplib, os, re
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#------------------------------------------------------------------------------#
# Fonctions Globales
#------------------------------------------------------------------------------#
def read_file(fichier):
    """ Lire un fichier"""
    with open(fichier, 'r') as fin: return fin.read()

def write_file(fichier, txt, arg):
    """ Ecrire dans un fichier """
    with open(fichier, arg) as fout: return fout.write(txt)

def write_email(me,toaddr,objet,message):
    msg=MIMEMultipart()
    msg['From']=me
    msg['To']=toaddr
    msg['Subject']=objet
    body=message
    msg.attach(MIMEText(body,'html'))
    return(msg)

# current path
cur_path = os.path.dirname(__file__)
print(cur_path)

if __name__ == "__main__":

    YEAR = 2020

    # Liste des participants de l'année en cours
    liste_participants = ["Adrien","Alexis","Anais","Anne","Bastien","Chloe","Clement",
    "Colas","Eric","Eva","Guillaume","Guimauve","Julie","Kevin","Laure","Loris","Marine","Mathilde","Quentin","Romane",
    "Samy","Tanguy","Thomas"]

    print("Cette année il y a %d participants" %(len(liste_participants)))

    filedir = "C:\\Users\\Sloutmyv\\Documents\\Programmation\\github\\PYTHON_SMALL_PROJECT\\Databases\\"

    if os.path.isfile(filedir + "Noel_" + str(YEAR) + "_memory.txt"):
        print("Le fichier Noel_" + str(YEAR) + "_memory.txt existe")
    else:
        if os.path.isfile(filedir + "Noel_" + str(YEAR-1) +"_memory.txt"):
            liste_tmp = [i for i in re.findall(".*",read_file(filedir + "Noel_" + str(YEAR-1) +"_memory.txt")) if i != '']
            liste_tampon = []
            for line in liste_tmp:
                el = [i for i in re.split("\s+",line) if i != '']
                if el[0] in liste_participants:
                    validateur = False
                    while validateur != True:
                        nb_aleatoire = randint(0,len(liste_participants)-1)
                        cible = liste_participants[nb_aleatoire]

                        # Conditions
                        if cible not in el and cible not in liste_tampon:
                            if (el[0] == "Anais" and cible == "Bastien") or (el[0] == "Bastien" and cible == "Anais"):
                                pass
                            elif (el[0] == "Eva" and cible == "Colas") or (el[0] == "Colas" and cible == "Eva"):
                                pass
                            elif (el[0] == "Laure" and cible == "Quentin") or (el[0] == "Quentin" and cible == "Laure"):
                                pass
                            elif (el[0] == "Romane" and cible == "Tanguy") or (el[0] == "Tanguy" and cible == "Romane"):
                                pass
                            elif (el[0] == "Caroline" and cible == "Florent") or (el[0] == "Florent" and cible == "Caroline"):
                                pass
                            elif (el[0] == "Chloe" and cible == "Kevin") or (el[0] == "Kevin" and cible == "Chloe"):
                                pass
                            elif (el[0] == "Mathilde" and cible == "clement") or (el[0] == "clement" and cible == "Mathilde"):
                                pass
                            elif (el[0] == "Loris" and cible == "Marine") or (el[0] == "Marine" and cible == "Loris"):
                                pass
                            elif (el[0] == "Mathilde" and cible == "Anne") or (el[0] == "Anne" and cible == "Mathilde"):
                                pass
                            else:
                                validateur = True
                                liste_tampon.append(cible)
                                el.append(cible)
                        else:
                            pass

                elif el[0] == 'Name':
                    el.append(str(int(el[len(el)-1])+1))
                else:
                    el.append('NaN')

                txt = ""
                for i in range(len(el)):
                    txt += el[i]+"   "
                txt +="\n"
                write_file(filedir+"Noel_" + str(YEAR) + "_memory.txt", txt, 'a')
        else:
            print("Erreur : le fichier n'existe pas")


# Envoie des mails
    if os.path.isfile(filedir + "my_adress"):
        liste_syc = [i for i in re.findall(".*",read_file(filedir + "my_adress")) if i != '']
        me = liste_syc[0]
        mdp = liste_syc[1]

    liste_tmp2 = [i for i in re.findall(".*",read_file(filedir+"Noel_" + str(YEAR) + "_memory.txt")) if i != '']
    liste_tmp2.pop(0)

    objet = "Noel Plantes & Fleurs " + str(YEAR)

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(me,mdp)

    for i in range(len(liste_tmp2)):
        list_tmp3 = liste_tmp2[i].split()
        print(list_tmp3)
        if list_tmp3[-1] == "NaN":
            pass
        else:
            toaddr = list_tmp3[1]
            message = """
<p>Salut <strong>%s</strong> !&nbsp;</p>
<p>Cette ann&eacute;e , tu devras offrir un cadeau &agrave; <span style="color: #ff0000;"><strong>%s</strong></span>.</p>
<p>Th&egrave;me : Pimp my gift : On r&eacute;cup&eacute;re, On r&eacute;pare, On transforme, On offre !</p>
<p>Ne jamais divulger le nom de la personne jusqu'&agrave; la remise du cadeau.</p>
<p>Merci de me confirmer la bonne reception de ce mail sur fb ou messenger&nbsp;<strong><span style="text-decoration: underline;">mais sans r&eacute;pondre au mail</span></strong> afin que je ne vois pas ta cible.</p>
<p>Bonne recherche</p>
<p>A bientot !</p>
<p>&nbsp;</p>
<p><span style="color: #999999;"><em><span style="font-size: 9pt;">R&eacute;sum&eacute; des No&euml;ls pr&eacute;c&eacute;dents :&nbsp;</span></em></span></p>
<p><span style="color: #999999;"><em><span style="font-size: 9pt;">2019 : %s&nbsp;</span></em></span></p>
<p><span style="color: #999999;"><em><span style="font-size: 9pt;">2018 : %s&nbsp;</span></em></span></p>
<p><span style="color: #999999;"><em><span style="font-size: 9pt;">2017 : %s&nbsp;</span></em></span></p>
<p><span style="color: #999999;"><em><span style="font-size: 9pt;">2016 : %s&nbsp;</span></em></span></p>
            """ %(list_tmp3[0],list_tmp3[6],list_tmp3[5],list_tmp3[4],list_tmp3[3],list_tmp3[2])

            msg = write_email(me,toaddr,objet,message)
            text = msg.as_string()
            s.sendmail(me,toaddr,text)

    s.quit()
