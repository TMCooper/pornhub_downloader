import phub
from phub import *
import os


PATH = os.path.dirname(os.path.abspath(__file__))
PATH_VID = os.path.join(PATH, "Vidéo")

Link_porn = input("Quelle est le lien que vous souhaité télécharger ? : ")

client = phub.Client()

video = client.get('https://fr.pornhub.com/view_video.php?viewkey=669e868825c52')
video.download('my-video.mp4', Quality.BEST)

