from client import Client


class Server:
    def __init__(self):
        self.current_client = None
        self.serving_time = 0
        self.free_time = 0
        self.finished = False

    """
        @function
        working
        @description
        Function that returns true or false depending on if a server is busy or not.
        ----------
        @parameters
        ----------
        self
    """

    def working(self):
        if self.current_client:
            return True
        return False

    """
        @function
        increment_serving_time
        @description
        Function that increments time if a client is being served.
        ----------
        @parameters
        ----------
        self
    """

    def increment_serving_time(self):
        self.serving_time += 1

    """
        @function
        increment_free_time
        @description
        Function that increments time if a server is free from a client.
        ----------
        @parameters
        ----------
        self
    """

    def increment_free_time(self):
        self.free_time += 1

    """
        @function
        add_client
        @description
        Function that adds client and resets serving time. 
        ----------
        @parameters
        ----------
        self
    """

    def add_client(self, client: Client):
        self.serving_time = 0
        self.current_client = client

    """
        @function
        free_server
        @description
        Function that frees a server from a client. 
        ----------
        @parameters
        ----------
        self
    """

    def free_server(self):
        client = self.current_client
        self.current_client = None
        return client

    """
        @function
        tick
        @description
        Function that creates a tick for a server. 
        ----------
        @parameters
        ----------
        self
    """

    def tick(self):
        if (not self.finished):
            if self.working():
                self.increment_serving_time()
            else:
                self.increment_free_time()
