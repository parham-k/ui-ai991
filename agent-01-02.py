import random
from base import BaseAgent, TurnData, Action
import json
###########################################################################################################

#targets has to be in a list
def find_targets(given_map, max_grid, targets):
    locations = []
    for item in targets:
        for x in range(max_grid):
            for y in range(max_grid):
                if given_map[x][y] == item:
                    #if i in given_map[k]:
                    locations.append([x, y])
    #returning positions which has been found in the map
    print(locations)
    if len(locations) == 0:
        return
    return locations

def find_closest_goal(current_pos, max_grid, goal_targets):
    #goal_targets is a list of a similar object. e.g [1, 2, 3, 4] which they are all Gems

    ####actual map avaz shode
    dummy_map = []
    with open("dummy_map.txt", "r") as reader:
        dummy_map = json.load(reader)
    reader.close()

    weight = 0
    dummy_map[current_pos[0]][current_pos[1]] = weight
    neighbors = get_neighbors_of_a_Coordinate(dummy_map, current_pos)
    while len(neighbors) != 0:
        weight += 1
        for coords in neighbors:
            #set weight for neighbors
            dummy_map[coords[0]][coords[1]] = weight
        neighbors = []
        #peyda kardan hamsaye haye noghati ke dar hale hazer weight barashon set shode
        targets = find_targets(dummy_map, max_grid, [weight])
        for i in targets:
            temp = get_neighbors_of_a_Coordinate(dummy_map, i)
            for coords in temp:
                neighbors.append(coords)

    with open("weight_map.txt", "w") as writer:
        json.dump(dummy_map, writer)
    writer.close()
    #weight_map is ready

    actual_map = []
    with open("actual_map.txt", "r") as reader:
        actual_map = json.load(reader)
    reader.close()

    coords_of_targets = find_targets(actual_map, max_grid, goal_targets)
    closest_coord = coords_of_targets[0]
    weight_map = []
    with open("weight_map.txt", "r") as reader:
        weight_map = json.load(reader)
    reader.close()
    closest_coord_weight = weight_map[coords_of_targets[0][0]][coords_of_targets[0][1]]

    for items in coords_of_targets:
        if weight_map[items[0]][items[1]] < closest_coord_weight:
            closest_coord = items
            closest_coord_weight = weight_map[items[0]][items[1]]
    return closest_coord


#setting weight of each slot to our default(200) which will change in uniform cast search.(except for Walls)
def mapmaker(sentMap, max_grid):
    for x in range(max_grid):
        for y in range(max_grid):
            if sentMap[x][y] != "*":
                sentMap[x][y] = 200
    return sentMap

def get_neighbors_of_a_Coordinate(dummy_map, coord):
    neighbors = []

    #Check top
    if coord[0] - 1 > -1:
        if dummy_map[coord[0] - 1][coord[1]] == 200:
            neighbors.append([coord[0] - 1, coord[1]])
    #Check right
    if coord[1] + 1 < len(dummy_map):
        if dummy_map[coord[0]][coord[1] + 1] == 200:
            neighbors.append([coord[0], coord[1] + 1])
    #Check bottom
    if coord[0] + 1 < len(dummy_map):
        if dummy_map[coord[0] + 1][coord[1]] == 200:
            neighbors.append([coord[0] + 1, coord[1]])
    #Check left
    if coord[1] - 1 > -1:
        if dummy_map[coord[0]][coord[1] - 1] == 200:
            neighbors.append([coord[0], coord[1] - 1])
    return neighbors



def uniformCastSearch(actual_map, dummy_map, current_pos, goal, max_grid):
    weight = 0
    dummy_map[goal[0]][goal[1]] = weight
    neighbors = get_neighbors_of_a_Coordinate(dummy_map, goal)
    #print(neighbors)
    while len(neighbors) != 0:
        weight += 1
        for coords in neighbors:
            #print(coords)
            #input("Press")
            dummy_map[coords[0]][coords[1]] = weight

        neighbors = []
        targets = find_targets(dummy_map, max_grid, [weight])
        for i in targets:
            temp = get_neighbors_of_a_Coordinate(dummy_map, i)
            for coords in temp:
                neighbors.append(coords)
    return dummy_map

def action_selector(path_map, current_pos):
    choices = []
    #Check top of the AI
    if current_pos[0] - 1 > -1 and path_map[current_pos[0] - 1][current_pos[1]] != '*':
        choices.append(path_map[current_pos[0] - 1][current_pos[1]])
    else:
        choices.append(200)
    #Check right of the AI
    if current_pos[1] + 1 < len(path_map) and path_map[current_pos[0]][current_pos[1] + 1] != '*':
        choices.append(path_map[current_pos[0]][current_pos[1] + 1])
    else:
        choices.append(200)
    #Check bottom of the AI
    if current_pos[0] + 1 < len(path_map) and path_map[current_pos[0] + 1][current_pos[1]] != '*':
        choices.append(path_map[current_pos[0] + 1][current_pos[1]])
    else:
        choices.append(200)
    #Check left of the AI
    if current_pos[1] - 1 > -1 and path_map[current_pos[0]][current_pos[1] - 1] != '*':
        choices.append(path_map[current_pos[0]][current_pos[1] - 1])
    else:
        choices.append(200)
    

    directions = {
        0 : "U",
        1 : "R",
        2 : "D",
        3 : "L"
    }
    
    return directions[choices.index(min(choices))]

###########################################################################################################

############


