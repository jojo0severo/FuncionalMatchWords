import java.util.ArrayList;

public class Node {
    private String value;
    private ArrayList<Node> filhos;

    public Node(String value){
        this.value = value;
        this.filhos = new ArrayList<>();
    }

    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
}
