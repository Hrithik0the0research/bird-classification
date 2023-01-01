import librosa
import librosa.display
from tensorflow.python.keras.models import load_model
import numpy as np
from sklearn.preprocessing import LabelEncoder
labelencoder=LabelEncoder()
filename="phyllergates cucullatus5.wav"
model=load_model("audio_classification1.h5")
audio, sample_rate = librosa.load(filename) 
mfccs_features = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=40)
mfccs_scaled_features = np.mean(mfccs_features.T,axis=0)

print(mfccs_scaled_features)
mfccs_scaled_features=mfccs_scaled_features.reshape(1,-1)
print(mfccs_scaled_features)
print(mfccs_scaled_features.shape)
predicted_label=model.predict_classes(mfccs_scaled_features)
print(predicted_label)
prediction_class = labelencoder.inverse_transform(predicted_label) 
print(prediction_class)
