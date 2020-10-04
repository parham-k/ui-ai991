package base;

import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.Socket;
import java.util.Arrays;

public abstract class BaseAgent {

    private final DataInputStream inputStream;
    private final DataOutputStream outputStream;
    public final String name;
    public final int agentCount, gridSize, maxTurns;
    public final double decisionTimeLimit;

    public BaseAgent() throws IOException {
        Socket connection = new Socket("127.0.0.1", 9921);
        inputStream = new DataInputStream(connection.getInputStream());
        outputStream = new DataOutputStream(connection.getOutputStream());
        name = inputStream.readUTF();
        agentCount = Integer.parseInt(inputStream.readUTF());
        gridSize = Integer.parseInt(inputStream.readUTF());
        maxTurns = Integer.parseInt(inputStream.readUTF());
        String decisionTimeLimitString = inputStream.readUTF();
        if (decisionTimeLimitString.equals("None"))
            decisionTimeLimit = Double.POSITIVE_INFINITY;
        else
            decisionTimeLimit = Double.parseDouble(decisionTimeLimitString);
    }

    private TurnData readTurnData(String firstLine) throws IOException {
        int turnsLeft = Integer.parseInt(firstLine);
        AgentData[] agentData = new AgentData[agentCount];
        for (int i = 0; i < agentCount; i++) {
            String[] info = inputStream.readUTF().split(" ");
            String name = info[0];
            String[] positionStrings = info[1].split(":");
            int positionRow = Integer.parseInt(positionStrings[0]);
            int positionColumn = Integer.parseInt(positionStrings[1]);
            Position position = new Position(positionRow, positionColumn);
            String carryingStatus = info[2];
            Integer carrying = null;
            if (!carryingStatus.equals("-"))
                carrying = Integer.parseInt(carryingStatus);
            int[] collected = new int[0];
            if (!info[3].equals("-")) {
                collected = new int[info[3].length()];
                for (int j = 0; j < collected.length; j++)
                    collected[j] = Integer.parseInt(info[3].split("")[j]);
            }
            agentData[i] = new AgentData(name, position, carrying, collected);
        }
        char[][] map = new char[gridSize][gridSize];
        for (int i = 0; i < gridSize; i++) {
            String row = inputStream.readUTF();
            for (int j = 0; j < gridSize; j++)
                map[i][j] = row.charAt(j);
        }
        return new TurnData(turnsLeft, agentData, map);
    }

    public String play() throws IOException {
        while (true) {
            String firstLine = inputStream.readUTF();
            if (firstLine.startsWith("WINNER"))
                return firstLine.split(" ")[1];
            TurnData turnData = readTurnData(firstLine);
            String actionName = doTurn(turnData).name();
            outputStream.writeUTF(actionName);
        }
    }

    public abstract Action doTurn(TurnData turnData);

}
