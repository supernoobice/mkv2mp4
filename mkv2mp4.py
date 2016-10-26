# converst MKV and WEBM files to MP4
import os
from os import listdir
from os.path import isfile, join

clips = [f for f in listdir(".") if isfile(join(".", f))]
counter = 0
for_encoding = []

for clip in clips:

	clean_title = clip.replace("'", "")
	os.rename(clip, clean_title)

	if clean_title.lower().endswith('.webm') or clean_title.lower().endswith('.mkv'):
		file_name = clean_title.split('.')

		if file_name[0] + ".mp4" in clips:
			print "[!] " + file_name[0] + ".mp4" + " already exists."

		else:
			
			for_encoding.append(clean_title)
			counter = counter + 1
			print "[+] " + clean_title

print "[*] " + str(counter) + " ready for encoding... "
answer = raw_input("Proceed [Y/n]?")

if answer == "Y":

	for clip in for_encoding:
		file_extensions = clip.split(".")

		os.system("ffmpeg -i '" + clip + "' -f mp4 -preset medium '" + file_extensions[0] + ".mp4'");

	os.system('open .')

else: 
	print "Ok, aborting..."
