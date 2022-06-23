import os, sys
folder = 'C:/Users/Sharvin/Documents/txt_folder'
for filename in os.listdir(folder):
    infilename = os.path.join(folder,filename)
    if not os.path.isfile(infilename): continue
    oldbase = os.path.splitext(filename)
    newname = infilename.replace('.csv', '.JSON')
    output = os.rename(infilename, newname)