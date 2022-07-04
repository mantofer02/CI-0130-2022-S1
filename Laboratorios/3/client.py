class Client:
    def __init__(self):
        self.queue_time = 0
        self.served_time = 0
        self.waiting = True
        self.finished = False

    def finish(self):
        self.finish = True

    def is_waiting(self):
        return self.waiting

    def set_wait(self, status):
        self.waiting = status

    def go_to_server(self):
        self.waiting = False

    def increment_queue_time(self, n):
        self.queue_time += n

    def increment_serverd_time(self, n):
        self.served_time += n

    def tick(self, n):
        if (not self.finished):
            if self.waiting:
                self.increment_queue_time(n)
            else:
                self.increment_serverd_time(n)
