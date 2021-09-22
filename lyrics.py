import requests
import base64
import json
import os
import random
import requests
from dotenv import find_dotenv, load_dotenv
import antest
load_dotenv(find_dotenv())

# used to hide, ID and Secret
ACCESS_TOKEN = os.getenv('client_access_token')

header = {}

header['Authorization'] = f"Bearer {ACCESS_TOKEN}"

param={
    'q' : antest.songName
}

r = requests.get('https://api.genius.com/search',
        headers=header, 
        params=param
)

response = r.json()
info = response['response']['hits'][0]['result']['url']

def get_lyricsURL(information):
    return information

lyricsURL = get_lyricsURL(info)

def rtnURL():
    return{
        'lyricsURL' : lyricsURL
    }