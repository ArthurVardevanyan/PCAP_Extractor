import os
import glob

#Spath is the Storage Path from Root till the main folder in which the program runs.
#This is needed because the cron job won't use the source folder as reference, instead is uses root as reference.
def path_verify(Spath):
    folder = "TShark"  # This is the subfolder where the generated pcap files are stored
    # Grabs the Files (Contains the Date Modifer metedata as well)
    fileList = glob.glob(Spath+folder+"/*.pcap") #Gathers all the Files
    fileList.sort(key=os.path.getmtime)  # Sorts Oldset to Newest
    Stripped_List = [os.path.basename(x) for x in fileList] # Strips the file path data to leave just the filename 
    if len(fileList) == 1:  # If No New Files, Exit Program
        print("No New Files")
        exit()
    return Stripped_List  # Returns the Stripped List to Main Function