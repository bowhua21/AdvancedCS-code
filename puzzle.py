"""
In this assignment you will implement and compare different search strategies
for solving the n-Puzzle, which is a generalization of the 8 and 15 puzzle to
squares of arbitrary size (we will only test it with 8-puzzles for now).
"""

import time


def state_to_string(state):
    row_strings = [" ".join([str(cell) for cell in row]) for row in state]
    return "\n".join(row_strings)


def swap_cells(state, i1, j1, i2, j2):
    """
    Returns a new state with the cells (i1,j1) and (i2,j2) swapped.
    """
    value1 = state[i1][j1]
    value2 = state[i2][j2]

    new_state = []
    for row in range(len(state)):
        new_row = []
        for column in range(len(state[row])):
            if row == i1 and column == j1:
                new_row.append(value2)
            elif row == i2 and column == j2:
                new_row.append(value1)
            else:
                new_row.append(state[row][column])
        new_state.append(tuple(new_row))
    return tuple(new_state)


def get_successors(state):
    """
    This function returns a list of possible successor states resulting
    from applicable actions.
    The result should be a list containing (Action, state) tuples.
    For example [("Up", ((1, 4, 2),(0, 5, 8),(3, 6, 7))),
                 ("Left",((4, 0, 2),(1, 5, 8),(3, 6, 7)))]
    """
    child_states = []

    for row in range(len(state)):
        for column in range(len(state[row])):
            if state[row][column] == 0:
                if column < len(state) - 1:  # Left
                    new_state = swap_cells(state, row, column, row, column + 1)
                    child_states.append(("Left", new_state))
                if column > 0:  # Right
                    new_state = swap_cells(state, row, column, row, column - 1)
                    child_states.append(("Right", new_state))
                if row < len(state) - 1:  # Up
                    new_state = swap_cells(state, row, column, row + 1, column)
                    child_states.append(("Up", new_state))
                if row > 0:  # Down
                    new_state = swap_cells(state, row, column, row - 1, column)
                    child_states.append(("Down", new_state))
                break
    return child_states


def goal_test(state):
    """
    Returns True if the state is a goal state, False otherwise.
    """
    counter = 0
    for row in state:
        for cell in row:
            if counter != cell:
                return False
            counter += 1
    return True


def bfs(state):
    """
    Breadth first search.
    Returns three values: A list of actions, the number of states expanded, and
    the maximum size of the frontier.
    """
    parents = {}  # We used to call this prev
    actions = {}  # Action that took you to each state.

    # Write code here for bfs.
    queue = []
    queue.append(state)

    while (queue):
        next_state = queue.pop(0)
        for action, succ_state in get_successors(next_state):
            pass

    return None  # Should return a list of actions.


def dfs(state):
    """
    Breadth first search.
    Returns three values: A list of actions, the number of states expanded, and
    the maximum size of the frontier.
    """
    parents = {}
    actions = {}

    # Write code here for dfs

    return None  # No solution found


def misplaced_heuristic(state):
    """
    Returns the number of misplaced tiles.
    """
    return 0  # replace this


def manhattan_heuristic(state):
    """
    For each misplaced tile, compute the manhattan distance between the current
    position and the goal position. THen sum all distances.
    """

    return 0  # replace this


def greedy_dfs(state, heuristic=misplaced_heuristic):
    """
    DFS, but using a heuristic to sort the neighboring states before adding
    them to the stack (the state closest to the goal should be on top of the
    stack.
    """
    return None


def best_first(state, heuristic=misplaced_heuristic):
    """
    Breadth first search using the heuristic function passed as a parameter.
    Returns three values: A list of actions, the number of states expanded, and
    the maximum size of the frontier.
    """

    # You might want to use these functions to maintain a priority queue
    # You may also use your own heap class here
    from heapq import heappush
    from heapq import heappop

    parents = {}
    actions = {}

    # Write best first search here.

    return None  # No solution found


def astar(state, heuristic=misplaced_heuristic):
    """
    A-star search using the heuristic function passed as a parameter.
    Returns three values: A list of actions, the number of states expanded, and
    the maximum size of the frontier.
    """
    # You might want to use these functions to maintain a priority queue
    # You may also use your own heap class here

    from heapq import heappush
    from heapq import heappop

    parents = {}
    actions = {}
    costs = {}

    costs[state] = 0

    # Write A* search here

    return None  # No solution found


def get_solution(state, parents, actions):
    """
    Helper function to retrieve the solution.
    """

    # Write solution traversal here

    return []


def print_result(solution):
    """
    Helper function to format test output.
    """
    if solution is None:
        print("No solution found.")
    else:
        print("Solution has {} actions.".format(len(solution)))


if __name__ == "__main__":

    # Easy test case
    test_state = ((1, 4, 2),
                  (0, 5, 8),
                  (3, 6, 7))

    # More difficult test case
    # test_state = ((7, 2, 4),
    #              (5, 0, 6),
    #              (8, 3, 1))

    print(state_to_string(test_state))
    print()

    print("====BFS====")
    solution = bfs(test_state)  #
    start = time.time()
    print_result(solution)
    end = time.time()
    if solution is not None:
        print(solution)
    print("Total time: {0:.3f}s".format(end - start))

    print()
    print("====DFS====")
    start = time.time()
    solution = dfs(test_state)
    end = time.time()
    print_result(solution)
    print("Teotal time: {0:.3f}s".format(end - start))

    print()
    print("====Greedy DFS (Misplaced Tiles Heuristic)====")
    start = time.time()
    solution = greedy_dfs(test_state, misplaced_heuristic)
    end = time.time()
    print_result(solution)
    print("Total time: {0:.3f}s".format(end - start))

    print()
    print("====Greedy Best-First (Misplaced Tiles Heuristic)====")
    start = time.time()
    solution = best_first(test_state, misplaced_heuristic)
    end = time.time()
    print_result(solution)
    print("Total time: {0:.3f}s".format(end - start))

    print()
    print("====A* (Misplaced Tiles Heuristic)====")
    start = time.time()
    solution = astar(test_state, misplaced_heuristic)
    end = time.time()
    print_result(solution)
    print("Total time: {0:.3f}s".format(end - start))

    # print()
    # print("====A* (Total Manhattan Distance Heuristic)====")
    # start = time.time()
    # solution, states_expanded, max_frontier = astar(test_state, manhattan_heuristic)
    # end = time.time()
    # print_result(solution, states_expanded, max_frontier)
    # print("Total time: {0:.3f}s".format(end-start))

