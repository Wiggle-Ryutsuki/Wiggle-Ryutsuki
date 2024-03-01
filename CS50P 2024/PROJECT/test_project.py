# Maimoona Aziz

from project import SNAKE, FRUIT, move_snake, grow_snake, count_score
import pygame
from pygame.math import Vector2


# Test keyboard inputs
def test_move_snake():
    snake = SNAKE()

    # Test going up
    snake._direction = Vector2(1, 0)
    assert move_snake(pygame.K_UP, snake) == Vector2(0, -1)

    # Test going down
    snake._direction = Vector2(1, 0)
    assert move_snake(pygame.K_DOWN, snake) == Vector2(0, 1)

    # Test going left
    snake._direction = Vector2(0, -1)
    assert move_snake(pygame.K_LEFT, snake) == Vector2(-1, 0)

    # Test going right
    snake._direction = Vector2(0, -1)
    assert move_snake(pygame.K_RIGHT, snake) == Vector2(1, 0)

    # Test going up with W
    snake._direction = Vector2(1, 0)
    assert move_snake(pygame.K_w, snake) == Vector2(0, -1)

    # Test going down WITH S
    snake._direction = Vector2(1, 0)
    assert move_snake(pygame.K_s, snake) == Vector2(0, 1)

    # Test going left WITH A
    snake._direction = Vector2(0, -1)
    assert move_snake(pygame.K_a, snake) == Vector2(-1, 0)

    # Test going right WITH D
    snake._direction = Vector2(0, -1)
    assert move_snake(pygame.K_d, snake) == Vector2(1, 0)

    # Test going left when facing right
    snake._direction = Vector2(1, 0)
    assert move_snake(pygame.K_LEFT, snake) == Vector2(1, 0)

    # Test going right then facing left
    snake._direction = Vector2(-1, 0)
    assert move_snake(pygame.K_RIGHT, snake) == Vector2(-1, 0)

    # Test going up when facing down
    snake._direction = Vector2(0, 1)
    assert move_snake(pygame.K_UP, snake) == Vector2(0, 1)

    # Test going down when facing up
    snake._direction = Vector2(0, -1)
    assert move_snake(pygame.K_DOWN, snake) == Vector2(0, -1)

    # Test random key
    snake._direction = Vector2(0, -1)
    assert move_snake(pygame.K_m, snake) == Vector2(0, -1)


# Test if snake grows and fruit randomizes
def test_grow_snake():
    snake = SNAKE()
    fruit = FRUIT()

    # Assert initial length is 3
    initial_snake_length = len(snake._snake)
    assert initial_snake_length == 3

    # Assert fruit position is not in snake when spawned
    fruit.randomize()
    assert fruit.pos not in snake._snake[1:]

    # Set initial fruit position
    fruit.pos = [10, 10]
    # Set snake position to fruit postion
    snake._snake[0] = [10, 10]

    # Run function
    grow_snake(fruit, snake)

    # Result:
    # Snake length = snake length + 1
    assert len(snake._snake) == 4
    # Fruit postion is no longer initial position
    assert fruit.pos != [10, 10]

    # ---------------------------------------------------------

    # Set initial fruit position
    fruit.pos = [10, 10]
    # Set snake position to some position not overlapping with fruit
    snake._snake[0] = [5, 5]

    # Remember the initial fruit position
    initial_fruit_position = fruit.pos

    # Reset snake length
    snake.reset()

    # Run the function to grow snake (assuming it doesn't eat the fruit)
    grow_snake(fruit, snake)

    # Result:
    # Snake length should remain the same
    assert len(snake._snake) == 3

    # Fruit position should remain the same
    assert fruit.pos == initial_fruit_position


# Test if score increments
def test_count_score():
    snake = SNAKE()

    # Make sure score starts from 0
    assert snake._score == 0
    assert snake._high_score == 0

    # Function increments by 1
    count_score(snake)

    assert snake._score == 1
    assert snake._high_score == 1

    snake._score = 5

    count_score(snake)

    assert snake._score == 6
    assert snake._high_score == 6

    # Case where gameover, score resets and highscore doesn't
    snake.reset()

    assert snake._score == 0
    assert snake._high_score == 6
