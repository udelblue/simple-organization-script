# reorg script 
import binascii
import sys,getopt
import os
import shutil
from os import listdir
from os.path import isfile, join


run = True

alpha = 'abcdefghijklmnopqrstuvwxyz'


def program():

        p = r"C:\\cacheTest\\cachedir\\"
        abspath =os.path.normcase(p)
        contin = str(input( "Reorg to take place on directory " + abspath + " of Type 'y' to confirm "))
        if contin == 'y' :
                print('reorg started')
                dname = os.path.dirname(abspath)
                os.chdir(dname)


                #create dirs a-z
                for al in alpha:
                        directory = al
                        if not os.path.exists(directory):
                                os.makedirs(directory)
                              
                print('moving files')
                #get all files
                onlyfiles = [f for f in listdir(dname) if isfile(join(dname, f))]
                for filename in onlyfiles:
                        letter = str(filename).lower()
                        letter = letter[0]
                        if os.path.exists(letter):
                                #move files
                                os.rename(filename , letter + "/" + filename)  
                print('moving directories')               
                #get all directories
                onlyDirs = [d for d in listdir(dname) if not isfile(join(dname, d))]
                for dirs in onlyDirs:
                        letter = str(dirs).lower()
                        letter = letter[0]
                        if not len(dirs) == 1:
                                #move all directories
                                shutil.move(os.path.join(dname , dirs), os.path.join(dname , letter + "/" + dirs))

                                                                
                print('reorg finished')
        print('end script')   
        
def runstop():
    global run
    run = False
    

while(run):
    program()
    runstop()
