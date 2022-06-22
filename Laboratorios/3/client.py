class Client:
    def __init__(self):
        self.queue_time = 0
        self.served_time = 0

    def increment_queue_time(self):
        self.queue_time += 1

    def increment_serverd_time(self):
        self.server_time += 1
