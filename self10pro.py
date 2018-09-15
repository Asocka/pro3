import LINGGER
from LINGGER import *
from akad.ttypes import *
from multiprocessing import Pool, Process
from time import sleep
import datetime, pafy, time, timeit, random, sys, ast, re, os, json, subprocess, threading, string, codecs, requests, tweepy, ctypes, urllib, wikipedia
from datetime import timedelta, date
from datetime import datetime
from bs4 import BeautifulSoup
from googletrans import Translator
import youtube_dl


sb = LineClient()
sb.log("Auth Token : " + str(sb.authToken))
channel = LineChannel(sb)
sb.log("Channel Access Token : " + str(channel.channelAccessToken))

pb1 =LineClient()
pb1.log("Auth Token : " + str(pb1.authToken))
channel1 = LineChannel(pb1)
pb1.log("Channel Access Token : " + str(channel.channelAccessToken))

pb2 = LineClient()
pb2.log("Auth Token : " + str(pb2.authToken))
channel2 = LineChannel(pb2)
pb2.log("Channel Access Token : " + str(channel.channelAccessToken))

pb3 = LineClient()
pb3.log("Auth Token : " + str(pb3.authToken))
channel3 = LineChannel(pb3)
pb3.log("Channel Access Token : " + str(channel.channelAccessToken))

pb4 = LineClient()
pb4.log("Auth Token : " + str(pb4.authToken))
channel4 = LineChannel(pb4)
pb4.log("Channel Access Token : " + str(channel.channelAccessToken))

pb5 = LineClient()
pb5.log("Auth Token : " + str(pb5.authToken))
channel5 = LineChannel(pb5)
pb5.log("Channel Access Token : " + str(channel.channelAccessToken))

pb6 = LineClient()
pb6.log("Auth Token : " + str(pb6.authToken))
channel6 = LineChannel(pb6)
pb6.log("Channel Access Token : " + str(channel.channelAccessToken))

pb7 = LineClient()
pb7.log("Auth Token : " + str(pb7.authToken))
channel7 = LineChannel(pb7)
pb7.log("Channel Access Token : " + str(channel.channelAccessToken))

pb8 = LineClient()
pb8.log("Auth Token : " + str(pb8.authToken))
channel8 = LineChannel(pb8)
pb8.log("Channel Access Token : " + str(channel.channelAccessToken))

pb9 = LineClient()
pb9.log("Auth Token : " + str(pb9.authToken))
channel9 = LineChannel(pb9)
pb9.log("Channel Access Token : " + str(channel.channelAccessToken))

pb10 = LineClient()
pb10.log("Auth Token : " + str(pb10.authToken))
channel10 = LineChannel(pb10)
pb10.log("Channel Access Token : " + str(channel.channelAccessToken))

poll = LinePoll(sb)
call = sb
creator = ["ud296655acef67cbd5e8208e63629f78b"]
owner = ["ud296655acef67cbd5e8208e63629f78b"]
admin = ["ud296655acef67cbd5e8208e63629f78b"]
staff = ["ud296655acef67cbd5e8208e63629f78b"]

sbProfile = sb.getProfile()
sbSettings = sb.getSettings()
sbMID = sb.profile.mid
pb1MID = pb1.getProfile().mid
pb2MID = pb2.getProfile().mid
pb3MID = pb3.getProfile().mid
pb4MID = pb4.getProfile().mid
pb5MID = pb5.getProfile().mid
pb6MID = pb6.getProfile().mid
pb7MID = pb7.getProfile().mid
pb8MID = pb8.getProfile().mid
pb9MID = pb9.getProfile().mid
pb10MID = pb10.getProfile().mid
mid = sb.getProfile().mid
PRANK = [pb1,pb2,pb3,pb4,pb5,pb6,pb7,pb8,pb9,pb10,sb]
Bots = [sbMID,pb1MID,pb2MID,pb3MID,pb4MID,pb5MID,pb6MID,pb7MID,pb8MID,pb9MID,pb10MID]

settings={
    "Picture":False,
    "group":{},
    "groupPicture":False,
    "changePicture":False,
    "autoJoinTicket":False,
    "userAgent": [
        "Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
        "Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 FirePHP/0.5",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux ppc; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux AMD64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1.1; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; U; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; rv:5.0) Gecko/20100101 Firefox/5.0"
    ]
}

wait = {
    "limit": 1,
    "owner":{},
    "admin":{},
    "addadmin":False,
    "delladmin":False,
    "staff":{},
    "addstaff":False,
    "dellstaff":False,
    "bots":{},
    "addbots":False,
    "dellbots":False,
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "Talkblacklist":{},
    "Talkwblacklist":False,
    "Talkdblacklist":False,
    "talkban":True,
    "contact":False,
    'autoJoin':True,
    'autoAdd':True,
    'autoLeave':False,
    'autoLeave1':False,
    "detectMention":True,
    "Mentionkick":False,
    "welcomeOn":False,
    "sticker":False,
    "selfbot":True,
    "mention":"SINI KAK GABUNG CHAT AJA 😊",
    "Respontag":"SEKAARNG TAG BESOK JATUH CINTA",
    "welcome":"Selamat datang & betah",
    "comment":"Like like & like by ARIFISTIFIK",
    "message":"Terimakasih sudah add saya 😃",
    }

read = {
    "readPoint":{},
    "readMember":{},
    "readTime":{},
    "ROM":{},
}

cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

with open('creator.json', 'r') as fp:
    creator = json.load(fp)
with open('owner.json', 'r') as fp:
    owner = json.load(fp)

Setbot = codecs.open("setting.json","r","utf-8")
Setmain = json.load(Setbot)

mulai = time.time()

tz = pytz.timezone("Asia/Jakarta")
timeNow = datetime.now(tz=tz)

def restart_program(): 
    python = sys.executable
    os.execl(python, python, * sys.argv)

def restartBot():

    python = sys.executable
    os.execl(python, python, *sys.argv)
