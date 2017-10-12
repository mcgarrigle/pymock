#!/usr/bin/env python

from service import Service

class Client(object):

    def __init__(self, the_service):
        print("initialising client")
        self.service = the_service("awesome")

    def run(self):
        print("calling service")
        self.service.call("hello")

if __name__ == "__main__":
    print("starting client")
    c = Client(Service)
    c.run()
    print("stopping client")
