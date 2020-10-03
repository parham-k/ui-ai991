import base.Action;
import base.AgentData;
import base.BaseAgent;
import base.TurnData;

import java.io.IOException;
import java.util.Arrays;
import java.util.Scanner;

public class Agent extends BaseAgent {

    private final Scanner scanner = new Scanner(System.in);

    public Agent() throws IOException {
        super();
        System.out.println("MY NAME: " + name);
        System.out.println("PLAYER COUNT: " + agentCount);
        System.out.println("GRID SIZE: " + gridSize);
        System.out.println("MAX TURNS: " + maxTurns);
        System.out.println("DECISION TIME LIMIT: " + decisionTimeLimit);
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
        System.out.print("> ");
        String actionName = scanner.next().toUpperCase();
        if (actionName.equals("U"))
            return Action.UP;
        if (actionName.equals("D"))
            return Action.DOWN;
        if (actionName.equals("L"))
            return Action.LEFT;
        if (actionName.equals("R"))
            return Action.RIGHT;
        return Action.values()[(int) (Math.random() * Action.values().length)];
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
