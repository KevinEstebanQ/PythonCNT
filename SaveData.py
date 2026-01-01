import os
import shutil
from datetime import datetime


Path = r"C:\Program Files (x86)\Steam\userdata\323590835\2246340\remote\win64_save"
Destination = r"C:\Users\Kevin\Desktop\MHWsaves"

###
Now = datetime.now().strftime("%Y-%m-%d at %H %M %S")
NewFolderName ="MHwilds_Save"+Now 



    
def Main():
    print("What do you want to do/n")
    print("1. Create save Data.")
    Answer = input("Answer:")   
    HandelFiles(Answer, Destination)
    
def HandelFiles(Answer, Destination):
    if (Answer  == "1") & os.path.exists(Path) & os.path.exists(Destination):
     os.chdir(Destination)
     os.mkdir(NewFolderName)
     os.chdir(Path)
     Destination = os.path.join(Destination, NewFolderName)
     shutil.copytree(Path, Destination, dirs_exist_ok=True)
    else:
       print("No such Directory")

Main()