# Artificial Intelligence Course

_Group Members:_

1. Yağmur Mutluer
2. Elif Nur Şağban


## Project I


### Breadth First Search

- Traverse through one level of children nodes, then traverse through the level of grandchildren nodes (and so on..)


![image](https://camo.githubusercontent.com/81237833eeedea03b1f124ef97a2834f07e81e53/687474703a2f2f7777772e6373652e756e73772e6564752e61752f7e62696c6c772f4a757374736561726368312e676966)

### Depth First Search

- Traverse through left subtree(s) first, then traverse through the right subtree(s)


### Uniform Cost Search

- Searches in branches which are more or less the same in cost.


### About Project I

- The code should accept the given graph from the terminal and the three algorithms should search and find the shortest path.


#### Resources

https://repl.it/@pn49571/shortest-distance-Breadth-first-search

https://medium.com/@akshdeep.sharma1/dfs-bfs-coding-blog-week-10-619175d9469

https://rextester.com/GDQAJ78015



## Project II Solving CSPs


### Kakuro Puzzle

- Figure below illustrates a simple Kakuros puzzle, solution of the puzzle, input file and the output file.
- Kakuro puzzles are similar with crosswords, but instead of letters the board is filled with digits (from 1 to 9).
- The board's squares need to be filled in with these digits in order to sum up to the specified numbers.
- To solve Kakuros Puzzle using the same digit more than once to obtain a given sum is not allowed.

![image](https://cdn1.imggmi.com/uploads/2019/10/22/ac4426485e2869da67ce0d2d43de4df7-full.png)

### Futoshiki Puzzle
- Futoshiki is a board-based puzzle game, also known under the name Unequal.It is playable on a square board having a given fixed size (4x4 for example).
- The purpose of the game is to discover the digits hidden inside the board's cells; each cell is filled with a digit between 1 and the board's size. On each row and column each digit appears exactly once; therefore, when revealed, the digits of the board form a so-called Latin square.
- At the beginning of the game some digits might be revealed. The board might also contain some inequalities between the board cells; these inequalities must be respected and can be used as clues in order to discover the remaining hidden digits.
- Each puzzle is guaranteed to have a solution and only one. In order to indicate a move, click the desired square and select a digit or the delete sign (X); you can also use the digits on your keyboard (in this case, the digit 0 is equivalent to the delete sign).


![image](https://cdn1.imggmi.com/uploads/2019/10/22/99844e0a08ab50de0579df6f3922fc62-full.png)


### About Project II

- Both code files should accept the given input files as "kakuro_input" and "futoshiki_input.txt".
- After running both codes should write outputs into the files as "kakuro_output" and "futoshiki_output.txt"

#### Resources 
https://developers.google.com/optimization/cp/original_cp_solver
https://www.kakuros.com/
https://www.futoshiki.org/

## About Project III

- This is about knapsack problem and solved by genetic algorithm. 
- There are 3 files called, "w, c, v" that stores weight, capacity and value. 
- Run the program such as "python knapsack.gy" and choose options as you like then output will be stored in out.txt

