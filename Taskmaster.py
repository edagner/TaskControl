import requests
import json


class TaskMaster:
    def __init__(self, url, name, password):
        self.url = url
        self.name = name
        self.password = password

    def view_all(self):
        res = requests.get(self.url + 'view', auth=(self.name, self.password))
        print(res.text)
