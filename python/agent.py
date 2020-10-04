import random
from base import BaseAgent, TurnData, Action


class Agent(BaseAgent):

    def __init__(self):
        BaseAgent.__init__(self)
        print(f"MY NAME: {self.name}")
        print(f"PLAYER COUNT: {self.agent_count}")
        print(f"GRID SIZE: {self.grid_size}")
        print(f"MAX TURNS: {self.max_turns}")
        print(f"DECISION TIME LIMIT: {self.decision_time_limit}")

    def do_turn(self, turn_data: TurnData) -> Action:
        print(f"TURN {self.max_turns - turn_data.turns_left}/{self.max_turns}")
        for agent in turn_data.agent_data:
            print(f"AGENT {agent.name}")
            print(f"POSITION: {agent.position}")
            print(f"CARRYING: {agent.carrying}")
            print(f"COLLECTED: {agent.collected}")
        for row in turn_data.map:
            print(''.join(row))
        action_name = input("> ").upper()
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