def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)
def runtime(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)
def logError(text):
    sb.log("[ ERROR ] " + str(text))
    tz = pytz.timezone("Asia/Jakarta")
    timeNow = datetime.now(tz=tz)
    timeHours = datetime.strftime(timeNow,"(%H:%M)")
    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
    inihari = datetime.now(tz=tz)
    hr = inihari.strftime('%A')
    bln = inihari.strftime('%m')
    for i in range(len(day)):
        if hr == day[i]: hasil = hari[i]
    for k in range(0, len(bulan)):
        if bln == str(k): bln = bulan[k-1]
    time = hasil + ", " + inihari.strftime('%d') + " - " + bln + " - " + inihari.strftime('%Y') + " | " + inihari.strftime('%H:%M:%S')
    with open("serverBug.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))
def speedtest(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours,24)
    weaks, days = divmod(days,7)
    if days == 0:
        return '%02d' % (secs)
    elif days > 0 and weaks == 0:
        return '%02d' %(secs)
    elif days > 0 and weaks > 0:
        return '%02d' %(secs)
def command(text):
    pesan = text.lower()
    if settings["setKey"] == True:
        if pesan.startswith(settings["keyCommand"]):
            prankbot = pesan.replace(settings["keyCommand"],"")
        else:
            prankbot = "Undefined command"
    else:
        prankbot = text.lower()
    return prankbot
def prankhelp():
    if settings['setKey'] == True:
        key = settings['keyCommand']
    else:
        key = ''
    prankMessage = "║╠ |ᴘʀᴀʙᴋʙᴏᴛs ᴄʀᴇᴀᴛᴏʀ| ╣║\n" + \
                  "║╠•" + key + "pkick *tag" + "\n" + \
                  "║╠•" + key + "pjoin" + "\n" + \
                  "║╠•" + key + "pbye" + "\n" + \
                  "║╠•" + key + "banlist" + "\n" + \
                  "║╠•" + key + "clearban" + "\n" + \
                  "║╠•" + key + "bye" + "\n" + \
                  "║╠•" + key + "me" + "\n" + \
                  "║╠•" + key + "mybots" + "\n" + \
                  "║╠•" + key + "responsename" + "\n" + \
                  "║╠•" + key + "clearchat" + "\n" + \
                  "║╠•" + key + "mymid" + "\n" + \
                  "║╠•" + key + "mypict" + "\n" + \
                  "║╠•" + key + "mycover" + "\n" + \
                  "║╠•" + key + "mystatus" + "\n" + \
                  "║╠•" + key + "myname" + "\n" + \
                  "║╠•" + key + "myvideo" + "\n" + \
                  "║╠•" + key + "botmid" + "\n" + \
                  "║╠•" + key + "smule *id" + "\n" + \
                  "║╠•" + key + "twitter *id" + "\n" + \
                  "║╠•" + key + "friendlist" + "\n" + \
                  "║╠•" + key + "friendblocklist" + "\n" + \
                  "║╠•" + key + "berita" + "\n" + \
                  "║╠•" + key + "memberlist" + "\n" + \
                  "║╠•" + key + "pendinglist" + "\n" + \
                  "║╠•" + key + "gruplist" + "\n" + \
                  "║╠•" + key + "gcreator" + "\n" + \
                  "║╠•" + key + "getmid *tag" + "\n" + \
                  "║╠•" + key + "getpict *tag" + "\n" + \
                  "║╠•" + key + "getcontact *tag" + "\n" + \
                  "║╠•" + key + "getstatus *tag" + "\n" + \
                  "║╠•" + key + "getname *tag" + "\n" + \
                  "║╠•" + key + "gpict" + "\n" + \
                  "║╠•" + key + "gname" + "\n" + \
                  "║╠•" + key + "gname *txt" + "\n" + \
                  "║╠•" + key + "ginfo" + "\n" + \
                  "║╠•" + key + "gid" + "\n" + \
                  "║╠•" + key + "gurl" + "\n" + \
                  "║╠•" + key + "url:on" + "\n" + \
                  "║╠•" + key + "url:off" + "\n" + \
                  "║╠•" + key + "ttl *01-02-1993" + "\n" + \
                  "║╠•" + key + "youtube *channel"
    return prankMessage
def bot(op):
    global time
    global ast
    global groupParam
    try:
        if op.type == 0:
            return

        if op.type == 11:
            if op.param3 == '1':
                if op.param1 in Prankname:
                    try:
                        G = random.choice(PRANK).getGroup(op.param1)
                    except:
                        pass
                    G.name = settings['prank_name'][op.param1]
                    try:
                        random.choice(PRANK).updateGroup(G)
                    except:
                        pass
                    if op.param2 in Bots:
                    	pass
                    else:
                        try:
                            random.choice(PRANK).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            pass
        if op.type == 19:
            if sbMID in op.param3:
                if op.param2 in Bots:
                    pb1.findAndAddContactsByMid(op.param3)
                    pb1.inviteIntoGroup(op.param1,[op.param3])
                    sb.acceptGroupInvitation(op.param1)
                else:
                    settings["blacklist"][op.param2] = True
                    try:
                        pb1.findAndAddContactsByMid(op.param3)
                        random.choice(PRANK).kickoutFromGroup(op.param1,[op.param2])
                        pb1.inviteIntoGroup(op.param1,[op.param3])
                        sb.acceptGroupInvitation(op.param1)
                    except:
                        pass
            if pb1MID in op.param3:
                if op.param2 in Bots:
                    pb2.findAndAddContactsByMid(op.param3)
                    pb2.inviteIntoGroup(op.param1,[op.param3])
                    pb1.acceptGroupInvitation(op.param1)
                else:
                    settings["blacklist"][op.param2] = True
                    try:
                        pb2.findAndAddContactsByMid(op.param3)
                        random.choice(PRANK).kickoutFromGroup(op.param1,[op.param2])
                        pb2.inviteIntoGroup(op.param1,[op.param3])
                        pb1.acceptGroupInvitation(op.param1)
                    except:
                        pass
            if pb2MID in op.param3:
                if op.param2 in Bots:
                    pb3.findAndAddContactsByMid(op.param3)
                    pb3.inviteIntoGroup(op.param1,[op.param3])
                    pb2.acceptGroupInvitation(op.param1)
                else:
                    settings["blacklist"][op.param2] = True
                    try:
                        pb3.findAndAddContactsByMid(op.param3)
                        random.choice(PRANK).kickoutFromGroup(op.param1,[op.param2])
                        pb3.inviteIntoGroup(op.param1,[op.param3])
                        pb2.acceptGroupInvitation(op.param1)
                    except:
                        pass
            if pb3MID in op.param3:
                if op.param2 in Bots:
                    pb4.findAndAddContactsByMid(op.param3)
                    pb4.inviteIntoGroup(op.param1,[op.param3])
                    pb3.acceptGroupInvitation(op.param1)
                else:
                    settings["blacklist"][op.param2] = True
                    try:
                        pb4.findAndAddContactsByMid(op.param3)
                        random.choice(PRANK).kickoutFromGroup(op.param1,[op.param2])
                        pb4.inviteIntoGroup(op.param1,[op.param3])
                        pb3.acceptGroupInvitation(op.param1)
                    except:
                        pass
            if pb4MID in op.param3:
                if op.param2 in Bots:
                    pb5.findAndAddContactsByMid(op.param3)
                    pb5.inviteIntoGroup(op.param1,[op.param3])
                    pb4.acceptGroupInvitation(op.param1)
                else:
                    settings["blacklist"][op.param2] = True
                    try:
                        pb5.findAndAddContactsByMid(op.param3)
                        random.choice(PRANK).kickoutFromGroup(op.param1,[op.param2])
                        pb5.inviteIntoGroup(op.param1,[op.param3])
                        pb4.acceptGroupInvitation(op.param1)
                    except:
                        pass
            if pb5MID in op.param3:
                if op.param2 in Bots:
                    pb6.findAndAddContactsByMid(op.param3)
                    pb6.inviteIntoGroup(op.param1,[op.param3])
                    pb5.acceptGroupInvitation(op.param1)
                else:
                    settings["blacklist"][op.param2] = True
                    try:
                        pb6.findAndAddContactsByMid(op.param3)
                        random.choice(PRANK).kickoutFromGroup(op.param1,[op.param2])
                        pb6.inviteIntoGroup(op.param1,[op.param3])
                        pb5.acceptGroupInvitation(op.param1)
                    except:
                        pass
            if pb6MID in op.param3:
                if op.param2 in Bots:
                    pb7.findAndAddContactsByMid(op.param3)
                    pb7.inviteIntoGroup(op.param1,[op.param3])
                    pb1.acceptGroupInvitation(op.param1)
                else:
                    settings["blacklist"][op.param2] = True
                    try:
                        pb7.findAndAddContactsByMid(op.param3)
                        random.choice(PRANK).kickoutFromGroup(op.param1,[op.param2])
                        pb7.inviteIntoGroup(op.param1,[op.param3])
                        pb6.acceptGroupInvitation(op.param1)
                    except:
                        pass
            if pb7MID in op.param3:
                if op.param2 in Bots:
                    pb10.findAndAddContactsByMid(op.param3)
                    pb10.inviteIntoGroup(op.param1,[op.param3])
                    pb7.acceptGroupInvitation(op.param1)
                else:
                    settings["blacklist"][op.param2] = True
                    try:
                        pb10.findAndAddContactsByMid(op.param3)
                        random.choice(PRANK).kickoutFromGroup(op.param1,[op.param2])
                        pb10.inviteIntoGroup(op.param1,[op.param3])
                        pb7.acceptGroupInvitation(op.param1)
                    except:
                        pass
            if pb8MID in op.param3:
                if op.param2 in Bots:
                    pb7.findAndAddContactsByMid(op.param3)
                    pb7.inviteIntoGroup(op.param1,[op.param3])
                    pb8.acceptGroupInvitation(op.param1)
                else:
                    settings["blacklist"][op.param2] = True
                    try:
                        pb7.findAndAddContactsByMid(op.param3)
                        random.choice(PRANK).kickoutFromGroup(op.param1,[op.param2])
                        pb7.inviteIntoGroup(op.param1,[op.param3])
                        pb8.acceptGroupInvitation(op.param1)
                    except:
                        pass
            if pb9MID in op.param3:
                if op.param2 in Bots:
                    pb8.findAndAddContactsByMid(op.param3)
                    pb8.inviteIntoGroup(op.param1,[op.param3])
                    pb9.acceptGroupInvitation(op.param1)
                else:
                    settings["blacklist"][op.param2] = True
                    try:
                        pb8.findAndAddContactsByMid(op.param3)
                        random.choice(PRANK).kickoutFromGroup(op.param1,[op.param2])
                        pb8.inviteIntoGroup(op.param1,[op.param3])
                        pb9.acceptGroupInvitation(op.param1)
                    except:
                        pass
            if pb10MID in op.param3:
                if op.param2 in Bots:
                    pb9.findAndAddContactsByMid(op.param3)
                    pb9.inviteIntoGroup(op.param1,[op.param3])
                    pb10.acceptGroupInvitation(op.param1)
                else:
                    settings["blacklist"][op.param2] = True
                    try:
                        pb9.findAndAddContactsByMid(op.param3)
                        random.choice(PRANK).kickoutFromGroup(op.param1,[op.param2])
                        pb9.inviteIntoGroup(op.param1,[op.param3])
                        pb10.acceptGroupInvitation(op.param1)
                    except:
                        pass
        if op.type == 19:
            if op.param2 in Bots:
            	pass
            else:
              try:
                 if op.param1 in Prankmember:
                     settings["blacklist"][op.param2] = True
                     G = random.choice(PRANK).getGroup(op.param1)
                     random.choice(PRANK).kickoutFromGroup(op.param1,[op.param2])
                     pb1.findAndAddContactsByMid(op.param3)
                     pb1.inviteIntoGroup(op.param1,[op.param3])
                 else:
                   pass
              except:
                try:
                    G = random.choice(PRANK).getGroup(op.param1)
                    random.choice(PRANK).kickoutFromGroup(op.param1,[op.param2])
                    pb2.findAndAddContactsByMid(op.param3)
                    pb2.inviteIntoGroup(op.param1,[op.param3])
                    settings["blacklist"][op.param2] = True
                except:
                    pass
        if op.type == 13:
            if op.param2 in Bots:
            	pass
            else:
              try:
                 if op.param1 in Prankinvite:
                     settings["blacklist"][op.param2] = True
                     G = random.choice(PRANK).getGroup(op.param1)
                     pb1.kickoutFromGroup(op.param1,[op.param2])
                     pb2.cancelGroupInvitation(op.param1,[contact.mid for contact in sb.getGroup(op.param1).invitee])
                 else:
                     pass
              except:
                try:
                    G = random.choice(PRANK).getGroup(op.param1)
                    pb2.kickoutFromGroup(op.param1,[op.param2])
                    pb3.cancelGroupInvitation(op.param1,[contact.mid for contact in sb.getGroup(op.param1).invitee])
                    settings["blacklist"][op.param2] = True
                except:
                    try:
                        G = random.choice(PRANK).getGroup(op.param1)
                        pb3.kickoutFromGroup(op.param1,[op.param2])
                        pb4.cancelGroupInvitation(op.param1,[contact.mid for contact in sb.getGroup(op.param1).invitee])
                        settings["blacklist"][op.param2] = True
                    except:
                        pass
        if op.type == 11:
            if op.param2 in Bots:
            	pass
            else:
              try:
                 if op.param1 in Prankqr:
                     settings["blacklist"][op.param2] = True
                     pb1.getGroup(op.param1)
                     random.choice(PRANK).kickoutFromGroup(op.param1,[op.param2])
                     G = pb2.getGroup(op.param1)
                     G.preventedJoinByTicket = True
                     pb2.updateGroup(G)
                 else:
                     pass
              except:
                try:
                    settings["blacklist"][op.param2] = True
                    pb3.getGroup(op.param1)
                    pb3.kickoutFromGroup(op.param1,[op.param2])
                    G = pb4.getGroup(op.param1)
                    G.preventedJoinByTicket = True
                    pb4.updateGroup(G)
                except:
                    pass
        if op.type == 17:
            if op.param2 in settings["blacklist"]:
               try:
                   random.choice(PRANK).kickoutFromGroup(op.param1,[op.param2])
                   random.choice(PRANK).sendMessage(op.param1, "そ、[Blacklist]そうですか(｀・ω・´)")
               except:
                   pass
        if op.type == 13:
            try:
                group = sb.getGroup(op.param1)
                contact = sb.getContact(op.param2)
                if settings["prankJoin"] == True:
                    sb.acceptGroupInvitation(op.param1)
            except Exception as error:
                logError(error)
        if op.type == 26:
            msg = op.message
            if settings["prankRespon"] == True:
                if msg.toType == 0:
                    sb.sendChatChecked(msg._from,msg.id)
                    contact = sb.getContact(msg._from)
                    cName = contact.displayName
                    balas = [cName + " maaf sibuk",cName + " gak bisa call sekarang",cName + " maaf lagi ada urusan", cName + " sabar nanti call balik"]
                    ret_ = "[Auto respon aktif] \nSorry " + random.choice(balas)
                    sb.sendMessage(msg._from,ret_)
                else:
                    pass
        if op.type == 25:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            setKey = settings["keyCommand"].title()
            if settings["setKey"] == False:
                 setKey = ''
            if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                if msg.toType == 0:
                    if sender != sb.profile.mid:
                        to = sender
                    else:
                        to = receiver
                elif msg.toType == 1:
                    to = receiver
                elif msg.toType == 2:
                    to = receiver
                if msg.contentType == 0:
                    if text is None:
                        return
                    else:
                        prankbot = command(text)
                        if prankbot == "help" or prankbot == "settings"or prankbot == "set":
                            try:
                                ret_ = "\n║╠•━╦CEK SETTINGS╦━\n║╠•━━━━━━━━━━━━━"
                                if settings["setKey"] == True: ret_ += "\n║╠•『Keyboard』Ξ 『ON』"
                                else: ret_ += "\n║╠•『Keyboard』Ξ 『OFF』"
                                if settings["prankRespon"] == True: ret_ += "\n║╠•『  Prankrespon  』Ξ 『ON』"
                                else: ret_ += "\n║╠•『  Prankrespon  』Ξ 『OFF』"
                                if settings["prankAdd"] == True: ret_ += "\n║╠•『 prankAdd 』Ξ 『ON』"
                                else: ret_ += "\n║╠•『 prankAdd 』Ξ 『OFF』"
                                if settings["prankJoin"] == True: ret_ += "\n║╠•『 prankJoin 』Ξ 『ON』"
                                else: ret_ += "\n║╠•『 prankJoin 』Ξ 『OFF』"
                                if settings["prankJoinLink"] == True: ret_ += "\n║╠•『 prankJoinLink 』Ξ 『ON』"
                                else: ret_ += "\n║╠•『 prankJoinLink 』Ξ 『OFF』"
                                if settings["prankcontact"] == True: ret_ += "\n║╠•『 prankContact 』Ξ 『ON』"
                                else: ret_ += "\n║╠•『 prankContact 』Ξ 『OFF』"
                                if settings["prankTL"] == True: ret_ += "\n║╠•『 prankTL 』Ξ 『ON』"
                                else: ret_ += "\n║╠•『 prankTL 』Ξ 『OFF』"
                                if msg.to in Prankqr: ret_+="\n║╠•『 protectLink 』Ξ 『ON』"
                                else: ret_ += "\n║╠•『 protectLink 』Ξ 『OFF』"
                                if msg.to in Prankname: ret_+="\n║╠•『 protectname 』Ξ 『ON』"
                                else: ret_ += "\n║╠•『 protectname 』Ξ 『OFF』"
                                if msg.to in Prankmember: ret_+="\n║╠•『 protectmember 』Ξ 『ON』"
                                else: ret_ += "\n║╠•『 protectmember 』Ξ 『OFF』"
                                if msg.to in Prankinvite: ret_+="\n║╠•『 protectinvite 』Ξ 『ON』"
                                else: ret_ += "\n║╠•『 protectinvite 』Ξ 『OFF』"
                                prankMessage = prankhelp()
                                sb.sendMessage(to, str(prankMessage)+str(ret_)+"\n║╠ |ᴘʀᴀʙᴋʙᴏᴛs ᴄʀᴇᴀᴛᴏʀ| ╣║\n╰━━━╩℘̰̰̈́ґ̰̰̈́∂̰̰̈́η̰̰̈́к╩̰̰̈́в̰̰̈́❍̰̰̈́т̰̰̈́ѕ̰̰̈́╩━━━╯")
                                sb.sendMessage(settings["server"], str(prankMessage)+str(ret_)+"\n║╠ |ᴘʀᴀʙᴋʙᴏᴛs ᴄʀᴇᴀᴛᴏʀ| ╣║\n╰━━━╩℘̰̰̈́ґ̰̰̈́∂̰̰̈́η̰̰̈́к╩̰̰̈́в̰̰̈́❍̰̰̈́т̰̰̈́ѕ̰̰̈́╩━━━╯")
                            except Exception as e:
                                sb.sendMessage("u0ac948397fbc732bd3bc5ca273faa698", str(e))
                        elif prankbot == "prankadd:on":
                            settings["prankAdd"] = True
                            sb.sendMessage(to, "Already on")
                        elif prankbot == "prankadd:off":
                            settings["prankAdd"] = False
                            sb.sendMessage(to, "Already off")
                        elif prankbot == "prankrespon:on":
                            settings["prankRespon"] = True
                            sb.sendMessage(to, "Already on")
                        elif prankbot == "prankrespon:off":
                            settings["prankRespon"] = False
                            sb.sendMessage(to, "Already off")
                        elif prankbot == "prankjoin:on":
                            settings["prankJoin"] = True
                            sb.sendMessage(to, "Already on")
                        elif prankbot == "prankjoin:off":
                            settings["prankJoin"] = False
                            sb.sendMessage(to, "Already off")
                        elif prankbot == "pranktl:on":
                            settings["prankTL"] = True
                            sb.sendMessage(to, "Already on")
                        elif prankbot == "pranktl:off":
                            settings["prankTL"] = False
                            sb.sendMessage(to, "Already off")
                        elif prankbot == "jointicket:on":
                            settings["prankJoinLink"] = True
                            sb.sendMessage(to, "Already on")
                        elif prankbot == "jointicket:off":
                            settings["prankJoinLink"] = False
                            sb.sendMessage(to, "Already off")
                        elif 'Prankqr:' in msg.text:
                              acil = msg.text.replace('Prankqr:','')
                              if acil == 'on':
                                  if msg.to in Prankqr:
                                       msgs = "Simi-simi sudah aktif"
                                  else:
                                       Prankqr.append(msg.to)
                                       ginfo = sb.getGroup(msg.to)
                                       msgs = "qr Group " +str(ginfo.name) + "di lindungi"
                                  sb.sendMessage(msg.to, msgs)
                              elif acil == 'off':
                                    if msg.to in Prankqr:
                                         Prankqr.remove(msg.to)
                                         ginfo = sb.getGroup(msg.to)
                                         msgs = "qr grup " +str(ginfo.name) + "tidak di lindungi"
                                    else:
                                         msgs = "sudah tidak aktif dalam grup ini"
                                    sb.sendMessage(msg.to, msgs)
                        elif 'Prankname:' in msg.text:
                              acil = msg.text.replace('Prankname:','')
                              if acil == 'on':
                                  if msg.to in Prankname:
                                       msgs = "Simi-simi sudah aktif"
                                  else:
                                       Prankname.append(msg.to)
                                       ginfo = sb.getGroup(msg.to)
                                       msgs = "name Group " +str(ginfo.name) + "di lindungi"
                                  sb.sendMessage(msg.to, msgs)
                              elif acil == 'off':
                                    if msg.to in Prankname:
                                         Prankname.remove(msg.to)
                                         ginfo = sb.getGroup(msg.to)
                                         msgs = "name grup " +str(ginfo.name) + "tidak di lindungi"
                                    else:
                                         msgs = "sudah tidak aktif dalam grup ini"
                                    sb.sendMessage(msg.to, msgs)
                        elif 'Prankinvite:' in msg.text:
                              acil = msg.text.replace('Prankinvite:','')
                              if acil == 'on':
                                  if msg.to in Prankinvite:
                                       msgs = "Simi-simi sudah aktif"
                                  else:
                                       Prankinvite.append(msg.to)
                                       ginfo = sb.getGroup(msg.to)
                                       msgs = "invite Group " +str(ginfo.name) + "di lindungi"
                                  sb.sendMessage(msg.to, msgs)
                              elif acil == 'off':
                                    if msg.to in Prankinvite:
                                         Prankinvite.remove(msg.to)
                                         ginfo = sb.getGroup(msg.to)
                                         msgs = "invite grup " +str(ginfo.name) + "tidak di lindungi"
                                    else:
                                         msgs = "sudah tidak aktif dalam grup ini"
                                    sb.sendMessage(msg.to, msgs)
                        elif 'Prankmember:' in msg.text:
                              acil = msg.text.replace('Prankmember:','')
                              if acil == 'on':
                                  if msg.to in Prankmember:
                                       msgs = "Simi-simi sudah aktif"
                                  else:
                                       Prankmember.append(msg.to)
                                       ginfo = sb.getGroup(msg.to)
                                       msgs = "member Group " +str(ginfo.name) + "di lindungi"
                                  sb.sendMessage(msg.to, msgs)
                              elif acil == 'off':
                                    if msg.to in Prankmember:
                                         Prankmember.remove(msg.to)
                                         ginfo = sb.getGroup(msg.to)
                                         msgs = "Member grup " +str(ginfo.name) + "tidak di lindungi"
                                    else:
                                         msgs = "sudah tidak aktif dalam grup ini"
                                    sb.sendMessage(msg.to, msgs)
#INI MEDIANYA CUMA BUAT BONUS AJA#
#KARNA TUJUANYA BUKAN KE MEDIA
#INI BUAT PROTECT GRUP MAYAN LAH HEHE.
#CREATOR BY ACIL PRANKBOTS.
                        elif prankbot.startswith("pkick "):
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    try:
                                        berak = [pb1,pb2,pb3,pb4,pb5,pb6,pb7,pb8,pb9,pb10]
                                        berakin = random.choice(berak)
                                        berakin.kickoutFromGroup(to,[ls])
                                        print (to,[ls])
                                    except:
                                        pass
                        elif prankbot == "banlist":
                                if settings["blacklist"] == {}:
                                    sb.sendMessage(to,"Tidak Ada kontak blacklist")
                                else:
                                    sb.sendMessage(to,"═══════List blacklist═══════")
                                    h = ""
                                    for i in settings["blacklist"]:
                                        h = sb.getContact(i)
                                        sb.sendContact(to,i)
                        elif prankbot == "clearban":
                            settings["blacklist"] = {}
                            sb.sendMessage(to,"deleted all blacklist")
                            pb1.sendMessage(to,"succes.!!")
                            pb2.sendMessage(to,"succes.!!")
                            pb3.sendMessage(to,"succes.!!")
                            pb4.sendMessage(to,"succes.!!")
                            pb5.sendMessage(to,"succes.!!")
                            pb6.sendMessage(to,"succes.!!")
                            pb7.sendMessage(to,"succes.!!")
                            pb8.sendMessage(to,"succes.!!")
                            pb9.sendMessage(to,"succes.!!")
                            pb10.sendMessage(to,"succes.!!")
                        elif prankbot == "pjoin":
                            G = sb.getGroup(msg.to)
                            ginfo = sb.getGroup(msg.to)
                            G.preventedJoinByTicket = False
                            sb.updateGroup(G)
                            invsend = 0
                            Ticket = sb.reissueGroupTicket(msg.to)
                            pb1.acceptGroupInvitationByTicket(to,Ticket)
                            pb2.acceptGroupInvitationByTicket(to,Ticket)
                            pb3.acceptGroupInvitationByTicket(to,Ticket)
                            pb4.acceptGroupInvitationByTicket(to,Ticket)
                            pb5.acceptGroupInvitationByTicket(to,Ticket)
                            pb6.acceptGroupInvitationByTicket(to,Ticket)
                            pb7.acceptGroupInvitationByTicket(to,Ticket)
                            pb8.acceptGroupInvitationByTicket(to,Ticket)
                            pb9.acceptGroupInvitationByTicket(to,Ticket)
                            pb10.acceptGroupInvitationByTicket(to,Ticket)
                            G = sb.getGroup(msg.to)
                            G.preventedJoinByTicket = True
                            random.choice(PRANK).updateGroup(G)
                        elif prankbot == "pbye":
                            pb1.leaveGroup(msg.to)
                            pb2.leaveGroup(msg.to)
                            pb3.leaveGroup(msg.to)
                            pb4.leaveGroup(msg.to)
                            pb5.leaveGroup(msg.to)
                            pb6.leaveGroup(msg.to)
                            pb7.leaveGroup(msg.to)
                            pb8.leaveGroup(msg.to)
                            pb9.leaveGroup(msg.to)
                            pb10.leaveGroup(msg.to)
                        elif prankbot == "bye":
                            sb.leaveGroup(msg.to)
                        elif prankbot == "me":
                            sb.sendContact(to, sender)
                        elif prankbot == "gruplist":
                            groups = sb.groups
                            ret_ = "╭━━━━━══[ Group List ]══━━━━━╮"
                            no = 0 + 1
                            for gid in groups:
                                group = sb.getGroup(gid)
                                ret_ += "\n┣═ {}. {} ┣═Member: {}".format(str(no), str(group.name), str(len(group.members)))
                                no += 1
                            ret_ += "\n╰━━━━━══[ Total {} Groups ]════━━━━━".format(str(len(groups)))
                        elif prankbot == "mybots":
                            sb.sendMessage(to,"┣━━╦━━━━━━━━━━━╦━━╣")
                            sb.sendContact(to, pb1MID)
                            sb.sendContact(to, pb2MID)
                            sb.sendContact(to, pb3MID)
                            sb.sendContact(to, pb4MID)
                            sb.sendContact(to, pb5MID)
                            sb.sendContact(to, pb6MID)
                            sb.sendContact(to, pb7MID)
                            sb.sendContact(to, pb8MID)
                            sb.sendContact(to, pb9MID)
                            sb.sendContact(to, pb10MID)
                            sb.sendMessage(to,"┣━━╦━━━KONTAK BOTS━━━╦━━╣")
                        elif prankbot == "responsename":
                            profile = pb1.getProfile()
                            text = profile.displayName + "􀜁􀅔􏿿"
                            pb1.sendMessage(to, text)
                            profile = pb2.getProfile()
                            text = profile.displayName + "􀜁􀅔􏿿"
                            pb2.sendMessage(to, text)
                            profile = pb3.getProfile()
                            text = profile.displayName + "􀜁􀅔􏿿"
                            pb3.sendMessage(to, text)
                            profile = pb4.getProfile()
                            text = profile.displayName + "􀜁􀅔􏿿"
                            pb4.sendMessage(to, text)
                            profile = pb5.getProfile()
                            text = profile.displayName + "􀜁􀅔􏿿"
                            pb5.sendMessage(to, text)
                            profile = pb6.getProfile()
                            text = profile.displayName + "􀜁􀅔􏿿"
                            pb6.sendMessage(to, text)
                            profile = pb7.getProfile()
                            text = profile.displayName + "􀜁􀅔􏿿"
                            pb7.sendMessage(to, text)
                            profile = pb8.getProfile()
                            text = profile.displayName + "􀜁􀅔􏿿"
                            pb8.sendMessage(to, text)
                            profile = pb9.getProfile()
                            text = profile.displayName + "􀜁􀅔􏿿"
                            pb9.sendMessage(to, text)
                            profile = pb10.getProfile()
                            text = profile.displayName + "􀜁􀅔􏿿"
                            pb10.sendMessage(to, text)
                        elif prankbot == "clearchat":
                            sb.removeAllMessages(op.param2)
                            sb.sendMessage(to, "Berhasil hapus semua chat")
                        elif prankbot == "mymid":
                            sb.sendMessage(to, "{}".format(sender))
                        elif prankbot == "speed":
                            start = time.time()
                            sb.sendMessage(to, "Ngacirr..")
                            elapsed_time = time.time() - start
                            sb.sendMessage(to,format(str(elapsed_time)))
                            pb1.sendMessage(to,format(str(elapsed_time)))
                            pb2.sendMessage(to,format(str(elapsed_time)))
                            pb3.sendMessage(to,format(str(elapsed_time)))
                            pb4.sendMessage(to,format(str(elapsed_time)))
                            pb5.sendMessage(to,format(str(elapsed_time)))
                            pb6.sendMessage(to,format(str(elapsed_time)))
                            pb7.sendMessage(to,format(str(elapsed_time)))
                            pb8.sendMessage(to,format(str(elapsed_time)))
                            pb9.sendMessage(to,format(str(elapsed_time)))
                            pb10.sendMessage(to,format(str(elapsed_time)))
                        elif prankbot == "botmid":
                            h = pb1.getContact(pb1MID)
                            pb1.sendMessage(to,h.mid)
                            h = pb2.getContact(pb2MID)
                            pb2.sendMessage(to,h.mid)
                            h = pb3.getContact(pb3MID)
                            pb3.sendMessage(to,h.mid)
                            h = pb4.getContact(pb4MID)
                            pb4.sendMessage(to,h.mid)
                            h = pb5.getContact(pb5MID)
                            pb5.sendMessage(to,h.mid)
                            h = pb6.getContact(pb6MID)
                            pb6.sendMessage(to,h.mid)
                            h = pb7.getContact(pb7MID)
                            pb7.sendMessage(to,h.mid)
                            h = pb8.getContact(pb8MID)
                            pb8.sendMessage(to,h.mid)
                            h = pb9.getContact(pb9MID)
                            pb9.sendMessage(to,h.mid)
                            h = pb10.getContact(pb10MID)
                            pb10.sendMessage(to,h.mid)
                        elif prankbot == "myname":
                            contact = sb.getContact(sender)
                            sb.sendMessage(to, "{}".format(contact.displayName))
                        elif prankbot == "mystatus":
                            contact = sb.getContact(sender)
                            sb.sendMessage(to, "{}".format(contact.statusMessage))
                        elif prankbot == "mypict":
                            sb.sendContact(to, sender)
                            contact = sb.getContact(sender)
                            sb.sendImageWithURL(to,"http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus))
                        elif prankbot == "myvideo":
                            contact = sb.getContact(sender)
                            sb.sendVideoWithURL(to,"http://dl.profile.line-cdn.net/{}/vp".format(contact.pictureStatus))
                        elif prankbot == "mycover":
                            channel = sb.getProfileCoverURL(sender)          
                            path = str(channel)
                            sb.sendImageWithURL(to, path)
                        elif prankbot.startswith("smule "):
                            sep = text.split(" ")
                            key = text.replace(sep[0] + " ","")
                            smule = "https://www.smule.com/"+ key
                            sb.sendMessage(to, "ini id smulenya kak\n" + smule)
                        elif prankbot.startswith("gname "):
                            if msg.toType == 2:
                                X = sb.getGroup(to)
                                sep = msg.text.split(" ")
                                X.name = msg.text.replace(sep[0] + " ","")
                                sb.updateGroup(X)
                        elif prankbot.startswith("twitter "):
                            sep = text.split(" ")
                            key = text.replace(sep[0] + " ","")
                            twitter = "https://www.twitter.com/"+ key
                            sb.sendMessage(to, "pencarian untuk user id "+key+"\nini twitternya kak\n"+twitter)
                        elif prankbot == "friendlist":
                            contactlist = sb.getAllContactIds()
                            kontak = sb.getContacts(contactlist)
                            num=1
                            msgs="╭━━━━━══[ Friend List ]══━━━━━╮"
                            for ids in kontak:
                                msgs+="\n[%i] %s" % (num, ids.displayName)
                                num=(num+1)
                            msgs+="\n━━━━━══[ Friend Result ]══━━━━━\nTotal : %i" % len(kontak)
                            sb.sendMessage(to, msgs)
                        elif prankbot == "berita":
                             r=requests.get("https://newsapi.org/v2/top-headlines?country=id&apiKey=1214d6480f6848e18e01ba6985e2008d")
                             data=r.text
                             data=json.loads(data)
                             hasil = "╔═════════❴BERITA TERKINI❵════════╗\n\n"
                             hasil += "║1. " + str(data["articles"][0]["title"])                                                        
                             hasil += "\n║    Sumber : " + str(data["articles"][0]["source"]["name"])
                             hasil += "\n║    Penulis : " + str(data["articles"][0]["author"])
                             hasil += "\n║    Link : " + str(data["articles"][0]["url"])
                             hasil += "\n═══════════════════════════\n║2. " + str(data["articles"][1]["title"])                                                        
                             hasil += "\n║    Sumber : " + str(data["articles"][1]["source"]["name"])
                             hasil += "\n║    Penulis : " + str(data["articles"][1]["author"])   
                             hasil += "\n║    Link : " + str(data["articles"][1]["url"])
                             hasil += "\n═══════════════════════════\n║3. " + str(data["articles"][2]["title"])                                                        
                             hasil += "\n║    Sumber : " + str(data["articles"][2]["source"]["name"])
                             hasil += "\n║    Penulis : " + str(data["articles"][2]["author"])
                             hasil += "\n║    Link : " + str(data["articles"][2]["url"])
                             hasil += "\n═══════════════════════════\n║4. " + str(data["articles"][3]["title"])                                                        
                             hasil += "\n║    Sumber : " + str(data["articles"][3]["source"]["name"])
                             hasil += "\n║    Penulis : " + str(data["articles"][3]["author"])
                             hasil += "\n║    Link : " + str(data["articles"][3]["url"])
                             hasil += "\n═══════════════════════════\nv5. " + str(data["articles"][4]["title"])                                                        
                             hasil += "\n║    Sumber : " + str(data["articles"][4]["source"]["name"])
                             hasil += "\n║    Penulis : " + str(data["articles"][4]["author"])
                             hasil += "\n║    Link : " + str(data["articles"][4]["url"])
                             hasil += "\n═══════════════════════════\n║6. " + str(data["articles"][5]["title"])                                                        
                             hasil += "\n║    Sumber : " + str(data["articles"][5]["source"]["name"])
                             hasil += "\n║    Penulis : " + str(data["articles"][5]["author"])
                             hasil += "\n║    Link : " + str(data["articles"][5]["url"])
                             hasil += "\n═══════════════════════════\n║7. " + str(data["articles"][6]["title"])                                                        
                             hasil += "\n║    Sumber : " + str(data["articles"][6]["source"]["name"])
                             hasil += "\n║    Penulis : " + str(data["articles"][6]["author"])
                             hasil += "\n║    Link : " + str(data["articles"][6]["url"])
                             hasil += "\n═══════════════════════════\n║8. " + str(data["articles"][7]["title"])                                                        
                             hasil += "\n║    Sumber : " + str(data["articles"][7]["source"]["name"])
                             hasil += "\n║    Penulis : " + str(data["articles"][7]["author"])
                             hasil += "\n║    Link : " + str(data["articles"][7]["url"])
                             hasil += "\n═══════════════════════════\n║9. " + str(data["articles"][8]["title"])                                                        
                             hasil += "\n║    Sumber : " + str(data["articles"][8]["source"]["name"])
                             hasil += "\n║    Penulis : " + str(data["articles"][8]["author"])
                             hasil += "\n║    Link : " + str(data["articles"][8]["url"])
                             hasil += "\n═══════════════════════════\n║10. " + str(data["articles"][9]["title"])                                                        
                             hasil += "\n║    Sumber : " + str(data["articles"][9]["source"]["name"])
                             hasil += "\n║    Penulis : " + str(data["articles"][9]["author"])
                             hasil += "\n║    Link : " + str(data["articles"][9]["url"])
                             hasil += "\n═══════════════════════════\n║11. " + str(data["articles"][10]["title"])                                                        
                             hasil += "\n║    Sumber : " + str(data["articles"][10]["source"]["name"])
                             hasil += "\n║    Penulis : " + str(data["articles"][10]["author"])
                             hasil += "\n║    Link : " + str(data["articles"][10]["url"] + "\n╚═════════════❴NEWS❵══════════════╝")
                             sb.sendMessage(to, str(hasil))
                        elif prankbot == "friendblocklist":
                            blockedlist = sb.getBlockedContactIds()
                            kontak = sb.getContacts(blockedlist)
                            num=1
                            msgs="╭━━━━━══[ Friend Block ]══━━━━━╮"
                            for ids in kontak:
                                msgs+="\n[%i] %s" % (num, ids.displayName)
                                num=(num+1)
                            msgs+="\n━━━━━══[ Block Result ]══━━━━━\nBlock Total : %i" % len(kontak)
                            sb.sendMessage(to, msgs)
                        elif prankbot == "gcreator":
                            sb.sendMessage(to, "━━━━══[Pembuat Grup]══━━━━")
                            group = sb.getGroup(to)
                            GS = group.creator.mid
                            sb.sendContact(to, GS)
                            sb.sendMessage(to, "━━━━══━━╩━━══━━━━")
                        elif prankbot == "memberlist":
                            if sender in sbMID:
                                if msg.toType == 2:
                                    group = sb.getGroup(to)
                                    ret_ = "╭━━━══[ Member List ]"
                                    no = 0 + 1
                                    for mem in group.members:
                                        ret_ += "\n┣═ {}. {}".format(str(no), str(mem.displayName))
                                        no += 1
                                    ret_ += "\n╰━━━══[ Total {} member]".format(str(len(group.members)))
                                    sb.sendMessage(to, str(ret_))
                                
                        elif prankbot == "pendinglist":
                            if sender in sbMID:
                                if msg.toType == 2:
                                    group = sb.getGroup(to)
                                    ret_ = "╭━━━══[ Pending List ]"
                                    no = 0 + 1
                                    if group.invitee is None or group.invitee == []:
                                        sb.sendMessage(to, "Tidak ada pendingan")
                                        return
                                    else:
                                        for pen in group.invitee:
                                            ret_ += "\n┣═ {}. {}".format(str(no), str(pen.displayName))
                                            no += 1
                                        ret_ += "\n╰━━━══[ Total {} tertunda]".format(str(len(group.invitee)))
                                        sb.sendMessage(to, str(ret_))
                        
                        elif prankbot == "ginfo":
                            if sender in sbMID:
                                group = sb.getGroup(to)
                                try:
                                    gCreator = group.creator.displayName
                                except:
                                    gCreator = "Tidak ditemukan"
                                if group.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(group.invitee))
                                if group.preventedJoinByTicket == True:
                                    gQr = "Closed"
                                    gTicket = "Qr tidak tersedia karna di tutup"
                                else:
                                    gQr = "Open"
                                    gTicket = "https://sb.me/R/ti/g/{}".format(str(sb.reissueGroupTicket(group.id)))
                                path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                                ret_ = "╭━━━━══[ Group Info ]"
                                ret_ += "\n┣═Nama Group : {}".format(str(group.name))
                                ret_ += "\n┣═ID Group : {}".format(group.id)
                                ret_ += "\n┣═Pembuat : {}".format(str(gCreator))
                                ret_ += "\n┣═Jumlah Member : {}".format(str(len(group.members)))
                                ret_ += "\n┣═Jumlah Pending : {}".format(gPending)
                                ret_ += "\n┣═━━━Kode Qr/Link━━━═"
                                ret_ += "\n┣═Group Ticket : {}".format(gTicket)
                                ret_ += "\n┣═Group Qr : {}".format(gQr)
                                ret_ += "\n╰━━━━══[ CREATOR PRANKBOT]"
                                sb.sendMessage(to, str(ret_))
                        elif prankbot.startswith("getmid "):
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                ret_ = ""
                                for ls in lists:
                                    ret_ += "{}".format(str(ls))
                                sb.sendMessage(to, str(ret_))
                        elif prankbot.startswith("getpict "):
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    path = "http://dl.profile.sb.naver.jp/" + sb.getContact(ls).pictureStatus
                                    sb.sendImageWithURL(to, str(path))
                        elif prankbot.startswith("getname "):
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    contact = sb.getContact(ls)
                                    sb.sendMessage(to, "┣━━NAMA DI TAMPILKAN━━╣\n{}".format(str(contact.displayName)))
                        elif prankbot.startswith("getstatus "):
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    contact = sb.getContact(ls)
                                    sb.sendMessage(to, "┣━━╦━━STATUS DI TAMPILKAN━━╦━━╣\n{}".format(str(contact.statusMessage)))
                        elif prankbot.startswith("getcontact "):
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    contact = sb.getContact(ls)
                                    mi_d = contact.mid
                                    sb.sendContact(to, mi_d)
                        elif prankbot == "gpict":
                            group = sb.getGroup(to)
                            path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                            sb.sendImageWithURL(to, path)
                        elif prankbot == "gname":
                            gid = sb.getGroup(to)
                            sb.sendMessage(to, "[Nama Group : ]\n" + gid.name)
                        elif prankbot == "gid":
                            gid = sb.getGroup(to)
                            sb.sendMessage(to,gid.id)
                        elif prankbot == "gurl":
                            if msg.toType == 2:
                                group = sb.getGroup(to)
                                if group.preventedJoinByTicket == False:
                                    ticket = sb.reissueGroupTicket(to)
                                    sb.sendMessage(to, "https://sb.me/R/ti/g/{}".format(str(ticket)))
                                else:
                                    group.preventedJoinByTicket = False
                                    sb.updateGroup(group)
                                    sb.sendMessage(to, "https://sb.me/R/ti/g/{}".format(str(ticket)))
                        elif prankbot == "url:on":
                            if msg.toType == 2:
                                group = sb.getGroup(to)
                                if group.preventedJoinByTicket == False:
                                    sb.sendMessage(to, "Sudah terbuka")
                                else:
                                    group.preventedJoinByTicket = False
                                    sb.updateGroup(group)
                                    sb.sendMessage(to, "Berhasil membuka Qr")
                        elif prankbot == "url:off":
                            if msg.toType == 2:
                                group = sb.getGroup(to)
                                if group.preventedJoinByTicket == True:
                                    sb.sendMessage(to, "Sudah tertutup")
                                else:
                                    group.preventedJoinByTicket = True
                                    sb.updateGroup(group)
                                    sb.sendMessage(to, "Berhasil menutup Qr")
                        elif prankbot.startswith("ttl "):
                            try:
                                sep = msg.text.split(" ")
                                tanggal = msg.text.replace(sep[0] + " ","")
                                r = requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                                data=r.text
                                data=json.loads(data)
                                ret_ = "╭━━━━════[Tanggal,Lahir]"
                                ret_ += "\n┣═Tanggal lahir : {}".format(str(data["data"]["lahir"]))
                                ret_ += "\n┣═Umur : {}".format(str(data["data"]["usia"]))
                                ret_ += "\n┣═Tanggal ultah : {}".format(str(data["data"]["ultah"]))
                                ret_ += "\n┣═Zodiak : {}".format(str(data["data"]["zodiak"]))
                                ret_ += "\n╰━━═════[CREATOR PRANKBOTS]"
                                sb.sendMessage(to, str(ret_))
                            except Exception as error:
                                logError(error)
                        elif prankbot.startswith("youtube "):
                            sb.sendMessage(to, "Waiting...")
                            sep = text.split(" ")
                            search = text.replace(sep[0] + " ","")
                            params = {"search_query": search}
                            with requests.session() as web:
                                web.headers["User-Agent"] = random.choice(settings["userAgent"])
                                r = web.get("https://www.youtube.com/results", params = params)
                                soup = BeautifulSoup(r.content, "html5lib")
                                ret_ = "╭━━━━━[ Youtube link di tampilkan ]━"
                                datas = []
                                for data in soup.select(".yt-lockup-title > a[title]"):
                                    if "&lists" not in data["href"]:
                                        datas.append(data)
                                for data in datas:
                                    ret_ += "\n┣[ {} ]".format(str(data["title"]))
                                    ret_ += "\n┣━ https://www.youtube.com{}".format(str(data["href"]))
                                ret_ += "\n╰━━━━━━━━[ Total {} link]━━━━━".format(len(datas))
                                sb.sendMessage(to, str(ret_))
                    if "/ti/g/" in text.lower():
                        if settings["prankJoinLink"] == True:
                            link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                            links = link_re.findall(text)
                            n_links = []
                            for l in links:
                                if l not in n_links:
                                    n_links.append(l)
                            for ticket_id in n_links:
                                group = sb.findGroupByTicket(ticket_id)
                                sb.acceptGroupInvitationByTicket(group.id,ticket_id)
                                pb1.acceptGroupInvitationByTicket(group.id,ticket_id)
                                pb2.acceptGroupInvitationByTicket(group.id,ticket_id)
                                pb3.acceptGroupInvitationByTicket(group.id,ticket_id)
                                pb4.acceptGroupInvitationByTicket(group.id,ticket_id)
                                pb5.acceptGroupInvitationByTicket(group.id,ticket_id)
                                pb6.acceptGroupInvitationByTicket(group.id,ticket_id)
                                pb7.acceptGroupInvitationByTicket(group.id,ticket_id)
                                pb8.acceptGroupInvitationByTicket(group.id,ticket_id)
                                pb9.acceptGroupInvitationByTicket(group.id,ticket_id)
                                pb10.acceptGroupInvitationByTicket(group.id,ticket_id)
                                sb.sendMessage(to, "Berhasil masuk ke group %s" % str(group.name))
                elif msg.contentType == 13:
                    if settings["prankcontact"] == True:
                        try:
                            contact = sb.getContact(msg.contentMetadata["mid"])
                            if line != None:
                                cover = sb.getProfileCoverURL(msg.contentMetadata["mid"])
                            else:
                                cover = "Tidak dapat masuk di line channel"
                            path = "http://dl.profile.line-cdn.net/{}".format(str(contact.pictureStatus))
                            try:
                                sb.sendImageWithURL(to, str(path))
                            except:
                                pass
                            ret_ = "╭━━━━══[ Contact Info ]"
                            ret_ += "\n┣═Nama : {}".format(str(contact.displayName))
                            ret_ += "\n┣═MID : {}".format(str(msg.contentMetadata["mid"]))
                            ret_ += "\n┣═Bio : {}".format(str(contact.statusMessage))
                            ret_ += "\n┣═Link Profile : http://dl.profile.line-cdn.net/{}".format(str(contact.pictureStatus))
                            ret_ += "\n┣═Link Cover : {}".format(str(cover))
                            ret_ += "\n╰━━━━══[CREATOR PRANKBOT]"
                            sb.sendMessage(to, str(ret_))
                        except:
                            sb.sendMessage(to, "Kontak tidak valid")
                elif msg.contentType == 16:
                        if settings["prankTL"] == True:
                            try:
                                ret_ = "╔══[ Details Post ]"
                                if msg.contentMetadata["serviceType"] == "GB":
                                    contact = sb.getContact(sender)
                                    auth = "\n╠ Penulis : {}".format(str(contact.displayName))
                                else:
                                    auth = "\n╠ Penulis : {}".format(str(msg.contentMetadata["serviceName"]))
                                purl = "\n╠ URL : {}".format(str(msg.contentMetadata["postEndUrl"]).replace("line://","https://sb.me/R/"))
                                ret_ += auth
                                ret_ += purl
                                if "mediaOid" in msg.contentMetadata:
                                    object_ = msg.contentMetadata["mediaOid"].replace("svc=myhome|sid=h|","")
                                    if msg.contentMetadata["mediaType"] == "V":
                                        if msg.contentMetadata["serviceType"] == "GB":
                                            ourl = "\n╠ Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                            murl = "\n╠ Media URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(msg.contentMetadata["mediaOid"]))
                                        else:
                                            ourl = "\n╠ Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                            murl = "\n╠ Media URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(object_))
                                        ret_ += murl
                                    else:
                                        if msg.contentMetadata["serviceType"] == "GB":
                                            ourl = "\n╠ Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                        else:
                                            ourl = "\n╠ Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                    ret_ += ourl
                                if "stickerId" in msg.contentMetadata:
                                    stck = "\n╠ Stiker : https://sb.me/R/shop/detail/{}".format(str(msg.contentMetadata["packageId"]))
                                    ret_ += stck
                                if "text" in msg.contentMetadata:
                                    text = "\n╠ Tulisan : {}".format(str(msg.contentMetadata["text"]))
                                    ret_ += text
                                ret_ += "\n╚══[ Finish ]"
                                sb.sendMessage(to, str(ret_))
                            except Exception as error:
                                logError(error)
                                traceback.print_tb(error.__traceback__)
    except Exception as error:
        logError(error)
        if op.type == 59:
            print (op)
while True:
    try:
      ops=oepoll.singleTrace(count=50)
      if ops != None:
        for op in ops: 
          bot(op)
          oepoll.setRevision(op.revision)
        
    except Exception as e:
        sb.log("[SINGLE_TRACE] ERROR : " + str(e))
