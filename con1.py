import wave
from sphfile import SPHFile
import os
from glob import glob

#path = './data/xeno-canto-dataset-full-all-Countries/Copsychusfulicatus/India/'  # Path of folder containing .sph files
path="/"
folder = os.fsencode(path)

filenames = []
folderpath = []
outputfile = []

filenames = []
folderpath = []
outputfile = []
i=1


for file in os.listdir(folder):
    filename = os.fsdecode(file)
    if filename.endswith( ('.sph') ): # whatever file types you're using...
        filenames.append(filename)

length = len(filenames)


for i in range(length):
	fpath = os.path.join(path+filenames[i])
	folderpath.append(fpath)
	outpath = os.path.join("outputc_"+str(i)+".wav")	
	outputfile.append(outpath)
print(folderpath)
print(outputfile)




for i in range(length):
	sph =SPHFile(folderpath[i])
	print(sph.format)
	sph.write_wav(outputfile[i], 0, 123.57 ) 