import requests
import base64, json
from dotenv import find_dotenv, load_dotenv
import os
import random
import spotify 

load_dotenv(find_dotenv())

#spotify database url
authUrl="https://accounts.spotify.com/api/token"

authHeader = {}
authData = {}
#hiding clients

clientID = os.getenv("clientID")
clientSecret = os.getenv("clientSecret")
#artisit IDs
Maria = "2sSGPbdZJkaSE2AbcGOACx"
Nudy = "5yPzzu25VzEk8qrGTLIrE1"
Gorilla = "3AA28KZvwAUcZuOKwyblJQ"

artistlist = [Maria, Gorilla, Nudy]
artistID = random.choice(artistlist)

auth_request = requests.post(authUrl, {
    'grant_type': 'client_credentials',
    'client_id': clientID,
    'client_secret': clientSecret,
})

# Base64 Encode Client ID and CLient Secret
def getAccessToken(clientID, clientSecret):
    message = f"{clientID}:{clientSecret}"
    message_bytes = message.encode("ascii")
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode("ascii")
    
    #convert the response to JSON
auth_response_data = auth_request.json()

# save the access token
auth_token = auth_response_data['access_token']

# base URL of all Spotify API endpoints, with specific new releases and header 
headers = {
    "Authorization": "Bearer " + auth_token
}
param = {
    'market' : 'US'
}
# actual GET request 
r = requests.get(f"https://api.spotify.com/v1/artists/{artistID}/top-tracks",
        headers=headers, 
        params=param
)

######
#convert response to JSON
response = r.json()
info = response['tracks'][0]

def get_SongName(information):
    return information['name']
songName = get_SongName(info)
def get_ArtistName(information):
    return information['artists'][0]['name']
ArtistName = get_ArtistName(info)
def get_Image(information):
    return information['album']['images'][0]['url']
Image = get_Image(info)
def get_Audio(information):
    return information["preview_url"]
Audio = get_Audio(info)
  ########  
def rtn():
    return {
    'songName' : songName,
    'ArtistName' : ArtistName,
    'Image' : Image,
    'Audio' : Audio
    }
print(json.dumps(rtn(),indent = 2))
