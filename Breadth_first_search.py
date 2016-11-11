from GWV_Labyrinth import Labyrinth


def search(frontier, closed_list):
    new_frontier = []
    if not frontier:
        return "failure"
    else:
        for node in frontier:
            if node.is_goal():
                print node.get_parent()
                return node
            else:
                open_neighbors = [x for x in node.get_neighbors() if x not in closed_list and x not in new_frontier]
                for n in open_neighbors:
                    n.set_parent(node)
                new_frontier += open_neighbors
        closed_list += frontier
        return search(new_frontier, closed_list)


def setup():
    maze = Labyrinth()
    start = maze.get_start()

    get_path(search([start], []))


def get_path(start_node):
    current = start_node
    path = ''
    while not current.is_start():
        path += str(current.get_position())
        current = current.get_parent()
    print(path)

if __name__ == '__main__':
    setup()
