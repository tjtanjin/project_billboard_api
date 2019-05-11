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
    Function to get song id from song name.
    Args:
        songname: name of the song to predict
    """
    #search and retrieve track id
    url = "https://api.spotify.com/v1/search?q={}&type=track".format(songname)
    res = get(url, headers = headers)
    #reject if unable to find song id
    try:
        res = res.json()['tracks']['items'][0]
        songid = res['id']
        songpop = res['popularity']
    except:
        return "Unable to find specified song."

    return songid, songpop

def get_song_features(songid, model):
    """
    Function to get song features from specified song based on model chosen
    Args:
        songid: id of the song to predict
        model: type of model chosen
    """
    #call spotify api to get song features
    url="https://api.spotify.com/v1/audio-analysis/{}".format(songid)
    ar=get(url, headers=headers)
    while "track" not in ar.json():
        ar=get(url, headers=headers)
    
    ar=ar.json()["track"]

    url="https://api.spotify.com/v1/audio-features/{}".format(songid)
    fr=get(url, headers=headers)
    fr=fr.json()

    #retrieve features and place into dataframe based on model choice
    if model == "xgboost":
        song_features = pd.DataFrame(columns=['acousticness', 'danceability', 'duration', 'energy', 'instrumentalness', 'key', 'liveness', 'loudness',
                                            'mode', 'speechiness', 'tempo', 'tempo_confidence', 'time_signature', 'time_signature_confidence', 'valence'])
        
        song_features = song_features.append({"acousticness": fr["acousticness"], "danceability": fr["danceability"], "duration": ar["duration"],
                                            "energy": fr["energy"], "instrumentalness": fr["instrumentalness"], "key": ar["key"],
                                            "liveness": fr["liveness"], "loudness": ar["loudness"], "mode": ar["mode"], "speechiness": fr["speechiness"], 
                                            "tempo": ar["tempo"], "tempo_confidence": ar["tempo_confidence"], "time_signature": ar["time_signature"],
                                            "time_signature_confidence": ar["time_signature_confidence"], "valence": fr["valence"]}, ignore_index = True)

    elif model == "knn":
        song_features = pd.DataFrame(columns=['acousticness', 'danceability', 'duration', 'energy', 'instrumentalness', 'key', 'key_confidence', 'liveness',
                                            'loudness', 'mode', 'mode_confidence', 'speechiness', 'tempo', 'tempo_confidence', 'time_signature', 'time_signature_confidence'])

        song_features = song_features.append({"acousticness": fr["acousticness"], "danceability": fr["danceability"], "duration": ar["duration"], "energy": fr["energy"],
                                            "instrumentalness": fr["instrumentalness"], "key": ar["key"], "key_confidence": ar["key_confidence"], "liveness": fr["liveness"],
                                            "loudness": ar["loudness"], "mode": ar["mode"], "mode_confidence": ar["mode_confidence"], "speechiness": fr["speechiness"], "tempo": ar["tempo"],
                                            "tempo_confidence": ar["tempo_confidence"], "time_signature": ar["time_signature"], "time_signature_confidence": ar["time_signature_confidence"]}, ignore_index = True)


    elif model == "logistic_regression":
        song_features = pd.DataFrame(columns=['duration', 'loudness', 'tempo', 'tempo_confidence', 'time_signature_confidence', 'key_confidence', 'mode_confidence', 'key',
                                            'mode', 'acousticness', 'energy', 'liveness', 'speechiness', 'valence'])

        song_features = song_features.append({"duration": ar["duration"], "loudness": ar["loudness"], "tempo": ar["tempo"],
                                           "tempo_confidence": ar["tempo_confidence"], "time_signature_confidence": ar["time_signature_confidence"], "key_confidence": ar["key_confidence"],
                                           "mode_confidence": ar["mode_confidence"], "key": ar["key"], "mode": ar["mode"], "acousticness": fr["acousticness"], 
                                           "energy": fr["energy"], "liveness": fr["liveness"], "speechiness": fr["speechiness"], "valence": fr["valence"]}, ignore_index = True)
    return song_features
