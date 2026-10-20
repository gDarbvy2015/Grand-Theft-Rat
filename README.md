# Rat Theft Auto

Closed-loop brain-computer interface simulation for rodent control of a simplified open-world driving and interaction environment.

**Subject:** Freddy  
**Interface:** Multi-channel neural decoder with online adaptation and reward-based learning

## Overview

This repository implements a research-style simulation of a rodent BCI system in which a rat learns to perform goal-directed actions in a reduced open-world task through decoded neural activity. Actions are mapped to a minimal action space (locomotion and interaction). Successful completion of objectives triggers reward delivery, which is used both as behavioral reinforcement and as a training signal for the decoder.

The system includes:

- Multi-channel neural activity simulation
- Online adaptive decoder
- Reward shaping
- Mission progression
- Physiological state monitoring
- Session logging

## Architecture
Rat-Theft-Auto/
├── main.py                 # Session runner
├── config.py               # Experimental parameters
├── models/
│   ├── neural_decoder.py   # Adaptive decoder
│   ├── rat_agent.py        # Subject model
│   └── reward_system.py    # Reward calculation and shaping
├── game/
│   ├── world.py            # Environment state
│   └── mission.py          # Task progression
├── monitoring/
│   └── physiology.py       # Heart rate, stress, arousal
└── utils/
    └── logger.py           # Session logging


## Requirements

A full session runs for a fixed number of steps. Neural activity is generated, decoded into actions, executed in the environment, and used to update both the behavioral record and the decoder weights. Physiological state is updated continuously. At the end of the session a JSON log is written.

## Decoder
The decoder maps a vector of simulated neural channels to an action distribution. Weights are updated online using a reward-modulated rule. Noise is injected at the input to approximate biological variability. Confidence of the selected action is reported at each step.

## Reward Schedule

Steal / acquire vehicle 1.0
Complete short drive 2.0
Complete medium drive 3.5
Successful evasion 2.5
Idle -0.1


