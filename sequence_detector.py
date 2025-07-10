import graphviz
from graphviz import Digraph 
import tempfile
import os
import random

def validate(s, label="string"): #used label for contextual error messages
    #Validate that the string contains only 0s and 1s
    if not s:
        raise ValueError(f"{label} cannot be empty.")
    for bit in s:
        if bit not in ['0', '1']:
            raise ValueError(f"{label} must contain only 0s and 1s.")
    return s

def compute_longest_prefix_suffix(sequence, current_prefix, bit):
    """
    Compute the longest prefix of sequence that is a suffix of current_prefix + bit.
    Returns the length of the longest matching prefix.
    """
    test_str = current_prefix + bit
    for j in range(min(len(test_str), len(sequence)), 0, -1):
        if sequence[:j] == test_str[-j:]:
            return j
    return 0

def generate_moore_fsm(sequence: str, overlapping=True):
    """
    Moore Machine : Output depends only on current state and not on input
    Returns:
      - fsm: dict of {state: {'0': next_state, '1': next_state}}
      - outputs: dict of {state: output}
    """
    sequence = validate(sequence, "Sequence")
    n = len(sequence)
    fsm = {}
    outputs = {}

    for i in range(n + 1):  # States S0 to Sn
        state = f"S{i}"
        fsm[state] = {}
        current_prefix = sequence[:i]  # History of bits leading to this state
        for bit in ['0', '1']:
            if i < n and bit == sequence[i]:
                next_state = f"S{i + 1}"
            else:
                fallback = compute_longest_prefix_suffix(sequence, current_prefix, bit)
                next_state = f"S{fallback}"
            fsm[state][bit] = next_state

        outputs[state] = '1' if i == n else '0' #Output is 1 only if complete sequence is detected

    # For non-overlapping: after detection, transition based on input bit
    if not overlapping:
        final_state = f"S{n}"
        for bit in ['0', '1']:
            # Check if the input bit starts a new prefix
            fallback = compute_longest_prefix_suffix(sequence, "", bit)
            fsm[final_state][bit] = f"S{fallback}"

    return fsm, outputs

def simulate_moore_fsm(fsm, outputs, input_stream):
    """
    Simulate Moore FSM on given input_stream.
    Returns: output string (1 for detected pattern)
    """
    input_stream = validate(input_stream, "Input stream")
    state = "S0"
    result = []

    for bit in input_stream:
        state = fsm[state][bit]
        result.append(outputs[state])

    return ''.join(result)

def generate_mealy_fsm(sequence: str, overlapping=True):
    """
    Generates FSM for given binary sequence (Mealy machine, overlapping/non-overlapping)
    Returns:
      - fsm: dict of {state: {'0': (next_state, output), '1': (next_state, output)}}
    """
    sequence = validate(sequence, "Sequence")
    n = len(sequence)
    fsm = {}

    for i in range(n + 1):  # States S0 to Sn
        state = f"S{i}"
        fsm[state] = {}
        current_prefix = sequence[:i]
        for bit in ['0', '1']:
            if i < n and bit == sequence[i]:
                next_state = f"S{i + 1}"
                output = '1' if (i + 1 == n) else '0'
            else:
                fallback = compute_longest_prefix_suffix(sequence, current_prefix, bit)
                next_state = f"S{fallback}"
                output = '0'
            fsm[state][bit] = (next_state, output)

    # For non-overlapping: after detection, transition to appropriate state
    if not overlapping:
        final_state = f"S{n}"
        for bit in ['0', '1']:
            fallback = compute_longest_prefix_suffix(sequence, "", bit)
            fsm[final_state][bit] = (f"S{fallback}", '0')

    return fsm

def simulate_mealy_fsm(fsm, input_stream):
    """
    Simulate Mealy FSM on given input_stream.
    Returns: output string (1 for detected pattern)
    """ 
    input_stream = validate(input_stream, "Input stream")
    state = "S0"
    result = []

    for bit in input_stream:
        next_state, output = fsm[state][bit]
        result.append(output)
        state = next_state

    return ''.join(result)

