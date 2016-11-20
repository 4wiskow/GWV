from GWV_Labyrinth import Labyrinth as L

#import scipy.spatial.distance as sp
from Queue import PriorityQueue


def a_star_search(frontier, closed_list, goal_position, maze):

    #TODO this guarantees termination
    if frontier.empty():  # No more nodes to look at means there is no solution.
        return None

    current = frontier.get()[1]

    if current.is_goal():
        return current

    else:
        #TODO portal functionality
        if current.is_portal():
            portal = maze.get_other_portal(current.is_portal(), current.get_position())

            portal.set_parent(current)

            portal.set_cost(current.get_cost()+1)

            current = portal

        open_neighbors = [x for x in current.get_neighbors() if x not in closed_list]

        for node in open_neighbors:
            new_cost = current.get_cost()

            #TODO this part allows us to find all optimal paths
            if node.get_cost() >= (new_cost + 1):  # update node if a shorter/equally long path has been found
                node.set_parent(current)
                node.set_cost(new_cost+1)
                # node.set_estimated_cost(heuristic(node, goal_position))
                node.set_estimated_cost(portal_heuristic(node, goal_position, maze))

                frontier.put((node.priority_number(), node))

        closed_list.append(current)

        return a_star_search(frontier, closed_list, goal_position, maze)


def setup_frontier():
    #  set up parameters for our search
    frontier = myQueue()
    closed_list = []
    maze = L()

    #  get start node to feed to a-star
    start = maze.get_start()
    start.set_cost(0)
    frontier.put((0, start))

    # get positions once instead of calling over and over again in heuristic
    goals = maze.get_goals()
    goal_positions = []
    for n in goals:
        goal_positions.append(n.get_position())

    end_of_path = a_star_search(frontier, closed_list, goal_positions, maze)

    # if there is a solution, print it, else print an error message!
    if end_of_path:
        paths = get_all_paths(end_of_path)
        print_path(paths[0], maze)  # just an example

    else:
        print('no solution found!')




def heuristic(node, goal_position):
    """
    The Manhattan Distance heuristic without regard to portals.
    :param node: Node to estimate distance to goal for.
    :param goal_position: Position of the goal in our maze
    :return: estimation of distance
    """

    return manhattan_distance_windows(node.get_position(), goal_position)

#TODO portal functionality, also multiple goals functionality
def portal_heuristic(node, goal_positions, maze):
    """
    Manhattan Distance heuristic working with portals. Returns the lowest calculated value to guarantee admissibility.
    :param node: Node to estimate distance to goal of.
    :param goal_positions: Positions of all goals in the maze
    :param maze: Instance of our maze
    :return: Estimation of shortest path to a goal
    """
    values = []
    for n in goal_positions:
        if node.is_portal():

            node = maze.get_other_portal(node.is_portal(), node.get_position())
        values.append(manhattan_distance_windows(node.get_position(), n))
    return min(values)


def print_path(path, maze):
    """
    Prints String of positions of nodes in the graph as well as graphic representation
    :param path: the path to print
    :param maze: our maze
    """

    string_rep = ''
    counter = 9  # make path a bit more readable. Follow path through increasing numbers: 0,1,...9,0,1,...
    for node in path:
        string_rep += str(node.get_position())
        node.set_type_of_node('' + str(counter))
        counter -= 1
        counter %= 10

    print(path)
    maze.print_search_state()


def get_all_paths(node):
    """
    Get all optimal paths to a goal. A path is represented by a list of node instances.
    :param node: the initial node (goal node)
    :return: the list of paths to the goal.
    """
    if node.is_start():
        return [[node]]
    else:
        following_list = []
        for i in node.get_parents():
            for k in get_all_paths(i):
                k.append(node)
                following_list.append(k)
        return following_list


def manhattan_distance_windows(u, v):
    """
    Implementation of scipy.spatial.distance.cityblock function,
    because windows sucks ass.
    """
    return reduce((lambda x, y: x+y), map((lambda x, y: abs(x-y)), u, v))


class myQueue(PriorityQueue):
    """Own naive implementation of a PriorityQueue which proved useful for debugging."""
    def _init(self, maxsize):
        self.queue = []

    def _put(self, item):
        self.queue.append(item)

    def _get(self):
        item = self.queue[0]
        self.queue = self.queue[1:]
        return item


if __name__ == "__main__":

    setup_frontier()













