from GWV_Labyrinth import Labyrinth


def search(stack, closed_list):
    if not stack:
        return "failure"
    else:
        current = stack.pop()
        if current.is_goal():

            return current

        if current.is_portal:

            #current = maze.get_other_portal(current.get_position())

         open_neighbors = [x for x in current.get_neighbors() if x not in closed_list and x not in stack]
        for n in open_neighbors:
            n.set_parent(current)
        stack += open_neighbors

        closed_list.append(current)
        return search(stack, closed_list)


def setup():
    maze = Labyrinth()
    start = maze.get_start()
    result = search([start], [])
    get_path(result)
    maze.print_search_state()


def get_path(goal_node):
    current = goal_node.get_parent()
    path = ''
    while not current.is_start():
        path += str(current.get_position())
        current.set_type_of_node('o')
        current = current.get_parent()
    return path

if __name__ == '__main__':
    setup()
