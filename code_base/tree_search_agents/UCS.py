
from tree_search_agents.TreeSearchAgent import *
from tree_search_agents.PriorityQueue import PriorityQueue
import time

from Environment import Position


class UCSAgent(TreeSearchAgent):
    def run(self, env: Environment) -> tuple[List[int], float, list]:
       
        fail = False
        success = False
        reachedGoal = None
        queue = PriorityQueue()
        start = env.starting_position
        queue.enqueue(start, 0)
        comeFrom = dict()
        val = dict()
        comeFrom[tuple(start)] = None
        val[tuple(start)] = 0

        expansionPath = []
        while not queue.is_empty():
            currentPos = queue.dequeue()
            expansionPath.append(currentPos)
            if env.get_node_type(currentPos) == 'G':
                success = True
                reachedGoal = currentPos
                break
            neighbours = []
            if currentPos[1] != env.limits[0]:
                left = [currentPos[0], currentPos[1]-1]
                neighbours.append(left)
            if currentPos[1] != env.limits[1]:
                right = [currentPos[0], currentPos[1]+1]
                neighbours.append(right)
            if currentPos[0] != env.limits[0]:
                up = [currentPos[0]-1, currentPos[1]]
                neighbours.append(up)
            if currentPos[0] != env.limits[1]:
                down = [currentPos[0]+1, currentPos[1]]
                neighbours.append(down)
            if len(neighbours) == 1 and env.get_node_type(neighbours[0]) == 'D':
                fail = True
                break
            for n in neighbours:
                new_val = val[tuple(currentPos)] + env.get_reward(currentPos, n)
                if tuple(n) not in val:
                    val[tuple(n)] = new_val
                    priority = new_val
                    queue.enqueue(n, priority)
                    comeFrom[tuple(n)] = currentPos
        
        path = []
        score = 0
        if not fail:
            positions = []
            positions.append(reachedGoal)
            next = comeFrom[tuple(reachedGoal)]
            positions.append(next)
            while next != start:
                next = comeFrom[tuple(next)]
                positions.append(next)
            positions.reverse()

            for i in range(len(positions)-1):
                pos1 = positions[i]
                pos2 = positions[i+1]
                if pos1[0] == pos2[0]:
                    if pos1[1] < pos2[1]:
                        path.append(3)
                    else:
                        path.append(1)
                else:
                    if pos1[0] < pos2[0]:
                        path.append(2)
                    else:
                        path.append(0)
            score = val[tuple(reachedGoal)]
        else:
            path = []
            score = 0
            expansionPath = []
            print("FAIL")

                
        return path, score, expansionPath

    @property
    def name(self) -> str:
        return "UCS"
