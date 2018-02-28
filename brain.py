# -*- coding: utf-8 -*-
import requests

class Brain():
    def __init__(self):
        super(Brain, self).__init__()

    def sendMSG(self, text) :
        data = {"text": text}
        response = requests.post("https://hooks.slack.com/services/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", json=data)
        print(response.status_code)