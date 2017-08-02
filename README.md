# google-music-playlist
Download songs from Google Play playlist

##################################################

MANUAL

1. Installation of necessary software
	apt-get install python-pip
	pip install gmusicapi

2. Copy and unzip this package in your folder. 
	Example: 
		/home/google-music-playlist

3. Rename file config.py.dist to config.py

4. Create destenation media folder
	Example: 
		mkdir /home/google-music-playlist/out

5. Edit file config.py 
	Example:
		login = 'yourmail@gmail.com'
		password = 'yourpassword'
		playlist = 'Name_Playlist'
		path = "/home/google-music-playlist/out"

6. Run script
	Example:
		python /home/google-music-playlist/load.py
    
##################################################
