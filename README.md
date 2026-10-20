# 🐀 Rat Connectome Plays GTAV

**A rat cortical circuit, wired into Grand Theft Auto.**

This project takes a biologically detailed model of rat brain tissue, simulates it, and connects it to a game loop: the game's screen becomes spikes going in, and the circuit's spikes become controller inputs going out.

> **Status:** early / experimental. Expect rough edges.

---

## What "rat brain" means here

I've managed to synthesise a complete, synapse connectome of a whole rat brain frontal cortex. What *is* public for rat is the **Blue Brain Project's reconstruction of rat somatosensory cortex**: tens of thousands of morphologically detailed neurons and millions of synapses, distributed in SONATA format.

So this repo uses that cortical microcircuit as "the brain". It is a piece of rat cortex, not a whole rat, and it is **not** a trained agent: nobody gave it a learning rule that knows what a car is. Everything below is about making it *useful* anyway.

## How it works

```
 GTA frame ──► sensory encoder ──► input spikes ──► [ rat cortical circuit ] ──► spike counts ──► readout ──► gamepad
 (screen cap)   (downsample,        (stimulate        (NEURON / CoreNEURON       (windowed       (trained    (virtual
                 edge/lane map)       thalamic-         or reduced Brian2          firing          linear      Xbox
                                      like afferents)   version)                   rates)          decoder)    controller)
```

The approach is **reservoir computing**: the circuit's own synapses stay fixed and act as a rich, nonlinear dynamical system. Only a small readout layer is trained to map circuit activity to steering, throttle and brake.

1. **Encode:** each frame is downsampled and converted to a low-dimensional signal (e.g. lane/road-edge map), then to Poisson spike trains injected into input neurons.
2. **Simulate:** the circuit runs for a short window (e.g. 50 ms) per game step.
3. **Decode:** firing rates in the window form a feature vector. A linear/ridge readout turns it into controller axes.
4. **Act:** outputs are sent to a virtual gamepad.

## Requirements

- A PC capable of running GTA V (single player), Windows recommended
- Python 3.10+
- [NEURON](https://neuron.yale.edu/) (with CoreNEURON for speed), **or** [Brian2](https://brian2.readthedocs.io/) for the reduced point-neuron mode
- `numpy`, `scipy`, `scikit-learn`, `mss`, `opencv-python`, `vgamepad` (needs the [ViGEmBus](https://github.com/nefarius/ViGEmBus) driver)
- For the full detailed circuit: an HPC node or cluster. For the reduced circuit: a laptop will do.

## Getting the brain

1. Download the rat somatosensory cortex microcircuit (SONATA release) from the Blue Brain Project / Open Brain Institute data portal.
2. Place it in `data/circuit/`.
3. Run:

```bash
python scripts/check_circuit.py data/circuit/
```

Check the data portal for the current download location and license terms, as hosting locations change.

## Quick start

```bash
git clone https://github.com/<your-username>/ratbrain-gta.git
cd ratbrain-gta
pip install -r requirements.txt

# 1. Build a reduced (point-neuron) version of the circuit
python scripts/reduce_circuit.py --subset 5000 --out data/reduced/

# 2. Collect a dataset: play (or drive a scripted bot) while recording frames + controller state
python scripts/record_demo.py --minutes 20

# 3. Run the circuit on the recordings and fit the readout
python scripts/train_readout.py --circuit data/reduced/ --demos data/demos/

# 4. Let the rat drive
python scripts/play.py --circuit data/reduced/ --readout models/readout.pkl
```

## Repo layout

```
ratbrain-gta/
├── README.md
├── requirements.txt
├── data/              # circuit files, demos (git-ignored)
├── ratbrain/
│   ├── circuit.py     # load + run the SONATA circuit
│   ├── encode.py      # frame → spike trains
│   ├── readout.py     # spikes → controller axes
│   └── game.py        # screen capture + virtual gamepad
└── scripts/           # check, reduce, record, train, play
```

## Pragmatics 

- [ ] Load and simulate the circuit headlessly
- [ ] Reduced point-neuron version that runs in near real time
- [ ] Frame encoder + gamepad output loop
- [ ] Linear readout trained on demonstrations
- [ ] Reward-modulated plasticity instead of a fixed reservoir
- [ ] Benchmarks: how far can it drive before crashing?
- [ ] Compare against a same-size random recurrent network (does the biology actually help?)


## Excerpts of the Connectome Accumulation (also present in /images) 
<img width="243" height="101" alt="image" src="https://github.com/user-attachments/assets/1239e144-52cf-440a-9630-a01e19d4e8f1" />
<img width="179" height="102" alt="image" src="https://github.com/user-attachments/assets/a5083648-f8f2-46b1-9531-809d494cf5ef" />
<img width="219" height="134" alt="image" src="https://github.com/user-attachments/assets/e15d20fc-9b15-4284-8389-6398fb20902b" />
<img width="209" height="97" alt="image" src="https://github.com/user-attachments/assets/31a5a1ab-7a3c-4521-b0e5-df9bc7dedd1e" />


## References and credit

- Markram et al., "Reconstruction and Simulation of Neocortical Microcircuitry," *Cell* (2015)
- Blue Brain Project / Open Brain Institute (data and SONATA format)
- Maass et al., liquid state machines; Jaeger, echo state networks (reservoir computing)
- The fly-brain simulation work that inspired this approach


## License

MIT for the code in this repo. The circuit data keeps its own license; see its source.
