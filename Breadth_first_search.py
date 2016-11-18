from GWV_Labyrinth import Labyrinth
from Queue import Queue

def search(frontier, closed_list, maze):
    """Dumb implementation of recursive bfs algorithm. Still works with portals tho."""
    new_frontier = []
    if not frontier:
        return "failure"
    else:
        for node in frontier:
            portal = node.is_portal()
            if node.is_goal():
                print node.get_parent()
                return node
            else:
                if portal:
                    other_portal = maze.get_other_portal(portal, node.get_position())
                    other_portal.set_parent(node)
                    node = other_portal
                    closed_list.append(node)
                open_neighbors = [x for x in node.get_neighbors() if x not in closed_list and x not in new_frontier]
                for n in open_neighbors:
                    n.set_parent(node)
                new_frontier += open_neighbors
        closed_list += frontier
        return search(new_frontier, closed_list, maze)


def smart_search(frontier, closed_list, maze):
    """Smarter implementation of the recursive breadth-first-search algorithm looking at only one node
    (2 in case of portal) per function call."""

    current = frontier.get()
    #closed_list.append(current) you have to be able to use portal again to go back

    if current.is_goal():
        return current

    else:
        if current.is_portal():  # Set other portal node as current node and continue search from there
            other_portal = maze.get_other_portal(current.is_portal(), current.get_position())
            other_portal.set_parent(current)
            current = other_portal

        closed_list.append(current)
        open_neighbors = [x for x in current.get_neighbors() if x not in closed_list and not frontier.contains(x)]
        for node in open_neighbors:
            node.set_parent(current)
            frontier.put(node)
        return smart_search(frontier, closed_list, maze)

def setup():
    maze = Labyrinth()
    start = maze.get_start()

    frontier = myQueue()
    frontier.put(start)
    #dumb version: get_path(search([start], [], maze))
    get_path(smart_search(frontier, [], maze))
    maze.print_search_state()


def get_path(start_node):
    current = start_node.get_parent()
    path = ''
    counter = 9  # make path a bit more readable. Follow path through increasing numbers: 0,1,...9,0,1,...
    while not current.is_start():
        path += str(current.get_position())
        current.set_type_of_node('' + str(counter))
        current = current.get_parent()
        counter -= 1
        counter %= 10
    print(path)


class myQueue(Queue):
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

if __name__ == '__main__':
    setup()
