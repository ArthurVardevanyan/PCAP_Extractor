import datetime
import os

# Grab the Storage Path, and the FileList from the main program


def TShark_data(Spath, fileList, folder):
    data = []
    row = 0
    # Strips the PCAP File into usefull information and stores it a temp txt file.
    os.system("tshark -r " + Spath + folder + "/" +
              fileList[0]+" -n  -z conv,ip -z endpoints,ip -T fields -e ipv6  >"+Spath+"Tables.txt") #TSharK Parameters
    count = 0
    # Makes the data cleaner for scrubbing.
    with open(Spath + 'Tables.txt') as infile:
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

    os.system("rm " + Spath + "Tables.txt")  # Removes Extra Files
    # Puts the Data into a variable
    for line in data:
        if len(line) == 7:
            row += 1
    data.insert(row, [])
    return data


# Imports the data into a 2D list for easy access. EData: EndpointData & CData: Conversation Data
def TShark_Setup(data, EData, CData):
    col = 0
    row = 0
    # Endpoint Data
    while data[row]:
        EData.append([])
        for col in range(0, 7):
            if "." in data[row][col]:
                EData[row].append(data[row][col])
            else:
                EData[row].append(int(data[row][col]))
        EData[row].append(datetime.datetime.now().strftime('%Y-%m-%d %H:%M'))
        EData[row].append(datetime.datetime.now().strftime('%Y-%m-%d %H:%M'))
        EData[row].append(None)  # Add Blank Sections for IPTrace Function
        EData[row].append(None)
        EData[row].append(None)
        EData[row].append(None)
        col = 0
        row += 1
    row += 1
    col = 0
    dataSplit = row
    row = 0
    # Conversation Data
    while dataSplit < len(data):
        CData.append([])
        for col in range(0, 8):
            if "." in data[dataSplit][col]:
                CData[row].append(data[dataSplit][col])
            else:
                CData[row].append(int(data[dataSplit][col]))
        CData[row].append(datetime.datetime.now().strftime('%Y-%m-%d %H:%M'))
        CData[row].append(datetime.datetime.now().strftime('%Y-%m-%d %H:%M'))
        col = 0
        row += 1
        dataSplit += 1


def TShark_Loop(data, EData, CData):
    # Endpoint Data
    col = 0
    row = 0
    dRow = 0
    while data[dRow]:
        while True:
            try:
                # Update the Data, and update the time last seen.
                if EData[row][col] == data[dRow][0]:
                    for col in range(0, 7):
                        if "." not in data[dRow][col]:
                            EData[row][col] += int(data[dRow][col])  # EDIT
                    EData[row][col +
                               2] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
                    break
            except:  # If the data does not exist to update, input the new data.
                EData.append([])
                for col in range(0, 7):
                    if "." in data[dRow][col]:
                        EData[row].append(data[dRow][col])
                    else:
                        EData[row].append(int(data[dRow][col]))  # EDIT
                EData[row].append(
                    datetime.datetime.now().strftime('%Y-%m-%d %H:%M'))
                EData[row].append(
                    datetime.datetime.now().strftime('%Y-%m-%d %H:%M'))
                # Add Blank Sections for IPTrace Function
                EData[row].append(None)
                EData[row].append(None)
                EData[row].append(None)
                EData[row].append(None)
                break
            row += 1
        col = 0
        row = 0
        dRow += 1
    row += 1
    col = 0
    row = 0
    dataSplit = dRow
    dRow = 1
    # Conversation Data
    while dRow < len(data) - dataSplit:
        while True:
            try:
                if CData[row][col] == data[dRow + dataSplit][0] and CData[row][col + 1] == data[dRow + dataSplit][1]:
                    for col in range(0, 8):
                        if "." not in data[dRow + dataSplit][col]:
                            CData[row][col] += int(data[dRow + dataSplit][col])
                    CData[row][col
                               + 2] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
                    break
            except:  # If the data does not exist to update, input the new data.
                CData.append([])
                for col in range(0, 8):
                    if "." in data[dRow + dataSplit][col]:
                        CData[row].append(data[dRow + dataSplit][col])
                    else:
                        CData[row].append(int(data[dRow + dataSplit][col]))
                CData[row].append(
                    datetime.datetime.now().strftime('%Y-%m-%d %H:%M'))
                CData[row].append(
                    datetime.datetime.now().strftime('%Y-%m-%d %H:%M'))
                break
            row += 1
        col = 0
        row = 0
        dRow += 1
