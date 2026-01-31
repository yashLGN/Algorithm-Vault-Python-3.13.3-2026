
"""

Problem Statement:
Implement the Tower of Hanoi algorithm using recursion.

The Tower of Hanoi is a mathematical puzzle consisting of three rods and a
number of disks of different sizes. All disks start on the first rod in
decreasing order of size, with the smallest disk on top.

The objective is to move all disks from the first rod to the last rod while
following these rules:\\\
1. Only one disk may be moved at a time.
2. Only the top-most disk of any rod can be moved.
3. A larger disk cannot be placed on top of a smaller disk.

The function hanoi_solver(n) should:
- Take an integer n representing the total number of disks.
- Solve the puzzle in exactly (2^n - 1) moves.
- Return a string showing the state of all three rods after each move,
  including the initial arrangement.
- Display each rod as a list of integers, separated by spaces, with each
  state on a new line.

"""

def hanoi_solver(n):
    # Initialize rods
    source = list(range(n, 0, -1))
    auxiliary = []
    target = []

    moves = []

    # Record initial state
    moves.append(f"{source} {auxiliary} {target}")

    def move_disks(num, src, aux, tgt):
        if num == 1:
            disk = src.pop()
            tgt.append(disk)
            moves.append(f"{source} {auxiliary} {target}")
        else:
            move_disks(num - 1, src, tgt, aux)
            move_disks(1, src, aux, tgt)
            move_disks(num - 1, aux, src, tgt)

    move_disks(n, source, auxiliary, target)

    return "\n".join(moves)