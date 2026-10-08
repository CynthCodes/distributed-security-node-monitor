import time

from node import Node
from monitor import Monitor


nodes = [
    Node("NODE-001"),
    Node("NODE-002"),
    Node("NODE-003"),
    Node("NODE-004"),
    Node("NODE-005")
]

monitor = Monitor()

while True:
    for node in nodes:
        heartbeat = node.heartbeat()
        monitor.receive_heartbeat(heartbeat)

    monitor.display_status()

    print("-" * 60)

    time.sleep(5)