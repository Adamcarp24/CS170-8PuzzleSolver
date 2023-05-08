import math

###
#This is my first time using python, so sorry if there is any bad practice in the code writing
#and any feedback would be much appreciated
###

class Node:
    def __init__(self, state, gval, hval):
        self.state = state
        self.gval = gval
        self.hval = hval

    def swap(self, i1, i2):
        temp = self.state[i2]
        self.state[i2] = self.state[i1]
        self.state[i1] = temp
    
    def updateH(self, newVal):
        self.hval = newVal

class Problem:
    def __init__(self):
        self.frontier = []
        self.expanded = []
        self.goalState = [1,2,3,4,5,6,7,8,0]

    def createChild(self, parent, direction, algoH):
        childState = parent.state.copy()
        child = Node(childState, parent.gval + 1, 0)
        i = child.state.index(0)

        #move blank space
        if(direction == "up"):
            child.swap(i, i-3)
        elif(direction == "down"):
            child.swap(i, i+3)
        elif(direction == "left"):
            child.swap(i, i-1)
        elif(direction == "right"):
            child.swap(i, i+1)

        #update hval depending on algorithm
        if(algoH == 1): child.updateH(self.tileH(child.state))
        elif(algoH == 2): child.updateH(self.euclidH(child.state))

        #check for repeated states with greater hvals (unsure if same state with lesser hval is possible? better safe than sorry)
        repeat = False
        for n in self.frontier:
            if((n.state == child.state) and (n.hval >= child.hval)): repeat = True
        for n in self.expanded:
            if((n.state == child.state) and (n.hval >= child.hval)): repeat = True
        
        #ignore child if repeated state
        if(not repeat): self.frontier.append(child)

    def createChildren(self, node, algoH):
        #find blank
        x = node.state.index(0)
        #cases for each position of blank
        #I could save room but readability
        if(x == 0):
            self.createChild(node, "down", algoH)
            self.createChild(node, "right", algoH)
        if(x == 1):
            self.createChild(node, "left", algoH)
            self.createChild(node, "down", algoH)
            self.createChild(node, "right", algoH)
        if(x == 2):
            self.createChild(node, "down", algoH)
            self.createChild(node, "left", algoH)
        if(x == 3):
            self.createChild(node, "up", algoH)
            self.createChild(node, "down", algoH)
            self.createChild(node, "right", algoH)
        if(x == 4):
            self.createChild(node, "up", algoH)
            self.createChild(node, "down", algoH)
            self.createChild(node, "left", algoH)
            self.createChild(node, "right", algoH)
        if(x == 5):
            self.createChild(node, "up", algoH)
            self.createChild(node, "down", algoH)
            self.createChild(node, "left", algoH)
        if(x == 6):
            self.createChild(node, "up", algoH)
            self.createChild(node, "right", algoH)
        if(x == 7):
            self.createChild(node, "up", algoH)
            self.createChild(node, "left", algoH)
            self.createChild(node, "right", algoH)
        if(x == 8):
            self.createChild(node, "up", algoH)
            self.createChild(node, "left", algoH)

    def tileH(self, state):
        #compare each tile to goal and add up misplaced tiles
        count = 0
        for i in range(0, len(state)):
            #not including blank tile
            if(state[i] != 0):
                if(state[i] != i+1): count += 1
        return count
    
    def euclidH(self, state):
        count = 0
        #create 2D list for x and y coords
        rows = [[state[0],state[1],state[2]],[state[3],state[4],state[5]],[state[6],state[7],state[8]]]

        for i in range(0, len(state)):
            if(state[i] != 0):
                if(state[i] != i+1):
                    x = 0
                    y = 0
                    for j in range(0,len(rows)):
                        for k in range (0, len(rows[j])):
                            if(rows[j][k] == i+1):
                                x = k
                                y = j
                    #find distance to correct position
                    if(i<3):
                        count += math.sqrt((x-i)**2 + (y-0)**2)
                    elif(i<6):
                        count += math.sqrt((x-(i-3))**2 + (y-1)**2)
                    else:
                        count += math.sqrt((x-(i-6))**2 + (y-2)**2)
        return count

