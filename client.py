#!/usr/bin/env python

from service import Service

class Client(object):

    def __init__(self):
        print("initialising client")
        self.service = Service("awesome")

    def run(self):
        print("calling service")
        self.service.call("hello")

if __name__ == "__main__":
    print("starting client")
    c = Client()
    c.run()
    print("stopping client")
