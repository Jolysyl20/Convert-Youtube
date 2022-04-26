import asyncio
import os
from datetime import datetime


char_to_replace = {'b\'': '',
                   '\\n': ' ',
                   '\\n!': ''}


def checkFileExistance(sPath):
    if not os.path.exists(sPath):
        print(sPath)
        # os.makedirs(sPath)
    return True


def deleteFile(path, file):
    fileToDelete = []
    nbs = os.path.getmtime(path + file)
    dt = datetime.now()
    dif = dt.timestamp() - nbs
    if dif > 7200:
        fileToDelete.append(file)
        os.remove(path + file)
    print(fileToDelete)
    return fileToDelete


def verif():
    path = os.listdir()
    print(path)
    oDelete = []
    oFichiers = []
    for p in path:
        print(p)
        if str(p) == 'mp3':
            print(p)
            sPath = 'mp3/'
            mp3 = os.listdir(sPath)

            for fichier in mp3:
                oDelete = deleteFile(sPath , fichier)

        if p == 'mp4':
            print(p)
            sPath = 'mp4/'
            mp4 = os.listdir(sPath)

            for fichier in mp4:
                oDelete = deleteFile(sPath , fichier)

    return oDelete


def verifUrl(url):
    try:
        result = False
        if "/" in url:
            if "www.youtube.com" in url:
                result = True
        return result
    except Exception as E:
        print("Probleme %s sur URL " % str(E))


def choiseVerison(version, name):
    ydl_opts = None
    if str(version) == 'mp3':
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': "mp3/" + name + '.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192'
            }],
            'postprocessor_args': [
                '-ar', '16000'
            ],
            'prefer_ffmpeg': True
        }
    else:
        ydl_opts = {
            'format': 'bestvideo[height<=480]+bestaudio/best[height<=480]',
            'videoformat': "mp4",
            'outtmpl': "mp4/" + name + '.%(ext)s',
            'writethumbnail': True,
            'writesubtitles': True,
            'writeautomaticsub': True,
            'subtitleslangs': 'en',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp4',

            }],

        }
    return ydl_opts


async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)



