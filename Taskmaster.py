import requests
import json


class TaskMaster:
    def __init__(self, url, name, password):
        self.url = url
        self.name = name
        self.password = password
        self.task_endpoint = "{}task/{}"
        self.taskstep_endpoint = "{}task_step/{}"

    def view_all(self):
        res = requests.get(self.url + 'view', auth=(self.name, self.password))
        print(res.text)

    def view_task(self, task_id):
        endpoint = self.task_endpoint.format(self.url, task_id)
        res = requests.get(endpoint, auth=(self.name, self.password))
        print(res.text)

    def add_task(self, task_name):
        endpoint = "{}tasks".format(self.url)
        res = requests.post(endpoint, json={"task_name": task_name}, auth=(self.name, self.password))
        print(res.text)

    def update_taskname(self, task_id, new_taskname):
        endpoint = self.task_endpoint.format(self.url, task_id)
        res = requests.put(endpoint, json={"task_name": new_taskname}, auth=(self.name, self.password))
        print(res.text)

    def delete_task(self, task_id):
        endpoint = self.task_endpoint.format(self.url, task_id)
        res = requests.delete(endpoint, auth=(self.name, self.password))
        print(res.text)

    def view_all_tasksteps(self):
        endpoint = "{}task_steps".format(self.url)
        res = requests.get(endpoint, auth=(self.name, self.password))
        print(res.text)

    def add_taskstep(self, task_id, step_name):
        endpoint = "{}task_steps".format(self.url)
        new_step = {"task_id": task_id, "step_name": step_name}
        res = requests.post(endpoint, json=new_step, auth=(self.name, self.password))
        print(res.text)

    def view_taskstep(self, taskstep_id):
        endpoint = self.taskstep_endpoint.format(self.url, taskstep_id)
        res = requests.get(endpoint, auth=(self.name, self.password))
        print(res.text)

    def complete_taskstep(self, taskstep_id):
        endpoint = self.taskstep_endpoint.format(self.url, taskstep_id)
        res = requests.put(endpoint, auth=(self.name, self.password))
        print(res.text)

    def delete_taskstep(self, taskstep_id):
        endpoint = self.taskstep_endpoint.format(self.url, taskstep_id)
        res = requests.delete(endpoint, auth=(self.name, self.password))
        print(res.text)

    def view_task_progress(self, task_id):
        endpoint = "{}task/{}/task_steps".format(self.url, task_id)
        res = requests.get(endpoint, auth=(self.name, self.password))
        print(res.text)
