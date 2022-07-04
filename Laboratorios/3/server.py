from client import Client


class Server:
    def __init__(self):
        self.current_client = None
        self.serving_time = 0
        self.free_time = 0
        self.finished = False

    def working(self):
        if self.current_client:
            return True
        return False

    def increment_serving_time(self, n):
        self.serving_time += 1

    def increment_free_time(self, n):
        self.free_time += 1

    def add_client(self, client: Client):
        self.serving_time = 0
        self.current_client = client

    def free_server(self):
        client = self.current_client
        self.current_client = None
        self.serving_time = 0
        return client

    def tick(self, n):
        if (not self.finished):
            if self.working():
                self.increment_serving_time(n)
            else:
                self.increment_free_time(n)
