
class Service:

    def __init__(self, endpoint):
        print("service initialising")
        self.endpoint = endpoint

    def call(self, record):
        print("service @", self.endpoint, "<=", record)

