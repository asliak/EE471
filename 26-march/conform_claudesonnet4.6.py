"""
Programming for the Puzzled -- Srini Devadas
You Will All Conform

Input is a list of 'F's and 'B's, in terms of forwards and backwards caps.
Output is a set of commands (printed out) to get either all 'F's or all 'B's.
Fewest commands are the goal.
"""


def please_conform(caps: list[str]) -> None:
    """
    Print the minimal commands needed to make all caps face the same direction.

    The direction that starts the sequence (caps[0]) always appears at least as
    many times as the other direction, so flipping all blocks that differ from
    caps[0] is always optimal.
    """
    if not caps:
        return

    # Flip every block that differs from the opening direction.
    flip_target = 'B' if caps[0] == 'F' else 'F'
    block_start = 0

    # Iterate one past the end; the sentinel value matches caps[0], which
    # forces the final differing block to close without duplicating logic.
    for i in range(1, len(caps) + 1):
        current = caps[i] if i < len(caps) else caps[0]

        if current != caps[i - 1]:
            if current == flip_target:
                # Entering a block that needs flipping — record its start.
                block_start = i
            else:
                # Leaving a block that needs flipping — emit the command.
                block_end = i - 1
                if block_start == block_end:
                    print(f"Person in position {block_start} flip your cap!")
                else:
                    print(
                        f"People in positions {block_start} through "
                        f"{block_end} flip your caps!"
                    )


if __name__ == "__main__":
    caps_list = ['F', 'F', 'B', 'B', 'B', 'F', 'B', 'B', 'B', 'F', 'F', 'B', 'F']
    caps_list_2 = ['F', 'F', 'B', 'B', 'B', 'F', 'B', 'B', 'B', 'F', 'F', 'F', 'F']

    print("Testing first caps list:")
    please_conform(caps_list)

    print("\nTesting second caps list:")
    please_conform(caps_list_2)
