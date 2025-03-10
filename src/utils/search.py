"""
Search utilities.
"""

# %%
import sys


# %%
class Node:
    """
    Defines a node in a graph. Each node contains a given state, a parent node and an action that
    leads to a new state.
    """

    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action


class Stack:
    """
    Defines a stack data structure. A stack is a last-in first-out (LIFO) data structure
    where elements are added to the top and removed from the top.
    """

    def __init__(self):
        self.frontier = []  # A frontier is a list of nodes. Starts as an empty list, as the search has not started yet.

    def add(self, node):
        """
        Adds a node to the frontier.

        Parameters:
            node (Node): the node to be added to the frontier.

        Returns:
            None
        """
        self.frontier.append(node)

    def contains_state(self, state):
        """
        Checks if a state is already in the frontier.

        Parameters:
            state: The state to check for in the frontier.

        Returns:
            bool: True if the state exists in the frontier, False otherwise.

                return any(node.state == state for node in self.frontier)
        """

    def empty(self):
        """
        Checks if the frontier is empty.

        Returns:
            bool: True if the frontier is empty, False otherwise.

        """
        return len(self.frontier) == 0

    def remove(self):
        """
        Removes and returns the most recently added node from the frontier.

        Raises:
            Exception: If the frontier is empty.

        Returns:
            Node: The node that was removed from the frontier.
        """
        if self.empty():
            raise Exception("Empty frontier")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node


class Queue(Stack):
    """
    Defines a queue data structure. A queue is a first-in first-out (FIFO) data structure
    where elements are added to the back and removed from the front.
    """

    def remove(self):
        if self.empty():
            raise Exception("Empty frontier")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node