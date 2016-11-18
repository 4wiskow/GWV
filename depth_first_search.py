from GWV_Labyrinth import Labyrinth


def search(stack, closed_list, maze):
    if not stack:
        return "failure"
    else:
        current = stack.pop()
        portal = current.is_portal()

        if current.is_goal():

            return current

        if portal:
            other_portal = maze.get_other_portal(portal, current.get_position())
            other_portal.set_parent(current)
            current = other_portal

        closed_list.append(current)
        open_neighbors = [x for x in current.get_neighbors() if x not in closed_list and x not in stack]
        for n in open_neighbors:
            n.set_parent(current)
        stack += open_neighbors

        closed_list.append(current)
        return search(stack, closed_list, maze)


def setup():
    maze = Labyrinth()
    start = maze.get_start()
    result = search([start], [], maze)
    get_path(result)
    maze.print_search_state()


def get_path(goal_node):
    current = goal_node.get_parent()
    path = ''
    counter = 1
    while not current.is_start():
        path += str(current.get_position())
        current.set_type_of_node('' + str(counter))
        current = current.get_parent()
        counter += 1
        counter %= 10
    return path

if __name__ == '__main__':
    setup()