class AlgoSelector:
    def __init__(self, method,initial):
        self.method = method
        self.initial = initial
        self.totalExpanded = 0
        self.maxQ = 1

    def run(self):
        if(self.method == 1):
            return self.UCS()
        if(self.method == 2):
            return self.AMT(1)
        if(self.method == 3):
            return self.AMT(2)

    #Uniform Cost Search
    def UCS(self):
        problem = Problem()
        start = Node(self.initial, 0, 0)
        problem.frontier.append(start)

        while(True):
            #no solution
            if(problem.frontier == []): return False

            if(len(problem.frontier) > self.maxQ):
                self.maxQ = len(problem.frontier)
            #expand first in frontier
            problem.expanded.append(problem.frontier.pop(0))
            self.totalExpanded += 1

            #expand state for terminal
            self.output(problem.expanded[len(problem.expanded)-1])

            #if expanded node is the goal then return said node
            if(problem.expanded[len(problem.expanded)-1].state == problem.goalState): return problem.expanded[len(problem.expanded)-1]
            #create all possible children nodes
            problem.createChildren(problem.expanded[len(problem.expanded)-1], 0)

            #sort frontier
            problem.frontier.sort(key=lambda x: x.gval)

    #A* with the Misplaced Tile heuristic or Euclidian Distance
    def AMT(self, code):
        problem = Problem()
        start = Node(self.initial, 0, 0)
        start.updateH(problem.tileH(self.initial))
        problem.frontier.append(start)

        while(True):
            #no solution
            if(problem.frontier == []): return False

            if(len(problem.frontier) > self.maxQ):
                self.maxQ = len(problem.frontier)
            #expand first in frontier
            problem.expanded.append(problem.frontier.pop(0))
            self.totalExpanded += 1

            #expand state for terminal
            self.output(problem.expanded[len(problem.expanded)-1])

            #if expanded node is the goal then return said node
            if(problem.expanded[len(problem.expanded)-1].state == problem.goalState): 
                bestGoal = problem.expanded[len(problem.expanded)-1]
                #check rest of frontier for a better goal node state
                print("Checking the rest of frontier for a better solution...")
                for n in problem.frontier:
                    if((n.state == problem.goalState) and (bestGoal.gval > n.gval)):
                        bestGoal = n   
                return bestGoal
            
            #create all possible children nodes, code 1 for tile heuristic, code 2 for euclidian
            problem.createChildren(problem.expanded[len(problem.expanded)-1], code)
            #sort frontier
            problem.frontier.sort(key=lambda x: x.gval+x.hval)

    #output function for expanding states with g & h values
    def output(self, node):
        print("\nThe best state to expand with g(n) = " + str(node.gval) + " and h(n) = " + str(node.hval) + " is...")
        for i in range(0, len(node.state)):
            print(str(node.state[i]) + " ", end="")
            if ((i+1)%3 == 0):
                print("")
        print("Expanding this node...\n")

#main
while(True):
    print("Welcome to acarp022 8 puzzle solver.\nType '1' to use a default puzzle, or '2' to enter your own puzzle.")
    type = int(input())
    if(type == 1 or type == 2):
        break

initialState = []
if(type == 2):
    lines = []
    print("Enter your puzzle, use a zero to represent the blank\nEnter the first row, use a space between numbers: ")
    line1 = input().split()
    print("Enter the second row, use space or tabs between numbers: ")
    line2 = input().split()
    print("Enter the third row, use space or tabs between numbers: ")
    line3 = input().split()

    lines.append(line1)
    lines.append(line2)
    lines.append(line3)
    for i in range (0,len(lines)):
        for j in range (0,len(lines[i])):
            initialState.append(int(lines[i][j]))

else:
    initialState = [1,0,3,4,2,6,7,5,8]

while(True):
    print("Enter your choice of algorithm:\nUniform Cost Search.\nA* with the Misplaced Tile heuristic.\nA* with the Euclidean distance heuristic.")
    method = int(input())
    if(method == 1 or method == 2 or method == 3):
        break

puzzle = AlgoSelector(method, initialState)
node = puzzle.run()

if(node):
    print("\nGoal!!!")
    print("\nTo solve this problem the search algorithm expanded a total of " + str(puzzle.totalExpanded) + " nodes.")
    print("The maximum number of nodes in the queue at any one time: " + str(puzzle.maxQ))
    print("The depth of the goal node was " + str(node.gval))

    """
    print("Would you like to show the goal path? y/n")
    ans = input()
    if(ans == "y"):
        #printing goal path...
    """

else:
    print("Failed to solve :(")