import quarto
from quarto import Quarto

ITERATIONS = 10


class Node(object):
    def __init__(self, state):
        self.state: Quarto = state
        self.children = []
        self.parent: Quarto = None
        self.explored = False
        # AI WINS/ PLAYER WINS
        self.result = [0, 0]

    def add_child(self, obj):
        self.children.append(obj)

    def set_parent(self, parent):
        self.parent = parent


def mcts(root: Quarto, time_limit=0.25, exploitation=0.5):
    tree_root: Node = Node(root)
    unexplored_nodes = []
    explored_nodes = []

    expand_node(tree_root, unexplored_nodes)

    # aqui se selecciona a un hijo random
    select_node(tree_root.children[0], explored_nodes)


def expand_node(node: Node, unexplored_nodes):
    for action in node.state.get_available_actions():
        child = Node(node.state.do_action(action))
        child.set_parent(node)
        node.add_child(child)
        unexplored_nodes.append(child)


def select_node(node: Node, explored_nodes):
    node.explored = True
    explored_nodes.append(node)
