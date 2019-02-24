import socket #Used for Gathering Internal Hostname
import ipinfo #API for gathering Public IP Information

def IpGeoL(ip_address): #https://ipinfo.io/
    access_token = 'SECERTKEY' #API KEY 
    handler = ipinfo.getHandler(access_token)
    Ip_Info = handler.getDetails(ip_address) #Gets all the data that the free version of the api gets.
    IPGeoD = (Ip_Info.org, Ip_Info.country_name,  Ip_Info.region, Ip_Info.city) #Only grabbing the parts that I want.
    return IPGeoD

def LHost(ip_address): 
    try: 
        return socket.gethostbyaddr(ip_address) #Internal Hostname
    except: 
        return None
  
def ipexport(EData):
   for ipData in range(0, len(EData)):
        if EData[ipData][9] == None and "192.168" not in EData[ipData][0] and "172." not in EData[ipData][0]: #External
            IpGeo = IpGeoL(EData[ipData][0]) #Function
            EData[ipData][9] = IpGeo[0].split(None, 1)[1]
            EData[ipData][10] = IpGeo[1]
            EData[ipData][11] = IpGeo[2]
            EData[ipData][12] = IpGeo[3]
        if EData[ipData][9] == None and "192.168" in EData[ipData][0] or "172." in EData[ipData][0]:     #Internal
            IpHost = LHost(EData[ipData][0]) #Function
            EData[ipData][10] = "Internal"
            if  IpHost != None:
                EData[ipData][9] = IpHost[0]
                