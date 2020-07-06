import os
import requests
import re
from shutil import copyfile

if not os.path.exists('music/'):
	os.makedirs('music')

thePath = "C:/Users/" + os.getlogin() + "/AppData/Local/GeometryDash/"
newgroundPath = "https://www.newgrounds.com/audio/listen/"

if not os.path.exists(thePath):
	thePath = "C:/Users/" + os.getlogin() + "/AppData/Local/Geometry Dash/"
	if not os.path.exists(thePath):
		with open('log.txt', "w+") as error_file:
			error_file.write("Sorry, I can't find Geometry Dash folder on your computer :/")
			error_file.close()
			quit()


totalLen = len([name for name in os.listdir(thePath)])
i = 0

for f in os.listdir(thePath):
	if f.endswith('.mp3'):
		f_ext = os.path.splitext(f)
		response = requests.get(newgroundPath + f_ext[0])
		title = re.search('(?<=<title>).+?(?=</title>)', response.content.decode(), re.DOTALL).group().strip()
		
		for char in title:
			if char in "\\/*[]%^&~:;":
				title = title.replace(char, '')

		copyfile(thePath + f, "music/" + title + ".mp3")

		i += 1
		print(round((i / totalLen) * 100), "%")

with open('log.txt', 'w+') as f:
	f.write("Completed!\n" + str(totalLen) + " - files converted")
	f.close()