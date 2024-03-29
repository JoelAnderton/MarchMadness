# MarchMadness
Creates a March Madness bracket based off the team's seed and a weighted coin flip.

My weighted coin flip works like this: It assigns one team to "heads" and other to "tails." Which ever team reaches their seed number first wins that bracket.

Example: 

Duke (seed 3) vs. Texas Tech (seed 5)

Duke = "Heads" (H)

Texas Tech = "Tails" (T)

Flips:
'H', 'T', 'T', 'T', 'H', 'T', 'T', 'T', 'H', 'H', 'H', 'T', 'H', 'T', 'H', 'T', 'T'

Winner is: Texas Tech

The winner is Texas Tech because in the first 7 flips there are 5 "T's" and only 2 "H's". Therefore, it is predicted that Texas Tech will upset Duke.

The program ensures the following attributes about the bracket:
- Must have at least one 5 seed vs. 12 seed upset
- Must have at least one 1 seed in the Final Four
- The sum of the seeds in the Final Four must be >= 12

### Example of output:

<img src="images/Output_example.PNG" width="200">

### March Madness 2023 Bracket Results
- Red X's are where the program guessed wrong.
- Red text are expected upsets.
- Highlighted teams are predicted winners of the First Four.

<img src="images/MarchMadness_2023.PNG" width="800">

# What I Learned
* How to do a weighted coin flip.
* Using "**" to unpack a dictionary.
* Loop through a list of dictionaries and pop() off the winners from the losers.
