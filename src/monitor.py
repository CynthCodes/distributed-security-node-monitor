class Monitor:
    def __init__(self):
        self.nodes = {}

    def receive_heartbeat(self, heartbeat):
        node_id = heartbeat["node_id"]
        self.nodes[node_id] = heartbeat

    def display_status(self):
        for node_id, heartbeat in self.nodes.items():
            print(
                f"{node_id} | "
                f"{heartbeat['status']} | "
                f"{heartbeat['timestamp']}"
            )