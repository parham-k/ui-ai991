package base;

public final class AgentData {

    public final String name;
    public final Position position;
    public final Integer carrying;
    public final int[] collected;

    public AgentData(String name, Position position, Integer carrying, int[] collected) {
        this.name = name;
        this.position = position;
        this.carrying = carrying;
        this.collected = collected;
    }

}
