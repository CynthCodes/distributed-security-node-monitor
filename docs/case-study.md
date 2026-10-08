# Case Study: When a Security Node Goes Silent

> **Fictional scenario created to demonstrate the security problem addressed by this project.**

## Background

Meridian Health Network (MHN) is a fictional healthcare organization operating several hospitals connected through a distributed healthcare network.

Each facility has a security-monitoring node responsible for communicating its health status to a central security monitoring system.

The organization relies on these nodes to maintain visibility across its distributed environment.

## The Incident

One Monday morning, the security team notices something unusual.

The monitoring node assigned to one of MHN's hospitals has stopped communicating with the central system.

The node was reporting normally a few minutes earlier.

Now, nothing.

At this point, the security team does not know what happened.

The machine could have lost network connectivity. The host could have crashed. The monitoring application could have stopped running. The system could be overloaded. The node could have been deliberately disconnected.

Or, potentially, an attacker could have disrupted the node.

The first problem is therefore not automatically identifying an attacker.

**The first problem is knowing that the node is no longer communicating.**

## The Problem

This is the problem the Distributed Security Node Health Monitor begins to address.

The project starts with a simple question:

**Which security nodes are currently alive and communicating with the central monitor?**

In Version 1, each simulated node periodically sends a heartbeat containing:

* A unique node identifier
* A timestamp
* Its current health status

The central monitor receives these heartbeats and maintains the latest known state of each node.

This establishes a basic visibility layer across the distributed environment.

## The Limitation of V1

V1 deliberately does not determine whether a node has failed.

It records the latest heartbeat received from each node.

If a node stops sending heartbeats, the current system does not yet know whether that represents a failure, a network problem, an application crash, or another condition.

That limitation creates the next problem:

**What should happen when a node that was previously communicating stops sending heartbeats?**

## Project Evolution

The project will address this problem incrementally.

### V1 — Heartbeat Monitoring

Establish visibility by receiving and recording periodic heartbeats from distributed security nodes.

### V2 — Failure Detection

Detect when a node has missed heartbeats for a defined period and identify it as potentially unavailable.

### V3 — Security Alerting

Convert relevant node failures into security events and generate appropriate alerts.

### V4 — Automated State Management

Introduce defined node states and controlled transitions based on observed conditions.

### V5 — Simulated Node Isolation

Simulate a controlled response in which a problematic node is removed from the active monitoring pool.

### V6 — Audit Logging

Record security-relevant events with timestamps and sufficient context to support investigation and accountability.

### V7 — Policy/GRC Layer

Introduce policy-driven decision-making so that automated responses can be evaluated against defined governance, risk, and compliance requirements.

## Project Objective

The objective is not to build a complete security operations platform in a single step.

Instead, the project demonstrates how a distributed security monitoring system can evolve from basic visibility into a controlled, auditable, and policy-aware response mechanism.

Each version introduces one additional capability while maintaining a clear connection to the original operational problem:

**A security node has gone silent. What does the system know, what should it do, and how can that decision be justified?**
