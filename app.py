import os

from flask import Flask, render_template
from antest import rtn
import lyrics


app = Flask(__name__)

@app.route('/')
def main(): ##hello world
    """ Returns root endpoint HTML """

    artist_data = rtn()
    lyricdata = lyrics.rtnURL()

    return render_template(
        "index.html",
        songName=artist_data['songName'],
        ArtistName=artist_data['ArtistName'],
        Image=artist_data['Image'],
        Audio=artist_data['Audio'],
        lyricsURL=lyricdata['lyricsURL']
    )

if __name__ == "__main__":

   app.run(host="localhost", port=8000, debug=True)



    #host="localhost", port=8000, debug=True
 #host = '0.0.0.0',
        #port= int(os.getenv("PORT",8080)),
#localhost
#8000