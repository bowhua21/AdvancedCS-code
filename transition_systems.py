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
                if column < len(state)-1: # Left 
                    new_state = swap_cells(state, row,column, row, column+1)
                    child_states.append(("Left",new_state))
                if column > 0: # Right 
                    new_state = swap_cells(state, row,column, row, column-1)
                    child_states.append(("Right",new_state))
                if row < len(state)-1:   #Up 
                    new_state = swap_cells(state, row,column, row+1, column)
                    child_states.append(("Up",new_state))
                if row > 0: # Down
                    new_state = swap_cells(state, row,column, row-1, column)
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
    Returns 2 values: A list of actions, the number of states expanded.  
    """
    parents = {} # We used to call this prev 
    actions = {} # Action that took you to each state. 

    # Write code here for bfs.  
    queue = []
    queue.append(state)

    tabu = set()
    tabu.add(state)
    total_states_visited = 0 
    while queue: 
      next_state = queue.pop(0)
      total_states_visited += 1 
      for action, neighbor_state in get_successors(next_state):
          if neighbor_state not in tabu:
            actions[neighbor_state] = action
            parents[neighbor_state] = next_state
            if goal_test(neighbor_state):
                return (get_solution(neighbor_state, parents, actions), total_states_visited)
            tabu.add(neighbor_state)
            queue.append(neighbor_state)

    return (actions, total_states_visited)

                               
     
def dfs(state):
    """
    Depth first search.
    Returns three values: A list of actions, the number of states expanded, and
    the maximum size of the frontier.  
    """
    parents = {} # We used to call this prev 
    actions = {} # Action that took you to each state. 

    # Write code here for dfs.  
    stack = []
    stack.append(state)

    tabu = set()
    tabu.add(state)
    total_states_visited = 0 
    while stack: 
      next_state = stack.pop()
      total_states_visited += 1 
      for action, neighbor_state in get_successors(next_state):
          if neighbor_state not in tabu:
            actions[neighbor_state] = action
            parents[neighbor_state] = next_state
            if goal_test(neighbor_state):
                return (get_solution(neighbor_state, parents, actions), total_states_visited)
            tabu.add(neighbor_state)
            stack.append(neighbor_state)

    return (actions, total_states_visited)
    
                


def misplaced_heuristic(state):
    """
    Returns the number of misplaced tiles.
    """
    counter = 0
    misplaced = 0
    for row in state:
        for cell in row: 
            if counter != cell and cell != 0: 
                misplaced += 1
            counter += 1
    return misplaced


def manhattan_heuristic(state):
    """
    For each misplaced tile, compute the manhattan distance between the current
    position and the goal position. THen sum all distances. 
    """
    total = 0
    for rowindex in range(len(state)):
        for colindex in range(len(state)): 
            cell = state[rowindex][colindex]
            targetrow = cell // 3
            targetcol = cell % 3
            rowdiff = abs(targetrow - rowindex)
            coldiff = abs(targetcol - colindex)
            total = total + rowdiff + coldiff
    return total


def greedy_dfs(state, heuristic = misplaced_heuristic): 
    """
    DFS, but using a heuristic to sort the neighboring states before adding 
    them to the stack (the state closest to the goal should be on top of the 
    stack.
    """
    parents = {} # We used to call this prev 
    actions = {} # Action that took you to each state. 

    # Write code here for dfs.  
    stack = []
    stack.append(state)

    tabu = set()
    tabu.add(state)
    total_states_visited = 0 
    while stack: 
      next_state = stack.pop()
      total_states_visited += 1 
      for action, neighbor_state in get_successors(next_state):
          if neighbor_state not in tabu:
            actions[neighbor_state] = action
            parents[neighbor_state] = next_state
            if goal_test(neighbor_state):
                return (get_solution(neighbor_state, parents, actions), total_states_visited)
            tabu.add(neighbor_state)
            if len(stack) == 0:
                stack.append(neighbor_state)
            else:
                counter = len(stack) - 1
                while(heuristic(neighbor_state) > heuristic(stack[counter])):
                    counter = counter - 1
                stack.insert(counter+1, neighbor_state)
            

    return (actions, total_states_visited)
    



def best_first(state, heuristic = misplaced_heuristic):
    """
    Breadth first search using the heuristic function passed as a parameter.
    Returns 2 values: A list of actions, the number of states expanded.  
    """

    # You might want to use these functions to maintain a priority queue
    # You may also use your own heap class here
    from heapq import heappush
    from heapq import heappop

    parents = {} # We used to call this prev 
    actions = {} # Action that took you to each state. 


    # Write code here for bfs.  
    queue = []
    queue.append(state)

    tabu = set()
    tabu.add(state)

    heap = []
    heap.heappush((heuristic(state), state))
    total_states_visited = 0
    while heap: 
      next_state = heappop(0)
      total_states_visited += 1 
      for action, neighbor_state in get_successors(next_state):
          if neighbor_state not in tabu:
            actions[neighbor_state] = action
            parents[neighbor_state] = next_state
            if goal_test(neighbor_state):
                return (get_solution(neighbor_state, parents, actions), total_states_visited)
            tabu.add(neighbor_state)
            state_with_cost = (heuristic(neighbor_state), neighbor_state)
            heap.heappush(state_with_cost)

    return (actions, total_states_visited)



def astar(state, heuristic = misplaced_heuristic):
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

    return None # No solution found

def get_solution(state, parents, actions):
    """
    Helper function to retrieve the solution.
    """

    solution = []
    while (state in parents):
        act = actions[state]
        solution.append(act)
        state = parents[state]
    return solution[::-1]

    


def print_result(solution):
    """
    Helper function to format test output. 
    """
    if solution is None: 
        print("No solution found.")
    else: 
        print("Solution has {} actions.".format(len(solution)))



if __name__ == "__main__":

    #Easy test case
    test_state = ((1, 4, 2),
                  (0, 5, 8), 
                  (3, 6, 7))  

    #More difficult test case
    #test_state = ((7, 2, 4),
    #              (5, 0, 6), 
    #              (8, 3, 1))  

    print(state_to_string(test_state))
    print()

    print("====BFS====")
    solution, nstates = bfs(test_state) #
    start = time.time()
    print_result(solution)
    end = time.time()
    if solution is not None:
        print(solution)
    print("Total states visited: ", nstates)
    print("Total time: {0:.3f}s".format(end-start))

    print() 
    print("====DFS====") 
    start = time.time()
    solution, nstates = dfs(test_state)
    end = time.time()
    print_result(solution)
    print("Total states visited: ", nstates)
    print("Total time: {0:.3f}s".format(end-start))

    
    print() 
    print("====Greedy DFS (Misplaced Tiles Heuristic)====") 
    start = time.time()
    solution = greedy_dfs(test_state, misplaced_heuristic)
    end = time.time()
    print_result(solution)
    print("Total time: {0:.3f}s".format(end-start))



    print() 
    print("====Greedy Best-First (Misplaced Tiles Heuristic)====") 
    start = time.time()
    solution = best_first(test_state, misplaced_heuristic)
    end = time.time()
    print_result(solution)
    print("Total time: {0:.3f}s".format(end-start))


    
    print() 
    print("====A* (Misplaced Tiles Heuristic)====") 
    start = time.time()
    solution = astar(test_state, misplaced_heuristic)
    end = time.time()
    print_result(solution)
    print("Total time: {0:.3f}s".format(end-start))

    #print() 
    #print("====A* (Total Manhattan Distance Heuristic)====") 
    #start = time.time()
    #solution, states_expanded, max_frontier = astar(test_state, manhattan_heuristic)
    #end = time.time()
    #print_result(solution, states_expanded, max_frontier)
    #print("Total time: {0:.3f}s".format(end-start))

