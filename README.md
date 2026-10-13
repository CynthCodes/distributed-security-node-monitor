# Distributed Security Node Health Monitor

A Python-based cybersecurity portfolio project that simulates node health monitoring and detects availability disruptions across a distributed environment.

## Project Status

**Current Version:** V2 — Missed Heartbeat Detection — Implemented and Functionally Verified

V2 has been tested by simulating a node stopping its heartbeat transmissions and confirming that the monitor detects the resulting unavailability.

## Overview

This project explores how a central monitoring component can track distributed node availability through periodic heartbeat messages.

Using a fictional multi-branch organisation, MHN, the project simulates how a monitoring system can identify unavailable nodes and support security teams in maintaining visibility across distributed infrastructure.

The project is evolving from basic heartbeat monitoring towards security-relevant event detection, structured alerting and auditable monitoring records.

A missed heartbeat is treated as an availability signal, not automatic proof of an attack or node compromise.

## Objectives

The primary objectives are to:

1. Simulate multiple nodes in a distributed environment.
2. Implement periodic heartbeat communication.
3. Maintain visibility into node availability.
4. Detect missed heartbeats and node availability changes.
5. Distinguish availability events from confirmed security incidents.
6. Generate structured events for relevant monitoring conditions.
7. Explore explicit maintenance handling and recovery behaviour.
8. Build towards reliable event history and repeatable testing.

## Architecture

The application consists of simulated nodes that send heartbeat messages to a central monitoring component. The monitor evaluates heartbeat activity against a configured timeout to identify nodes that stop reporting.

See [`docs/architecture.md`](docs/architecture.md) for the architecture and component responsibilities.

## Technology

- Python
- Git
- GitHub

## Development Roadmap

| Version | Capability | Status |
|---|---|---|
| V1 | Heartbeat monitoring | Complete |
| V2 | Missed heartbeat detection | Implemented and functionally verified for the offline-node simulation |
| V3 | Security-relevant event detection and structured alerting | Planned |
| V4 | Explicit node state management and recovery handling | Planned |
| V5 | Planned downtime and maintenance handling | Planned |
| V6 | Persistent event history and audit logging | Planned |
| V7 | Input validation, repeatable tests and resilience improvements | Planned |

## Security Considerations

The project considers threats and limitations including heartbeat interruption, forged or stale messages, planned downtime, false recovery indications, excessive duplicate alerts and monitoring-service failure.

Heartbeat monitoring alone cannot establish whether a node is compromised. Additional validation and security controls would be needed for a production deployment.

See [`docs/threat-model.md`](docs/threat-model.md) for the documented threats, assumptions and scope.

## Documentation

- [`docs/architecture.md`](docs/architecture.md) — system architecture.
- [`docs/case-study.md`](docs/case-study.md) — fictional MHN scenario.
- [`docs/development-log.md`](docs/development-log.md) — implementation progress and verification records.
- [`docs/threat-model.md`](docs/threat-model.md) — threat model and security assumptions.

## Disclaimer

This project is a controlled simulation for cybersecurity learning and research. It does not connect to or control real medical, industrial or other critical infrastructure. It is not a production-ready monitoring or incident-response system.