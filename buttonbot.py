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
    # evt has useful properties, including pathname
    def process_IN_CLOSE_WRITE(self, evt):
        buttonbot.bot.emoji(":wolf:")

buttonbot = Buttonbot()
handler = ModHandler()
wm = pyinotify.WatchManager()
notifier = pyinotify.Notifier(wm, handler)
wdd = wm.add_watch('log.txt', pyinotify.IN_CLOSE_WRITE)
notifier.loop()
