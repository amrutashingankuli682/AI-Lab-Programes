import math
# Represents the game tree nodes
class Node:
    def __init__(self, value=None):
        self.value = value
        self.children = []
# Minimax algorithm with alpha-beta pruning
def minimax_alpha_beta(node, depth, alpha, beta, maximizingPlayer):
    if depth == 0 or len(node.children) == 0:
        return node.value
    if maximizingPlayer:
        value = -math.inf
        for child in node.children:
            value = max(value, minimax_alpha_beta(child, depth - 1, alpha, beta, False))
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return value
    else:
        value = math.inf
        for child in node.children:
            value = min(value, minimax_alpha_beta(child, depth - 1, alpha, beta, True))
            beta = min(beta, value)
            if beta <= alpha:
                break
        return value
# Example usage
if __name__ == "__main__":
    # Construct a simple game tree
    root = Node()
    root.value = 3
    node1 = Node()
    node1.value = 5
    root.children.append(node1)
    node2 = Node()
    node2.value = 6
    root.children.append(node2)
    node3 = Node()
    node3.value = 9
    node1.children.append(node3)
    node4 = Node()
    node4.value = 1
    node1.children.append(node4)
    node5 = Node()
    node5.value = 2
    node2.children.append(node5)
    node6 = Node()
    node6.value = 0
    node2.children.append(node6)
    # Perform minimax with alpha-beta pruning
    result = minimax_alpha_beta(root, 3, -math.inf, math.inf, True)
    print("Optimal value:", result)
