from platform import node
import quarto
from quarto import Quarto
import random
import time
AI_WIN = 1
ITERATIONS = 10


class Node(object):
    def __init__(self, state, id=0):
        self.state: Quarto = state
        self.children: list[Node] = []
        self.parent: Node = None
        self.explored = False
        self.id = id
        self.leads_to_one = False
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

    elapsed_time = 0
    start_time = time.time()
    while (elapsed_time < time_limit):

        current_node = tree_root
        while(not current_node.state.has_finished()):
            rand_value = random.random()
            if (current_node.explored and rand_value > exploitation):
                """
                Si este estado ha sido explorado antes, entonces genere un número
                al azar, de ser mayor al exploitation entonces se elige la acción
                que lleva al mejor estado conocido
                """
                # current_node = find_best_state(current_node)
                index = 0
                chosen = False
                while (not chosen and index < len(current_node.children)):
                    current_child = current_node.children[index]
                    if (current_child.result == [1, 0]):
                        current_node = current_child
                        chosen = True
                    else:
                        index += 1
            else:
                current_node.explored = True
                current_node = expand_node(current_node)

        # Si en el estado final gana la IA
        if current_node.state.get_winner() == AI_WIN:
            current_node.result = [1, 0]

            while (current_node != tree_root):
                current_node.leads_to_one = True

                if (ai_wins(current_node)):        
                    current_node.parent.result = current_node.result
                    
                current_node = current_node.parent

        else:
            current_node.result = [0, 1]

            while (current_node != tree_root):
                current_node.parent.result = current_node.result
                current_node = current_node.parent

        end_time = time.time()
        elapsed_time = end_time - start_time

    # aqui se selecciona a un hijo random
    # select_node(tree_root.children[0], explored_nodes)

    current_node = tree_root
    print(f"SOY RAIZ {current_node.result}")
    if (current_node.result != [1, 0]):
        current_node = find_best_state(current_node)

    return current_node.state

# Return none is it has all children, so it does not expand

def ai_wins(current_node: Node):
    for child in current_node.parent.children:
        if (child.result == [0, 1]):
            return False

    return True

def find_best_state(current_node: Node):
    """

    """

    index = 0
    chosen = False
    result_node: Node = current_node
    while (not chosen and index < len(current_node.children)):
        current_child = current_node.children[index]
        if (current_child.result == [1, 0]):
            print("Sirve")
            result_node = current_child
            chosen = True
        else:
            if (current_child.leads_to_one):
                print("Llevo a 1.")
                result_node = current_child
                chosen = True
                """result_node = find_best_state(current_child)
                if (result_node.result == [1, 0]):
                    chosen = True"""

        index += 1

    return result_node

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

"""
root = Node(Quarto())
expand_node(root)
"""

def run():
    result = mcts(Quarto())
    print(result.result)

if __name__ == "__main__":
    run()