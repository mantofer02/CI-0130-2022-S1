import quarto
from quarto import Quarto
import random

ITERATIONS = 10


class Node(object):
    def __init__(self, state, id=0):
        self.state: Quarto = state
        self.children: list[Node] = []
        self.parent: Quarto = None
        self.explored = False
        self.id = id
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

# Return none is it has all children, so it does not expand


def expand_node(node: Node, unexplored_nodes):
    actions = node.state.get_available_actions()
    if len(node.children) == len(actions):
        return None

    index = random.randint(0, len(actions) - 1)
    child = Node(state=node.state.do_action(action=actions[index]), id=index)

    while (is_duplicate(node, child)):
        index = (index + 1) % len(actions)
        child = Node(state=node.state.do_action(
            action=actions[index]), id=index)

    child.set_parent(node)
    node.add_child(child)
    unexplored_nodes.append(child)

    print(child.id)
    return child


def select_node(node: Node, explored_nodes):
    node.explored = True
    explored_nodes.append(node)


def is_duplicate(node: Node, child: Node):
    for i in node.children:
        if i.id == child.id:
            return True
    return False


root = Node(Quarto())
expand_node(root, [])
