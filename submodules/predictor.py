import pickle
from submodules.retrieve_song import get_song_id, get_song_features


def predict_popularity(songname, model):
	"""
	Function to predict song popularity.
	Args:
		songname: name of the song to predict
		model: model to use for prediction
	"""
	#retrieve song id of specified song on spotify
	songid, songpop = get_song_id(songname)
	#reject if unable to find song
	if songid == "Unable to find specified song.":
		return "Unable to find specified song."
	#extract song features based on song id
	song_features = get_song_features(songid, songpop)
	#predict based on model and return predictions
	if model == "xgboost":
		loaded_model = pickle.load(open("./models/xgboost_model", "rb"))
		prediction = loaded_model.predict_proba(song_features.iloc[0])
		prediction = round(prediction[0][1], 2)
	elif model == "knn":
		loaded_model = pickle.load(open("./models/knn", "rb"))
		prediction = loaded_model.predict_proba(song_features.iloc[0])
		prediction = round(prediction[0][1], 2)
	
	return str(prediction)
