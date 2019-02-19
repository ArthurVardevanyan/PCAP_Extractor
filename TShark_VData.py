import datetime

def TShark_Setup(data, EData,CData):
        
        i=0
        j = 0
        while data[j]:
            EData.append([])
            for i in range(0,7):
                if "." in data[j][i]:
                    EData[j].append(data[j][i])
                else:
                    EData[j].append(int(data[j][i]))
            EData[j].append(datetime.datetime.now().strftime('%Y-%m-%d %H:%M'))
            EData[j].append(datetime.datetime.now().strftime('%Y-%m-%d %H:%M'))

            i = 0
            j += 1

        j += 1
        i = 0
        dSplt = j
        j = 0
        
        while dSplt < len(data):
            CData.append([])
            for i in range(0,8):
                if "." in data[dSplt][i]:
                    CData[j].append(data[dSplt][i])
                else:
                    CData[j].append(int(data[dSplt][i]))
            CData[j].append(datetime.datetime.now().strftime('%Y-%m-%d %H:%M'))
            CData[j].append(datetime.datetime.now().strftime('%Y-%m-%d %H:%M'))
            i = 0
            j += 1
            dSplt += 1

def TShark_Loop(data, EData,CData):
        i=0
        j = 0
        l = 0
        k = 0
        while data[l]:
            while k == k:
                if EData[j][i] == data[l][0]:
                    for i in range(0,7):
                        if "." not in data[l][i]:
                            EData[j][i] += int(data[l][i])
                    EData[j][i+2]  = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
                    break
                if EData[j][i]  == None:
                    EData.append([])
                    for i in range(0,7):
                        if "." in data[l][i]:
                            EData[j].append(data[j][i])
                        else:
                            EData[j].append(int(data[j][i]))
                    EData[j].append(datetime.datetime.now().strftime('%Y-%m-%d %H:%M'))
                    EData[j].append(datetime.datetime.now().strftime('%Y-%m-%d %H:%M'))
                    break
                j += 1    
            i = 0
            j = 0
            l += 1
        j += 1
        i = 0
        j = 0
        chunk = l
        l = 1

        while l < len(data)-chunk:
            while k == k:
                if CData[j][i] == data[l+chunk][0] and CData[j][i+1] == data[l+chunk][1]:
                    for i in range(0,8):
                        if "." not in data[l+chunk][i]:
                            CData[j][i]  += int(data[l+chunk][i])
                    CData[j][i+2] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
                    break
                if CData[j][i] == None:
                    for i in range(0,8):
                        if "." in data[l+chunk][i]:
                           CData[j].append(data[l+chunk][i])
                        else:
                            CData[j].append(int(data[l+chunk][i]))
                    CData[j].append(datetime.datetime.now().strftime('%Y-%m-%d %H:%M'))
                    CData[j].append(datetime.datetime.now().strftime('%Y-%m-%d %H:%M'))
                    break
                j += 1
            i = 0
            j = 0
            l += 1 