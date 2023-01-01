from os import path
from pydub import AudioSegment
import os
from glob import glob
# files                                                                         
src = "./Sunadarban_13Birds_MP3/white-bellied sea eagle"
src=os.path.join(os.path.abspath(src))

dst = "./sundarban_wav/white-bellied sea eagle/"
data_dir=os.path.join(os.path.abspath(src))
audio_files=glob(data_dir+"/*.mp3")

# convert wav to mp3                       
for i in range(len(audio_files)):                                     
    sound = AudioSegment.from_mp3(audio_files[i])
    sound.export(dst+"haliaeetus leucogaster"+str(i)+".wav", format="wav")