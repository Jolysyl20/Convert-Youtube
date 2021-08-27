import logging
import sys
import youtube_dl
from flask import Flask, request, send_file, render_template


logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/download_video', methods=["GET", "POST"])
def download_video():
    # je recupere le lien inscrit dans l'input
    youtube_url = request.form['URL']
    # je renomme la musique au nom de l'app car un peu de pub ca mange pas de pain
    name = 'youtube-convert'
    # je declare les options de telechargement
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
    # je declare le lien de telechargement afin de retourner le fichier à l'utilisateur
    path ="mp3/" + name + '.mp3'
    # declaration pour telecharger le lien youtube avec la configuration desiré
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([youtube_url])
    # je retourne le fichier telechargé
    return send_file(path, as_attachment=True)

# set FLASK_APP=app.py
# set FLASK_ENV=development

