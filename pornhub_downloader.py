import phub
from phub import *
import os
from bs4 import BeautifulSoup
import re
import requests


PATH = os.path.dirname(os.path.abspath(__file__))
PATH_VID = os.path.join(PATH, "Vidéo")
PATH_PLAY = os.path.join(PATH, "Playlist")
EXTENTION = ".mp4"
QUALITE = Quality.BEST

def main ():
    try:
        client = phub.Client()
        
        lang = input("What is your language ? (FR/EN) : ").lower()

        while lang not in ["fr", "en"]:
            lang = input("What is your language ? FR or EN").lower()
        
        if lang in["en"]:
            print("Press Q if you want to exit the program")
            choix = input("Do you want to download a video or a playlist? V/P: ").lower()

        else:
            print("Appuier sur Q si vous voulez quitté le programme")
            choix = input("Voulez vous télécharger une viéo ou une playlist ? V/P : ").lower()

        while choix not in ["v", "p", "q"]:
            if lang in["en"]:
                choix = input("Please enter V or P: ").lower()

            else:
                choix = input("Veulliez saisir V ou P : ").lower()

        if choix in ["v"]:

            if lang in["en"]:
                Link_porn = input("What is the link you want to download ? : ")
            else:
                Link_porn = input("Quelle est le lien que vous souhaité télécharger ? : ")

            if not os.path.exists(PATH_VID):
                os.mkdir(PATH_VID)
        
            video = client.get(Link_porn)
            titre = PATH_VID+"\\"+video.title+EXTENTION
            video.download(titre, QUALITE)
        
        if choix in ["p"]:

            if lang in ["en"]:
                Link_porn = input("What is the link you want to download? : ")

            else:
                Link_porn = input("Quel est le lien que vous souhaité télécharger ? : ")

            if not os.path.exists(PATH_PLAY):
                    os.mkdir(PATH_PLAY)

            url = Link_porn

            response = requests.get(url)
            html_content = response.text

            soup = BeautifulSoup(html_content, 'html.parser')

            try:
                ID_LP = Link_porn.split("playlist/")[1]

                pattern = re.compile(f'/view_video\.php\?viewkey=[\w]+&pkey={ID_LP}')
                links = set([a['href'] for a in soup.find_all('a', href=True) if pattern.match(a['href'])])        
                
                for i in links:
                    video = client.get(f'https://fr.pornhub.com{i}')
                    titre = PATH_PLAY+"\\"+video.title+EXTENTION
                    video.download(titre, QUALITE)

            except IndexError:
                try:
                    ID_LP = Link_porn.split("&pkey=")[1]
                    url_playlist = (f'https://fr.pornhub.com/playlist/{ID_LP}')

                    url = url_playlist

                    response = requests.get(url)
                    html_content = response.text

                    soup = BeautifulSoup(html_content, 'html.parser')

                    pattern = re.compile(f'/view_video\.php\?viewkey=[\w]+&pkey={ID_LP}')
                    links = set([a['href'] for a in soup.find_all('a', href=True) if pattern.match(a['href'])])

                    for i in links:
                        video = client.get(f'https://fr.pornhub.com{i}')
                        titre = PATH_PLAY+"\\"+video.title+EXTENTION
                        video.download(titre, QUALITE)
                except IndexError:
                    if lang in ["en"]:
                        print("\nError the link you provided is not a playlist please enter the correct option in the future...")
                    else:
                        print("\nErreur le lien que vous avez fournit n'est pas une playlist veulliez saisir la bonne option a l'avenir..")
                    return

        if choix in ["q"]:
            exit()
    except KeyboardInterrupt:
        if lang in ["en"]:
            print("\nCTRL + C entered by the user to stop the program...")
        else:
            print("\nCTRL + C saisit par l'utilisateur arret du programme...")

if __name__ == "__main__":
    main()