import java.util.HashMap;

public class MapSum {

    private Node root;

    private class Node {
        private int value;
        private HashMap<Character, Node> next;

        public Node() {
            this(0);
        }

        public Node(int value) {
            this.value = value;
            this.next = new HashMap<>();
        }
    }

    /**
     * Initialize your data structure here.
     */
    public MapSum() {
        root = new Node();
    }

    public void insert(String key, int val) {
        Node curNode = root;
        for (int i = 0; i < key.length(); i++) {
            Character c = key.charAt(i);
            if (!curNode.next.containsKey(c)) {
                curNode.next.put(c, new Node());
            }
            curNode = curNode.next.get(c);
        }
        curNode.value = val;
    }

    // 设计一个递归函数去完成它
    public int sum(String prefix) {
        Node curNode = root;
        for (int i = 0; i < prefix.length(); i++) {
            Character c = prefix.charAt(i);
            if (curNode.next.containsKey(c)) {
                curNode = curNode.next.get(c);
            } else {
                return 0;
            }
        }
        return sum(curNode);
    }

    // 计算以 node 为根节点的所有 value 值的和
    private int sum(Node node) {
        int res = node.value;
        for (Character key : node.next.keySet()) {
            // 一直找到根节点
            res += sum(node.next.get(key));
        }
        return res;
    }
}
