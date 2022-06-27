from server import Server
from client import Client
from typing import List


class Queue:
    # lambd and mu are functions
    def __init__(self, lmax, s, lambd, mu) -> None:
        self.lmax = lmax
        self.s = s
        self.lambd = lambd
        self.mu = mu

        self.clients_on_wait: List[Client] = []
        self.clients_on_servers: List[Client] = []
        self.servers: List[Server] = []
        self.time = 0
        self.clients_served = 0
        self.clients_lost = 0

        self.init_servers()
        self.simulation(30)

    def init_servers(self):
        for i in range(self.s):
            self.servers.append(Server())

    def tick(self):
        self.time += 1
        for i in self.clients_on_wait:
            i.tick()

        for i in self.clients_on_servers:
            i.tick()

        for i in self.servers:
            i.tick()

    def simulation(self, time_limit):
        while (self.time < time_limit):

            self.clients_on_wait.append(Client())

            for server in self.servers:
                if (server.working() == False):
                    if (len(self.clients_on_wait) > 0):

                        client = self.clients_on_wait.pop(0)
                        client.set_wait(False)
                        server.add_client(client)
                        self.clients_on_servers.append(client)

            self.tick()

            for i in self.clients_on_servers:
                print("Time of client " + str(i.served_time))

            print("Finished after " + str(self.time))
            input()

    def print_results(self):
        pass
