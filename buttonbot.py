import config

from slackbot import Bot

class Buttonbot():
    def __init__(self):
        self.bot = Bot()
        self.listen()

    def listen(self):
        if self.bot.sc.rtm_connect():
            # while True:
            self.bot.emoji(":wolf:")
        else:
            print("Slack connection failed")


buttonbot = Buttonbot()
