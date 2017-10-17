
class Service:

    def __init__(self, endpoint):
        print("service initialising")
        self.endpoint = endpoint

    def send(self, record):
        print("service @", self.endpoint, "<=", record)

