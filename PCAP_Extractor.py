import os
from path_verify import path_verify
from TShark_data import TShark_data
from iptrace import ipexport
from TShark_VData import TShark_Setup
from TShark_VData import TShark_Loop
from mysql_DB import MYSQL_Data_Import 
from mysql_DB import MYSQL_DB_ED
from mysql_DB import MYSQL_DB_CD

Spath = ""
# Spath = "/home/arthur/SSD_Storage/" #Server Path, ONLY UNCOMMENT IN PRODUCTION
# Infinte Loop - As long as their are files to process, the program will run.
while True:
    files = path_verify(Spath)
    
    try:
        EData = MYSQL_Data_Import("edata") #Endpoint MySql DataTable
        CData = MYSQL_Data_Import("cdata") #Conversation MySql DataTable
        DB_S = 1 #If DataTable Exsist 
    except:  
        DB_S = 0 #If DataTable Doesn't Exsist 
   
    data = TShark_data(Spath, files) #Function: Cleans up the PCAP file into a usable format.
    if DB_S == 0: #If DataTable Doesn't Exsist 
        EData = [] 
        CData = []
        TShark_Setup(data, EData,CData) #Set's up the Variable and Table information.
        ipexport(EData, 0) #Network Data
        MYSQL_DB_ED(EData) #Creates the MySql Tables.
        MYSQL_DB_CD(CData)  
    if DB_S == 1:  #If DataTable Exsist 
        TShark_Loop(data, EData,CData) #Updates the DataTables
        ipexport(EData, 0)  #Network Data
        MYSQL_DB_ED(EData) #Updates the MySql Tables.
        MYSQL_DB_CD(CData) 
   
    os.system("rm "+Spath+"Tables.txt")  # Removes Extra Files
    os.system("rm "+Spath+"Table_Condensend.txt")  # Removes Extra Files
    os.system("rm "+Spath+"TShark/"+files[0])  # Removes Extra Files

