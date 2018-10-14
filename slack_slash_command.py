# -*- coding: utf-8 -*-
import os

import requests
from slacker import Slacker

CHANNEL = os.getenv("CHANNEL")
API_TOKEN = os.getenv("API_TOKEN")
MESSAGE = os.getenv("MESSAGE")


def lambda_handler(event, context):
    from requests.sessions import Session
    with Session() as session:
        slack = Slacker(API_TOKEN, session=session)
        if COMMAND[0] == "":
                slack.chat.command(CHANNEL, MESSAGE, "")
        else:
                slack.chat.post_message(CHANNEL, MESSAGE)

if __name__ == '__main__': main()
