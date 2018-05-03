import config
import pyinotify

from slackbot import Bot

class Buttonbot():
    def __init__(self):
        self.bot = Bot()
        self.listen()

    def listen(self):
        if self.bot.sc.rtm_connect():
            self.bot.emoji(":wolf:")
        else:
            print("Slack connection failed")

class ModHandler(pyinotify.ProcessEvent):
    def process_IN_CLOSE_WRITE(self, evt):
        fileHandle = open("log.txt", "r")
        lineList = fileHandle.readlines()
        fileHandle.close()
        emoji = lineList[-1]
        buttonbot.bot.emoji(emoji)
        if emoji == ':hal_9000:':
            buttonbot.bot.message('playpause')

buttonbot = Buttonbot()
handler = ModHandler()
wm = pyinotify.WatchManager()
notifier = pyinotify.Notifier(wm, handler)
wdd = wm.add_watch("log.txt", pyinotify.IN_CLOSE_WRITE)
notifier.loop()
