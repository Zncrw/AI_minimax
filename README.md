<h1>AI_minimax</h1> 

<h2>About project:</h2> 
<p>In this project i want to program simple AI bot to play tic-tac-toe game on 3x3 gaming board.
AI is using minimax algorithm to find out the best move posible and then perform this move. Player should not
be able to beat this simple AI in this game, best posible outcome for user is draw.</p>
<h3>About minimax algoritm:</h3>
<p>Minimax algoritm, is used in strategic game between two players. Algoritm is building decision tree and minimalizing/maximalixing the outcome. This algoritm is mostly used in game development.</p>
 <h4>How algorithm works?:</h4>
 <ol>
   <li>Try moves</li>
   <p>Algorithm generates every posible move in curent state and try it</p>
   
   <li>Evaluate</li>
   <p>For every posible move evaluate function gets "score" to determine the best move</p>

   <li>Minimize / Maximize</li>
   <p> If it is the current players turn, the algorithm chooses the move that has maximal score so he maximize chance to win the game. If it is  opponents turn, the algorithm chooses the move that minimizes the score</p>

   <li>Recursive call</li>
   <p>Algorithm is recursive calling himself for each posible move (repeating steps 1-3) until a terminal state of game (win/loss/draw) </p>

   <li>Choose best move</li>
   <p>Here algorithm takes best move posible and waits for opponent</p>   
 </ol>
 <h2>Libraries:</h2>
 <p> In this project i decided to use NUMPY library to make game board(grid) and used function numpy.trace
 to check diagonals for a winner. Any other libraries used here are in base package of python 3. For version of numpy
 check file <a href="requirements.txt">requirments</a> </p>

 <h2>Showcase:</h2>

  
<p>For the further information you can visit page <a>https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-1-introduction/</a></p>
