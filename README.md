FSM Visualizer
A Python implementation of Moore and Mealy Finite State Machines (FSMs) for detecting binary sequences, with vibrant Graphviz visualizations featuring random light colors and maximized diagrams.
Project Overview
FSM Visualizer detects specific binary sequences (e.g., "1010") in input streams using Moore and Mealy FSMs. It supports overlapping and non-overlapping modes and generates clear, colorful state diagrams to visualize state transitions. Key features include:

Moore FSM: Outputs "1" when the full sequence is detected, based on state.
Mealy FSM: Outputs depend on state and input, optimizing efficiency.
Visualization: Dynamic diagrams with random pastel colors, maximized size, and labels indicating FSM type and mode (e.g., “Overlapping Moore FSM for sequence: 1010”).
Applications: Pattern matching in text processing, network packet analysis, digital circuit design, compiler lexical analysis, and error detection.

Real-World Applications

Text Processing: Detects patterns in binary or text data, similar to search tools or bioinformatics (e.g., finding DNA sequences).
Network Packet Analysis: Identifies bit patterns in network streams for protocol validation or security monitoring (e.g., detecting a "1010" header).
Digital Circuit Design: Simulates sequential circuits for signal pattern detection in hardware like FPGAs or microcontrollers.
Compiler Design: Tokenizes code by detecting patterns, useful for lexical analysis.
Error Detection: Finds specific markers in data streams for integrity checks in communication systems.

Features

Validates binary inputs for correctness using validate function.
Generates FSMs with efficient state transitions via longest prefix-suffix matching (compute_longest_prefix_suffix).
Simulates FSMs to produce output strings (e.g., "0000100" for "101010") using simulate_moore_fsm and simulate_mealy_fsm.
Visualizes FSMs with Graphviz, featuring random light colors, large-scale diagrams, and clear labels (visualize_fsm).
Supports both Moore and Mealy FSMs with user-defined sequences and overlapping/non-overlapping modes.

Installation

Clone the Repository:
git clone https://github.com/Shubhan9/FSM-Visualizer.git
cd FSM-Visualizer


Install Dependencies:Install Python 3.8+ and required libraries:
pip install graphviz

Install Graphviz software:

Windows: Download from Graphviz website and add to PATH.
Mac: brew install graphviz
Linux: sudo apt-get install graphviz


Run the Code:
python sequence_detector.py



Usage
Run the script and follow the prompts:
$ python sequence_detector.py
FSM Sequence Detector
----------------------
Choose FSM type (moore/mealy): moore
Enter the binary sequence to detect (e.g., 1011): 1010
Enter input bitstream (e.g., 1101011011): 101010
Overlapping? (y/n): y
Save FSM diagram? (y/n): y
Visualize FSM? (y/n): y


Outputs the FSM’s transition table, simulation results (e.g., "0000100"), and a colorful diagram (saved as fsm_moore_1010_overlap.png).

Example Output
For sequence="1010", input_stream="101010", overlapping=True:

FSM:S0 (Output: 0): {'0': 'S0', '1': 'S1'}
S1 (Output: 0): {'0': 'S2', '1': 'S1'}
S2 (Output: 0): {'0': 'S0', '1': 'S3'}
S3 (Output: 0): {'0': 'S4', '1': 'S1'}
S4 (Output: 1): {'0': 'S0', '1': 'S1'}


Output: "0000100" (detects "1010" at positions 1-4).
Diagram: A colorful state diagram with title “Overlapping Moore FSM for sequence: 1010”.

Screenshots

Future Improvements

Support non-binary sequences (e.g., letters for text processing).
Add a GUI for interactive input and visualization (e.g., using tkinter).
Include performance analysis for large input streams.
Implement unit tests for robustness (e.g., using unittest).

License
MIT License
