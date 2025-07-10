# FSM Visualizer

A Python-based tool to detect binary sequences (e.g., `1010`) using Moore and Mealy Finite State Machines (FSMs), with vibrant Graphviz visualizations using random pastel colors and maximized clarity.

---

## Overview

FSM Visualizer detects user-defined binary sequences in input streams, supporting overlapping and non-overlapping modes. It auto-generates FSMs, simulates them, produces output strings (e.g., `0000100`), and generates colorful, labeled state diagrams.

Ideal for applications like network packet analysis, digital circuit simulation, and compiler design, this tool helps users intuitively understand how FSMs operate.

---

## Features

- Input Validation: Only allows valid binary sequences (`0` and `1`).
- FSM Generation: Auto-creates Moore and Mealy FSMs using prefix-suffix logic.
- Simulation: Outputs `1` when the sequence is matched (e.g., detect `1010` in `101010`).
- Visualization: Generates large, colorful FSM diagrams labeled with the type and mode.
- Flexible Modes: Supports both FSM types (Moore/Mealy) and detection styles (Overlapping/Non-overlapping).

---

## Real-World Applications

- Network Packet Analysis: Detect headers, footers, and control sequences in binary streams.
- Digital Circuit Design: Simulate sequential logic for FPGA/microcontroller development.
- Text & Bioinformatics: Pattern detection in text, DNA/RNA sequences, etc.
- Compiler Design: Used in tokenization and lexical analysis.
- Error Detection: Identify start/end markers or errors in transmission.

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/Shubhan9/FSM-Visualizer.git
cd FSM-Visualizer
```

### Install Python Dependencies

Requires Python 3.8+

```bash
pip install graphviz
```

### Install Graphviz (Software)

**Windows:** Download from https://graphviz.org/download/ and add to PATH  
**Mac:**

```bash
brew install graphviz
```

**Linux:**

```bash
sudo apt-get install graphviz
```

---

## Usage

Run the program and follow the CLI prompts:

```bash
python sequence_detector.py
```

### Sample Session

```
FSM Sequence Detector
----------------------
Choose FSM type (moore/mealy): moore
Enter the binary sequence to detect (e.g., 1011): 1010
Enter input bitstream (e.g., 1101011011): 101010
Overlapping? (y/n): y
Save FSM diagram? (y/n): y
Visualize FSM? (y/n): y
```

---

## Example Output

**Input:**

- Sequence: `1010`
- Input Stream: `101010`
- Overlapping: `True`

**FSM (Moore):**

```
S0 (Output: 0): {'0': 'S0', '1': 'S1'}
S1 (Output: 0): {'0': 'S2', '1': 'S1'}
S2 (Output: 0): {'0': 'S0', '1': 'S3'}
S3 (Output: 0): {'0': 'S4', '1': 'S1'}
S4 (Output: 1): {'0': 'S0', '1': 'S1'}
```

**Result:**

```
Output: "0000100"  → Detected `1010` at positions 1–4
```

**Diagram:**

- Saved as `fsm_moore_1010_overlap.png`
- Labeled and pastel-colored for clarity

---

## Future Improvements

- Support non-binary input (e.g., text or DNA characters)
- Add GUI using `tkinter` or `PyQt`
- Performance benchmarks for large streams
- Add `unittest`/`pytest` testing modules

---

## License

This project is licensed under the MIT License.
