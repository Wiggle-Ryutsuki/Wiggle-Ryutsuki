# Classic Snake Game with Python

**Video Demo: <https://youtu.be/lHdLmZ--Boo>**

The classic snake game is a timeless favorite, often remembered from the days when it came as a preloaded gem on your parent's old phone. Now the game has been remodeled as one of Google’s minigames and even branched off to inspire other snake themed games.

In this simple game, the player plays as the snake. The goal is to guide the snake to consume randomly appearing fruit, thereby increasing its length.

## Instructions

* Use the **W, A, S, D** keys or **UP, DOWN, LEFT, RIGHT** keys to move the snake.

* Eat the fruit to grow longer.

* Be careful not to collide with the walls or with the snake's own body.

* High scores are displayed at the top-left corner of the screen.

## Project

For my final project in CS50P, I took the opportunity to explore the fundamentals of game-making by recreating the beloved snake game. The game has a simple logic which revolves around moving the snake, making it eat fruits to grow, all while ensuring it doesn’t collide with the walls or itself.

## Process

### Researching Libraries

In order to create my game, I needed to research Python libraries that specialize in game-making.

[**Pygame**](https://www.pygame.org/wiki/about) is a free set of Python modules designed for writing video games. Pygame has great functionality which allows anyone to create fully featured games and multimedia programs in the Python language.

The Pygame documentation also has several introductory tutorials which helped me get the gist of all the basic functions needed to build a simple game.

### Setting The Screen

As with all games, a display screen is needed so that we can see the game and so that it acts as a base for our objects. The screen is structured like a grid, making it easier to coordinate the positioning of the fruit and snake. To achieve this, a default cell size and the number of cells is initialized and used as parameters for the screen.

On top of the screen, I lay a surface which functions as the grass graphics.

### Initializing Objects

Now for the important part, the objects. The two main objects are the **Snake** and the **Fruit**.

#### Fruit

I created a class for fruit so that all fruit related activities are organized. The main function of the fruit is to appear in random cells. The only methods inside of the fruit class is the **randomize()** method, which picks a random X and Y coordinate within the screen and sets the position of fruit to that, and the **draw_fruit()** method which renders the fruit graphics.

#### Snake

The snake object is more complex than the fruit since there is a lot to handle as it’s the playable object. As the snake moves, it would need to be animated. We also must handle “game overs” when the snake collides with the wall or itself.

The snake is not a shape appended to the screen but is actually part of the screen itself. I chose to make some of the cells in the grid the snake, therefore, the snake is initialized as 3 cells together in a place. Then the snake “grows”, one more cell is rendered as the snake.

The snake has many components initialized. Aside from importing the images needed for rendering, the snake body is initialized as three horizontal cells in the grid. Next, we have the direction the snake will be facing and moving towards. Then lastly the score and high score variables that will keep track of the score.

The **slither()** method cuts and pastes the snake body one cell forward at a time in the direction that is inputted, therefore simulating an animation effect while also making the snake move continuously.

The **collision()** method checks if the snake head is about to go into the same space as the wall or itself. Once it confirms what the next direction is in a “game over position”, the method calls the **reset()** method which resets the snake’s position, length, and score.

### Creating The Function That Handles Input

The most important part of the snake is moving it around, so the program will need to take a key input from the player and have the snake move in that direction. Pygame thankfully has modules that cover input from keyboards, computer mice, and joysticks, so I take advantage of the keyboard modules.  

I created a dictionary which associates arrow keys with (X, Y) coordinates and built a function that takes key inputs and returns the (X, Y) direction. The direction returned gets set as the direction in the snake class (*snake._direction*), where the **slither()** method then makes the snake move towards that direction.  

This function also handles the sound that plays when the snake moves, each direction correlating to a different sound.

I test this function by asserting that the correct coordinate is returned when a key is pressed. I also tested for alternative movement keys (WASD) and made sure the snake is unable to move to the opposite direction from where it is facing currently, therefore returning the same current position.

### Creating The Function That Handles Growing

The next function for the snake is the growing function. When the snake eats the fruit, it is supposed to grow one block and then the fruit is spawned in another random position.

The **grow_snake()** function checks if the first item in the snake, the head, is in the same block as the fruit. Once it has confirmed that the head is in contact with the fruit, the fruit's position is randomized to simulate the fruit “disappearing” when eaten. Then a block from the grid is appended to the end of the snake list and is rendered to be part of the snake.

The function also checks to make sure the fruit doesn’t spawn inside the snake body and plays the crunch sound when the fruit is “eaten”.

The way I test this function is different. Since this function does not return a value but alters it, I set some objects to certain values, like setting the snake length and the fruit position, then I run the function and assert that the snake length has increased, and the fruit position is no longer the same. Then tested the opposite, where the snake has not eaten the fruit and therefore had not grown and the fruit had not moved.

### Creating The Function That Handles Scoring

Lastly, we have the function that increments the score. The **count_score()** function simply adds to the score and high score objects in the snake class. The high score object is only incremented if the score is higher than the high score, therefore the high score will stop incrementing if the score is lower, in cases where the snake is reset after a gameover. Another function is coded to handle rendering the scoreboard at the top of the screen.

This function also alters values instead of returning them. So, I check the function by setting the current score and high score and running the function, then asserting that the scores have increased. I also tested for the case where the snake has reset along with the score, but the high score shouldn’t.

## Final Comments

Overall, I had a lot of fun exploring the basics of game-making. This library has made it ten times easier by abstracting all the hard stuff and simplifying it into modules, but I still learned a lot about the basic necessities for games.  

This course was excellent, and I was able to deepen my understanding of python and its logic. I hope to continue exploring the python language and make many more programs that will continue to boggle my brain but end with satisfying results.

This was CS50!
