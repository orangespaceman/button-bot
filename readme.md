# Button bot

Use a Raspberry Pi to detect interactions with the [buttons](https://github.com/thegingerbloke/button-basher) and send them through to our [Slack awkbot](https://github.com/thegingerbloke/awkbot-slack)


## Installation

1. Set up a new raspberry pi, plug the usb from the buttons makey makey into the pi

2. Check out this repo onto the pi

3. Install requirements: `pip install -r requirements.txt` (optional - do this in a virtualenv)

4. Set up a new _slack bot_ for the buttons:

  - Install the Bot Slack integration. Visit the following URL, replacing {SLACK-ACCOUNT-NAME} with your account:

    ```
    https://{SLACK-ACCOUNT-NAME}.slack.com/apps/A0F7YS25R-bots
    ```

  - Create a new bot user - e.g. @buttonbot

    ```
    https://{SLACK-ACCOUNT-NAME}.slack.com/apps/new/A0F7YS25R-bots
    ```
  - Once saved, take a note of the Slackbot API key

  - Add the bot user to all channels that you want it to work in

5. Can't remember, probably something important

6. Duplicate `config.sample.py`, call it `config.py`

    ```
    cp config.example.py config.py
    ```

7. Add the relevant config values to the config

8. Set up `buttonbot.service` to run when the Pi boots

    ```
    sudo cp buttonbot.service /lib/systemd/system/
    sudo systemctl enable buttonbot.service
    ```

    - To manually start/stop this service, run:

    ```
    sudo service buttonbot start
    sudo service buttonbot stop
    sudo service buttonbot status
    ```

9. Create a file in this directory called `log.txt` and set its permissions:

    ```
    touch log.txt
    chmod 777 log.txt
    ```

10. Install and set up [xbindkeys](https://wiki.archlinux.org/index.php/Xbindkeys) to detect when a button has been pressed and write the result to a text file:

    ```
    sudo apt-get install xbindkeys
    ```

    - Once installed, edit the config file:

    ```
    nano .xbindkeysrc
    ```

    - Add the following to the end of the file, adjusting the input keys and emojis as necessary:

    ```
    "echo ':dog:' >> /home/pi/button-bot/log.txt"
      Control+Shift+Alt+h
    ```