from pydub import AudioSegment
from os import path
src="pavo/download"
tst="test.wav"
audSeg = AudioSegment.from_mp3(src)
audSeg.export(tst, format="wav")