import os, sys
folder = 'C:/Users/user1/Documents/batch_folder' #folder path that contains files to be change
for filename in os.listdir(folder):
    infilename = os.path.join(folder,filename)
    if not os.path.isfile(infilename): continue
    oldbase = os.path.splitext(filename)
    newname = infilename.replace('.csv', '.JSON') #left = original ext, right = desired ext
    output = os.rename(infilename, newname)
