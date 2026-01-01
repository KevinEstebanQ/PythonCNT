import os 
import json
#Define function to encode the data of the directory
def EncodeStructure(root_path):
    #function to recursively identify files or directories inside the path
    def TranverseDir(path):

        items = [] #array to store the information to be returned

        #list every item inside the path and set them to "entry"
        for entry in os.listdir(path):

            #make a temporary new path joining the given path with the entry found inside it, this can either create a new path pointing to a folder or a file
            tempPath = os.path.join(path, entry)

            #check if the temporary path created earlier is a directory
            if os.path.isdir(tempPath):
                #if the path points to a directory the the structure has to be updated, the function is called recursively as the structure has to show the files inside the newly found directory
                items.append({"type":"Dir",
                              "name": entry,
                              "SubDirectory":TranverseDir(tempPath)})
            #if the path point to a file then update the structure accordingly, setting the type to a file and showing the name : "entry"
            else:
                items.append({"Type": "File",
                              "name": entry})
                
        #after the structure is saved in items as a list of dictionaries, the list is returned
        return items
    #takes the output of TransverseDir and saves it to a dictionary
    return {"type": "Dir",
            "name": os.path.basename(root_path),
            "SubDirectory":TranverseDir(root_path)}


def main():
    #simple boolean to keep loop going until a val id apath is given
    LoopBool = True
    while LoopBool: 
        #ask user for input and strip for correctness
        UserDirectory = input("please enter a path: ").strip()

        #check if the path is a directory in the computer
        if os.path.isdir(UserDirectory):

            #encode the structure to generate the dictionary
            newStructure = EncodeStructure(UserDirectory)

            #create the json file
            with open("struct.dat", "w", encoding="utf-8") as f:
                json.dump(newStructure, f, indent=4)
                print("directory structure has been created")
                LoopBool = False

        #tell the user the given directory is invalid 
        else:
            print("given path is not a valid directory")
            continue


if __name__ == "__main__":
    main()