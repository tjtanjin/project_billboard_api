import pickle, re
from submodules.retrieve_song import get_song_id, get_song_features


def predict_popularity(songname):

	songid = get_song_id(songname)
	song_features = get_song_features(songid)
	loaded_model = pickle.load(open("./models/model3", "rb"))
	prediction = loaded_model.predict_proba(song_features.iloc[0])
	
	return str(prediction[0][1])
