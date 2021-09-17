import discord
from bs4 import BeautifulSoup
import requests


def test():
    embedVar = discord.Embed(title="Title", description="Desc", color=0x00ff00)
    embedVar.add_field(name="Field1", value="hi", inline=False)
    embedVar.add_field(name="Field2", value="hi2", inline=False)
    return embedVar

def bootloader():
    embedVar = discord.Embed(title="Bootloader", description="To unlock the bootloader you'll need to go to Settings > About Phone and find your Build number. Tap on it 7 times and you'll see a small text and at the bottom of the screen saying \"You\'re now a developer\". After that, you need to go to Settings > Developer Options and find the option that says OEM Unlocking. If it is grayed out then your phone might not be fully paid out or it is a Verizon model. (Verizon models except the OG Pixel cannot be unlocked, therefore cannot be rooted) If the option is available then you can go ahead and enable it. After that you need to shut down your device and after it powers off hold the volume down button and power. After that, you will be brought to the bootloader. At this point, you will need to install Platform-tools (you can type !tool and it should be the first link) and plug your device into your computer. Open a terminal/CMD window in the Platform-tools folder and type in fastboot flashing unlock. After that, you will be prompted if you want to unlock your device or not. after it is complete you can reboot your device by choosing the reboot button or typing in the fastboot reboot command on your computer.", color=0xff0000)
    embedVar.add_field(name="WARNING", value="Unlocking the bootloader will wipe your device and erase all information on it. Make sure to back-up your data before doing so. Locking the bootloader back up will mostlikely result in a brick of your device. Never lock the bootloader unless you're 100% stock.", inline=False)
    return embedVar

def magisk():
    zipLinksList = []
    r = requests.get('https://github.com/topjohnwu/Magisk/releases/tag/v22.0')
    soup = BeautifulSoup(r.text, 'html.parser')
    for link in soup.find_all('a'):
        zipLink = link.get('href')
        if "/topjohnwu/Magisk/releases/download" in zipLink:
            zipLinksList.append(zipLink)
    embedVar = discord.Embed(title="Magisk", description="Stable version should work for most. Newer versions of Android may require temporary use of Canary or Beta builds.", color=0x00ae9a)
    embedVar.add_field(name="Magisk XDA Thread", value="https://forum.xda-developers.com/apps/magisk/official-magisk-v7-universal-systemless-t3473445", inline=False)
    embedVar.add_field(name="Magisk Canary XDA Thread", value="https://forum.xda-developers.com/apps/magisk/dev-magisk-canary-channel-bleeding-edge-t3839337", inline=False)

    embedVar.add_field(name="Magisk Stable", value="https://github.com"+zipLinksList[0], inline=False)
    embedVar.add_field(name="Magisk Canary", value="https://raw.githubusercontent.com/topjohnwu/magisk_files/canary/app-debug.apk", inline=False)
    return embedVar

def blod():
    embedVar = discord.Embed(title="osm0sis' BootLoop of Death (BLOD)", description="inks to files which may temporarily fix the BLOD. Links include patched TWRP & BLOD Workaround Injector flashable ZIP.", color=0xc20f0b)
    embedVar.add_field(name="Patched (angler/Nexus 6P) TWRP 3.2.1-0 with File-based Encryption Compatibility", value="https://basketbuild.com/filedl/devs?dev=osm0sis&dl=osm0sis/osmods/twrp-3.2.1-0-fbe-4core-angler.img", inline=False)
    embedVar.add_field(name="Patched (bullhead/Nexus 5X) TWRP 3.2.1-0 with File-based Encryption Compatibility", value="https://basketbuild.com/filedl/devs?dev=osm0sis&dl=osm0sis/osmods/twrp-3.2.1-0-fbe-4core-bullhead.img", inline=False)
    embedVar.add_field(name="Bootloop of Death Workaround Injector (Flashable ZIP)", value="https://basketbuild.com/filedl/devs?dev=osm0sis&dl=osm0sis/osmods/N5X-6P_BLOD_Workaround_Injector_Addon-AK2-signed.zip", inline=False)
    return embedVar

def safetynet():
    embedVar = discord.Embed(title="SafetyNet", description="The SafetyNet Attestation API is an anti-abuse API that allows app developers to assess the Android device their app is running on. The API should be used as a part of your abuse detection system to help determine whether your servers are interacting with your genuine app running on a genuine Android device. The SafetyNet Attestation API provides a cryptographically-signed attestation, assessing the device's integrity. In order to create the attestation, the API examines the device's software and hardware environment, looking for integrity issues, and comparing it with the reference data for approved Android devices. The generated attestation is bound to the nonce that the caller app provides. The attestation also contains a generation timestamp and metadata about the requesting app.\n\nTLDR: It blocks some features of your phone due to root. But can be avoided.", color=0xf08283)
    embedVar.add_field(name="Current guide to fixing SafetyNet", value="https://www.thecustomdroid.com/fix-safetynet-hardware-attestation-guide/", inline=False)
    return embedVar

def tools():
    embedVar = discord.Embed(title="Tools", description="Useful tools for rooting.", color=0xffa526)
    embedVar.add_field(name="Android SDK Platform Tools (adb & fastboot)", value="https://developer.android.com/studio/releases/platform-tools", inline=False)
    embedVar.add_field(name="Google Factory Images for Nexus/Pixel Devices (For faster access use `!image`. To learn more use `!help image`)", value="https://developers.google.com/android/images#", inline=False)
    embedVar.add_field(name="Google Full OTA Images for Nexus/Pixel Devices", value="https://developers.google.com/android/ota#", inline=False)
    embedVar.add_field(name="Google USB Drivers", value="https://developer.android.com/studio/run/win-usb", inline=False)
    return embedVar

def drivers():
    embedVar = discord.Embed(title="Drivers", description="How to install drivers for the device based on the operating system.", color=0x3ddc84)
    embedVar.add_field(name="Windows", value="""Open device manager
Find Unknown "Android" device (likely listed under Other devices with an exclamation mark)
Update driver
Browse my computer for driver software
Let me pick from a list of devices, select List All Devices
Under "Android device" or "Google Inc", you will find "Android Bootloader Interface"
Choose "Android Bootloader Interface"
Click "yes" when it says that driver might not be compatible""", inline=False)
    embedVar.add_field(name="Linux/Mac", value="For Linux and Mac it should already be preinstalled and working. No need for anything :)", inline=False)
    return embedVar

def squabbi():
    embedVar = discord.Embed(title="Squabbi", description="Squabbi is the creator of MaowDroid. He is the owner of the server. He lives in Australia so his timezone is different from most users here. He loves technology, mostly consumer desktop and laptops, mobile technology in the phone department; and now recently mechanical keyboards.", color=0xbceaee)
    embedVar.add_field(name="Website", value="https://www.squabbi.com/", inline=False)
    embedVar.add_field(name="Donations", value="https://ko-fi.com/squabbi", inline=False)
    return embedVar

def microbyte():
    embedVar = discord.Embed(title="Micr0byte", description="Micr0byte is the creator of Micr0Doge! He is a helper of the server and got into rooting in 2020. He enjoys coding and technology. He uses Linux but is also knowledgeable in other Operating Systems, like Windows and Mac. He still attends school so he is busy at times.", color=0xe06666)
    embedVar.add_field(name="Donations", value="https://www.paypal.com/donate?business=43KUXHDXR5L5L&currency_code=USD", inline=False)
    return embedVar
    