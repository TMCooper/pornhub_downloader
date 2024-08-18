import phub
from phub import *
import os


PATH = os.path.dirname(os.path.abspath(__file__))
PATH_VID = os.path.join(PATH, "Vidéo")
EXTENTION = ".mp4"
QUALITE = Quality.BEST

def main ():
    client = phub.Client()
    
    choix = input("Voulez vous télécharger une viéo ou une playlist ? : ")

    while choix not in ["V", "v", "P", "p"]:
        choix = input("Veulliez saisir V ou P : ")

    if choix in ["V", "v"]:

        Link_porn = input("Quelle est le lien que vous souhaité télécharger ? : ")

        if not os.path.exists(PATH_VID):
            os.mkdir(PATH_VID)
    
        video = client.get(Link_porn)
        titre = PATH_VID+"\\"+video.title+EXTENTION
        video.download(titre, QUALITE)
    

if __name__ == "__main__":
    main()