# -*- coding: utf-8 -*-
import requests

class Brain():
    def __init__(self):
        super(Brain, self).__init__()

    def sendMSG(self, text) :
        data = {'text': text}
        response = requests.post('https://hooks.slack.com/services/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', json=data)
        print(response.status_code)