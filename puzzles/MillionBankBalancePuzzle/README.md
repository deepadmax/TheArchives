# Million Bank Balance Puzzle
This is my solution to [a puzzle from Matt Parker's Maths Puzzles](https://youtu.be/ILrqPpLpwpE).

Because the only restriction was that the two deposits had to be integers,
you could run the Fibonacci-like sequence backward and go into the negative numbers.

I thought I'd be clever and generate a sequence with 1,000,000 elements.
It turns out that this takes days, even on a high-end gaming desktop computer.


## Generate sequence
You can execute `millionset.py` to start generating
the 1,000,000 element sequence toward the **P£1,000,000**.<br>
If it's ever interrupted, it will read from the log file the next time
and pick up where it left off.

## Extract deposits
Run `extract_deposits.py` to read the last entry of the log,
calculate what the deposits would need to be, and store them in individual files,
`x.deposit` and `y.deposit`

## Check deposits
You can check whether the deposits given in the `.deposit` files
work to meet the target, by running `check_deposits.py`.
If the values are predicted to never reach the target, it will terminate.