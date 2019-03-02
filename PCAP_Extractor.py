import os
from path_verify import path_verify
from TShark_data import TShark_data
from iptrace import ipexport
from TShark_data import TShark_Setup
from TShark_data import TShark_Loop
from mysql_DB import MYSQL_Data_Import
from mysql_DB import MYSQL_DB_ED
from mysql_DB import MYSQL_DB_CD
from mysql_DB import MYSQL_Login

# Super Secert & Secure Login Credentials
DataBase_Login = ('localhost', 'TShark', 'TSharkpassword', 'TShark')

Spath = ""
# This is the subfolder where the generated pcap files are stored (Must Already Exist)
folder = "TShark"
# Spath = "/***************/" #PCAP_Extracotr File Path From Root, ONLY UNCOMMENT IN PRODUCTION
# Infinte Loop - As long as their are files to process, the program will run.
while True:
    files = path_verify(Spath, folder)

    try:
        # Endpoint MySql DataTable
        EData = MYSQL_Data_Import("edata", MYSQL_Login(DataBase_Login))
        # Conversation MySql DataTable
        CData = MYSQL_Data_Import("cdata", MYSQL_Login(DataBase_Login))
        DB_S = 1  # If DataTable Exist
    except:
        DB_S = 0  # If DataTable Doesn't Exist

    # Function: Cleans up the PCAP file into a usable format.
    data = TShark_data(Spath, files, folder)
    if DB_S == 0:  # If DataTable Doesn't Exist
        EData = []
        CData = []
        # Set's up the Variable and Table information.
        TShark_Setup(data, EData, CData)
        ipexport(EData)  # Network Data
        MYSQL_DB_ED(EData, MYSQL_Login(DataBase_Login))  # Creates the MySql Tables.
        MYSQL_DB_CD(CData, MYSQL_Login(DataBase_Login))
    if DB_S == 1:  # If DataTable Exist
        TShark_Loop(data, EData, CData)  # Updates the DataTables
        ipexport(EData)  # Network Data
        MYSQL_DB_ED(EData, MYSQL_Login(DataBase_Login))  # Updates the MySql Tables.
        MYSQL_DB_CD(CData, MYSQL_Login(DataBase_Login))

    os.system("rm " + Spath + folder + "/" + files[0])  # Removes Extra Files
