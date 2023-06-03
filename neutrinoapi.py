import http.client
import json


class IpData:
    def __init__(self, idd, keyy):
        self.id = idd
        self.key = keyy
        self.conn = http.client.HTTPSConnection("neutrinoapi.net")

        self.headers = {
            'User-ID': self.id,
            'API-Key': self.key,
            'Content-Type': "application/x-www-form-urlencoded"

        }


    def infoCreate(self, var1, data1, var2, data2):
        info = var1 + "=" + data1 + "&" + var2 + "="
        if data2 ==False: info += "false"
        elif data2==True: info += "true"
        else:
            print("info_create_error")
            exit()
        return info

    def infoCreate2(self, infoList):
        print("INFOLIST" , infoList)
        info = ""
        lentest = 0
        for i in infoList:
            info += i[0]
            info += "="
            if i[1] == False:
                info += "false"
            elif i[1] == True:
                info += "true"
            else:
                info += i[1]
            lentest+=1
            if lentest != len(infoList):
                info += "&"
        return info


    def caller(self,info, type):
        self.conn.request("POST", type, info, self.headers)
        res = self.conn.getresponse()
        data = res.read()
        return data.decode("utf-8")

    def ipPrint(self, ip):
        print(self.id + "  " + self.key)
        print(ip)


    def ipProbe(self, ip):
        info = "ip=" + ip

        return(self.caller(info, "/ip-probe"))
    




    def ipInfo(self, ip, reverse=False):
        info = "ip=" + ip + "&reverse-lookup="
        if reverse == False: info += "false"
        elif reverse == True: info += "true"
        else: 
            print("error")
            exit()
        return(self.caller(info, "/ip-info"))


    def ipBlocklist(self, ip, VPN=False):
        info = "ip=" + ip + "&vpn-lookup="
        if VPN ==False: info += "false"
        elif VPN == True: info += "true"
        else:
            print("error")
            exit()

        return(self.caller(info, "/ip-blocklist"))



    def emailValidate(self,email, typos=False):
        info2 = self.infoCreate2((("email",email),("fix-typos",typos)))

        return(self.caller(info2, "/email-validate"))

    def phoneValidate(self, number, country_code="", ip=""):
        info = self.infoCreate2((("number", number),("country-code", country_code),("ip", ip)))
        return(self.caller(info, "/phone-validate"))


    def userAgent(self, ua, ua_version="", ua_platform="", ua_platform_version="", ua_mobile="", device_model="",device_brand=""):
        info = self.infoCreate2((("ua", ua),("ua-version", ua_version),("ua-platform", ua_platform),("ua-platform-version", ua_platform_version),("ua-mobile", ua_mobile),("device-model", device_model),("device-brand", device_brand)))
        print(info)
        return(self.caller(info, "/ua-lookup"))
    
    def currencyConvert(self, from_value, from_type, to_type):
        info = self.infoCreate2((("from-value", from_value),("from-type", from_type),("to-type", to_type)))
        return(self.caller(info, "/convert"))

    def htmlClean(self, content, output_type):
        info = self.infoCreate2((("content", content),("output-type", output_type)))
        return(self.caller(info, "/html-clean"))





#print(json.loads(data)["country-code"])