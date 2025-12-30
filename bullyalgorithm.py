class Node:
    def __init__(self, node_id, is_alive=True):
        self.node_id = node_id
        self.is_alive = is_alive

    def start_election(self, all_nodes):
        print(f"\nNode {self.node_id} notices coordinator failed. Starting election...")
        
        # Find all nodes with a higher ID
        higher_nodes = [n for n in all_nodes if n.node_id > self.node_id]
        
        ok_received = False
        for target in higher_nodes:
            if target.is_alive:
                print(f"Node {self.node_id} sends ELECTION to Node {target.node_id}. Received OK.")
                ok_received = True
                # The higher node would now call start_election() in a real system
                return target.start_election(all_nodes)
        
        if not ok_received:
            print(f"Node {self.node_id} is the new Coordinator!")
            return self.node_id

# Setup: 5 nodes, Node 4 (highest) is dead
nodes = [Node(0), Node(1), Node(2), Node(3), Node(4, is_alive=False)]

# Node 1 detects Node 4 is down
new_leader = nodes[1].start_election(nodes)
print(f"Election complete. Current Leader ID: {new_leader}")