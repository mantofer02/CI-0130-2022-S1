from server import Server
from client import Client
from typing import List
from math_util import rand_exp


try:
    from colorama import Fore
    from colorama import Style
except ModuleNotFoundError:
    class Object():
        pass
    Fore = Object()
    Style = Object()
    Fore.YELLOW = ''
    Fore.GREEN = ''
    Fore.RED = ''
    Style.RESET_ALL = ''

TIME_LIMIT = 30
ARRIVE_EVENT = 'arrive'
SERVE_EVENT = 'serve'


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

        self.event_list = []

        self.init_servers()
        self.simulation(TIME_LIMIT)
        self.print_results()

    def init_servers(self):
        for i in range(self.s):
            self.servers.append(Server())

    def tick(self, n):
        for i in range(len(self.clients_on_wait)):
            self.clients_on_wait[i].tick(n)

        for i in range(len(self.clients_on_servers)):
            if (self.clients_on_servers[i]):
                self.clients_on_servers[i].tick(n)

        for i in self.servers:
            i.tick(n)

    def simulation(self, time_limit):
        print("Beginning simulation:")
        print(" Time Limit: " + str(TIME_LIMIT))
        print(" Amount of servers: " + str(self.s))
        print(" lmax: " + str(self.lmax))
        print()

        tick_counter = 0
        while (self.time < time_limit):
            if (len(self.event_list)):
                if (self.event_list[0][0] == ARRIVE_EVENT):
                    self.add_client_to_queue()
                    tick_counter = rand_exp(
                        self.lambd(self.get_n())) + self.time
                    self.event_list.append(
                        (ARRIVE_EVENT, tick_counter, None))
                    self.event_list.pop(0)
                else:
                    if (self.event_list[0][0] == SERVE_EVENT):
                        self.free_client_from_server(self.event_list[0][2])
                        self.event_list.pop(0)
            else:
                self.add_client_to_queue()
                tick_counter = rand_exp(
                    self.lambd(self.get_n())) + self.time
                self.event_list.append(
                    (ARRIVE_EVENT, tick_counter, None))

            for i in range(len(self.servers)):
                if (self.servers[i].working() == False):
                    self.add_client_to_server(i)

            self.event_list.sort(key=lambda tup: tup[1])

            prev_time = self.time
            self.time = self.event_list[0][1]
            self.tick(self.time - prev_time)

    def get_n(self):
        n = 0
        for client in self.clients_on_servers:
            if (client):
                n += 1

        return len(self.clients_on_wait) + n

    def add_client_to_queue(self):
        if (self.get_n() <= self.lmax):
            print(f"  {Fore.RED}client added to queue!{Style.RESET_ALL}")
            self.clients_on_wait.append(Client())
        else:
            print(
                f"  {Fore.RED}client arrived but queue was full!{Style.RESET_ALL}")
            self.clients_lost += 1

    def free_client_from_server(self, i):
        self.clients_finished.append(self.servers[i].free_server())
        self.clients_on_servers[i] = None
        print(f"  {Fore.GREEN}client freed from system!{Style.RESET_ALL}")
        self.clients_served += 1

    def add_client_to_server(self, i):
        if (len(self.clients_on_wait) > 0):
            print(
                f"  {Fore.YELLOW}server attending client!{Style.RESET_ALL}")
            client = self.clients_on_wait.pop(0)
            client.set_wait(False)
            self.servers[i].add_client(client)
            self.clients_on_servers[i] = client
            self.event_list.append(
                (SERVE_EVENT, rand_exp(self.mu(self.get_n())) + self.time, i))

    def print_results(self):
        print()
        print("Results:")
        print("    Clients Lost: " + str(self.clients_lost))
        print("    Clients Served: " + str(self.clients_served))
        idle_time = 0
        for i in self.servers:
            idle_time += i.free_time
        print("    Servers idle time total: " + str(idle_time))
        print("    Servers idle average time: " + str(idle_time/self.s))
