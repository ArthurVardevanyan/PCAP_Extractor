import os
import glob

# Spath is the Storage Path from Root till the main folder in which the program runs.
# This is needed because the cron job won't use the source folder as reference, instead is uses root as reference.


def path_verify(Spath, folder):
    # Grabs the Files (Contains the Date Modifer metedata as well)
    fileList = glob.glob(Spath + folder + "/*.pcap")  # Gathers all the Files
    fileList.sort(key=os.path.getmtime)  # Sorts Oldset to Newest
    # Strips the file path data to leave just the filename
    # Strip filepath to filename.
    Stripped_List = [os.path.basename(x) for x in fileList]
    if len(fileList) == 1:  # If No New Files, Exit Program
        print("No New Files")
        exit()
    return Stripped_List  # Returns the Stripped List to Main Function
