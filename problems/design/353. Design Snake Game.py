# https://leetcode.com/problems/design-snake-game/
# Difficulty: Medium
# Tags: snake_game snake queue design

# Problem
# Design a Snake game that is played on a device with screen size height x width. Play the game online if you are not familiar with the game.

# The snake is initially positioned at the top left corner (0, 0) with a length of 1 unit.

# You are given an array food where food[i] = (ri, ci) is the row and column position of a piece of food that the snake can eat. When a snake eats a piece of food, its length and the game's score both increase by 1.

# Each piece of food appears one by one on the screen, meaning the second piece of food will not appear until the snake eats the first piece of food.

# When a piece of food appears on the screen, it is guaranteed that it will not appear on a block occupied by the snake.

# The game is over if the snake goes out of bounds (hits a wall) or if its head occupies a space that its body occupies after moving (i.e. a snake of length 4 cannot run into itself).

# Implement the SnakeGame class:

#     SnakeGame(int width, int height, int[][] food) Initializes the object with a screen of size height x width and the positions of the food.
#     int move(String direction) Returns the score of the game after applying one direction move by the snake. If the game is over, return -1.


# Solution
# Time: O(1) for init, O(1) for `move`. Space O(mn) -> storing snake cells (can be mn if snake occupies every cell).
# The only tricky part in this problem is to simulate snake movement. It can be done using a queue data structure (reverse logic).

from collections import deque
from typing import List


class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.height = height
        self.width = width
        self.snake = deque([(0, 0)])  # queue
        self.occupied = {(0, 0)}  # set
        self.score = 0
        self.food = food
        self.curr_food_idx = 0
        self.dirs = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}

    def move(self, direction: str) -> int:
        headR, headC = self.snake[0]

        dy, dx = self.dirs[direction]
        newR, newC = headR + dy, headC + dx

        # hits the wall
        if newR < 0 or newR >= self.height or newC < 0 or newC >= self.width:
            return -1

        # eats itself
        if (newR, newC) != self.snake[-1] and (newR, newC) in self.occupied:
            return -1

        # eats food
        if (
            self.curr_food_idx < len(self.food)
            and newR == self.food[self.curr_food_idx][0]
            and newC == self.food[self.curr_food_idx][1]
        ):
            self.score += 1
            self.curr_food_idx += 1
        else:
            tail = self.snake.pop()
            self.occupied.remove(tail)

        self.snake.appendleft((newR, newC))
        self.occupied.add((newR, newC))

        return self.score


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)
