from client import Client


class Server:
    def __init__(self):
        self.current_client = None

    def working(self):
        if self.current_client:
            return True
        return False

    def increment_queue_time(self):
        self.queue_time += 1

    def increment_serverd_time(self):
        self.server_time += 1

    def add_client(self, client):
        self.current_client = client
