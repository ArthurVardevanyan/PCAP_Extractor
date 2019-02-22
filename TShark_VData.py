import datetime

def TShark_Setup(data, EData,CData): #Imports the data into a 2D list for easy access. EData: EndpointData & CData: Conversation Data
        col = 0
        row = 0
        #Endpoint Data
        while data[row]: 
            EData.append([]) 
            for col in range(0,7):
                if "." in data[row][col]:
                    EData[row].append(data[row][col])
                else:
                    EData[row].append(int(data[row][col]))
            EData[row].append(datetime.datetime.now().strftime('%Y-%m-%d %H:%M'))
            EData[row].append(datetime.datetime.now().strftime('%Y-%m-%d %H:%M'))
            EData[row].append(None) #Add Blank Sections for IPTrace Function
            EData[row].append(None)
            EData[row].append(None)
            EData[row].append(None)
            col = 0
            row += 1
        row += 1
        col = 0
        dataSplit = row
        row = 0
        #Conversation Data 
        while dataSplit < len(data):
            CData.append([])
            for col in range(0,8):
                if "." in data[dataSplit][col]:
                    CData[row].append(data[dataSplit][col])
                else:
                    CData[row].append(int(data[dataSplit][col]))
            CData[row].append(datetime.datetime.now().strftime('%Y-%m-%d %H:%M'))
            CData[row].append(datetime.datetime.now().strftime('%Y-%m-%d %H:%M'))
            col = 0
            row += 1
            dataSplit += 1

def TShark_Loop(data, EData,CData):
        #Endpoint Data
        col=0
        row = 0
        dRow = 0
        while data[dRow]:
            while True:
                try:
                    if EData[row][col] == data[dRow][0]: #Update the Data, and update the time last seen.
                        for col in range(0,7):
                            if "." not in data[dRow][col]:
                                EData[row][col] += int(data[dRow][col])#EDIT
                        EData[row][col+2]  = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
                        break
                except: #If the data does not exist to update, input the new data.
                    EData.append([])
                    for col in range(0,7):
                        if "." in data[dRow][col]:
                            EData[row].append(data[dRow][col])
                        else:
                            EData[row].append(int(data[dRow][col])) #EDIT
                    EData[row].append(datetime.datetime.now().strftime('%Y-%m-%d %H:%M'))
                    EData[row].append(datetime.datetime.now().strftime('%Y-%m-%d %H:%M'))
                    EData[row].append(None) #Add Blank Sections for IPTrace Function
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
        #Conversation Data
        while dRow < len(data)-dataSplit:
            while True:
                try:
                    if CData[row][col] == data[dRow+dataSplit][0] and CData[row][col+1] == data[dRow+dataSplit][1]:
                        for col in range(0,8):
                            if "." not in data[dRow+dataSplit][col]:
                                CData[row][col]  += int(data[dRow+dataSplit][col])
                        CData[row][col+2] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
                        break
                except: #If the data does not exist to update, input the new data.
                    CData.append([])
                    for col in range(0,8):
                        if "." in data[dRow+dataSplit][col]:
                           CData[row].append(data[dRow+dataSplit][col])
                        else:
                            CData[row].append(int(data[dRow+dataSplit][col]))
                    CData[row].append(datetime.datetime.now().strftime('%Y-%m-%d %H:%M'))
                    CData[row].append(datetime.datetime.now().strftime('%Y-%m-%d %H:%M'))
                    break
                row += 1
            col = 0
            row = 0
            dRow += 1 