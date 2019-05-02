import json, os
import pandas as pd
from requests import get, post

# post Client Credentials to Spotify's Token API to obtain Token
basic_token = os.environ["spotify_token"]
res = post('https://accounts.spotify.com/api/token', headers = {'Authorization': '{}'.format(basic_token)}, data= {'grant_type': 'client_credentials'})
token = 'Bearer {}'.format(res.json()['access_token'])

# define headers to include Token
headers = {'Authorization': token, "Accept": 'application/json', 'Content-Type': "application/json"}

def get_song_id(songname):
    """
    Function to get song ids and song popularity from song names.
    Args:
        track_namelist: list of all song names
        track_artistlist: list of all song artists (currently not used to query)
    """
    #to store track ids and popularity

    #search and retrieve track ids and popularity
    url = "https://api.spotify.com/v1/search?q={}&type=track".format(songname)
    res = get(url, headers = headers)
    try:
        res = res.json()['tracks']['items'][0]
        songid = res['id']
    except:
        return "Unable to find specified song."

    return songid

def get_song_features(songid):
    song_features = pd.DataFrame(columns=["duration", "loudness", "tempo", "time_signature", "key", "mode", 
    "acousticness", "danceability", "energy", "instrumentalness", "liveness", "speechiness", "valence"])
    url="https://api.spotify.com/v1/audio-analysis/{}".format(songid)
    ar=get(url, headers=headers)
    while "track" not in ar.json():
        ar=get(url, headers=headers)
    
    ar=ar.json()["track"]

    url="https://api.spotify.com/v1/audio-features/{}".format(songid)
    fr=get(url, headers=headers)
    fr=fr.json()

    song_features = song_features.append({"duration": ar["duration"], "loudness": ar["loudness"], "tempo": ar["tempo"],
                                           "time_signature": ar["time_signature"], "key": ar["key"], "mode": ar["mode"],
                                           "acousticness": fr["acousticness"], "danceability": fr["danceability"], "energy": fr["energy"], "instrumentalness": fr["instrumentalness"], 
                                           "liveness": fr["liveness"], "speechiness": fr["speechiness"], "valence": fr["valence"]}, ignore_index = True)

    return song_features
