import pickle, re
from submodules.retrieve_song import get_song_id, get_song_features


def predict_popularity(songname):
	songid = get_song_id(songname)
	song_features = get_song_features(songid)
	loaded_model = pickle.load(open("../models/model3", "rb"))

	try:
		prediction = loaded_model.predict(song_features, validate_features=True)
	except Exception as ex:
		arrangement = re.search('expected(...){18}', str(ex))
		arrangement = arrangement.group(0)
		print(arrangement[9:])
		print(type(arrangement))



	#return prediction
predict_popularity("Girls like you")
#print(predict_popularity("Girls like you"))