class Client:
    def __init__(self):
        self.queue_time = 0
        self.served_time = 0
        self.waiting = True
        self.finished = False

    """
        @function
        finish
        @description
        Function that indicates that a client has a state of "served".
        ----------
        @parameters
        ----------
        self
    """

    def finish(self):
        self.finish = True

    """
        @function
        is_waiting
        @description
        Function that indicates that a client is waiting to be served. 
        ----------
        @parameters
        ----------
        self
    """

    def is_waiting(self):
        return self.waiting

    """
        @function
        set_wait
        @description
        Function that sets a client as a waiting status. 
        ----------
        @parameters
        ----------
        self
        status: string
                status to know wheter a client is waiting or not.
    """

    def set_wait(self, status):
        self.waiting = status

    """
        @function
        go_to_server
        @description
        Function that indicates that a client is about to be served. 
        ----------
        @parameters
        ----------
        self
    """

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
