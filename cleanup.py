import datetime 
import os 
import shutil

#returns only the files not directories
def files(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            yield file 

currenttime=datetime.datetime.now() 
basedir = "/motionimg/" 
newdir=basedir + "a{:%Y%m%d}/".format(currenttime)

#create the directory

if not os.path.exists(newdir):
        os.makedirs(newdir)

#move the files

for i in files(basedir):
        os.rename(basedir+i,newdir+i)
