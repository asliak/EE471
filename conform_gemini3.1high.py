"""
Programming for the Puzzled -- Srini Devadas
You Will All Conform

Input is a list of 'F's and 'B's, in terms of forwards and backwards caps.
Output is a set of commands (printed out) to get either all 'F's or all 'B's.
Fewest commands are the goal.
"""

def please_conform(caps: list[str]) -> None:
    """
    Determines and prints the minimal number of commands needed
    to make all elements in the array conform to the same direction.
    """
    if not caps:
        return

    # The group that doesn't start the sequence will always appear fewer or equal
    # times compared to the starting group. Thus, flipping the elements that
    # do NOT match the first element guarantees the minimal number of flips.
    start_idx = 0
    flip_target = 'B' if caps[0] == 'F' else 'F'

    # We iterate one past the array's end to cleanly wrap up the final block.
    # The simulated final element matches caps[0], forcing the target block to close.
    for i in range(1, len(caps) + 1):
        current_cap = caps[i] if i < len(caps) else caps[0]

        if current_cap != caps[i - 1]:
            if current_cap == flip_target:
                start_idx = i
            else:
                end_idx = i - 1
                if start_idx == end_idx:
                    print(f"Person in position {start_idx} flip your cap!")
                else:
                    print(f"People in positions {start_idx} through {end_idx} flip your caps!")


if __name__ == "__main__":
    caps_list = ['F', 'F', 'B', 'B', 'B', 'F', 'B', 'B', 'B', 'F', 'F', 'B', 'F']
    caps_list_2 = ['F', 'F', 'B', 'B', 'B', 'F', 'B', 'B', 'B', 'F', 'F', 'F', 'F']
    
    print("Testing first caps list:")
    please_conform(caps_list)
    
    # print("\nTesting second caps list:")
    # please_conform(caps_list_2)