class Agent(BaseAgent):

    def __init__(self):
        BaseAgent.__init__(self)
        print(f"MY NAME: {self.name}")
        print(f"PLAYER COUNT: {self.agent_count}")
        print(f"GRID SIZE: {self.grid_size}")
        print(f"MAX TURNS: {self.max_turns}")
        print(f"DECISION TIME LIMIT: {self.decision_time_limit}")
        self.lookingForGem = True
        self.moveTowardsTheGem = False
        self.lookingForStation = False
        self.moveTowardsTheStation = False
        self.startOver = False
        self.checkForDestinationOfStation = False
        self.checkForDestinationOfGem = False

    def do_turn(self, turn_data: TurnData) -> Action:
        print(f"TURN {self.max_turns - turn_data.turns_left}/{self.max_turns}")
        for agent in turn_data.agent_data:
            print(f"AGENT {agent.name}")
            print(f"POSITION: {agent.position}")
            print(f"CARRYING: {agent.carrying}")
            print(f"COLLECTED: {agent.collected}")
        for row in turn_data.map:
            print(''.join(row))

        #for some reasons Python consider our two maps as one(e.g we have "actual_map" and "dummy_map" and if we make any changes to one of them it will apply on the other as well xD )
        with open("actual_map.txt", "w") as writer:
            json.dump(turn_data.map, writer)
        writer.close()
        max_grid = len(turn_data.map)
        current_pos = [agent.position[0], agent.position[1]]
        '''with open("current_pos.txt", "w") as writer:
            json.dump(current_pos, writer)
        writer.close()'''

    #####################################################################

        if self.startOver:
            #print("Start Over")
            self.lookingForGem = True
            self.moveTowardsTheGem = False
            self.lookingForStation = False
            self.moveTowardsTheStation = False
            self.checkForDestinationOfGem = False
            self.checkForDestinationOfStation = False
            self.startOver = False

    ######################################################################

        if self.lookingForGem:
            #print("looking for gem")
            dummy_map = mapmaker(turn_data.map, max_grid)
            with open("dummy_map.txt", "w") as writer:
                json.dump(dummy_map, writer)
            writer.close()

            goal_targets = ['0', '1', '2', '3', '4']
            closest_gem = find_closest_goal(current_pos, max_grid, goal_targets)
            with open("closest_gem.txt", "w") as writer:
                json.dump(closest_gem, writer)
            writer.close()
            actual_map = []
            with open("actual_map.txt", "r") as reader:
                actual_map = json.load(reader)
            reader.close()
            path_map = []
            path_map = uniformCastSearch(actual_map, dummy_map, current_pos, closest_gem, max_grid)
            with open("path_map.txt", "w") as writer:
                json.dump(path_map, writer)
            writer.close()
            #preventing to calculating same data over and over
            #if len(closest_gem) == 2
            self.moveTowardsTheGem = True
            self.lookingForGem = False
            self.checkForDestinationOfGem = True

    ###########################################################################

        if self.checkForDestinationOfGem:
            with open("closest_gem.txt", "r") as reader:
                closest_gem = json.load(reader)
            reader.close()
            #We arrived at gem position
            if closest_gem == current_pos:
                self.checkForDestinationOfGem = False
                self.moveTowardsTheGem = False
                self.lookingForStation = True

    ############################################################################

        if self.moveTowardsTheGem:
            #print("move toward the gem")
            #starting to move towards the Gem
            with open("path_map.txt", "r") as reader:
                path_map = json.load(reader)
            reader.close()
            action_name = action_selector(path_map, current_pos)

    #############################################################################

        closest_station = []
        if self.lookingForStation:
            #print("looking for station")
            #We got the gem. Now let's find the closest station
            with open("actual_map.txt", "r") as reader:
                turn_data.map = json.load(reader)
            reader.close()
            dummy_map = mapmaker(turn_data.map, max_grid)
            goal_targets = ['a']
            closest_station = find_closest_goal(current_pos, max_grid, goal_targets)
            with open("closest_station.txt", "w") as writer:
                json.dump(closest_station, writer)
            writer.close()
            actual_map = []
            with open("actual_map.txt", "r") as reader:
                actual_map = json.load(reader)
            reader.close()
            path_map = []
            path_map = uniformCastSearch(actual_map, dummy_map, current_pos, closest_station, max_grid)
            with open("path_map.txt", "w") as writer:
                json.dump(path_map, writer)
            writer.close()
            #if closest_station != []
            self.moveTowardsTheStation = True
            self.checkForDestinationOfStation = True
            self.lookingForStation = False

    #################################################################################

        if self.moveTowardsTheStation:
            #print("move towards the station")
            #starting to move towards the Gem
            with open("path_map.txt", "r") as reader:
                path_map = json.load(reader)
            reader.close()
            action_name = action_selector(path_map, current_pos)
            if action_name == "":
                return random.choice(list(Action))

    ##################################################################################

        if self.checkForDestinationOfStation:
            with open("closest_station.txt", "r") as reader:
                closest_station = json.load(reader)
            reader.close()
            #We arrived at gem position
            if closest_station == current_pos:
                self.moveTowardsTheStation = False
                self.startOver = True
                self.checkForDestinationOfStation = False

    ##################################################################################

        #action_name = input("> ").upper()
        if action_name == "U":
            return Action.UP
        if action_name == "D":
            return Action.DOWN
        if action_name == "L":
            return Action.LEFT
        if action_name == "R":
            return Action.RIGHT
        return random.choice(list(Action))


if __name__ == '__main__':
    winner = Agent().play()
    print("WINNER: " + winner)
