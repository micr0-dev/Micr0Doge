from bs4 import BeautifulSoup
import requests

codeNameDict = {"pixel 5":"redfin","pixel 4a 5g":"bramble","pixel 4a":"sunfish","pixel 4":"flame","pixel 4 xl":"coral","pixel 3a":"sargo","pixel 3a xl":"bonito","pixel 3":"blueline","pixel 3 xl":"crosshatch","pixel 2":"walleye","pixel 2 xl":"taimen","pixel":"sailfish","pixel xl":"marlin","pixel c":"ryu","nexus 6p":"angler","nexus 5x":"bullhead","nexus 6":"shamu","nexus player":"fugu","nexus 9 lte":"volantisg","nexus 9 wifi":"volantis","nexus 5":"hammerhead","nexus 7":"razor","nexus 10":"mantary","nexus 4":"occam"}

def tableDataText(table):       
    rows = []
    trs = table.find_all('tr')
    headerow = [td.get_text(strip=True) for td in trs[0].find_all('th')] # header row
    if headerow: # if there is a header row include first
        rows.append(headerow)
        trs = trs[1:]
    for tr in trs: # for every table row
        rows.append([td.get_text(strip=True) for td in tr.find_all('td')]) # data row
    return rows

#Getting the website with a Completed TOS cookie
r = requests.get('https://developers.google.com/android/images', cookies=dict(devsite_wall_acks="nexus-image-tos"))
#Parsing the HTML
soup = BeautifulSoup(r.text, 'html.parser')
device = "redfin"
if device in codeNameDict:
    codeName = codeNameDict[device]
elif device in codeNameDict.values():
    codeName = device
else:
    print("Invalid Device / Not Supported Device")

tablelist = soup.find_all('table')

for images in tableDataText(tablelist[1]):
    print("Version: `"+str(images[0])+"`", "SHA-256 Checksum: `"+str(images[-1])+"`")
