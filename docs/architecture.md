# System Architecture

## Purpose

The Distributed Security Node Health Monitor simulates a centralized monitoring component responsible for receiving heartbeat information from multiple distributed nodes and maintaining their current health state.

## Initial Architecture

```text
Node A ─────┐
Node B ─────┤
Node C ─────┤──→ Central Health Monitor
Node D ─────┤
Node E ─────┘
                    │
                    ↓
              Node Inventory

