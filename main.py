# -*- coding: utf-8 -*-
import os

import requests
from slacker import Slacker

CHANNEL = os.getenv("CHANNEL")
API_TOKEN = os.getenv("API_TOKEN")
COMMAND = os.getenv("COMMAND")
TEXT = os.getenv("TEXT")


def main():
    from requests.sessions import Session
    with Session() as session:
        slack = Slacker(API_TOKEN, session=session)
        slack.chat.command(CHANNEL, COMMAND, TEXT)


if __name__ == '__main__': main()
