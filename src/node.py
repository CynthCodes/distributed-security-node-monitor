from datetime import datetime


class Node:
    def __init__(self, node_id):
        self.node_id = node_id

    def heartbeat(self):
        return {
            "node_id": self.node_id,
            "timestamp": datetime.now(),
            "status": "healthy"
        }