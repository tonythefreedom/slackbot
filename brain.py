# -*- coding: utf-8 -*-
import requests

class Brain():
    def __init__(self):
        super(Brain, self).__init__()

    def sendMSG(self, text, channel) :
        data = {"text": text}
        if channel == 1:
            response = requests.post("https://hooks.slack.com/services/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", json=data)
        elif channel == 2:
            response = requests.post("https://hooks.slack.com/services/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", json=data)
        print(response.status_code)