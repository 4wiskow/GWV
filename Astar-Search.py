from GWV_Labyrinth import Labyrinth as L

#import scipy.spatial.distance as sp
from Queue import PriorityQueue


def A_star_search(frontier, closed_list, goal_position, maze):

    if frontier.empty():  # No more nodes to look at means there is no solution
        return None

    current = frontier.get()[1]

    if current.is_goal():
        return current

    else:
        if current.is_portal():
            portal = maze.get_other_portal(current.is_portal(), current.get_position())

            portal.set_parent(current)

            portal.set_cost(current.get_cost()+1)

            current = portal

        open_neighbors = [x for x in current.get_neighbors() if x not in closed_list]
        #TODO: do we have update the cost if we a node in a shorter way

        for node in open_neighbors:
            new_cost = current.get_cost()

            if node.get_cost() > (new_cost + 1):  # update node if a shorter path than before has been found
                node.set_parent(current)
                node.set_cost(new_cost+1)
                # node.set_estimated_cost(heuristic(node, goal_position))
                node.set_estimated_cost(portal_heuristic(node, goal_position, maze))

                frontier.put((node.priority_number(), node))

        closed_list.append(current)

        return A_star_search(frontier, closed_list, goal_position, maze)


def setup_frontier():

    frontier = myQueue()
    closed_list = []
    maze = L()
    start = maze.get_start()
    start.set_cost(0)
    frontier.put((0, start))

    goals = maze.get_goal()
    goal_positions = []
    for n in goals:
        goal_positions.append(n.get_position())

    get_path(A_star_search(frontier, closed_list, goal_positions, maze))
    maze.print_search_state()


def heuristic(node, goal_position):

    #return sp.cityblock(node.get_position(), goal_position)
    return manhattan_distance_windows(node.get_position(), goal_position)


def portal_heuristic(node, goal_positions, maze):
    values = []
    for n in goal_positions:
        if node.is_portal():

            node = maze.get_other_portal(node.is_portal(), node.get_position())
        values.append(manhattan_distance_windows(node.get_position(), n))
        #return sp.cityblock(node.get_position(), goal_position)
    return min(values)


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


def manhattan_distance_windows(u, v):
    """
    Implementation of scipy.spatial.distance.cityblock function,
    because windows sucks ass.
    """
    return reduce((lambda x, y: x+y), map((lambda x, y: abs(x-y)), u, v))


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


if __name__ == "__main__":

    setup_frontier()













