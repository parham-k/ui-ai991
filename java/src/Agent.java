import base.Action;
import base.AgentData;
import base.BaseAgent;
import base.TurnData;

import java.io.IOException;
import java.util.Arrays;

public class Agent extends BaseAgent {

    public Agent() throws IOException {
        super();
    }

    @Override
    public Action doTurn(TurnData turnData) {
        System.out.println("TURN " + (maxTurns - turnData.turnsLeft) + "/" + maxTurns);
        for (AgentData agent : turnData.agentData) {
            System.out.println("AGENT " + agent.name);
            System.out.println("POSITION: (" + agent.position.row + ", " + agent.position.column + ")");
            System.out.println("CARRYING: " + agent.carrying);
            System.out.println("COLLECTED: " + Arrays.toString(agent.collected));
        }
        for (int i = 0; i < gridSize; i++) {
            for (int j = 0; j < gridSize; j++)
                System.out.print(turnData.map[i][j]);
            System.out.println();
        }
        return Action.UP;
    }

    public static void main(String[] args) {
        try {
            String winner = new Agent().play();
            System.out.println("WINNER: " + winner);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

}
