import os

# Grab the Storage Path, and the FileList from the main program


def TShark_data(Spath, fileList, folder):
    data = []
    row = 0
    # Strips the PCAP File into usefull information and stores it a temp txt file.
    os.system("tshark -r "+Spath+ folder + "/" +
              fileList[0]+" -n  -z conv,ip -z endpoints,ip -T fields -e ipv6  >"+Spath+"Tables.txt")
    count = 0
    # Makes the data cleaner for scrubbing.
    with open(Spath+'Tables.txt') as infile:
        for line in infile:
            if not line.strip():
                continue  # skip the empty line
            if line[0] == "=":
                count += 1
            if count == 3:
                count = 0
            if str(line[0]) not in "0123456789":
                continue
            newstr = line.replace("|", "")
            newstr1 = newstr.replace("<", "")
            newstr2 = newstr1.replace("-", "")
            newstr3 = newstr2.replace(">", "")
            thinned = " ".join(newstr3.split())

            data.append(thinned.split())
           
    # Puts the Data into a variable
    for line in data:
        if len(line) == 7:
            row += 1
    data.insert(row, [])
    return data
