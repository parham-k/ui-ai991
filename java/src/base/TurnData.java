package base;

public class TurnData {

    public final int turnsLeft;
    public final AgentData[] agentData;
    public final char[][] map;

    public TurnData(int turnsLeft, AgentData[] agentData, char[][] map) {
        this.turnsLeft = turnsLeft;
        this.agentData = agentData;
        this.map = map;
    }

}
