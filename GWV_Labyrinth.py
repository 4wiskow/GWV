from copy import deepcopy
import sys


class Labyrinth:
    """
    Reads an ASCII-art representation of a search problem, converts it into a graph upon which
    to execute search algorithms.
    """

    def __init__(self):
        textlines = self.read_file()

        self.portals = []
        self.input_matrix = [[char for char in row] for row in textlines]

        self.representation = self.create_representation()
        self.connect_nodes(self.representation)
        #self.print_search_state()

    def read_file(self):
        """
        Read the textfile containing the problem described in ascii-art
        :return String containig the ASCII-characters without linebreaks
        """

        environments = ['blatt3_environment.txt', 'blatt3_environment_b.txt']
        choice = raw_input('Please choose the environment to use:\n'
                           '0: blatt3_environment.txt\n'
                           '1: blatt3_environment_b.txt\n')
        while choice not in ['0', '1']:
            choice = raw_input('To choose the environment, please put in the corresponding number:\n')

        labyrinth = open(environments[int(choice)], 'r')
        ascii = labyrinth.readlines()

        for i, n in enumerate(ascii):
            k = n[:-1]
            ascii[i] = k
        return ascii

    def create_representation(self):
        """
        Create a 2D-Array containing either a Node-Object where necessary
        or an 'x' where no node is to be created (e.g. a wall). This Array
        sticks to the layout given by the textfile, meaning that adjacent
        characters in the textfile are adjacent Nodes in this array.
        :return 2D-Array containing Node-Objects and obstacle indicators ('x')
        """

        node_matrix = deepcopy(self.input_matrix)

        for rownumber, row in enumerate(self.input_matrix):
            for colnumber, val in enumerate(row):
                if self.input_matrix[rownumber][colnumber] == '1':
                    new_node = Node(val)
                    node_matrix[rownumber][colnumber] = new_node
                    self.portals.append(('1', new_node))
                elif self.input_matrix[rownumber][colnumber] == '2':
                    new_node = Node(val)
                    node_matrix[rownumber][colnumber] = new_node
                    self.portals.append(('2', new_node))
                elif val != 'x':
                    node_matrix[rownumber][colnumber] = Node(val)
                else:
                    node_matrix[rownumber][colnumber] = 'x'

        return node_matrix

    def connect_nodes(self, matrix):
        """
        Connect nodes which have been created before. Two nodes are connected
        if they are adjacent to each other in the 2D-Array (vertically or horizontally).
        :param matrix: 2D-Array containing the nodes / obstacle indicators
        """
        for rownumber, row in enumerate(self.input_matrix):
            for colnumber, val in enumerate(row):
                if self.input_matrix[rownumber][colnumber] != 'x':
                    matrix[rownumber][colnumber].find_neighbors(matrix, (colnumber, rownumber))
                else:
                    matrix[rownumber][colnumber] = 'x'

    def print_search_state(self):
        """
        Put out a human-readable representation of a search state
        :return String of the search state in ascii-art
        """

        ascii_rep = ''
        for row in self.representation:
            for col in row:
                ascii_rep += col.__str__()  # DarfErDas?
            ascii_rep += '\n'
        print(ascii_rep)

    def get_start(self):
        """
        Looks for the start node in the graph.
        :return: the start node
        """
        for row in self.representation:
            for node in row:
                if node != 'x' and node.is_start():
                    return node

    def get_goal(self):
        """
        Looks for the start node in the graph.
        :return: the start node
        """
        for row in self.representation:
            for node in row:
                if node != 'x' and node.is_goal():
                    return node


    def get_other_portal(self, portal_type, position):
        for tuple in self.portals:
            if tuple[0] == portal_type and tuple[1].get_position() != position:
                return tuple[1]


class Node:
    """
    Nodes that can be connected to form a graph.
    """

    def __init__(self, type_of_node):
        self.typeOfNode = type_of_node
        self.neighbors = []
        self.parentNode = None
        self.position = (0, 0)
        self.cost = sys.maxint
        self.estimated_cost = sys.maxint


    def __str__(self):
        """
        More suitable String representation of a node.
        :return: ' ', 'g' or 's' depending on the type of the node
        """
        return str(self.typeOfNode)

    def find_neighbors(self, matrix, position):
        """
        Find adjacent nodes and save them for later use. This effectively forms the connections between nodes.
        :param matrix: The 2D-Array containing the nodes / obstacle indicators
        :param position: the position of the current node in the Array
        """
        # (x, y)
        self.position = position

        x = position[0]
        y = position[1]

        links = matrix[y][x - 1]
        rechts = matrix[y][x + 1]
        oben = matrix[y - 1][x]
        unten = matrix[y + 1][x]

        temp_neighbors = [links, rechts, oben, unten]

        self.neighbors = [i for i in temp_neighbors if i != 'x']

    def get_neighbors(self):
        """
        Getter for the Connections
        :return: List of neighbors
        """
        return self.neighbors

    def is_goal(self):
        """
        Is this node a goal?
        :return: True, if this node is a goal
        """
        return self.typeOfNode == 'g'

    def is_start(self):
        """
        Is this node the start?
        :return: True, if this node is the start
        """
        return self.typeOfNode == 's'

    def set_parent(self, node):
        self.parentNode = node

    def get_parent(self):
        return self.parentNode

    def get_position(self):
        return self.position

    def set_type_of_node(self, type):
        self.typeOfNode = type

    def is_portal(self):
        if self.typeOfNode == '1' or self.typeOfNode == '2':
            return self.typeOfNode

    def get_cost(self):

        return self.cost

    def set_cost(self, new_cost):

        self.cost = new_cost

    def set_estimated_cost(self, estimated_cost):

        self.cost = estimated_cost

    def get_estimated_cost(self):

        return self.cost

    def increment_cost(self):

        self.cost += 1

    def priority_number(self):

        return self.get_cost() + self.get_estimated_cost()


if __name__ == '__main__':
    maze = Labyrinth()
