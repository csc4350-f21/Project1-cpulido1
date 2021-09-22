import os

from flask import Flask, render_template
from antest import rtn

app = Flask(__name__)

@app.route('/')
def hello_world():
    """ Returns root endpoint HTML """

    artist_data = rtn()

    return render_template(
        "index.html",
        songName=artist_data['songName'],
        ArtistName=artist_data['ArtistName'],
        Image=artist_data['Image'],
        Audio=artist_data['Audio']

    )
if __name__ == '__main__':
    app.run(host="localhost", port=8000, debug=True)
