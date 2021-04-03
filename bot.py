#Importing
import data

import discord
from dotenv import load_dotenv

from datetime import datetime

import os

from bs4 import BeautifulSoup
import requests

#Codename Dictionary for conversion
codeNameDict = {"pixel 5":"redfin","pixel 4a 5g":"bramble","pixel 4a":"sunfish","pixel 4":"flame","pixel 4 xl":"coral","pixel 3a":"sargo","pixel 3a xl":"bonito","pixel 3":"blueline","pixel 3 xl":"crosshatch","pixel 2":"walleye","pixel 2 xl":"taimen","pixel":"sailfish","pixel xl":"marlin","pixel c":"ryu","nexus 6p":"angler","nexus 5x":"bullhead","nexus 6":"shamu","nexus player":"fugu","nexus 9 lte":"volantisg","nexus 9 wifi":"volantis","nexus 5":"hammerhead","nexus 7":"razor","nexus 10":"mantary","nexus 4":"occam"}

#Constants
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = 825833645457276989

guild = None

client = discord.Client()

@client.event
async def on_ready():
    global guild
    for guild in client.guilds:
        if guild.id == GUILD:
            break
    
    print("""
█████████████████████████████████████████████▀███████
█▄─▀█▀─▄█▄─▄█─▄▄▄─█▄─▄▄▀█─▄▄─█▄─▄▄▀█─▄▄─█─▄▄▄▄█▄─▄▄─█
██─█▄█─███─██─███▀██─▄─▄█─██─██─██─█─██─█─██▄─██─▄█▀█
▀▄▄▄▀▄▄▄▀▄▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▀▄▄▄▄▀▀▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀ By Micr0byte, For Squabbi (Version 0.4)\n""")
    print(str(client.user)+' is connected to the following guild:\n'+str(guild.name)+' (id: '+str(guild.id)+')')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    while True:
        if len(message.content) <= 0:
            break
        if message.content[0] == "!":
            version = ""
            codeName = None
            zipLinksList = []
            listMessage = message.content.lower()[1:].split()
            embedVar = discord.Embed(title="Title", description="Desc", color=0x00ff00)

            logmsg = "["+str(datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))+"] "+str(message.author.name)+": "+str(message.content)+"\n"
            print(logmsg, end='')
            logfile = open(str(os.path.realpath(__file__))[:-6]+"Log.txt", "a")
            logfile.write(logmsg)
            logfile.close()

            if listMessage[0] == "help":
                helpFile = open(str(os.path.realpath(__file__))[:-6]+"help.txt", "r")
                helpText = helpFile.read()
                helpFile.close()
                if len(listMessage) > 1:
                    await message.channel.send('\n'.join([s for s in helpText.split("\n") if ' '.join(listMessage[1:]) in s]))
                    break
                await message.channel.send(helpText)
            elif listMessage[0] == "image" or listMessage[0] == "img":
                async with message.channel.typing():
                    extensions = [s for s in listMessage if "-" in s]
                    if len(extensions) != 0:
                        listMessage.remove(extensions[0])
                        if extensions[0][1] == "r":
                            version = "r"
                        elif extensions[0][1] == "l":
                            version = "l"
                        else:
                            await message.channel.send("Invalid Extension")
                            break
                    #Getting the website with a Completed TOS cookie
                    r = requests.get('https://developers.google.com/android/images', cookies=dict(devsite_wall_acks="nexus-image-tos"))
                    #Parsing the HTML
                    soup = BeautifulSoup(r.text, 'html.parser')
                    device = " ".join(listMessage[1:]).lower()
                    if device in codeNameDict:
                        codeName = codeNameDict[device]
                    elif device in codeNameDict.values():
                        codeName = device
                    else:
                        await message.channel.send("Invalid Device / Not Supported Device")
                        break
                    for link in soup.find_all('a'):
                        zipLink = link.get('href')
                        if codeName in zipLink and "dl.google.com" in zipLink:
                            zipLinksList.append(zipLink)
                if version == "l":
                    imgLink = "<https://developers.google.com/android/images#"+codeName+">"
                elif version == "r":
                    imgLink = zipLinksList[0]
                else:
                    imgLink = zipLinksList[-1]
                await message.channel.send('''```diff
- WARNING: Please use these Images only for '''+codeName+" ("+list(codeNameDict.keys())[list(codeNameDict.values()).index(codeName)].title()+"). If not it may result in a hard brick of the device -```"+'\n'+imgLink)
            elif listMessage[0] == "magisk" or listMessage[0] == "m":
                async with message.channel.typing():
                    embedVar = data.magisk()
                await message.channel.send(embed=embedVar)
            elif listMessage[0] == "tools" or listMessage[0] == "t":
                await message.channel.send(embed=data.tools())
            elif listMessage[0] == "blod":
                await message.channel.send(embed=data.blod())
            elif listMessage[0] == "safetynet" or listMessage[0] == "sn":
                await message.channel.send(embed=data.safetynet())
            elif listMessage[0] == "bootloader" or listMessage[0] == "bl":
                await message.channel.send(embed=data.bootloader())
            elif listMessage[0] == "squabbi":
                await message.channel.send(embed=data.squabbi())
            elif listMessage[0] == "microbyte" or listMessage[0] == "micro" or listMessage[0] == "micr0" or listMessage[0] == "micr0byte":
                await message.channel.send(embed=data.microbyte())
            elif listMessage[0] == "crew":
                await message.channel.send(embed=data.squabbi())
                await message.channel.send(embed=data.microbyte())
            elif listMessage[0] == "cake":
                await message.delete()
                await message.author.create_dm()
                await message.author.dm_channel.send("The Cake is a Lie.", delete_after=0.1)
            elif listMessage[0] == "test":
                #print(message.author.joined_at.timestamp())
                pass
            else:
                await message.channel.send("Invalid command. Use `!help` for list of commands.")
        break

client.run(TOKEN)