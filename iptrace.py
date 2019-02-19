import socket #Used for Gathering Internal Hostname
import ipinfo #API for gathering Public IP Information

def IpGeoL(ip_address): #https://ipinfo.io/
    access_token = 'YOURAPIKEYGOESHERE' #API KEY 
    handler = ipinfo.getHandler(access_token)
    Ip_Info = handler.getDetails(ip_address) #Gets all the data that the free version of the api gets.
    IPGeoD = (Ip_Info.org, Ip_Info.country_name,  Ip_Info.region, Ip_Info.city) #Only grabbing the parts that I want.
    return IPGeoD

def LHost(ip_address): 
    try: 
        return socket.gethostbyaddr(ip_address) #Internal Hostname
    except: 
        return None
  
def ipexport(EData, i):
   for IPD in range(0, len(EData)):
        if EData[IPD][9] == None and "192.168" not in EData[IPD][0] and "172." not in EData[IPD][0]: #External
            IpGeo = IpGeoL(EData[IPD][0]) #Function
            EData[IPD][9] = IpGeo[0].split(None, 1)[1]
            EData[IPD][10] = IpGeo[1]
            EData[IPD][11] = IpGeo[2]
            EData[IPD][12] = IpGeo[3]
        if EData[IPD][9] == None and "192.168" in EData[IPD][0] or "172." in EData[IPD][0]:     #Internal
            IpHost = LHost(EData[IPD][0]) #Function
            EData[IPD][10] = "Internal"
            if  IpHost != None:
                EData[IPD][9] = IpHost[0]
                