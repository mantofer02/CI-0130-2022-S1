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

    """
        @function
        increment_queue_time
        @description
        Function that increments the queue time. 
        ----------
        @parameters
        ----------
        self
    """

    def increment_queue_time(self):
        self.queue_time += 1

        """
        @function
        increment_serverd_time
        @description
        Function that increments the served time. 
        ----------
        @parameters
        ----------
        self
    """

    def increment_serverd_time(self):
        self.served_time += 1

    """
        @function
        tick
        @description
        Function that creates a tick for a client. 
        ----------
        @parameters
        ----------
        self
    """

    def tick(self):
        if (not self.finished):
            if self.waiting:
                self.increment_queue_time()
            else:
                self.increment_serverd_time()
