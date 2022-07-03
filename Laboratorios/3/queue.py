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
        self.clients_on_servers: List[Client] = [None] * self.s
        self.clients_finished: List[Client] = []
        self.servers: List[Server] = []
        self.time = 0
        self.clients_served = 0
        self.clients_lost = 0

        self.init_servers()
        self.simulation(1000)

    def init_servers(self):
        for i in range(self.s):
            self.servers.append(Server())

    def tick(self):
        self.time += 1
        for i in range(len(self.clients_on_wait)):
            self.clients_on_wait[i].tick()

        for i in range(len(self.clients_on_servers)):
            if (self.clients_on_servers[i]):
                self.clients_on_servers[i].tick()

        for i in self.servers:
            i.tick()

    def simulation(self, time_limit):
        lambd_counter = 0
        while (self.time < time_limit):
            # print("Lambda value = " + str(self.lambd(self.get_n())))
            if (lambd_counter >= self.lambd(self.get_n())):
                self.add_client_to_queue()
                lambd_counter = 0

            for i in range(len(self.servers)):
                if (self.servers[i].serving_time >= self.lambd(self.get_n())):
                    self.free_client_from_server(i)

            for i in range(len(self.servers)):
                if (self.servers[i].working() == False):
                    if (len(self.clients_on_wait) > 0):
                        print("client on server!")
                        client = self.clients_on_wait.pop(0)
                        client.set_wait(False)
                        self.servers[i].add_client(client)
                        self.clients_on_servers[i] = client

            self.tick()
            lambd_counter += 1
        print(self.time)
        input()

    def get_n(self):
        n = 0
        for client in self.clients_on_servers:
            if (client):
                n += 1

        return len(self.clients_on_wait) + n

    def add_client_to_queue(self):
        if (self.get_n() <= self.lmax):
            print("client added to queue!")
            self.clients_on_wait.append(Client())

    def free_client_from_server(self, i):
        self.clients_finished.append(self.servers[i].free_server())
        self.clients_on_servers[i] = None
        print("client freed from system!")
        self.clients_served += 1

    def print_results(self):
        pass
