from GWV_Labyrinth import Labyrinth as L

import scipy.spatial.distance as sp
from Queue import PriorityQueue


def A_star_search(frontier, closed_list, goal_position, maze):
    #if frontier.empty():
    #    return None

    current = frontier.get()[1]

    if current.is_goal():

        return current

    else:
        if current.is_portal():

            portal = maze.get_other_portal(current.is_portal(), current.get_position())

            portal.set_parent(current)

            current = portal


        open_neighbors = [x for x in current.get_neighbors() if x not in closed_list]
        #TODO: do we have update the cost if we a node in a shorter way


        for node in open_neighbors:
            frontier_node = frontier.contains(node)

            node.set_parent(current)
            node.increment_cost()
            #node.set_estimated_cost(heuristic(node, goal_position))
            node.set_estimated_cost(portal_heuristic(node, goal_position, maze))

            if not frontier_node or frontier_node.priority_number() > node.priority_number():
                frontier.put((node.priority_number(), node))

        closed_list.append(current)


        return A_star_search(frontier, closed_list, goal_position, maze)

def setup_frontier():

    frontier = myQueue()

    closed_list = []

    maze = L()

    frontier.put((0, maze.get_start()))

    goal_position = maze.get_goal().get_position()

    get_path(A_star_search(frontier, closed_list, goal_position, maze))
    maze.print_search_state()


def heuristic(node, goal_position):

    return sp.cityblock(node.get_position(), goal_position)


def portal_heuristic(node, goal_position, maze):

    if node.is_portal():

        node = maze.get_other_portal(node.is_portal(), node.get_position())

    return sp.cityblock(node.get_position(), goal_position)


def get_path(start_node):
    if start_node:
        current = start_node.get_parent()
        path = ''
        counter = 9  # make path a bit more readable. Follow path through increasing numbers: 0,1,...9,0,1,...
        while not current.is_start():
            path += str(current.get_position())
            current.set_type_of_node('' + str(counter))
            current = current.get_parent()
            counter -= 1
            counter %= 10

    else:
        path = 'There is no solution!'
    print(path)


class myQueue(PriorityQueue):
    """Own naive implementation of a queue with added function checking for contents."""
    def _init(self, maxsize):
        self.queue = []
    def _put(self, item):
        self.queue.append(item)
    def _get(self):
        item = self.queue[0]
        self.queue = self.queue[1:]
        return item
    def contains(self, item):
        return item in self.queue


if __name__ == "__main__":

    setup_frontier()













