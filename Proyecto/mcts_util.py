from platform import node
import quarto
from quarto import Quarto
import random
AI_WIN = 1
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
    # unexplored_nodes = []
    # explored_nodes = []

    current_node = tree_root
    while(current_node.state.has_finished() == False):
        rand_value = random.random()
        if current_node.explored == True and rand_value > exploitation:
            """
            Si este estado ha sido explorado antes, entonces genere un número
            al azar, de ser mayor al exploitation entonces se elige la acción
            que lleva al mejor estado conocido
            """
            pass
        else:
            current_node.explored = True
            current_node = expand_node(current_node)
    if current_node.state.get_winner() == AI_WIN:
        current_node.result = [1, 0]
    else:
        current_node.result = [0, 1]

    # aqui se selecciona a un hijo random
    # select_node(tree_root.children[0], explored_nodes)

# Return none is it has all children, so it does not expand


def expand_node(node: Node):
    actions = node.state.get_available_actions()
    index = random.randint(0, len(actions) - 1)
    child = Node(state=node.state.do_action(action=actions[index]), id=index)

    if (is_duplicate(node, child)):
        return get_duplicate(node, child)

    else:
        child.set_parent(node)
        node.add_child(child)
        return child


def is_duplicate(node: Node, child: Node):
    for i in node.children:
        if i.id == child.id:
            return True
    return False


def get_duplicate(node: Node, child: Node):
    for i in node.children:
        if i.id == child.id:
            return i


root = Node(Quarto())
expand_node(root, [])