def visualize_fsm(fsm, outputs=None, fsm_type='moore', filename=None, sequence=None, save=False, overlapping=True):
    """
    General-purpose FSM visualizer for both Mealy and Moore machines.
    Displays FSM type in label, maximizes image size, and uses random light colors for nodes.
    Pops up preview, optionally saves with sequence in filename/label.
    """
    dot = Digraph(format='png')
    
    dot.attr(rankdir='LR', size='0,0', ratio='fill', margin='0', dpi='300')

    light_colors = ['#FFD1DC', '#D1FFD7', '#D1E9FF', '#FFF9D1', '#E6D1FF', '#FFE4E1', '#E1FFE4', '#FFDFD1', '#D1FFF4', '#F0D1FF', '#FFF0D1', '#D1DFFF', '#F9D1FF', '#FFEFD1', '#D1FFF8', '#FFD1F9', '#E1E1FF', '#FFE9D1', '#E1FFF5', '#F4FFD1']
    

    # Adding sequence and FSM type as a label at the top
    label = f"{fsm_type.capitalize()} {'Overlapping' if overlapping else 'Non-Overlapping'} Sequence Detector"
    if sequence:
        label += f" for sequence: {sequence}"
    dot.attr(label=label, labelloc='t', fontsize='20')

    # Create nodes with appropriate labels, shapes, and random light colors
    for state in fsm:
        node_color = random.choice(light_colors)  # Pick a random light color
        if fsm_type == 'moore':
            label = f"{state}/{outputs[state]}"
            shape = 'doublecircle' if outputs[state] == '1' else 'circle'
        else:  # Mealy
            label = state
            shape = 'circle'
        dot.node(state, label=label, shape=shape, style='filled', fillcolor=node_color)

    # Adding transitions based on FSM type
    for state in fsm:
        for input_bit in fsm[state]:
            if fsm_type == 'moore':
                next_state = fsm[state][input_bit]
                label = input_bit
            else:  # Mealy
                next_state, output = fsm[state][input_bit]
                label = f"{input_bit}/{output}"
            dot.edge(state, next_state, label=label)

    # Render to a temporary file for preview
    temp_filename = tempfile.mktemp(suffix='.png')
    temp_path = dot.render(temp_filename, view=True)

    # Save if requested
    if save:
        if not filename:
            filename = f"fsm_{fsm_type}_{sequence}_{'overlap' if overlapping else 'nonoverlap'}"
        output_path = dot.render(filename, view=True)
        print(f"FSM diagram saved as {filename}.png")
        return output_path
    else:
        print("Diagram not saved.")
        return None
    
if __name__ == "__main__":
    print("FSM Sequence Detector\n----------------------")
    try:
        fsm_type = input("Choose FSM type (moore/mealy): ").strip().lower()
        if fsm_type not in ['moore', 'mealy']:
            raise ValueError("Invalid FSM type. Choose 'moore' or 'mealy'.")

        sequence = input("Enter the binary sequence to detect (e.g., 1011): ")
        input_stream = input("Enter input bitstream (e.g., 1101011011): ")
        mode = input("Overlapping? (y/n): ").strip().lower()
        overlapping = (mode == 'y')
        save_diagram = input("Save FSM diagram? (y/n): ").strip().lower() == 'y'

        if fsm_type == 'moore':
            fsm, outputs = generate_moore_fsm(sequence, overlapping=overlapping)
            print(f"\nGenerated FSM (Moore, {'Overlapping' if overlapping else 'Non-overlapping'}):")
            for state in fsm:
                print(f"{state} (Output: {outputs[state]}): {fsm[state]}")
            result = simulate_moore_fsm(fsm, outputs, input_stream)
        else:  # mealy
            fsm = generate_mealy_fsm(sequence, overlapping=overlapping)
            print(f"\nGenerated FSM (Mealy, {'Overlapping' if overlapping else 'Non-overlapping'}):")
            for state in fsm:
                print(f"{state}: {{'0': {fsm[state]['0']}, '1': {fsm[state]['1']}}}")
            result = simulate_mealy_fsm(fsm, input_stream)
            outputs = None

        print(f"\nInput Stream: {input_stream}")
        print(f"Detection Output: {result}")

        # Visualization
        viz = input("Visualize FSM? (y/n): ").strip().lower()
        if viz == 'y':
            visualize_fsm(fsm, outputs, fsm_type=fsm_type, sequence=sequence, save=save_diagram)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")