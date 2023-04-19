# AI-GridGame

There are start, goal, death, mountain, and flat nodes in a grid. The purpose is finding the road from starting node to any of the goal nodes with a minimum cost. Choose a Grid Pickle File to try a scenerio. As a result, total score, expansion path, and the road will be printed for both A* and UCS algorithms. 

Cost Table:

 From         To         Transition Cost
 _______________________________________
 
 Flat         Flat            -1
 Flat         Mountain        -3
 Mountain     Mountain        -2
 Mountain     Flat            -1
 Any          Goal            100
 Any          Death          -100
 
 
