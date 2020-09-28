from base import BaseAgent, TurnData, Action


class Agent(BaseAgent):

    def do_turn(self, turn_data: TurnData) -> Action:
        print(f"TURN {self.max_turns - turn_data.turns_left}/{self.max_turns}")
        for agent in turn_data.agent_data:
            print(f"AGENT {agent.name}")
            print(f"POSITION: {agent.position}")
            print(f"CARRYING: {agent.carrying}")
            print(f"COLLECTED: {agent.collected}")
        for row in turn_data.map:
            print(''.join(row))
        return Action.DOWN


if __name__ == '__main__':
    winner = Agent().play()
    print("WINNER: " + winner)
