from gmusicapi import Mobileclient

import config
from mutagen.id3 import ID3, TPE1, ID3NoHeaderError
from mutagen.easyid3 import EasyID3
import os
import time
import urllib2

def buildFileName(track):
    name = "%s - %s (%s)" % (track["track"]["artist"], track["track"]["title"], track["track"]["album"])
    name = name.replace('/', '-') + ".mp3"
    return name

def loadTrack(track):
    if type(track) == type(None):
        return False

    name = buildFileName(track)
    file_name = config.path + "/" + name

    if os.path.isfile(file_name):
        print name + " already exists"
        return False

    url = api.get_stream_url(track["trackId"])
    f = open(file_name, 'wb')
    u = urllib2.urlopen(url)
    meta = u.info()
    file_size = int(meta.getheaders("Content-Length")[0])
    print "Downloading: %s Bytes: %s" % (file_name, file_size)

    file_size_dl = 0
    block_sz = 8192
    while True:
        buffer = u.read(block_sz)
        if not buffer:
            break

        file_size_dl += len(buffer)
        f.write(buffer)
        status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
        status = status + chr(8)*(len(status)+1)
        print status,

    f.close()

    audio = EasyID3()
    audio['title'] = track["track"]["title"]
    audio['artist'] = track["track"]["artist"]
    audio['album'] = track["track"]["album"]
    audio['composer'] = track["track"]["composer"]
    audio.save(file_name)

    return True

def loadPlaylist(playlist):
    for track in playlist["tracks"]:
        if loadTrack(track):
            time.sleep(2)

api = Mobileclient()
api.login(config.login, config.password, Mobileclient.FROM_MAC_ADDRESS)

platlists = api.get_all_user_playlist_contents()

for playlist in platlists:
    if playlist.get('name') == config.playlist:
        loadPlaylist(playlist)
