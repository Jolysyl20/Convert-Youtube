import logging
import os
import asyncio
import sys
import youtube_dl
from coreIo import *
from flask import Flask, request, send_file, render_template, send_from_directory
from titleSong import titleDownload
import time

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
app = Flask(__name__)


@app.route("/")
def index():
    delet = verif()
    print(delet)
    return render_template('index.html')


@app.route("/frame", methods=["GET", "POST"])
def frame():
    url = request.form['URL']
    if not verifUrl(url):
        return render_template('index.html', div="choisir un lien youtube")

    return render_template('download.html', div=str(url))


@app.route('/download_video', methods=["GET", "POST"])
def download_video():
    path = ""
    ydl_opts = None
    youtube_url = request.form['URL']
    try:

        verison = request.form['choix']
        # je renomme la musique au nom de la musique et de l'app car un peu de pub ca mange pas de pain
        name = titleDownload(youtube_url )
        # je declare les options de telechargement
        ydl_opts = choiseVerison(verison, name)
        # je declare le lien de telechargement afin de retourner le fichier à l'utilisateur
        path = verison + "/" + name + '.' + verison
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([youtube_url])
    except:
        return render_template('index.html', div="une erreur est survenue")
    # declaration pour telecharger le lien youtube avec la configuration desiré

    finally:
        return render_template('complet.html', progress="Merci votre fichier " + verison, download = path, name = name )
# set FLASK_APP=app.py
# set FLASK_ENV=development
@app.route('/uploads', methods=['GET', 'POST'])
def download():
    path = request.form['path']
    return send_file(path, as_attachment=True)
# set FLASK_APP=app.py
# set FLASK_ENV=development