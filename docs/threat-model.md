# Threat Model: Distributed Security Node Health Monitor

**Version:** 1.0  
**Environment:** Fictional MHN multi-branch network  
**Scope:** Heartbeat monitoring, node availability, state transitions and security-relevant event detection

## 1\. Problem Statement

MHN operates distributed systems across Calabar Headquarters, Oyo, Abuja, Lagos and Enugu. The organisation needs visibility into whether its monitored nodes continue reporting as expected.

The Distributed Security Node Health Monitor receives periodic heartbeats from simulated nodes and records their reported status. Its security purpose is to identify changes in expected node availability and provide evidence that supports operational investigation.

A missing heartbeat is not proof of an attack. It may result from network failure, process termination, resource exhaustion, planned maintenance or deliberate disruption. Likewise, a node reporting a healthy status is not necessarily uncompromised.

The monitor must therefore distinguish observable events from inferred causes.

## 2\. Assets and Trust Boundaries

|Asset|Security concern|
|-|-|
|Node identity and inventory|Messages may be attributed to the wrong node or originate from unauthorised sources.|
|Heartbeat observations|Messages may be delayed, duplicated, stale, forged or missing.|
|Health-state records|Incorrect state transitions may conceal outages or create false alarms.|
|Alert and event history|Missing or altered records may undermine investigation.|
|Monitoring service|Its failure may remove visibility across multiple nodes.|
|Monitoring configuration|Incorrect thresholds or maintenance settings may suppress or distort detection.|

The principal trust boundary is between a monitored node and the central monitor. The monitor must not assume that received data is trustworthy merely because it contains a familiar node identifier or a healthy status.

## 3\. Priority Threats

### T1: Heartbeat interruption

An attacker or infrastructure failure prevents a node's heartbeats from reaching the monitor.

**Risk:** The node becomes unavailable without timely recognition.

**Required behaviour:** Detect a missed-heartbeat condition after a configured timeout and record when the condition is recognised.

### T2: Forged or stale heartbeat

A client submits a heartbeat using an unauthorised identity, or an old heartbeat is accepted as evidence of current liveness.

**Risk:** The monitor may incorrectly classify an unavailable or compromised node as healthy.

**Required behaviour:** Validate node identity and message structure. Measure liveness using monitor-side receipt time. Treat cryptographic authentication and replay protection as future controls until implemented.

### T3: Planned downtime mistaken for an incident

An authorised node is offline for maintenance.

**Risk:** False alerts create noise and reduce operator trust. Conversely, incorrectly extended maintenance can conceal a genuine outage.

**Required behaviour:** Represent approved maintenance explicitly, bound it by time, record its reason and ensure that expiry restores normal monitoring.

### T4: False recovery

A node sends an isolated heartbeat after an outage but remains unstable or unable to provide its intended service.

**Risk:** The monitor reports recovery prematurely.

**Required behaviour:** Define recovery criteria explicitly and test intermittent connectivity. If recovery requires consecutive valid heartbeats, that requirement must be configurable and verified.

### T5: Alert flooding or duplicate events

Repeated heartbeat failures or invalid messages generate excessive alerts.

**Risk:** Important events are obscured, and monitoring or notification resources may be exhausted.

**Required behaviour:** Deduplicate notifications for a continuing incident while preserving meaningful state changes and recovery events.

### T6: Monitoring-service failure

The monitor crashes, stops processing messages or loses its in-memory state.

**Risk:** The organisation loses visibility without knowing that the monitoring component itself has failed.

**Required behaviour:** Make monitoring failures observable and test restart behaviour. Independent supervision is a future enhancement unless already implemented.

## 4\. Security Assumptions

1. Node identifiers are expected to be unique, but uniqueness alone does not authenticate a sender.
2. Heartbeat delivery may be delayed, lost, duplicated or interrupted.
3. Node-generated timestamps and self-reported status are not independently trustworthy.
4. A heartbeat demonstrates recent communication, not endpoint integrity or full service health.
5. Planned maintenance must be supplied through an explicit operational process; silence alone cannot establish that maintenance is authorised.
6. The monitor can fail independently of the nodes it monitors.
7. In-memory state and console output do not provide durable audit history.
8. The current environment is a simulation, not a production healthcare deployment.

These assumptions delimit the claims that can be made about the project.

## 5\. Scope and Limitations

The project covers simulated node heartbeats, availability assessment, health-state transitions, detection of missed heartbeats, recovery handling and security-relevant event records.

It does not currently claim to prevent denial-of-service attacks, prove endpoint integrity, detect all malware, isolate compromised hosts, inspect encrypted application traffic or guarantee production-grade availability.

Authentication, replay protection, durable audit logging, independent monitor supervision and production alert delivery must be treated as future controls until implemented and tested.

## 6\. Validation Criteria

The threat model will be validated through controlled scenarios:

* Registered nodes reporting normally.
* A node missing its heartbeat timeout.
* Delayed or dropped heartbeats.
* Recovery after an outage.
* Planned maintenance and maintenance expiry.
* Unknown node identifiers.
* Repeated failure events and alert deduplication.
* Monitoring-service interruption and restart.

For every scenario, record the initial condition, injected event, expected outcome, actual outcome and evidence. An unimplemented control is a known gap, not a passing test.

## 7\. Security Position

The monitor's primary contribution is improved visibility into distributed-node availability. Its security value depends on detecting meaningful changes, handling expected downtime correctly, preserving useful evidence and communicating the limitations of its observations.

**The central design principle is that a heartbeat is evidence of communication, not proof of security.**

