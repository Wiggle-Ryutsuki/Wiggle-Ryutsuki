# Maimoona Aziz
# Python snake game with Pygame

import pygame
from pygame.math import Vector2
import random

pygame.init()
CELL_SIZE = 40
CELL_NUM = 25
SCREEN = pygame.display.set_mode((CELL_NUM * CELL_SIZE, CELL_NUM * CELL_SIZE))
SURFACE = pygame.Surface(((CELL_NUM * CELL_SIZE) - (2 * CELL_SIZE), (CELL_NUM * CELL_SIZE) - (2 * CELL_SIZE)))
RUNNING = True


class FRUIT:
    # Initialize fruit components
    def __init__(self):
        self.randomize()
        self._fruit = pygame.image.load("Graphics/apple.png").convert_alpha()
        self._fruit = pygame.transform.scale(self._fruit, (CELL_SIZE, CELL_SIZE))

    # Method that materializes fruit
    def draw_fruit(self):
        fruit_rect = pygame.Rect(self.pos.x * CELL_SIZE, self.pos.y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        SCREEN.blit(self._fruit, fruit_rect)

    # Method that randomizes position of apple
    def randomize(self):
        self.x = random.randint(1, CELL_NUM - 2)
        self.y = random.randint(1, CELL_NUM - 2)
        self.pos = pygame.math.Vector2(self.x, self.y)


class SNAKE:
    # Initialize snake components
    def __init__(self):
        self._snake = [Vector2(6, 10), Vector2(5, 10), Vector2(4, 10)]
        self._direction = Vector2(0, 0)
        self._score = 0
        self._high_score = 0
        self._first_move = True

        # Graphics for Snake
        self.head_up = pygame.image.load("Graphics/head_up.PNG").convert_alpha()
        self.head_up = pygame.transform.scale(self.head_up, (CELL_SIZE, CELL_SIZE))
        self.head_down = pygame.image.load("Graphics/head_down.PNG").convert_alpha()
        self.head_down = pygame.transform.scale(self.head_down, (CELL_SIZE, CELL_SIZE))
        self.head_left = pygame.image.load("Graphics/head_left.PNG").convert_alpha()
        self.head_left = pygame.transform.scale(self.head_left, (CELL_SIZE, CELL_SIZE))
        self.head_right = pygame.image.load("Graphics/head_right.PNG").convert_alpha()
        self.head_right = pygame.transform.scale(self.head_right, (CELL_SIZE, CELL_SIZE))

        self.tail_up = pygame.image.load("Graphics/tail_up.PNG").convert_alpha()
        self.tail_up = pygame.transform.scale(self.tail_up, (CELL_SIZE, CELL_SIZE))
        self.tail_down = pygame.image.load("Graphics/tail_down.PNG").convert_alpha()
        self.tail_down = pygame.transform.scale(self.tail_down, (CELL_SIZE, CELL_SIZE))
        self.tail_left = pygame.image.load("Graphics/tail_left.PNG").convert_alpha()
        self.tail_left = pygame.transform.scale(self.tail_left, (CELL_SIZE, CELL_SIZE))
        self.tail_right = pygame.image.load("Graphics/tail_right.PNG").convert_alpha()
        self.tail_right = pygame.transform.scale(self.tail_right, (CELL_SIZE, CELL_SIZE))

        self.body_vertical = pygame.image.load("Graphics/body_vertical.PNG").convert_alpha()
        self.body_vertical = pygame.transform.scale(self.body_vertical, (CELL_SIZE, CELL_SIZE))
        self.body_horizontal = pygame.image.load("Graphics/body_horizontal.PNG").convert_alpha()
        self.body_horizontal = pygame.transform.scale(self.body_horizontal, (CELL_SIZE, CELL_SIZE))

        self.body_tr = pygame.image.load("Graphics/body_topright.PNG").convert_alpha()
        self.body_tr = pygame.transform.scale(self.body_tr, (CELL_SIZE, CELL_SIZE))
        self.body_tl = pygame.image.load("Graphics/body_topleft.PNG").convert_alpha()
        self.body_tl = pygame.transform.scale(self.body_tl, (CELL_SIZE, CELL_SIZE))
        self.body_br = pygame.image.load("Graphics/body_bottomright.PNG").convert_alpha()
        self.body_br = pygame.transform.scale(self.body_br, (CELL_SIZE, CELL_SIZE))
        self.body_bl = pygame.image.load("Graphics/body_bottomleft.PNG").convert_alpha()
        self.body_bl = pygame.transform.scale(self.body_bl, (CELL_SIZE, CELL_SIZE))

        self.trophy = pygame.image.load("Graphics/trophy.PNG").convert_alpha()
        self.trophy = pygame.transform.scale(self.trophy, (CELL_SIZE, CELL_SIZE))

        # Sounds for snake
        self.crunch_sound = pygame.mixer.Sound("Sounds/cronch.wav")
        self.gameover_sound = pygame.mixer.Sound("Sounds/gameover_sound.wav")
        self.up_sound = pygame.mixer.Sound("Sounds/up.wav")
        self.down_sound = pygame.mixer.Sound("Sounds/down.wav")
        self.left_sound = pygame.mixer.Sound("Sounds/left.wav")
        self.right_sound = pygame.mixer.Sound("Sounds/right.wav")

    # Materialize snake
    def draw_snake(self):
        self.head_direction()
        self.tail_direction()
        for index, block in enumerate(self._snake):
            x_pos = block.x * CELL_SIZE
            y_pos = block.y * CELL_SIZE
            snake_rect = pygame.Rect(x_pos, y_pos, CELL_SIZE, CELL_SIZE)

            # Head
            if index == 0:
                SCREEN.blit(self.head, snake_rect)
            # Tail
            elif index == len(self._snake) - 1:
                SCREEN.blit(self.tail, snake_rect)
            # Body
            else:
                prev = self._snake[index + 1] - block
                next = self._snake[index - 1] - block

                # Check for horizontal and vertical
                if prev.x == next.x:
                    SCREEN.blit(self.body_vertical, snake_rect)
                elif prev.y == next.y:
                    SCREEN.blit(self.body_horizontal, snake_rect)

                # Check for corners
                else:
                    if prev.x == -1 and next.y == -1 or prev.y == -1 and next.x == -1:
                        SCREEN.blit(self.body_tl, snake_rect)
                    elif prev.x == 1 and next.y == -1 or prev.y == -1 and next.x == 1:
                        SCREEN.blit(self.body_tr, snake_rect)
                    elif prev.x == -1 and next.y == 1 or prev.y == 1 and next.x == -1:
                        SCREEN.blit(self.body_bl, snake_rect)
                    elif prev.x == 1 and next.y == 1 or prev.y == 1 and next.x == 1:
                        SCREEN.blit(self.body_br, snake_rect)

    # Moving motion for snake
    def slither(self):
        if not self._direction == Vector2(0, 0):
            snake_copy = self._snake[:-1]
            snake_copy.insert(0, snake_copy[0] + self._direction)
            self._snake = snake_copy[:]

    # Determine head direction by checking where the neck is
    def head_direction(self):
        neck = self._snake[1] - self._snake[0]

        # If neck is on the right, head is facing left
        if neck == Vector2(1, 0):
            self.head = self.head_left

        # If neck is on the left, head is facing right
        elif neck == Vector2(-1, 0):
            self.head = self.head_right

        # If neck is on the bottom, head is facing up
        elif neck == Vector2(0, 1):
            self.head = self.head_up

        # If neck is on the top, head is facing down
        elif neck == Vector2(0, -1):
            self.head = self.head_down

    # Determine tail direction by checking where the body is
    def tail_direction(self):
        body = self._snake[-2] - self._snake[-1]

        # If body is on the right, tail is facing left
        if body == Vector2(1, 0):
            self.tail = self.tail_left

        # If body is on the left, tail is facing right
        elif body == Vector2(-1, 0):
            self.tail = self.tail_right

        # If body is on the bottom, tail is facing up
        elif body == Vector2(0, 1):
            self.tail = self.tail_up

        # If body is on the top, tail is facing down
        elif body == Vector2(0, -1):
            self.tail = self.tail_down

    # Checks if snake collides with wall or itself
    def collision(self):
        head = self._snake[0]

        # If head = to wall, gameover
        if not 1 <= head.x < (CELL_NUM - 1) or not 1 <= head.y < (CELL_NUM - 1):
            self.gameover_sound.play()
            self.reset()

        # If any of the blocks from the head down = to the head, gameover
        for block in self._snake[2:]:
            if block == head:
                self.gameover_sound.play()
                self.reset()

    # Plays a crunch sound
    def crunch(self):
        self.crunch_sound.play()

    # Plays movement sounds
    def move_sounds(self, key):
        SOUNDS = {
            pygame.K_UP: self.up_sound,
            pygame.K_DOWN: self.down_sound,
            pygame.K_LEFT: self.left_sound,
            pygame.K_RIGHT: self.right_sound,

            pygame.K_w: self.up_sound,
            pygame.K_s: self.down_sound,
            pygame.K_a: self.left_sound,
            pygame.K_d: self.right_sound,
        }

        sound = SOUNDS.get(key)
        if sound:
            sound.play()

    # Reset snake
    def reset(self):
        self._snake = [Vector2(6, 10), Vector2(5, 10), Vector2(4, 10)]
        self._direction = Vector2(0, 0)
        self._score = 0
        self._first_move = True


def main():
    # Initialize
    fruit = FRUIT()
    snake = SNAKE()
    global RUNNING

    SCREEN_UPDATE = pygame.USEREVENT
    pygame.time.set_timer(SCREEN_UPDATE, 150)
    clock = pygame.time.Clock()

    while RUNNING:
        # Default colors for screen
        SCREEN.fill((176, 158, 79))
        SURFACE.fill((255, 241, 162))
        grass()
        SCREEN.blit(SURFACE, (CELL_SIZE, CELL_SIZE))

        # Materialize objects
        fruit.draw_fruit()
        snake.draw_snake()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUNNING = False

            if event.type == pygame.KEYDOWN:
                snake._direction = move_snake(event.key, snake)
            if event.type == SCREEN_UPDATE:
                grow_snake(fruit, snake)
                snake.slither()
                snake.collision()

        display_score(fruit, snake)

        pygame.display.update()
        clock.tick(60)

    pygame.quit()


# Function that handles user input (keyboard)
def move_snake(key, snake):
    DIRECTIONS = {
        pygame.K_UP: Vector2(0, -1),
        pygame.K_DOWN: Vector2(0, 1),
        pygame.K_LEFT: Vector2(-1, 0),
        pygame.K_RIGHT: Vector2(1, 0),

        pygame.K_w: Vector2(0, -1),
        pygame.K_s: Vector2(0, 1),
        pygame.K_a: Vector2(-1, 0),
        pygame.K_d: Vector2(1, 0),
    }

    new_direction = DIRECTIONS.get(key, snake._direction)

    if snake._first_move == True:
        if new_direction != Vector2(-1, 0):
            snake._first_move = False
            snake.move_sounds(key)
            return new_direction
        else:
            return snake._direction
    else:
        if new_direction != -snake._direction:
            if new_direction != snake._direction:
                snake.move_sounds(key)
            return new_direction
        else:
            return snake._direction


# Function that handles eating fruit and growing snake
def grow_snake(fruit, snake):
    # When snake head touches fruit, fruit respawns and snake grows 1 block
    if snake._snake[0] == fruit.pos:
        # Make fruit displace
        fruit.randomize()

        # Check to make sure fruit doesn't spawn in the snake
        while fruit.pos in snake._snake[1:]:
            fruit.randomize()

        snake.crunch()
        count_score(snake)

        # Grow snake by 1 vector
        snake._snake.append(snake._snake[-1])


# Function that handles score
def count_score(snake):
    snake._score += 1
    if snake._score > snake._high_score:
        snake._high_score = snake._score


# Function that handles displaying score (needs to be separate to show continuously)
def display_score(fruit, snake):
    font = pygame.font.Font("Fonts/Longsile.ttf", 30)

    score = snake._score
    high_score = snake._high_score

    score_surface = font.render(str(score), True, (56, 74, 12))
    high_score_surface = font.render(str(high_score), True, (56, 74, 12))

    x_pos = CELL_SIZE * 2
    h_x_pos = CELL_SIZE * 4
    y_pos = CELL_SIZE / 2

    score_rect = score_surface.get_rect(center=(x_pos, y_pos))
    high_score_rect = high_score_surface.get_rect(center=(h_x_pos, y_pos))

    apple_rect = fruit._fruit.get_rect(midright=(score_rect.left, score_rect.centery))
    trophy_rect = snake.trophy.get_rect(midright=(high_score_rect.left, high_score_rect.centery))

    bg_rect = pygame.Rect(apple_rect.left, apple_rect.top, apple_rect.width + score_rect.width, apple_rect.height)
    bg_rect = pygame.Rect(trophy_rect.left, trophy_rect.top, trophy_rect.width + high_score_rect.width, trophy_rect.height)

    pygame.draw.rect(SCREEN, (176, 158, 79), bg_rect)
    pygame.draw.rect(SCREEN, (176, 158, 79), bg_rect)

    SCREEN.blit(score_surface, score_rect)
    SCREEN.blit(fruit._fruit, apple_rect)

    SCREEN.blit(high_score_surface, high_score_rect)
    SCREEN.blit(snake.trophy, trophy_rect)


# Function that handles rendering grass
def grass():
    grass_color = (224, 203, 108)

    for row in range(CELL_NUM):
        if row % 2 == 0:
            for col in range(CELL_NUM):
                if col % 2 == 0:
                    grass_rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                    pygame.draw.rect(SURFACE, grass_color, grass_rect)
        else:
            for col in range(CELL_NUM):
                if col % 2 != 0:
                    grass_rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                    pygame.draw.rect(SURFACE, grass_color, grass_rect)


if __name__ == "__main__":
    main()
