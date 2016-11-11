from GWV_Labyrinth import Labyrinth


def search(nodes, closed_list):
    frontier = []
    for node in nodes:
        if node.is_goal():
            return "success"
        open_neighbors = [x for x in node.get_neighbors() if x not in closed_list and x not in frontier]
        frontier += open_neighbors
    closed_list += nodes
    return search(frontier, closed_list)


def setup():
    maze = Labyrinth()
    start = maze.get_start()
    print(search([start], []))


if __name__ == '__main__':
    setup()
