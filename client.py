#!/usr/bin/env python

from service import Service

class Client(object):

    def __init__(self, service):
        print("initialising client")
        self.service = service

    def run(self):
        print("calling service")
        self.service.send("hello")

if __name__ == "__main__":
    print("starting client")
    s = Service("awesum")
    c = Client(s)
    c.run()
    print("stopping client")
