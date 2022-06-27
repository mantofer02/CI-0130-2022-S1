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

    def increment_queue_time(self):
        self.queue_time += 1

    def increment_serverd_time(self):
        self.served_time += 1

    def tick(self):
        if (not self.finished):
            if self.waiting:
                self.increment_queue_time()
            else:
                self.increment_serverd_time()
